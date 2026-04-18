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
- **Secret.encoding(str, str, str) -> None**<br>
- **Secret.decoding(str, str, str) -> None**<br>
- **test() -> str**

Exam<br>
-
**Example**<br>
```python
import secret_to_file
secret = secret_to_file.Secret()
secret.encoding("origin.txt", "new.txt", "test_key")
secret.decoding("new.txt", "test_key", "origin_decode.txt")
```
**Output**<br>
```output
+------------------------------------+
| Time           : 0.01366 seconds   |
+------------------------------------+
```

License<br>
-

This project is licensed under the terms of the MIT license.