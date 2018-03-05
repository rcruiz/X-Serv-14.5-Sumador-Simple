#!/usr/bin/python3

import sys


def suma(operando1, operando2):
    return operando1 + operando2


def resta(operando1, operando2):
    return operando1 - operando2


def mult(operando1, operando2):
    return operando1 * operando2


def div(operando1, operando2):
    try:
        return operando1 / operando2
    except ZeroDivisionError:
        return(" No se puede dividir entre 0.")

funciones = {
    'suma': suma,
    'resta': resta,
    'multiplica': mult,
    'divide': div
}


if __name__ == "__main__":
    try:
        funcion = str(sys.argv[1])
        operando1 = float(sys.argv[2])
        operando2 = float(sys.argv[3])
    except IndexError:
        sys.exit("Introduce python calculadora.py funcion operando1 operando2")
    except ValueError:
        sys.exit("Introduzca operandos válidos: enteros o float con punto")
    try:
        res = funciones[funcion](operando1, operando2)
    except KeyError:
        sys.exit("Operaciones permitidas: suma, resta, multiplica, divide")
    print(res)
