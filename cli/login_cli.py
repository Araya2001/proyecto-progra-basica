import service.login_module


def print_first_screen():
    print("\n-- SESIÓN DE USUARIO --\n")


def promt_user():
    print("Por favor elija una opción:")
    promt_user_is_valid = False
    int_selection = 0
    while not promt_user_is_valid:
        int_selection = int(input("\t1. Iniciar sesión\n\t2. Crear usuario\n\t3. Salir¶"))
        if 1 <= int_selection <= 3:
            promt_user_is_valid = True
        else:
            print("¡Por favor ingrese una opción válida!")
    if int_selection == 1:
        prompt_type_selection = "LOGIN"
    elif int_selection == 2:
        prompt_type_selection = "CREATE"
    else:
        prompt_type_selection = "EXIT"
    return prompt_type_selection


def is_valid():
    prompt_user_is_valid = False
    should_continue = False
    while not prompt_user_is_valid:
        prompt_type = promt_user()
        if prompt_type == "LOGIN":
            print("Ingrese los datos de inicio de sesión:")
            str_user = str(input("\tUsuario: "))
            str_password = str(input("\tClave: "))
            user = service.login_module.validate_user(str_user, str_password)
            if user is not None:
                print("Bienvenido,", str_user)
                prompt_user_is_valid = True
                should_continue = True
            else:
                print("Usuario o contraseña no son validas")
        if prompt_type == "CREATE":
            print("Ingrese los datos de usuario a crear:")
            str_user = str(input("\tUsuario: "))
            str_password = str(input("\tClave: "))
            user = service.login_module.create_user(str_user, str_password)
            if user:
                print("Bienvenido,", str_user)
                prompt_user_is_valid = True
                should_continue = True
            else:
                print("No fue posible crear el usuario")
        if prompt_type == "EXIT":
            print("¡SALIENDO DEL SISTEMA!")
            prompt_user_is_valid = True
    return should_continue
