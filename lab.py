import math

def function1(x):
    return math.cos(x) + math.tan(x)

def function2(x):
    return (1 / math.tan(x)) + math.sin(x)

def function3(x):
    return (x * math.log(x)) ** 3

def calculate_function(x):
    if x < 2.3:
        return function1(x)
    elif x < 2.7:
        return function2(x)
    else:
        return function3(x)

x = 2
while x <= 3:

    print(calculate_function(x))

    x += 0.1


print("\n\t task2")

for i in range(1, 11):
    x = i / 10
    k = 0
    calc_sum = 0
    val = 100500
    while abs(val) >= 0.001:
        val =  (x / ((2 * k - 1) * (2 * k + 3))) * math.cos(2 * k + 1)
        calc_sum += val
        k += 1
    
    print(calc_sum)
