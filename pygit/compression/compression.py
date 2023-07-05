import zlib


def compress_content(content:str):
    compressed_file = zlib.compress(content)
    return compressed_file


def decompress_content(content:bytes):
    decompressed_file = zlib.decompress(content)
    return decompressed_file


def compress_file(filename:str):
  with open(filename, 'r') as f:
    compressed = compress_content(f.read())
  return compressed







    



