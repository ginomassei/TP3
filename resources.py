import random
import style


# Creación de la clase participante.
class Participante:
    def __init__(self, nombre=None, continente=None, ranking=None):
        self.nombre = nombre
        self.continente = continente
        self.ranking = ranking
        self.puntaje = 0


# Funciones propias.
def to_string(participante):
    r = ''
    r += 'Nombre del competidor: ' + participante.nombre + ' | '
    r += ' Continente: ' + str(participante.continente) + ' | '
    r += ' Ranking: ' + str(participante.ranking)
    return r


def load(opt=0):
    # Carga el vector de registros.
    # Por defecto, realiza la carga de manera automática.
    if opt == 0:
        style.print_blue_text('Los artículos seran cargados de manera automática...')
    else:
        style.print_blue_text('Carga manual...')

    # Vector de participantes.
    v = [None] * 16

    # Lista con los 16 posibles nombres.
    nombres = ['AED', 'MAD', 'ALG', 'SOR', 'ACO', 'AM1', 'ASI', 'AM2',
               'SSL', 'PPR', 'SOP', 'DSI', 'COM', 'GDA', 'SIM', 'ECO']

    for i in range(len(v)):
        if opt == 1:  # Carga manual
            style.print_blue_text(f'\nParticipante número {i + 1}')

            nombre = input('Nombre del competidor: ')
            continente = validate_between(0, 4, 'Continente(entre 0 y 4): ')
            ranking = validate(0, 'Ranking: ')

        else:  # Carga automática
            nombre = random.choice(nombres)
            # Eliminación del nombre usado en la lista original.
            nombres.remove(nombre)

            continente = random.randint(0, 4)
            ranking = random.randint(0, 100)

        # Creo el registro con los datos, y lo agrego al arreglo de registros.
        v[i] = Participante(nombre, continente, ranking)

    return v


def match_generation(participants):
    first = 0
    last = -1

    n = len(participants)
    match_array = []

    while first < (n / 2):
        match_array.append([participants[first], participants[last]])
        first += 1
        last -= 1

    return match_array


def match_print(match_array):

    instancia = ''
    if len(match_array) == 8:
        instancia = 'Octavos de final'

    if len(match_array) == 4:
        instancia = 'Cuartos de final'

    if len(match_array) == 2:
        instancia = 'Semifinales'

    style.print_red_text('\nEnfrentamientos - ' + instancia)
    print()

    for i in range(len(match_array)):
        print(f"{match_array[i][0].nombre} vs {match_array[i][1].nombre}")


def match_simulation(match_array):

    c = 0
    suma = 0
    winners_array = []

    for i in range(len(match_array)):
        while c < 2:
            match_array[i][c].puntaje = random.randint(0, 1000)
            suma += match_array[i][c].puntaje
            c += 1

        if match_array[i][0].puntaje > match_array[i][1].puntaje:
            winners_array.append(match_array[i][0])

        else:
            winners_array.append(match_array[i][1])

        c = 0

    prom = round(suma / (len(match_array * 2)), 2)
    print('\nEl puntaje promedio obtenido por los equipos en esta instancia fue: ' + str(prom))

    return winners_array


def participants_per_continent(vec):
    continent_acum = [0] * 5
    for i in vec:
        continent_acum[i.continente] += 1
    return continent_acum


def show_participants_per_continent(data):
    style.print_red_text(f'\nParticipantes de América: {data[0]}')
    style.print_red_text(f'Participantes de Europa: {data[1]}')
    style.print_red_text(f'Participantes de Asia: {data[2]}')
    style.print_red_text(f'Participantes de Africa: {data[3]}')
    style.print_red_text(f'Participantes de Oceanía: {data[4]}')


def print_reg(vec):
    for i in vec:
        print(to_string(i))


def ranking_shell_sort(vec):
    # Utilizamos shell sort, porque si en un momento se desee ampliar el programa, ya tenemos un algoritmo de
    # ordenamiento lo suficientemente potente, para manejar grandes cantidades de datos.
    n = len(vec)
    h = 1

    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = vec[j]
            k = j - h
            while k >= 0 and y.ranking < vec[k].ranking:  # Efectúo la comparación basada en el ranking.
                vec[k+h] = vec[k]
                k -= h
            vec[k+h] = y
        h //= 3


def validate(value, message):
    # Valida el que el valor sea mayor al especificado en el parámetro.
    n = int(input(message))
    while n <= value:
        style.print_red_text('Valor no admitido.')
        n = int(input(message))
    return n


def validate_between(bottom, top, message):
    # Valida que el valor ingresado esté dentro del rango especificado en los parámetros.
    n = int(input(message))
    while n < bottom or n > top:
        style.print_red_text('Valor no admitido.')
        n = int(input(message))
    return n
