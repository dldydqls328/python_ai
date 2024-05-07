def print_fx(fx):
    texts = "f(x) = "
    expo = len(fx) - 1

    for i in range(len(fx)):
        coef = fx[i]
<<<<<<< HEAD

=======
>>>>>>> 44f67511960c9e498c2b6030a6df7b238f2e5429
        if coef == 0:
            expo = expo - 1
            continue
        if coef >= 0 and i != 0:
            texts = texts + "+"
<<<<<<< HEAD
        # texts = texts + str(coef) + "x^" + str(expo) + " "
        texts = texts + f"{coef}x^{expo} "
=======
        texts = texts + str(coef) + "x^" + str(expo) + " "
>>>>>>> 44f67511960c9e498c2b6030a6df7b238f2e5429
        expo = expo - 1
    return texts


<<<<<<< HEAD
def calculate_fx(fx, x):
    expo = len(fx) - 1
    result = 0

    for k in range(len(fx)):
        coef = fx[k]
=======
cofficient = [5, -2, 0, 6]

def cal_fx(fx, x):
    result = 0
    expo = len(fx) - 1
    for i in range (len(fx)):
        coef = fx[i]
>>>>>>> 44f67511960c9e498c2b6030a6df7b238f2e5429
        result = result + coef * x ** expo
        expo = expo - 1

    return result

<<<<<<< HEAD

coefficient = [5, -2, 0, 6]

print(print_fx(coefficient))
x = int(input("Input x value : "))
print(calculate_fx(coefficient, x))
=======
print(print_fx(cofficient))
x = int(input("Input x value : "))
print(cal_fx(cofficient, x))
>>>>>>> 44f67511960c9e498c2b6030a6df7b238f2e5429
