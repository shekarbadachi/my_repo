#filter and lambda usage
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_no = list(filter(lambda x: x % 2 == 0, num))
print odd_no
mul_of_three = [y for y in range(1, 31) if (y % 3) == 0]
print mul_of_three
