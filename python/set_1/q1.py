import sys
import base64

def main():
    decoded = bytes.fromhex(sys.argv[1])
    b64_encoded = base64.b64encode(decoded)
    print(b64_encoded)

if __name__ == "__main__":
    sys.exit(main())
