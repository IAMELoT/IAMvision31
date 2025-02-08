import zlib
import base64

class CompressionAgent:
    @staticmethod
    def compress(data):
        """ Compresses data using zlib and encodes it in base64. """
        compressed = zlib.compress(data.encode())
        return base64.b64encode(compressed).decode()

    @staticmethod
    def decompress(compressed_data):
        """ Decompresses data using zlib and decodes from base64. """
        decoded_data = base64.b64decode(compressed_data)
        return zlib.decompress(decoded_data).decode()