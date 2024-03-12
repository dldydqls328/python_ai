number = int(input("Input number : "))

is_prime_number = True
if number < 2:
    is_prime_number = False
else:
    i = 2
    while i*i < number:
        if number % i == 0:
            #is_primenumber = is_prime_number + 1
            is_prime_number = False  #Remove the plus operation
            break  #Exit the loop when the first divisor is found.
        print(i, end=" ")
        i += 1

#if is_prime_number == 0:
if is_prime_number:
    print(f"{number} is prime number")
else:
    print(f"{number} is NOT prime number")