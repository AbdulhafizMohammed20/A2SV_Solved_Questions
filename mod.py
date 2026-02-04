# Enter your code here. Read input from STDIN. Print output to STDOUT
def result_pow(a,b,m):
    power = a**b
    result_pow = power % m
    print(power)
    print(result_pow)

a = int(input())
b = int(input())
m = int(input())

result_pow(a,b,m)
