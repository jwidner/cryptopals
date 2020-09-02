import sys
from string import ascii_lowercase, punctuation, digits, whitespace

# letter frequency table
# source: <https://en.wikipedia.org/wiki/Letter_frequency>
FREQUENCY = \
    {'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043,  'e': 0.13,    'f': 0.022,
     'g': 0.02,  'h': 0.061, 'i': 0.07,  'j': 0.0015, 'k': 0.0077,  'l': 0.04,
     'm': 0.024, 'n': 0.067, 'o': 0.075, 'p': 0.019,  'q': 0.00095, 'r': 0.06,
     's': 0.063, 't': 0.091, 'u': 0.028, 'v': 0.0098, 'w': 0.024,   'x': 0.0015,
     'y': 0.02,  'z': 0.00074}

def xor(ciphertext):
    """Yield Single-byte XOR against the cipher for each possible byte."""
    for byte in range(255):
        yield bytes(byte^x for x in ciphertext)

def freq(c, b):
    count = 0
    for x in b:
        if x == c:
            count += 1
    return count/len(b)

def score(b: bytes):
    """Best score is 0."""
    # decode bytes to ascii
    try:
        b = b.decode().lower()
    except UnicodeDecodeError:
        return float('inf')
    # discard strings containing weird characters
    valid = ascii_lowercase + punctuation + whitespace + digits
    for c in b:
        if not c in valid:
            return float('inf')
    # score what's left, lower=better
    score = 0
    for c in ascii_lowercase:
        score += abs(freq(c, b) - FREQUENCY[c])
    return score

def main():
    decoded = bytes.fromhex(sys.argv[1])
    l = [x for x in xor(decoded)]
    l.sort(key=score)
    print(l[:5])

if __name__ == "__main__":
    sys.exit(main())
