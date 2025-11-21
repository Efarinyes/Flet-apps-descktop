import flet as ft
from calculatorClass import CalculatorApp

def main(page: ft.Page):
    page.title = 'Calculadora App'
    calc = CalculatorApp()
    page.add(calc)


ft.app(main)