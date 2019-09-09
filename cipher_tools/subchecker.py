import sys

map = {ord(first) : second for first, second in zip(sys.argv[2], sys.argv[3])}

print(sys.argv[1].translate(map))
