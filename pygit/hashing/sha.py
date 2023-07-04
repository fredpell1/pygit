import os
import hashlib

def build_header(filename:str, filetype:str): return f"{filetype} #{os.path.getsize(filename)}\0"

def create_hash(filename:str, filetype:str):
    assert filetype in ['blob', 'tree', 'commit']
    with open(filename, 'r') as f:
        header = build_header(filename,filetype)
        content = f.read()
    hasher = hashlib.sha1(header + content)
    return hasher.hexdigest()

