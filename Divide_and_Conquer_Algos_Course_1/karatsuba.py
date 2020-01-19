"""
    Simple karatsuba multiplication
"""


class Multiply:
    """
        This class implements Karatsuba multiplication using a recursive approach
    """
    def __init__(self):
        pass

    def _pad_zeros(self, num: str, n_zeros: int, at_front=False) -> str:
        """
            takes in an string, returns padded string (at end or front)
        """
        zeros = '0'*n_zeros
        if at_front:
            return zeros + num
        return num + zeros

    def recursive_karatsuba_multiplication(self, num1: int, num2: int) -> int:
        """
            Takes in 2 integers, multiplies them recursively using
            karatsuba multiplication formula
        """
        num1, num2 = str(num1), str(num2)
        len_num1 = len(num1)
        len_num2 = len(num2)
        if len_num1 != len_num2:
            if len_num1 > len_num2:
                num2 = self._pad_zeros(str(num2), len_num1 - len_num2, at_front=True)
            else:
                num1 = self._pad_zeros(str(num1), len_num2 - len_num1, at_front=True)
        # length may changed here.
        # However, we now have both num1 and num2 of same length 
        len_num = len(num1)
        
        if len_num == 1:
            return int(num1) * int(num2)

        # split the num1, num2 into a, b, c, d
        a_s, b_s, c_s, d_s = num1[:len_num//2], num1[len_num//2:], num2[:len_num//2], num2[len_num//2:]
        a, b, c, d = int(a_s), int(b_s), int(c_s), int(d_s)

        # step1: comupute ac
        ac = self.recursive_karatsuba_multiplication(a, c)
        # step2: compute bd
        bd = self.recursive_karatsuba_multiplication(b, d)
        # step3 (Gauss trick): compute (ab * cd) to compute ab + bc 
        ab_bc =  self.recursive_karatsuba_multiplication( (a+b), (c+d)) - ac - bd

        # karatsuba formula
        # ac (with padded zeros on right) + ab_bc (with padded zeros on right) + ac
        
        # output = int(self._pad_zeros(str(ac), 2 * (len_num - len_num // 2), at_front=False))
        # output += int(self._pad_zeros(str(ab_bc), len_num - len_num//2, at_front=False))
        # output += bd

        # karatsuba formula
        # x.y = ((10 ^n) * ac) + ((10^(n/2)) * (ab+bc)) + bd
        output = ac * (10 ** (2 * (len_num - (len_num//2))))
        output += ab_bc * (10 ** (len_num - (len_num//2)))
        output += bd
        return output

    def iterative_karatsuba_multiplication(self, num1, num2):
        raise NotImplementedError


if __name__=="__main__":
    multiplyNums = Multiply()
    # n1 = 1234
    # n2 = 5678
    n1 = 123456
    n2 = 56789
    # n1 = 3141592653589793238462643383279502884197169399375105820974944592
    # n2 = 2718281828459045235360287471352662497757247093699959574966967627
    recursive_output= multiplyNums.recursive_karatsuba_multiplication(n1, n2)

    print('num1', n1)
    print('num2', n2)
    print('recursive_output output', recursive_output)
