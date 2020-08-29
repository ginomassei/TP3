import resources as rs
import style as s


def option1_2(participants, option):
    if option == 1:
        rs.manual_load(participants)
    elif option == 2:
        rs.random_load(participants)

    rs.ranking_shell_sort(participants)

    data = rs.participants_per_continent(participants)
    s.print_red_text(f'Participantes de América: {data[0]}')
    s.print_red_text(f'Participantes de Europa: {data[1]}')
    s.print_red_text(f'Participantes de Asia: {data[2]}')
    s.print_red_text(f'Participantes de Africa: {data[3]}')
    s.print_red_text(f'Participantes de Oceanía: {data[4]}')


def option3(participants):
    rs.print_reg(participants)


def option4(participants):
    pass


def main():
    participants_array = 16 * [None]  # Creación del vector contenedor de los participantes.
    option = -1

    while option != 0:
        print('\nMenú de opciones:')
        print('1 - Cargar el vector de competidores de forma manual.')
        print('2 - Generar el vector de competidores de forma automática.')
        print('3 - Mostrar el vector cargado.')
        print('4 - Generar competición.')

        print('0 - Salir.')

        option = int(input('\nIngrese su opción: '))

        if option == 1 or option == 2:
            option1_2(participants_array, option)

        if option == 3:
            option3(participants_array)

        if option == 4:
            option4(participants_array)

    match_array = rs.match_generation(participants_array)
    rs.match_print(match_array)


if __name__ == "__main__":
    main()
