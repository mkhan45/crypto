from collections import Counter
import sys

print(sys.argv[1:])
common = "ETAOINSRHLDCUMFPGWYBVKXJQZ"
print("Counts of all letters:")
print(list(zip(Counter(''.join(sys.argv[1:])).most_common(), common)))
print("Counts of first letters:")
print(Counter([word[0] for word in ' '.join(sys.argv[1:]).split()]).most_common())
print("TOAWBCDSFMRHIYEGINPUJK")
