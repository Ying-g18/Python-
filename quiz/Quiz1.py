#no1
#i = 1
#while i < 11:
    #print(i)
    #i = i + 1
#no2
#i = 1
#for i in range(1, 9):
    #for j in range(1, i):
        #print(j, end=" ")
    #print()
#no.3
#num = int(input("Enter a number : "))
#i = 1
#sum = 0

#while i <= num:
    #sum += i
    #i += 1
#print(f"The sum is {sum}")

#no.4

#num = int(input("Enter a positive integer : "))

#for i in range(1,11):
    #result = i * num
    #print(result)


#no.5
#my_list = input("Enter a list : ").split()
#my_list = list(map(int, my_list))
#temp = []

#for item in my_list:
    #if item % 5 == 0 and item <= 150:
        #if item < 500:
            #break
        #print(item)



#no.6

#num = int(input("Enter a positive integer greater than 10 : "))
#count = 1

#while num > 10:
    #num = (num/10)
    #count += 1
#print(count)

#no.7

#num = int(input("Enter any number : "))

#for i in range(num, 0, -1):
    #for j in range(i, 0, -1):
        #print(j, end=" ")
    #print()

#no.8

#my_list = input("Enter a list : ").split()
#my_list = list(map(int, my_list))
#my_list = my_list[::-1]
#print(my_list)

#no.9
#num = int(input("Enter a negative integer : "))

#for i in range(num, 0, 1):
    #print(i)


#no.10

#for i in range(5):
    #print(i)
#print("Done !")


#no.11

#num_1 = int(input("Enter a starting number : "))
#num_2 = int(input("Enter the ending number : "))

#for j in range(num_1, num_2+1, 1):
    #if j % 2 != 0 and j % 3 != 0 and j % 5 != 0 and j % 7 != 0:
        #print(j)

#no.12

a = 0
b = 1

for i in range(8):
    sum = a+b
    a = b
    b = sum
    print(sum)


#no.13

#num = int(input("Enter the number : "))
#fac = 1

#for i in range(num, 0, -1):
    #fac = fac * i
#print(f"Factorial of {num} is {fac}")

#no.14

#print("Given number : 76542")
#num = 76542
#reverse = (num % 10)*10000 + int((num % 100)/10)*1000 + int((num % 1000)/100) * 100 + int((num %10000)/1000)*10+int(num/10000)
#print(f"The reverse is {reverse}")


#no.15

#my_list = input("Enter a list : ").split()
#my_list = list(map(int, my_list))

#for item in my_list:
    #temp = my_list.index(item)
    #if temp % 2 != 0:
        #print(item, end=" ")

#no.16

#num = int(input("Enter a positive integer : "))

#for i in range(num+1):
    #c = i ** 3
    #print(f"Current number is {i} and the cube is {c}")

#no.17

#term = int(input("Enter the number of terms :"))
#a = 0
#b = 0

#for i in range(term):
    #sum = 2 * (10 ** i) + a
    #a = sum
    #b = b + a
#print(b)

#no.18

#for i in range(6):
    #for j in range(i):
        #print("*",end=" ")
    #print()
#for i in range(6):
    #for j in range(6, i, -1):
        #print("*",end=" ")
    #print()

