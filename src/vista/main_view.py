"""
    Clase que controla el view_components
"""

from PyQt6.QtWidgets import QMainWindow, QApplication
from src.vista.view_components import Ui_MainWindow
from src.logica.calculadora_area import CalculadoraArea
import sys


class Calculadora(QMainWindow):
    """
    Clase principal de la aplicación que gestiona la interfaz gráfica
    y la lógica para calcular el área de distintas figuras geométricas.
    """

    def __init__(self):
        """
        Inicializa la interfaz y conecta los eventos de los componentes.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSeleccionarCalculadora.currentIndexChanged.connect(
            self.cambiar_vista
        )
        self.ui.pushButton.clicked.connect(self.calcular_area)

        self.configurar_enter_para_inputs()
        self.establecer_funciones()

    def establecer_funciones(self):
        """
        Asocia cada índice del ComboBox a su función de cálculo correspondiente
        y a las funciones que recuperan los valores de los inputs.
        """
        self.calculadora = {
            0: [CalculadoraArea.calc_area_cirulo, self.ui.inpRadio.text],
            1: [
                CalculadoraArea.calc_area_rectangulo,
                self.ui.inpBaseRect.text,
                self.ui.inpAlturaRect.text,
            ],
            2: [CalculadoraArea.calc_area_cuadrado, self.ui.inpLado.text],
            3: [
                CalculadoraArea.calc_area_triangulo,
                self.ui.inpBaseTri.text,
                self.ui.inpAlturaTri.text,
            ],
        }

    def cambiar_vista(self, index):
        """
        Cambia la página activa del QStackedWidget dependiendo
        de la figura seleccionada.

        :param index: Índice del ComboBox seleccionado
        """
        self.ui.stackedWidget.setCurrentIndex(index)

    def calcular_area(self):
        """
        Obtiene los datos ingresados, calcula el área usando
        la función correspondiente, y muestra el resultado.
        """
        index = self.ui.cbSeleccionarCalculadora.currentIndex()
        data = self.calculadora.get(index)
        calculator = data[0]

        try:
            datos = [float(fn()) for fn in data[1:]]
            area = calculator(*datos)
            self.ui.inpArea.setText(f"{area:.2f}")
        except ValueError:
            self.ui.inpArea.setText("Entrada inválida")

    def configurar_enter_para_inputs(self):
        """
        Configura los eventos de tecla Enter para cada input,
        de modo que se avance al siguiente campo o se calcule
        el área directamente.
        """
        # Círculo
        self.ui.inpRadio.returnPressed.connect(self.calcular_area)

        # Rectángulo
        self.ui.inpBaseRect.returnPressed.connect(
            lambda: self.ui.inpAlturaRect.setFocus()
        )
        self.ui.inpAlturaRect.returnPressed.connect(self.calcular_area)

        # Cuadrado
        self.ui.inpLado.returnPressed.connect(self.calcular_area)

        # Triángulo
        self.ui.inpBaseTri.returnPressed.connect(
            lambda: self.ui.inpAlturaTri.setFocus()
        )
        self.ui.inpAlturaTri.returnPressed.connect(self.calcular_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec())
