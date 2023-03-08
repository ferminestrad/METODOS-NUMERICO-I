while True:
    try:
        nusuario=input("Ingresa nombre de usuario (6-12 caracteres)")
        if len(nusuario)>=6 and len(nusuario)<=12 and nusuario.isalnum():
            print("Nombre de usuario valido, bienvenido")
            break
        elif len(nusuario)<7:
            print("Debe contener mas de 6 caracteres")
        elif len(nusuario)>12:
             print("Debe contener menos de 12 caracteres")
        else:
            print("El nombre no debe contener caracteres")
    except:
        print("ERROR")