#!/usr/bin/env python3
import sys


def decode_level09(data):
    decoded = bytearray()
    i = 0

    for b in data:
        value = b - i

        # keep value inside valid byte range (0–255)
        if value < 0:
            value += 256

        decoded.append(value)
        i = i + 1

    return decoded.decode(errors="ignore")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <encoded_file>")
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        encoded = f.read()

    print(decode_level09(encoded))
