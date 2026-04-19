class Secret:

    def __init__(self):
        self._chunk_size = 64 * 1024
    
    def encoding(self, origin:str, new:str, output:str) -> None:
        """
        This function is an encoder function
        """
        length = 0
        with open(origin, "rb") as f1, open(new, "rb") as f2, open(output, "wb") as f3:
            while True:
                o_data = f1.read(self._chunk_size)
                n_data = f2.read(self._chunk_size)
                o_data = o_data.hex()
                n_data = n_data.hex()

                if not o_data: break

                if len(n_data) > len(o_data):
                    n_data = n_data[:len(o_data)] 
                    length = len(o_data) + 2

                o_data = (int(o_data, 16))
                n_data = (int(n_data, 16))

                key = o_data ^ n_data

                key = hex(key)

                if length != 0:
                    key = key[:2] + ( "0" * ( length - len(key))) + key[2:]
                else:
                    if len(key) != 131074:
                        key = key[:2] + ( "0" * ( 131074 - len(key))) + key[2:]
                
                key = key[2:]
                key = bytes.fromhex(key)
                
                f3.write(key)
    
    def decoding(self, new:str, key:str, output:str) -> None:
        """
        This function is an decoder function
        """
        length = 0
        with open(key, "rb") as f1, open(new, "rb") as f2, open(output, "wb") as f3:
            while True:
                o_data = f1.read(self._chunk_size)
                n_data = f2.read(self._chunk_size)
                o_data = o_data.hex()
                n_data = n_data.hex()

                if not o_data: break

                if len(n_data) > len(o_data):
                    n_data = n_data[:len(o_data)] 
                    length = len(o_data) + 2

                o_data = (int(o_data, 16))
                n_data = (int(n_data, 16))
        
                chunk = o_data ^ n_data

                chunk = hex(chunk)

                if length != 0:
                    chunk = chunk[:2] + ( "0" * ( length - len(chunk))) + chunk[2:]
                else:
                    if len(key) != 131074:
                        chunk = chunk[:2] + ( "0" * ( 131074 - len(chunk))) + chunk[2:]
                
                chunk = chunk[2:]
                chunk = bytes.fromhex(chunk)

                f3.write(chunk)

def test() -> str:
    """
    This is a test function
    """
    from time import time
    start = time()
    secret = Secret()
    secret.encoding("origin.txt", "new.txt", "test_key")
    secret.decoding("new.txt", "test_key")
    end = time()
    print(f"+------------------------------------+\n| Time           : {end - start:.5f} seconds   |\n+------------------------------------+\n")

if __name__ == "__main__":
    test()
