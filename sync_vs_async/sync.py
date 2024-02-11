# Synchronous code example
import time


def fetch_data():
    print("Start fetching")
    time.sleep(2)  # Simulating a blocking I/O operation
    print("Done fetching")
    return {'data': 1}


def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(1)


def main():
    value = fetch_data()
    print(value)
    print_numbers()


main()

# Output will be:
#
# Start fetching
# Done fetching
# {'data': 1}
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
