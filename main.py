import numpy as np
from math import gcd
from fractions import Fraction as frac

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def checkPrime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if (count == 2):
        count = 0
        return 1
    else:
        count = 0
        return 0


def nthPrime(num):
    num = int(num)
    number = 1
    count = 0
    temp = 1
    while (temp):
        if (checkPrime(number)):
            count = count + 1
        if (count == num):
            print(num, " (st,nd,th) prime is ", number)
            temp = 0
            return number
        number = number + 1


def countPrime(num=0):
    count = 0
    num = int(num)
    numbers = [];
    for i in range(1, num + 1):
        if (checkPrime(i)):
            count = count + 1
            numbers.append(i)

    print("Has ", count, "prime numbers from 0 to ", num)
    print(numbers)
    return count, numbers


def fermatNumber(num):
    temp = 1
    count = 1

    while (temp):
        testNum = pow(2, pow(2, count)) + 1
        if (testNum == num):
            print(num, " is a Fermat Number")
            return (str(num) + " IS A FERMAT NUMBER \n")
            temp = 0
        elif (testNum > num):
            temp = 0
        else:
            count = count + 1
    return


def mersenePrime(num):
    temp = 1
    count = 1
    while (temp):
        testNum = pow(2, count) - 1
        if (testNum == num):
            print(num, " is a Mersenne Prime number")
            return (str(num) + " IS A MERSENNE PRIME \n")
        elif (testNum > num):
            temp = 0
        else:
            count = count + 1
    return


def factorialPrime(num):
    temp = 1
    count = 0
    while (temp):
        facNum1 = factorial(count) + 1
        facNum2 = factorial(count) - 1

        if (facNum1 == num or facNum2 == num):
            print(num, " is a Factorial Prime")
            temp = 0
            return (str(num) + " IS A FACTORIAL PRIME \n")
        elif (facNum1 > num):
            temp = 0
        else:
            count = count + 1
    return


def cousinPrime(num):
    if checkPrime(num + 4):
        print(num + 4, " is the Cousin Prime of ", num)
        return str(num + 4) + " IS COUSIN PRIME OF " + str(num) + "\n"

    if checkPrime(num - 4):
        print(num - 4, " is the Cousin Prime of ", num)
        return str(num - 4) + " IS COUSIN PRIME OF " + str(num) + "\n"

    return


def sexyPrime(num):
    if (checkPrime(num + 6)):
        print(num + 6, " is the Sexy Prime of ", num)
        return (str(num + 6) + " IS SEXY PRIME OF " + str(num) + "\n")
    if (checkPrime(num - 6)):
        print(num - 6, " is the Sexy Prime of ", num)
        return (str(num - 6) + " IS SEXY PRIME OF " + str(num) + "\n")
    return


def twinPrime(num):
    if (checkPrime(num + 2)):
        print(num + 2, " is the Twin Prime of ", num)
        return (str(num + 2) + " IS TWIN PRIME OF " + str(num) + "\n")
    if (checkPrime(num - 2)):
        print(num - 2, " is the Twin Prime of ", num)
        return (str(num - 2) + " IS TWIN PRIME OF " + str(num) + "\n")
    return


def balancePrime(num):
    previous = 0
    after = 0
    temp = 1
    count = num + 1
    for i in range(num - 1, 0, -1):
        if (checkPrime(i)):
            previous = i
            break

    while (temp):
        if (checkPrime(count)):
            after = count
            temp = 0
        else:
            count = count + 1

    if ((previous + after) / 2 == num):
        print(num, " is a Balanced Prime number")
        return (str(num) + " IS BALANCED PRIME \n")
    else:
        return
    return

##methods for eular functions
def gcd (p,q):
    while q != 0 :
        p,q=q,p%q
    return p

def is_coprime(x,y):
    return gcd(x,y) ==1

def phi_func(x):
    if x ==1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return n

def eularPiFunction(num):
    num = int(num)
    integers = phi_func(num)
    # print(integers)
    return integers

def remove_eponent(value):
    decimal = value.split('e')
    ret_val = format(((float(decimal[0]))*(10**int(decimal[1]))),'.8f')
    return ret_val

def awFunction(num):
    num = int(num)
    numbers = eularPiFunction(num)
    # numbers = np.array(numbers)
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm =lcm * i // gcd(lcm, i)

    tot = 0
    for j in range(0, len(numbers)):
        tot_temp = tot + lcm / numbers[j]
        tot = tot + lcm // numbers[j]

    return tot_temp,tot/pow(num,2),tot%pow(num,2)


def mainFunc(num):
    i = 0
    count = 0
    results = []
    num = int(num)
    if (num >= 1):
        if (checkPrime(num)):
            print(num, " is a prime number")
            results.append(str(num) + " IS A PRIME NUMBER\n")
            if (balancePrime(num)):
                results.append(balancePrime(num))
            if (cousinPrime(num)):
                results.append(cousinPrime(num))
            if (twinPrime(num)):
                results.append(twinPrime(num))
            if (sexyPrime(num)):
                results.append(sexyPrime(num))
            if (mersenePrime(num)):
                results.append(mersenePrime(num))
            if (fermatNumber(num)):
                results.append(fermatNumber(num))
            if (factorialPrime(num)):
                results.append(factorialPrime(num))
            count = 0
        else:
            print(num, " is not a prime number")
            results.append(str(num) + " IS NOT A PRIME\n")
            count = 0
    elif (num < 1 or type(num) == str):
        print("Enter a valid number")
    return results
# while(1):
#     print("********* Prime Number Calculater *********\n")
#     print("1. Number of Prime Numbers")
#     print("2. Check Prime")
#     print("3. nth prime")
#     temp = int(input("Enter your choice : "))
#     num = int(input("Enter a number (Enter only a number) : "))
#     if(temp == 1):
#         countPrime(num)
#     elif(temp == 2):
#         mainFunc(num)
#     elif(temp == 3):
#         nthPrime(num)
#     else:
#         print("Invalid....!")
#     print("\n")
