"""
    Ejecuta las ventanas principales
"""

from src.vista.main_view import Calculadora, QApplication, sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec())
