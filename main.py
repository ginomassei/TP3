import resources
import style


def option1_2(participants):


    data = resources.participants_per_continent(participants)
    style.print_red_text(f'\nParticipantes de América: {data[0]}')
    style.print_red_text(f'Participantes de Europa: {data[1]}')
    style.print_red_text(f'Participantes de Asia: {data[2]}')
    style.print_red_text(f'Participantes de Africa: {data[3]}')
    style.print_red_text(f'Participantes de Oceanía: {data[4]}')


def main():
    style.print_blue_text('Bienvenido!')
    v = []  # Creación del vector contenedor de los participantes.

    # Menú de opciones.
    print('-' * 80)
    option = -1
    while option != 0:
        # Listado de opciones.
        print('\nMenú de opciones:')
        print('1 - Cargar el vector de competidores de forma manual.')
        print('2 - Generar el vector de competidores de forma automática.')
        print('3 - Mostrar el vector cargado ordenado por ranking.')
        print('4 - Generar competición.')

        style.print_blue_text('\n0 - Salir.')

        option = int(input('\nIngrese su opción: '))
        print('-' * 80)

        # Tratamiento de la opción seleccionada.
        if option == 1:
            v = resources.load(1)
            style.print_green_text('Vector cargado correctamente.')

        elif option == 2:
            v = resources.load()
            style.print_green_text('Vector cargado correctamente.')

        elif option == 3:
            if len(v) != 0:
                resources.ranking_shell_sort(v)
                resources.print_reg(v)
            else:
                style.print_red_text('No hay elementos para mostrar.')

        elif option == 4:
            if len(v) != 0:
                match_arr = resources.match_generation(v)
                n = 0
                c = 0

                while n < 3:
                    if c > 0:
                        match_arr = resources.match_generation(winners_arr)

                    resources.match_print(match_arr)
                    input('\nPresione enter para continuar.')
                    winners_arr = resources.match_simulation(match_arr)
                    c += 1
                    n += 1
            else:
                style.print_red_text('No hay elementos cargados.')


if __name__ == "__main__":
    main()
