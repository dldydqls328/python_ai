number = int(input("Input number : "))

if number < 2:
    count = 1
else:
    count = 0
    for i in range (2, number):
        if number % i == 0:
            count = count + 1
            break
        print(1, end=" ")

if count == 0:
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")