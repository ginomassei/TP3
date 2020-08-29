import resources as rs


def option1(participantes):
    rs.manual_load(participantes)


def option2(participantes):
    rs.random_load(participantes)


def main():
    participantes = 16 * [None]  # Creación del vector contenedor de los participantes.
    option = 0

    while option != -1:
        print('\nMenú de opciones:')
        print('1 - Cargar el vector de competidores de forma manual.')
        print('2 - Cargar el vector de competidores de forma automática.')

        option = int(input('\nIngrese su opción: '))

        if option == 1:
            option1(participantes)

        if option == 2:
            option2(participantes)


if __name__ == "__main__":
    main()
