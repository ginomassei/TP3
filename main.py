import resources as rs


def option1():
    rs.manual_load()


def option2():
    rs.random_load()


def main():
    option = 0

    while option != -1:
        print('/nMenú de opciones:')
        print('1 - Cargar el vector de competidores de forma manual.')
        print('2 - Cargar el vector de competidores de forma automática.')

        option = int(input('/nIngrese su opción: '))

        if option == 1:
            option1()

        if option == 2:
            option2()


if __name__ == "__main__":
    main()
