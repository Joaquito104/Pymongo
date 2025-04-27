from System import Users
usuarios = Users.usuario()

print('Bienvenido.')
print ("Iniciando Seccion")

while True:

    usuarios()
    continuar = input('Desea continuar [s/n]: ')

    if continuar.lower() == 's':
        continue
    else:
        break

print('Cerrando seccion...')
