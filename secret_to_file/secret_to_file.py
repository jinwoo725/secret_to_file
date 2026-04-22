class Secret:

    def __init__(self, *, size:int = 64, prefix:int = 1) -> None:
        """
        This function is an init function
        prefix 0 is byte, 1 is kilobyte, 2 is megabyte
        size * prefix
        """
        match prefix:
            case 0:
                scale = 1
            case 1:
                scale = 1024
            case 2:
                scale = 1024 * 1024
            case _:
                scale = 1024
        self._chunk_size = size * scale
    
    def convert(self, file1:str, file2:str, output:str) -> None:
        """
        This function is an Convert function
        origin, new, key | new, key, origin
        """
        with open(file1, "rb") as f1, open(file2, "rb") as f2, open(output, "wb") as f3:
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

                chunk = chunk[:2] + ( "0" * ( length - len(chunk))) + chunk[2:]
                
                chunk = chunk[2:]
                chunk = bytes.fromhex(chunk)

                f3.write(chunk)
