import math

def main():
  solution = 0
  a = 1
  b = 1
  for a in range(100,500):
    for b in range(100,500):
      c_sqr = a*a + b*b
      c = math.sqrt(c_sqr)
      if a + b + c == 1000:
        solution = int(a*b*c)
        break
  print(solution);
main()