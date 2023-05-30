num = int(input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

if num % 2 != 0 and num in primes:
    print("zoj")
else:
    print("fard")