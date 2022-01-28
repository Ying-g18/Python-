
stop = False
sum = 0
while not stop:
      n = int(input("Enter a positive integer : "))
      if n >= 0:
            sum += n
      else:
            stop = True

print(sum)
