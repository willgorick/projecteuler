def main():
  found = False
  solution = 2520
  while not found:
    divisible = True
    solution += 2520
    for x in range(11, 21, 1):
      if solution % x != 0: 
        divisible = False
        break
    if divisible:
      found = True
  print(solution)
    

 

main()