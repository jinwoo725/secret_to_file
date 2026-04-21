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
- **Secret.convert(str, str, str) -> None**<br>

Exam<br>
-
**Example**<br>
```python
import secret_to_file
secret = secret_to_file.Secret()
secret.convert("origin.txt", "new.txt", "test_key")
secret.convert("new.txt", "test_key", "origin_decode.txt")
```
**Output**<br>
```output

```

License<br>
-

This project is licensed under the terms of the MIT license.
