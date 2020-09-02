import sys

def fixed_xor(x, y):
    assert len(x) == len(y), "Fixed XOR has different length arguments."
    return bytes(a^b for a,b in zip(x,y))

BUFFER = bytes.fromhex("686974207468652062756c6c277320657965")

def main():
    decoded = bytes.fromhex(sys.argv[1])
    print(BUFFER)
    print(fixed_xor(decoded, BUFFER))

if __name__ == "__main__":
    sys.exit(main())
