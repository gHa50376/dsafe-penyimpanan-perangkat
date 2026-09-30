"""Device-only durable files, with per-Streamlit-session working copies.

No data/draft file is written to the host. A component confirms IndexedDB
transactions before the next application run may proceed.
"""
import base64
import fnmatch
import json
import uuid
from pathlib import Path, PurePosixPath
import streamlit as st

_PREFIX = '_dsafe_device_'
_COMPONENT_KEY = 'dsafe_device_storage'
_JS = (Path(__file__).parent / 'browser_storage.js').read_text(encoding='utf-8')
_bridge = st.components.v2.component('dsafe_device_storage', html='<span hidden></span>', js=_JS, isolate_styles=False)

def _state():
    return st.session_state

def _files():
    return _state().setdefault(_PREFIX+'files', {})

def _changed():
    _state()[_PREFIX+'dirty'] = True

def synchronize():
    """Read once, then persist dirty files with optimistic revision checking."""
    state = _state()
    hydrated = state.get(_PREFIX+'hydrated', False)
    request = state.get(_PREFIX+'request')
    if request is None or (state.get(_PREFIX+'dirty') and (request.get('operation') != 'write' or state.get(_PREFIX+'committed_request') == request.get('id'))):
        request = {'id':str(uuid.uuid4()), 'operation':'write' if hydrated and state.get(_PREFIX+'dirty') else 'read'}
        if request['operation'] == 'write':
            request.update(files=dict(_files()), expectedRevision=state.get(_PREFIX+'revision', 0))
        state[_PREFIX+'request'] = request
    result = _bridge(key=_COMPONENT_KEY, data=request, default={'result':None}, height=1,
                     on_result_change=lambda: None).result
    if not isinstance(result, dict) or result.get('id') != request['id']:
        if request['operation'] == 'read':
            st.info('Membuka penyimpanan perangkat…')
        elif state.get(_PREFIX+'dirty'):
            st.info('Menyimpan data ke perangkat…')
        st.stop()
    if not result.get('ok'):
        st.error(result.get('error') or 'Penyimpanan perangkat belum tersedia.')
        if state.get(_PREFIX+'dirty'):
            # Offer the pending book as the same standard backup JSON, without
            # falsely reporting a successful browser transaction.
            try:
                book=json.loads(BrowserPath('/data/buku_kerja_v341.json').read_text())
                payload={'format':'dsafe-buku-kerja-v1','data':book}
                st.download_button('Unduh data yang belum tersimpan',json.dumps(payload,ensure_ascii=False),
                                   'cadangan-belum-tersimpan.json','application/json')
            except (ValueError, FileNotFoundError):
                pass
        if st.button('Coba lagi',key=_PREFIX+'retry'):
            state.pop(_PREFIX+'request',None)
            st.rerun()
        st.stop()
    if request['operation'] == 'read' and not hydrated:
        files=result.get('files')
        if not isinstance(files,dict) or any(not isinstance(k,str) or not isinstance(v,str) for k,v in files.items()):
            st.error('Data penyimpanan perangkat tidak valid.')
            st.stop()
        state[_PREFIX+'files']=dict(files)
        state[_PREFIX+'hydrated']=True
        state[_PREFIX+'revision']=int(result['revision'])
        state[_PREFIX+'dirty']=False
        state[_PREFIX+'committed_request']=request['id']
    elif request['operation'] == 'write' and state.get(_PREFIX+'dirty'):
        state[_PREFIX+'revision']=int(result['revision'])
        state[_PREFIX+'dirty']=False
        state[_PREFIX+'committed_request']=request['id']
    # Existing acknowledgements can be reused during read-only reruns.

def finish():
    if _state().get(_PREFIX+'dirty'):
        st.rerun()

def stop():
    finish()
    st.stop()

def clear_ui_state():
    """Reset/restore must keep storage transport and pending writes alive."""
    for key in list(st.session_state):
        if not key.startswith(_PREFIX) and key != _COMPONENT_KEY:
            del st.session_state[key]

class BrowserPath:
    """Minimal file interface for unchanged draft/backup routines."""
    def __init__(self, value): self.value=str(PurePosixPath(value))
    def __truediv__(self, name): return BrowserPath(PurePosixPath(self.value)/name)
    def __str__(self): return self.value
    def __repr__(self): return f'BrowserPath({self.value!r})'
    def __hash__(self): return hash(self.value)
    def __eq__(self, other): return isinstance(other,BrowserPath) and self.value==other.value
    def __lt__(self, other): return self.value<other.value
    @property
    def name(self): return PurePosixPath(self.value).name
    @property
    def suffix(self): return PurePosixPath(self.value).suffix
    def with_suffix(self, suffix): return BrowserPath(PurePosixPath(self.value).with_suffix(suffix))
    def exists(self): return self.value in _files() or self.value in ('/data','/draft_storage')
    def is_file(self): return self.value in _files()
    def mkdir(self, *args, **kwargs): return None
    def read_bytes(self):
        try:return base64.b64decode(_files()[self.value],validate=True)
        except KeyError:raise FileNotFoundError(self.value) from None
    def read_text(self, encoding='utf-8'): return self.read_bytes().decode(encoding)
    def write_bytes(self, value):
        encoded=base64.b64encode(bytes(value)).decode('ascii')
        if _files().get(self.value) != encoded:
            _files()[self.value]=encoded;_changed()
        return len(value)
    def write_text(self, value, encoding='utf-8'): self.write_bytes(value.encode(encoding));return len(value)
    def unlink(self, missing_ok=False):
        if self.value in _files():del _files()[self.value];_changed()
        elif not missing_ok:raise FileNotFoundError(self.value)
    def replace(self, target):
        target=target if isinstance(target,BrowserPath) else BrowserPath(target)
        payload=self.read_bytes();target.write_bytes(payload)
        if self != target:self.unlink()
        return target
    def glob(self, pattern):
        prefix=self.value.rstrip('/')+'/'
        return [BrowserPath(key) for key in _files() if key.startswith(prefix)
                and '/' not in key[len(prefix):] and fnmatch.fnmatch(key[len(prefix):],pattern)]
