## Compressor Toolbox for Python
<hr>

### Example
```
from compressor import Compressor

d = {"a": 1, "b": 2}

compressed_d = Compressor.compress_dict(d)

decompressed_d = Compressor.decompress_dict(compressed_d)
```