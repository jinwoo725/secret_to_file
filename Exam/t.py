from secret_to_file import Secret
import secrets

path = __file__[:len(__file__) - 4]

def run():
    for i in [path + "A", path + "B", path + "C"]:
        temp = secrets.token_hex(128)
        with open(i, "w") as f:
            f.write(temp)

    secret = Secret(size = 256, prefix = 0)

    secret.convert(path + "A", path + "B", path + "AB")
    secret.convert(path + "A", path + "C", path + "AC")

    secret.convert(path + "AC", path + "B", path + "ACB")
    secret.convert(path + "AB", path + "C", path + "ABC")

    secret.convert(path + "Exam.json", path + "ACB", path + "Exam.json.encode")
    secret.convert(path + "Exam.json.encode", path + "ABC", path + "Exam.json.decode")
    
if __name__ == "__main__":
    run()