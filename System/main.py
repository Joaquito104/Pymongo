import Users

print('Bienvenido.')

inicio = input('Desea iniciar? [s/N]: ')
if inicio == 's':

    print ("Iniciando Seccion")

    while True:

        usuarios = Users.usuario()
        continuar = input('[s/n]: ')

        if continuar.lower() == 's':
            continue
        else:
            print('Cerrando seccion...')
            break

