from pygit.compression.compression import *


def test_compress_content():
  content = 'blob 16\u0000what is up, doc?'.encode('utf-8')
  print(compress_content(content))
  temp = compress_content(content)
  assert temp == b"x\x9CK\xCA\xC9OR04c(\xCFH,Q\xC8,V(-\xD0QH\xC9O\xB6\a\x00_\x1C\a\x9D"


def test_decompress_content():
  content = b'x\x9cK\xca\xc9OR04c(\xcfH,Q\xc8,V(-\xd0QH\xc9O\xb6\x07\x00_\x1c\x07\x9d'
  print(decompress_content(content))
  temp = decompress_content(content)
  assert temp == b'blob 16\x00what is up, doc?'
