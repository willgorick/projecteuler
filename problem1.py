
def main():
  solution = 0
  for x in range(1000):
    if x%3 == 0 or x %5 == 0:
      solution += x
  print(solution)

main()