import math

def main():
  prime_n = 2000000
  sieve = [True] * 2000000
  product = 0
  for i in range(2, prime_n):
    if sieve[i]:
      product += i
      for j in range(2*i, prime_n, i):
        sieve[j] = False
  print(product)
main()