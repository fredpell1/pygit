import zlib

def compress_content(content:str):
    compressed_file = zlib.compress(content)
    return compressed_file


def compress_file(filename:str):
  with open(filename, 'r') as f:
    compressed = compress_content(f.read())
  return compressed






    



