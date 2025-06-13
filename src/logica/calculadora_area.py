class CalculadoraArea:
    """
        Clase que calcula areas de figuras geometricas
        Figuras implementadas:
            -circulo
            -rectangulo
            -triangulo
    """
    pi = 3.1416

    @staticmethod
    def calc_area_cirulo(radio: int or float) -> float:
        """
        Calcula el area de un circulo
        :param radio:
        :return: area de un circulo
        """
        return CalculadoraArea.pi*(radio**2)

    @staticmethod
    def calc_area_triangulo(base: int or float, altura: int or float) -> int or float:
        """
        Calcula el area de un triangulo
        :param base:
        :param altura:
        :return: area
        """
        return CalculadoraArea.calc_area_rectangulo(base, altura)/2

    @staticmethod
    def calc_area_rectangulo(base: int or float, altura: int or float) -> int or float:
        """
        Calcula el area de un rectangulo
        :param base:
        :param altura:
        :return:
        """
        return base*altura

    @staticmethod
    def calc_area_cuadrado(lado: int or float):
        """
        Calcula el area de un cuadrado
        :param lado:
        :return:
        """
        return CalculadoraArea.calc_area_rectangulo(lado, lado)
