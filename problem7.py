import math

def main():
  #establish sieve using 2 * prime estimate formula
  prime_n = 10001
  p_n = int( 2 * prime_n * math.log(prime_n))
  sieve = [True] * p_n

  primes_seen = 0
  for i in range(2, p_n):
    if sieve[i]:
      primes_seen += 1
      if primes_seen == prime_n:
        print(i)
        break
      for j in range(2*i, p_n, i):
        sieve[j] = False
main()