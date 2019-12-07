
class Multiply(object):
    def __init__(self):
        pass
    def calc_karatsuba_multiplication(self, num1, num2):
        a, b = num1[:len(num1)//2], num1[len(num1)//2:]
        c, d = num1[:len(num1)//2], num1[len(num1)//2:]
        return a
        


num1 = '3141592653589793238462643383279502884197169399375105820974944592'
num2 = '2718281828459045235360287471352662497757247093699959574966967627'

multiplyNums = Multiply()
output = multiplyNums.calc_karatsuba_multiplication(num1, num2)

print('num1', num1)
print('num2', num2)
print('output', output)

