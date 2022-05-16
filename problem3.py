def main():
  n = 600851475143
  div = 2
  factors = []
  while n > 1:
    while n%div == 0:
      factors.append(div)
      n /= div
    div += 1
  print(max(factors))

main()