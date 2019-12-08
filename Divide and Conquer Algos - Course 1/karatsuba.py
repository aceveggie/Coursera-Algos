import sys

#sys.setrecursionlimit(10000)

class Multiply(object):
    def __init__(self):
        pass
    
    def pad_leading_zeros(self, num1, num2):
        n_zeros = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            # pad zeros in num2 at front
            return num1, '0'*n_zeros + num2
        return '0'*n_zeros + num1, num2
    
    def pad_trailing_zeros(self, num1, n_zeros):
        return num1 + '0'*n_zeros

            
    def recursive_karatsuba_multiplication(self, num1, num2):
        num1, num2 = str(num1), str(num2)

        if(len(num1) != len(num2)):
            num1, num2 = self.pad_leading_zeros(num1, num2)
        assert(len(num1) == len(num2))
        n = len(num1)
        
        # define your base case (for last case in recursion)
        if n==1:
            return int(num1)*int(num2)
        a, b = int(num1[:n//2]), int(num1[n//2:])
        c, d = int(num2[:n//2]), int(num2[n//2:])

        print('a',a,'b',b,'c',c,'d',d)
        ac = self.recursive_karatsuba_multiplication(a, c)
        bd = self.recursive_karatsuba_multiplication(b, d)
        # a_b = a + b
        # c_d = c + d
        # ab_cd = self.recursive_karatsuba_multiplication(a_b, c_d) - ac - bd
        # return int((10**n) * ac) +  int((10**(n/2)) * (ab_cd)) + int(bd)
        ad = self.recursive_karatsuba_multiplication(a, d)
        bc = self.recursive_karatsuba_multiplication(b, c)
        return int((10**n) * ac) +  int((10**(n//2)) * (ad + bc)) + int(bd)

    # def calc_karatsuba_multiplication(self, num1, num2):
        '''
        non recursive: basic solution
        '''
        # print(len(num1) == len(num2))
        # len1 = len(num1)
        # len2 = len(num2)

        # a, b = int(num1[:len(num1)//2]), int(num1[len(num1)//2:])
        # c, d = int(num2[:len(num2)//2]), int(num2[len(num2)//2:])
        
        # ac = a * c # step 1
        # bd = b * d # step 2
        # step3 = (a+b)*(c+d)
        # step4 = step3 - bd - ac
        # ad = a*d
        # bc = b*c
        # print('a',a)
        # print('b',b)
        # print('c',c)
        # print('d',d)
        # print('len1', len1)
        # print('len2', len2)

        # print('step1 ac', ac)
        # print('step2 bd', bd)
        # print('step3', step3)
        # print('step4', step4)
        
        # output = (10**len1) * ac
        # output += (10**(len1/2)) * (ad+bc)
        # output += bd
        # return output

        
num1 = '3141592653589793238462643383279502884197169399375105820974944592'
num2 = '2718281828459045235360287471352662497757247093699959574966967627'

# num1 = '5678'
# num2 = '1234'

multiplyNums = Multiply()
# output = multiplyNums.calc_karatsuba_multiplication(num1, num2)
output= multiplyNums.recursive_karatsuba_multiplication(num1, num2)

print('num1', num1)
print('num2', num2)
print('output', output)

