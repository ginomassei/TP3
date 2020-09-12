import resources
import style


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

            # Mostrar la estadística pedida.
            data = resources.participants_per_continent(v)
            resources.show_participants_per_continent(data)

        elif option == 2:
            v = resources.load()
            style.print_green_text('Vector cargado correctamente.')

            # Mostrar la estadística pedida.
            data = resources.participants_per_continent(v)
            resources.show_participants_per_continent(data)

        elif option == 3:
            if len(v) != 0:
                resources.ranking_shell_sort(v)
                resources.print_reg(v)
            else:
                style.print_red_text('No hay elementos para mostrar.')

        elif option == 4:
            if len(v) != 0:
                match_arr = resources.match_generation(v)
                c = 0
                #Ciclo while para que se ejecute en octavos, cuartos y semifinales (3 fases)
                while c < 3:
                    #La primera vez, el partido ya está generado anteriormente
                    if c > 0:
                        match_arr = resources.match_generation(winners_arr)

                    resources.match_print(match_arr)

                    print()
                    input('\033[32;1m' + 'Presione enter para continuar.' + '\033[m')
                    #Si es la semifinal, debemos almacenar el arreglo de 3er y 4to puesto también
                    if c == 2:
                        winners_arr, third_arr = resources.match_simulation(match_arr)

                    else:
                        winners_arr = resources.match_simulation(match_arr)

                    c += 1

                resources.final_simulation(winners_arr, third_arr)
                input('\033[32;1m' + '\nPresione enter para mostrar la lista de participantes actualizada.' + '\033[m')
                resources.ranking_shell_sort(v)
                resources.print_reg(v)


            else:

                style.print_red_text('No hay elementos cargados.')


if __name__ == "__main__":
    main()
