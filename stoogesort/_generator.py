#!/usr/bin/python
import numpy as np
from argparse import ArgumentParser


def generate_random_array(n: int = 10):
    ''' Genera un arreglo de valores aleatorios de tamaño n 
       n: int Cantidad de elementos
    '''
    return np.random.randint(low=0, high=2e9, size=n)

if __name__ == '__main__':
    argument_parser = ArgumentParser(
        prog='array random number generator for numpy',
        description='Genera números aleatorios'
        )
    argument_parser.add_argument('filename',)
    argument_parser.add_argument('-n', required=True)
    args = vars(argument_parser.parse_args())
    
    array = generate_random_array(int(args['n']))
    np.savetxt(args['filename'], array)
