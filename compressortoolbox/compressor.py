import zlib, json, base64

class Compressor:
    @classmethod
    def compress_string(cls, s):
        try:
            str_encoded = s.encode("utf-8")
        except Exception:
            raise Exception("Compress: unable to encode")

        try:
            str_zipped = zlib.compress(str_encoded)
        except Exception:
            raise Exception("Compress: unable to zip")
        try:
            str_b64_encoded = base64.b64encode(str_zipped)
        except Exception:
            raise Exception("Compress: unable to encode base 64")

        try:
            str_ascii = str_b64_encoded.decode('ascii')
        except Exception:
            raise Exception("Compress: unable to decode ascii")

        return str_ascii

    @classmethod
    def compress_dict(cls, obj):
        try:
            json_string = json.dumps(obj)
        except Exception:
            raise Exception("Compress: unable to dump json")

        return cls.compress_string(json_string)

    @classmethod
    def decompress_string(cls, s):
        try:
            str_b64_decoded = base64.b64decode(s)
        except Exception:
            raise Exception("Decompress: unable to decode base 64")

        try:
            str_unzipped = zlib.decompress(str_b64_decoded)
        except Exception:
            raise Exception("Decompress: unable to unzip")

        try:
            str_decoded = str_unzipped.decode('utf-8')
        except Exception:
            raise Exception("Decompress: unable to decode utf-8")

        return str_decoded

    @classmethod
    def decompress_dict(cls, s):
        json_string = cls.decompress_string(s)

        try:
            json_dict = json.loads(json_string)
        except Exception:
            raise Exception("Decompress: unable to json loads")

        return json_dict