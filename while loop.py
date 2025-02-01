#  example 1
#index  0  1  2  3  4
lst = [10,20,30,40,50,]
product = 1
index = 0 # = 10
while index < len(lst):  # index = 0 lst = 5  0<5 if true enters while true
    product *= lst[index] 
    index += 1
    print("Product is: {}".format(product))

#  example 2
numbers = [1, 2, 3]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
else:
    print("no items left in the list")

#  example 3
num = int(input("Enter a number: "))
isDivisible = False;
i = 2;
while i<num:
    if num % i == 0:
        isDivisible = True;
        print("{}is Divisible by {}".format(num,i))
    i += 1;
    
if isDivisible:
    print("{} is not a prime number".format(num))
else:
     print("{} is a prime number".format(num))
