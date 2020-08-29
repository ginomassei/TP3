import resources as rs


def option1(participantes):
    rs.manual_load(participantes)
    rs.ranking_shell_sort(participantes)


def option2(participantes):
    rs.random_load(participantes)
    rs.ranking_shell_sort(participantes)


def option3(participantes):
    rs.print_reg(participantes)


def option4(participantes):
    pass


def main():
    participantes = 16 * [None]  # Creación del vector contenedor de los participantes.
    option = -1

    while option != 0:
        print('\nMenú de opciones:')
        print('1 - Cargar el vector de competidores de forma manual.')
        print('2 - Cargar el vector de competidores de forma automática.')
        print('3 - Mostrar el vector cargado.')
        print('4 - Generar competición.')

        print('0 - Salir.')

        option = int(input('\nIngrese su opción: '))

        if option == 1:
            option1(participantes)

        if option == 2:
            option2(participantes)

        if option == 3:
            option3(participantes)

        if option == 4:
            option4(participantes)


if __name__ == "__main__":
    main()
