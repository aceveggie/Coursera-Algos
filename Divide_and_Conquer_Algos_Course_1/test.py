num1 = 1234
num2 = 5678

# num1 = 12345
# num2 = 56789
# num1 = 3141592653589793238462643383279502884197169399375105820974944592
# num2 = 2718281828459045235360287471352662497757247093699959574966967627


class Multiply:
    def __init__(self):
        pass
    def _pad_zeros(self, num: str, n_zeros: int, at_front=False) -> str:
        zeros = '0'*n_zeros
        if at_front:
            return zeros + num
        return num + zeros
    def karatsuba(self, num1: int, num2: int) -> int:
        num1_s, num2_s = str(num1), str(num2)
        lnum1 = len(num1_s)
        lnum2 = len(num2_s)
        if lnum1 != lnum2:
            if lnum1 > lnum2:
                num2_s = self._pad_zeros(num2_s, lnum1 - lnum2, at_front = True)
            else:
                num1_s = self._pad_zeros(num1_s, lnum2 - lnum1, at_front = True)
        lnum = len(num1_s)
        if lnum == 1:
            return num1 * num2
        a_s, b_s = num1_s[:lnum//2], num1_s[lnum//2:]
        c_s, d_s = num2_s[:lnum//2], num2_s[lnum//2:]
        a, b, c, d = int(a_s), int(b_s), int(c_s), int(d_s)
        print('a, b', a, b)
        print('c, d', c, d)
        ac = self.karatsuba(a, c)
        bd = self.karatsuba(b, d)
        ab_bc = self.karatsuba(a+b, c+d) - ac - bd

        # karatsuba formala
        # ac with (2 * (n - (n//2)) padded zeros in end)
        # + 
        # ab_bc with (2 * n//2) padded zeros in end
        # +
        # bd
        output = int(self._pad_zeros(str(ac), 2 * (lnum - (lnum//2)), at_front=False))
        output += int(self._pad_zeros(str(ab_bc), lnum - lnum//2, at_front=False))
        output += bd
        return output

if __name__=="__main__":
  a = Multiply()
  output = a.karatsuba(num1, num2)
  print('output', output)