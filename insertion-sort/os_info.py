from os import name, cpu_count
from psutil import cpu_count as cpu, virtual_memory

def print_os():
    total_mem = virtual_memory().total
    print(
            '+----------------------------------------------------+',
            f'Total Physical CPU: {cpu(False)}', 
            f'Total CPU: {cpu_count()}',
            f'Nombre S.O: {name}',
            f'Total Memoria (B): {total_mem} | {round(total_mem / 1024 / 1024 / 1024, 2) }GB',
            '+----------------------------------------------------+',
            sep='\n')

def print_usr():
    print(
            '+----------------------+-------------+',
            '|     Neoterux         | Luis Bajaña |',
            '+----------------------+-------------+',
            sep='\n')


if __name__ == '__main__':
    print_os()
    print_usr()
