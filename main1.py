import math

class Vector:
    def __init__(self, coordinates):
        if not isinstance(coordinates, list):
            raise ValueError("Координаты вектора должны быть заданы списком.")
        if not all(isinstance(coord, (int, float)) for coord in coordinates):
            raise ValueError("Координаты вектора должны быть числами.")
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Можно складывать только векторы.")
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны быть одной размерности.")
        return Vector([a + b for a, b in zip(self.coordinates, other.coordinates)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Можно вычитать только векторы.")
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны быть одной размерности.")
        return Vector([a - b for a, b in zip(self.coordinates, other.coordinates)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Умножение вектора на скаляр
            return Vector([a * other for a in self.coordinates])
        elif isinstance(other, Vector):
            # Скалярное произведение
            if self.dimension != other.dimension:
                raise ValueError("Векторы должны быть одной размерности.")
            return sum(a * b for a, b in zip(self.coordinates, other.coordinates))
        else:
            raise ValueError("Неподдерживаемый тип для умножения.")

    def __rmul__(self, scalar):
        # Умножение скаляра на вектор (скаляр * вектор)
        return self.__mul__(scalar)

    def dot(self, other):
        # Скалярное произведение
        return self.__mul__(other)

    def cosine(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Косинус угла можно вычислить только между векторами.")
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны быть одной размерности.")
        dot_product = self.dot(other)
        norm_self = self.norm()
        norm_other = other.norm()
        if norm_self == 0 or norm_other == 0:
            raise ValueError("Один из векторов имеет нулевую длину.")
        return dot_product / (norm_self * norm_other)

    def norm(self):
        # Евклидова норма
        return math.sqrt(sum(a**2 for a in self.coordinates))

    def __repr__(self):
        return f"Vector({self.coordinates})"

# Пример использования:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Сложение
v3 = v1 + v2
print("v1 + v2:", v3)

# Вычитание
v4 = v1 - v2
print("v1 - v2:", v4)

# Скалярное произведение
dot_product = v1 * v2
print("Скалярное произведение v1 и v2:", dot_product)

# Умножение на скаляр
v5 = v1 * 2
print("v1 * 2:", v5)

# Косинус угла
cosine = v1.cosine(v2)
print("Косинус угла между v1 и v2:", cosine)

# Евклидова норма
norm_v1 = v1.norm()
print("Евклидова норма v1:", norm_v1)