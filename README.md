## Compressor Toolbox for Python
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/compressortoolbox.git
```


### Example
```
from compressortoolbox.compressor import Compressor

d = {"a": 1, "b": 2}

compressed_d = Compressor.compress_dict(d)

decompressed_d = Compressor.decompress_dict(compressed_d)
```