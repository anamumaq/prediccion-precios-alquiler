# solicita correo
correo = input("Escribe tu correo electrónico: ")

# split texto
dominio = correo.split('@')[1]
nombre = correo.split('@')[0]

# imprime nombre y dominio
print('nombre: ', nombre, '   dominio: ', dominio)
