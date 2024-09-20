# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

def evenOdd(input_num):
    if(input_num % 2 == 0):
        return 'even'
    else:
        return 'odd'

def SumofNumbers(input_num):
    total_sum = sum(range(1, input_num + 1))
    return total_sum

def max(n1, n2, n3):
    if(n1 >= n2 and n1 >= n3):
        return n1
    elif(n2 >= n1 and n2 >= n3):
        return n2   
    else:
        return n3
