def main():
  solution = 2
  curr_fib = 2
  prev_fib = 1
  while (curr_fib < 4000000):
    next_fib = curr_fib + prev_fib
    if next_fib > 4000000:
      break
    prev_fib = curr_fib
    curr_fib = next_fib
    if curr_fib %2 == 0:
      solution += curr_fib
  print(solution)
main()