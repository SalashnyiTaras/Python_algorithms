class Complex:
    """__str__ method and redefining standard methods"""
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        str_re = str(self.re)
        if self.im > 0:
            str_im = '+' + str(self.im) + 'i'
        else:
            str_im = str(self.im) + 'i'
        return str_re + str_im

    def __add__(self, other):
        sum_re = self.re + other.re
        sum_im = self.im + other.im
        return Complex(sum_re, sum_im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            image = self.re * other.re - self.im * other.im
            real = self.re * other.im + self.im * other.re
            return Complex(real, image)
        elif isinstance(other, int) or isinstance(other, float):
            real = self.re * other
            image = self.im * other
            return Complex(real, image)
    __rmul__ = __mul__


a = Complex(1, 2)
b = Complex(3, -4.5)
print(a)
print(b)
print(a + b)
print(a * b)
print(3.5 * a)
print(a * 3.5)