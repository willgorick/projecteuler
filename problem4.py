def main():
  solution = 0
  for x in range(0, 999):
    for y in range(0, 999):
      if (x*y == reverse(x*y) and x*y > solution):
        solution = x*y
  print(solution)

def reverse(n):
  m = 0;
  while n > 0:
    m = m * 10 + n % 10;
    n = n / 10;
  return m;

main()

