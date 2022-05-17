def main():
  a_sum, b_sum = 0, 0
  for x in range(1, 101):
    a_sum += x*x
    b_sum += x
  print(b_sum * b_sum - a_sum)
main()