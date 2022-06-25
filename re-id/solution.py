def solution(i):
    def is_prime(n):
        """Assumes n a positive integer, n > 1
           Returns True is n is a prime number, False otherwise."""
        # test each number from 2
        for j in range(2, n):
            if not (n % j):
                return False
        # n is necessarily prime
        return True

    def get_primes_str(i):
        """Assumes i a positive integer
           Returns a string of prime numbers"""
        # initialize prime string
        prime_str = ""
        # start with 2 as first prime number
        num = 2
        # add primes to prime_string until string longer than index + 5
        while len(prime_str) < (i + 5):
            if is_prime(num):
                prime_str += str(num)
            num += 1
        return prime_str[i:i + 5]

    return get_primes_str(i)


def main():
    # test 1
    print("Test 1 - solution(0)")
    print("Expected output: 23571")
    print(f"Actual output: {solution(0)}")

    # test 2
    print("Test 1 - solution(3)")
    print("Expected output: 71113")
    print(f"Actual output: {solution(3)}")


if __name__ == "__main__":
    main()