# Implementacion de Insertion Sort por Luis Bajaña Í
from os_info import print_usr, print_os
from random import random
from time import time_ns

def gen_sample(n=10):
    return [random() for i in range(n)]

def insertion_sort(A):
    for j in range(1, len(A)):
       # print(f'j = {j}')
        key = A[j]
        # print( f'key at {j} is {key}')
        i = j - 1
        # print(f'testing previous key: {i} => {A[i]} | {A[i] > key} ')
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        #    print(f'i= {i}')
        A[i+1] = key


def as_interval(ns):
    if ns == 0:
        return "0 nanosegundos"

    conversiones = [
        (365 * 24 * 60 * 60 * 1_000_000_000, "año", "años"),
        (30 * 24 * 60 * 60 * 1_000_000_000, "mes", "meses"),
        (7 * 24 * 60 * 60 * 1_000_000_000, "semana", "semanas"),
        (24 * 60 * 60 * 1_000_000_000, "día", "días"),
        (60 * 60 * 1_000_000_000, "hora", "horas"),
        (60 * 1_000_000_000, "minuto", "minutos"),
        (1_000_000_000, "segundo", "segundos"),
        (1_000_000, "milisegundo", "milisegundos"),
        (1_000, "microsegundo", "microsegundos"),
        (1, "nanosegundo", "nanosegundos")
    ]

    partes = []
    ns_restantes = abs(ns)

    for ns_unidad, singular, plural in conversiones:
        if ns_restantes >= ns_unidad:
            cantidad = ns_restantes // ns_unidad
            ns_restantes = ns_restantes % ns_unidad

            unidad = singular if cantidad == 1 else plural
            partes.append(f"{cantidad} {unidad}")

            if len(partes) >= 2:
                break

    if not partes and ns != 0:
        partes = [f"{ns} nanosegundos"]

    resultado = ", ".join(partes)
    if ns < 0:
        resultado = f"-{resultado}"

    return resultado

if __name__ == '__main__':
    print_usr()
    print_os()
    samples = 6
    for i in range(samples+1):
        max_items = 10**i
        print(f'+-----------[ Muestra de n={max_items} ]----------+')
        init_sample_t = time_ns()
        sample = gen_sample(max_items)
        end_sample_t = time_ns()
        print(f'[~] Tiempo en generar muestra (n = {max_items}): {as_interval(end_sample_t - init_sample_t)}' )

        init_sort_t = time_ns()
        insertion_sort(sample)
        end_sort_t = time_ns()
        print(f'[t] Tiempo en ordenar muestra: {as_interval(end_sort_t - init_sort_t)}')
        print('---------------------------------------')

    # a = gen_sample()
    # print(a)
    # insertion_sort(a)
    # print(a)
