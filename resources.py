import random


class Participante:
    def __init__(self, nombre=None, continente=None, ranking=None):
        self.nombre = nombre
        self.continente = continente
        self.ranking = ranking


def to_string(participante):
    r = ''
    r += ('Nombre del competidor: ' + participante.nombre + ' | ')
    r += (' Continente: ' + str(participante.continente) + ' | ')
    r += (' Ranking: ' + str(participante.ranking))

    return r


def random_load(vec):
    # Lista con los 16 posibles nombres
    nombres = ['AED', 'MAD', 'ALG', 'SOR', 'ACO', 'AM1', 'ASI', 'AM2',
               'SSL', 'PPR', 'SOP', 'DSI', 'COM', 'GDA', 'SIM', 'ECO']

    # Generación de un vector de participantes seleccionando los datos de forma aleatoria
    for i in range(len(vec)):
        nombre = random.choice(nombres)
        continente = random.randint(0, 4)
        ranking = random.randint(0, 100)

        vec[i] = Participante(nombre, continente, ranking)

        # Eliminación del nombre usado en la lista original
        nombres.remove(nombre)


def manual_load(vec):
    # Generación de un vector de participantes cargando los datos manualmente
    for i in range(len(vec)):
        print('Competidor ' + str(i+1))
        nombre = input('Nombre del competidor: ')
        continente = verify_in_range(int(input('Continente(entre 0 y 4): ')), 0, 5)
        ranking = int(input('Ranking: '))

        vec[i] = Participante(nombre, continente, ranking)


def match_generation():
    pass


def match_simulation():
    pass


def verify_in_range(num, n, x):
    while not(num in range(n, x)):
        print('Error. Debe ingresar un valor entre ' + str(n) + ' y ' + str(x - 1))
        num = int(input('Continente(entre 0 y 4): '))

    return num


def print_reg(vec):
    for i in vec:
        print(to_string(i))
