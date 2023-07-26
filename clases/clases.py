import math

class Circulo:
    """
    >>> test.area()
    28.274333882308138
    >>> test.circumference()
    18.84955592153876
    >>> test.radio = 2
    >>> test.information()
    Has instanciado un círculo con las siguientes características:
    Radio: 2.00
    Área: 12.57
    Perímetro o Circunferencia: 12.57
    >>> test * 2
    Has instanciado un círculo con las siguientes características:
    Radio: 4.00
    Área: 50.27
    Perímetro o Circunferencia: 25.13
    """

    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self._radio = radio
        self.information()
        self.__str__()

    def __str__(self):
        return f"Círculo con radio: {self._radio:.2f}"

    def information(self):
        print("Has instanciado un círculo con las siguientes características:")
        print(f"Radio: {self._radio:.2f}")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro o Circunferencia: {self.circumference():.2f}")

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, new_radio):
        if new_radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self._radio = new_radio

    def area(self):
        return math.pi * self._radio ** 2

    def circumference(self):
        return 2 * math.pi * self._radio

    def __mul__(self, n):
        if n <= 0:
            raise ValueError("El número multiplicador debe ser mayor que 0")
        new_circle = Circulo(self._radio * n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'test': Circulo(3)})
    try:
        user_circle_radius = float(input("Ingrese un radio para crear un círculo: "))
        user_circle = Circulo(user_circle_radius)
        print("Área del círculo: ", user_circle.area())
        print("Perímetro del círculo: ", user_circle.circumference())

        user_circle.radio = int(input("Ingrese nuevo radio: "))
        print(user_circle.information())
        multiplied_circle = user_circle * int(input("Ingrese multiplicador: "))
    except ValueError as e:
        print("Se ha producido un error: ", e)

