class Secret:

    def __init__(self):
        self._o_data = []
        self._n_data = []
        self._b_key = []
        self._key = []
        self._legth = 0
        
    def encoding(self, origin:str, new:str, file:str) -> None:
        """
        This function is an encoder function
        """
        with open(origin, "rb") as f:
            self._o_raw = f.read()
            self._o_hex = self._o_raw.hex()
            self._o_hex = [self._o_hex[i:i+64] for i in range(0, len(self._o_hex), 64)]
        with open(new, "rb") as f:
            self._n_raw = f.read()
            self._n_hex = self._n_raw.hex()
            self._n_hex = [self._n_hex[i:i+64] for i in range(0, len(self._n_hex), 64)]
        
        self._n_hex = self._n_hex[:len(self._o_hex)]
        self._n_hex[-1] = self._n_hex[-1][:len(self._o_hex[-1])]

        for i in self._o_hex:
            self._o_data.append(int(i, 16))

        for i in self._n_hex:
            self._n_data.append(int(i, 16))
        
        self._legth = len(self._o_hex[-1]) + 2

        for i, j in zip(self._o_data, self._n_data):
            self._b_key.append(i ^ j)
        
        for i in self._b_key:
            self._key.append(hex(i))

        for i, j in enumerate(self._key):
            if i == len(self._key) - 1:
                self._key[i] = self._key[i][:2] + ( "0" * ( self._legth - len(j))) + self._key[i][2:]
            else:
                if len(j) != 66:
                    self._key[i] = self._key[i][:2] + ( "0" * ( 66 - len(j))) + self._key[i][2:]
        
        for i, _ in enumerate(self._key):
            self._key[i] = self._key[i][2:]
        
        self._key = "".join(self._key)
        self._key = bytes.fromhex(self._key)

        with open(file, "wb") as f:
           f.write(self._key)
        
        self.restore()
    
    def decoding(self, new:str, key:str, output:str) -> None:
        """
        This function is an decoder function
        """
        with open(key, "rb") as f:
            self._o_raw = f.read()
            self._o_hex = self._o_raw.hex()
            self._o_hex = [self._o_hex[i:i+64] for i in range(0, len(self._o_hex), 64)]
        with open(new, "rb") as f:
            self._n_raw = f.read()
            self._n_hex = self._n_raw.hex()
            self._n_hex = [self._n_hex[i:i+64] for i in range(0, len(self._n_hex), 64)]
        
        self._n_hex = self._n_hex[:len(self._o_hex)]
        self._n_hex[-1] = self._n_hex[-1][:len(self._o_hex[-1])]

        for i in self._o_hex:
            self._o_data.append(int(i, 16))

        for i in self._n_hex:
            self._n_data.append(int(i, 16))
        
        self._legth = len(self._o_hex[-1]) + 2

        for i, j in zip(self._o_data, self._n_data):
            self._b_origin.append(i ^ j)
        
        for i in self._b_origin:
            self._origin.append(hex(i))

        for i, j in enumerate(self._origin):
            if i == len(self._origin) - 1:
                self._origin[i] = self._origin[i][:2] + ( "0" * ( self._legth - len(j))) + self._origin[i][2:]
            else:
                if len(j) != 66:
                    self._origin[i] = self._origin[i][:2] + ( "0" * ( 66 - len(j))) + self._origin[i][2:]
        
        for i, _ in enumerate(self._origin):
            self._origin[i] = self._origin[i][2:]
        
        self._origin = "".join(self._origin)
        self._origin = bytes.fromhex(self._origin)

        with open(output, "wb") as f:
           f.write(self._origin)
        
        self.restore()


    def restore(self) -> None:
        self._o_data = []
        self._n_data = []
        self._b_key = []
        self._key = []
        self._b_origin = []
        self._origin = []
        self._legth = 0

def test() -> str:
    """
    This is a test function
    """
    from time import time
    start = time()
    secret = Secret()
    secret.encoding("origin.txt", "new.txt", "test_key")
    secret.decoding("new.txt", "test_key", "origin_decode.txt")
    end = time()
    text1 = f"""+------------------------------------+
| Time           : {end - start:.5f} seconds   |
+------------------------------------+\n"""
    print(text1)

if __name__ == "__main__":
    test()
