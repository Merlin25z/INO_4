import math

class ComplexNumber:
    def __init__(self, real=0, imaginary=0, magnitude=None, angle=None):
        if magnitude is not None and angle is not None:
            # Создание из полярной формы
            self.real = magnitude * math.cos(angle)
            self.imaginary = magnitude * math.sin(angle)
        else:
            # Создание из алгебраической формы
            self.real = real
            self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)

    def get_algebraic_form(self):
        return self.real, self.imaginary

    def get_polar_form(self):
        magnitude = math.sqrt(self.real**2 + self.imaginary**2)
        angle = math.atan2(self.imaginary, self.real)
        return magnitude, angle

    def __repr__(self):
        return f"ComplexNumber(real={self.real}, imaginary={self.imaginary})"

# Пример использования:
# Создание комплексного числа в алгебраической форме
z1 = ComplexNumber(3, 4)
print("z1 в алгебраической форме:", z1.get_algebraic_form())
print("z1 в полярной форме:", z1.get_polar_form())

# Создание комплексного числа в полярной форме
z2 = ComplexNumber(magnitude=5, angle=math.radians(45))
print("z2 в алгебраической форме:", z2.get_algebraic_form())
print("z2 в полярной форме:", z2.get_polar_form())

# Операции с комплексными числами
z3 = z1 + z2
print("z1 + z2:", z3.get_algebraic_form())

z4 = z1 - z2
print("z1 - z2:", z4.get_algebraic_form())

z5 = z1 * z2
print("z1 * z2:", z5.get_algebraic_form())

z6 = z1 / z2
print("z1 / z2:", z6.get_algebraic_form())