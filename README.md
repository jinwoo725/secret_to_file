secret_to_file<br>
-

A beginner's secret_to_file in Python

install<br>
-
Linux&MacOS
-
**Bash/Zsh**
```bash
pip3 install secret_to_file
```
Windows
-
**CMD/PowerShell**
```cmd
pip install secret_to_file
```

function<br>
-
- **Secret(size:int, prefix:int)**<br>
- **Secret.convert(file1:str, file2:str, output:str) -> None**<br>

Exam<br>
-
**Example**<br>
```python
import secret_to_file
secret = secret_to_file.Secret() #default size = 64, prefix = 1
#secret = secret_to_file.Secret(size = 256, prefix = 0) 256 byte
#secret = secret_to_file.Secret(size = 128) 128 kilobyte
#secret = secret_to_file.Secret(prefix = 2) 64 megabyte
secret.convert("origin.txt", "new.txt", "test_key")
secret.convert("new.txt", "test_key", "origin_decode.txt")
```
**Output**<br>
```output

```

License<br>
-

This project is licensed under the terms of the MIT license.
