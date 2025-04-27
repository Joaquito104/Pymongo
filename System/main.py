import Users

def main():

    print('Bienvenido.')
    inicio = input('Desea iniciar? [s/N]: ')

    if inicio.lower() == 's':
        print("Iniciando Sesión")

        while True:
            Users.usuario()
            continuar = input('Desea continuar [s/n]: ')

            if continuar.lower() != 's':
                print('Cerrando sesión...')
                break

if __name__ == "__main__":
    main()
