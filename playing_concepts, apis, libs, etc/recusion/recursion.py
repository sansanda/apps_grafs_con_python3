import sys

sys.setrecursionlimit(15000)


def recurse(actual_depth, max_depth):
    actual_depth = actual_depth + 1
    print(actual_depth)
    if actual_depth > max_depth - 2:
        return None
    recurse(actual_depth, max_depth)


if __name__ == "__main__":
    max_depth = 15000
    while True:
        recurse(0, max_depth)
