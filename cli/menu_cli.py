import cli.login_cli
import service.employee_module
import service.provider_module


def draw_menu_options():
    print("\n-- MODULOS --\n")
    print("\t1. EMPLEADOS")
    print("\t2. CLIENTES")
    print("\t3. PROVEEDORES")
    print("\t4. PRODUCTOS")
    print("\t5. VENTAS")
    print("\t6. SALIR")
    print("\n-- MODULOS --\n")


def start_cli():
    cli.login_cli.print_first_screen()
    if cli.login_cli.is_valid():
        draw_menu_options()


def route_mode_to_service(selection):
    if selection == 1:
        print("\n-- EMPLEADOS --\n")
        for employee_row in service.employee_module.find_all():
            print("ID: " + employee_row[service.employee_module.ID_COL] +
                  ", NOMBRE: " + employee_row[service.employee_module.EMPLOYEE_NAME_COL] +
                  ", APELLIDO: " + employee_row[service.employee_module.EMPLOYEE_LASTNAME_COL] +
                  ", CÉDULA: " + employee_row[service.employee_module.EMPLOYEE_ID_COL] +
                  ", SALARIO: " + employee_row[service.employee_module.EMPLOYEE_SALARY_COL] +
                  ", POSICIÓN: " + employee_row[service.employee_module.EMPLOYEE_POSITION_COL]
                  )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UN NUEVO EMPLEADO")
            print("\t2. ACTUALIZAR UN EMPLEADO")
            print("\t3. ELIMINAR UN EMPLEADO")
            print("\t4. SALIR")
            selection = get_selection()
            if 1 <= selection <= 4:
                if selection == 1:
                    str_name = str(input("Ingrese el nombre: "))
                    str_lastname = str(input("Ingrese el apellido: "))
                    str_employee_id = str(input("Ingrese la cédula: "))
                    int_salary = int(input("Ingrese el salario: "))
                    str_position = str(input("Ingrese la posición: "))
                    if service.employee_module.save(str_name, str_lastname, str_employee_id, int_salary, str_position):
                        print("Empleado se ha guardo con éxito")
                    else:
                        print("Empleado no se ha logrado guardar")
                elif selection == 2:
                    int_id = str(input("Ingrese el identificador: "))
                    str_name = str(input("Ingrese el nombre: "))
                    str_lastname = str(input("Ingrese el apellido: "))
                    str_employee_id = str(input("Ingrese la cédula: "))
                    int_salary = int(input("Ingrese el salario: "))
                    str_position = str(input("Ingrese la posición: "))
                    if service.employee_module.update(int_id, str_name, str_lastname, str_employee_id, int_salary,
                                                      str_position):
                        print("Empleado se ha actualizado con éxito")
                    else:
                        print("Empleado no se ha logrado actualizar")
                elif selection == 3:
                    int_id = str(input("Ingrese el identificador: "))
                    if service.employee_module.delete(int_id):
                        print("Empleado se ha eliminado con éxito")
                    else:
                        print("Empleado no se ha logrado eliminar")
                else:
                    return "EXIT"
    elif selection == 2:
        print("\n-- CLIENTES --\n")
        print("Por favor, seleccione una de las siguientes opciones:")
        print("\t1. AGREGAR UN NUEVO CLIENTE")
        print("\t2. ELIMINAR UN CLIENTE")
        print("\t3. ACTUALIZAR UN CLIENTE")
        selection = get_selection()
        if 1 <= selection <= 3:
            if selection == 1:
            elif selection == 2:
            else:

    elif selection == 3:
        print("\n-- PROVEEDORES --\n")
        for provider_row in service.provider_module.find_all():
            print("ID: " + provider_row[service.provider_module.ID_COL] +
                  ", NOMBRE: " + provider_row[service.provider_module.PROVIDER_NAME_COL] +
                  ", TIPO: " + provider_row[service.provider_module.PROVIDER_TYPE_COL] +
                  ", RUTA - INICIO: " + provider_row[service.provider_module.PROVIDER_ROUTE_START_COL] +
                  ", RUTA - FINAL: " + provider_row[service.provider_module.PROVIDER_ROUTE_END_COL] +
                  ", ¿ES CONTINENTAL?: " + provider_row[service.provider_module.PROVIDER_IS_CONTINENTAL_COL]
                  )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UN NUEVO PROVEEDOR")
            print("\t2. ELIMINAR UN PROVEEDOR")
            print("\t3. ACTUALIZAR UN PROVEEDOR")
            selection = get_selection()
            if 1 <= selection <= 3:
                if selection == 1:
                elif selection == 2:
                else:
    elif selection == 4:
        print("\n-- PRODUCTOS --\n")
    elif selection == 5:
        print("\n-- VENTAS --\n")


def get_selection():
    return int(input("Ingrese una opción: "))


def get_id_selection():
    return int(input("Ingrese el identificador: "))