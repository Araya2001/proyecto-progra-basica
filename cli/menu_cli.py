import cli.login_cli
import service.employee_module
import service.provider_module
import service.product_module
import service.sales_module
import service.customer_module


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
        while route_mode_to_service(get_selection()) != "EXIT":
            draw_menu_options()
        return "EXIT"


def route_mode_to_service(selection):
    break_flag = False
    while not break_flag:
        if selection == 1:
            print("\n-- EMPLEADOS --\n")
            if len(service.employee_module.find_all()) != 0:
                for employee_row in service.employee_module.find_all():
                    print("ID: " + str(employee_row[service.employee_module.ID_COL]) +
                          ", NOMBRE: " + employee_row[service.employee_module.EMPLOYEE_NAME_COL] +
                          ", APELLIDO: " + employee_row[service.employee_module.EMPLOYEE_LASTNAME_COL] +
                          ", CÉDULA: " + str(employee_row[service.employee_module.EMPLOYEE_ID_COL]) +
                          ", SALARIO: " + str(employee_row[service.employee_module.EMPLOYEE_SALARY_COL]) +
                          ", POSICIÓN: " + employee_row[service.employee_module.EMPLOYEE_POSITION_COL]
                          )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UN NUEVO EMPLEADO")
            print("\t2. ACTUALIZAR UN EMPLEADO")
            print("\t3. ELIMINAR UN EMPLEADO")
            print("\t4. SALIR")
            selection_scoped = get_selection()
            if 1 <= selection_scoped <= 4:
                if selection_scoped == 1:
                    str_name = str(input("Ingrese el nombre: "))
                    str_lastname = str(input("Ingrese el apellido: "))
                    str_employee_id = str(input("Ingrese la cédula: "))
                    int_salary = int(input("Ingrese el salario: "))
                    str_position = str(input("Ingrese la posición: "))
                    if service.employee_module.save(str_name, str_lastname, str_employee_id, int_salary,
                                                    str_position):
                        print("Empleado se ha guardo con éxito")
                    else:
                        print("Empleado no se ha logrado guardar")
                elif selection_scoped == 2:
                    int_id = get_id_selection()
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
                elif selection_scoped == 3:
                    int_id = get_id_selection()
                    if service.employee_module.delete(int_id):
                        print("Empleado se ha eliminado con éxito")
                    else:
                        print("Empleado no se ha logrado eliminar")
                else:
                    break_flag = True
        elif selection == 2:
            print("\n-- CLIENTES --\n")
            if len(service.customer_module.find_all()) != 0:
                for customer_row in service.customer_module.find_all():
                    print("ID: " + str(customer_row[service.customer_module.ID_COL]) +
                          ", NOMBRE: " + customer_row[service.customer_module.CUSTOMER_NAME_COL] +
                          ", CÉDULA: " + str(customer_row[service.customer_module.CUSTOMER_ID_COL]) +
                          ", NÚMERO DE TELÉFONO: " + str(customer_row[service.customer_module.CUSTOMER_PHONE_NUMBER_COL]) +
                          ", DIRECCIÓN: " + customer_row[service.customer_module.CUSTOMER_ADDRESS_COL]
                          )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UN NUEVO CLIENTE")
            print("\t2. ELIMINAR UN CLIENTE")
            print("\t3. ACTUALIZAR UN CLIENTE")
            print("\t4. SALIR")
            selection_scoped = get_selection()
            if 1 <= selection_scoped <= 4:
                if selection_scoped == 1:
                    str_name = str(input("Ingrese el nombre: "))
                    str_cutomer_id = str(input("Ingrese la cédula: "))
                    str_phone_number = str(input("Ingrese el número de teléfono: "))
                    str_addr = str(input("Ingrese la dirección: "))
                    if service.customer_module.save(str_name, str_cutomer_id, str_phone_number, str_addr):
                        print("Cliente se ha guardo con éxito")
                    else:
                        print("Cliente no se ha logrado guardar")
                elif selection_scoped == 2:
                    int_id = get_id_selection()
                    str_name = str(input("Ingrese el nombre: "))
                    str_cutomer_id = str(input("Ingrese la cédula: "))
                    str_phone_number = str(input("Ingrese el número de teléfono: "))
                    str_addr = str(input("Ingrese la dirección: "))
                    if service.customer_module.update(int_id, str_name, str_cutomer_id, str_phone_number, str_addr):
                        print("Cliente se ha actualizado con éxito")
                    else:
                        print("Cliente no se ha logrado actualizar")
                elif selection_scoped == 3:
                    int_id = get_id_selection()
                    if service.customer_module.delete(int_id):
                        print("Cliente se ha eliminado con éxito")
                    else:
                        print("Cliente no se ha logrado eliminar")
                else:
                    break_flag = True
        elif selection == 3:
            print("\n-- PROVEEDORES --\n")
            if len(service.provider_module.find_all()) != 0:
                for provider_row in service.provider_module.find_all():
                    print("ID: " + str(provider_row[service.provider_module.ID_COL]) +
                          ", NOMBRE: " + provider_row[service.provider_module.PROVIDER_NAME_COL] +
                          ", TIPO: " + provider_row[service.provider_module.PROVIDER_TYPE_COL] +
                          ", RUTA - INICIO: " + provider_row[service.provider_module.PROVIDER_ROUTE_START_COL] +
                          ", RUTA - FINAL: " + provider_row[service.provider_module.PROVIDER_ROUTE_END_COL] +
                          ", ¿ES CONTINENTAL?: " + provider_row[service.provider_module.PROVIDER_IS_CONTINENTAL_COL]
                          )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UN NUEVO PROVEEDOR")
            print("\t2. ACTUALIZAR UN PROVEEDOR")
            print("\t3. ELIMINAR UN PROVEEDOR")
            print("\t4. SALIR")
            selection_scoped = get_selection()
            if 1 <= selection_scoped <= 4:
                if selection_scoped == 1:
                    str_name = str(input("Ingrese el nombre: "))
                    str_type = str(input("Ingrese el tipo: "))
                    str_route_start = str(input("Ingrese el inicio de la ruta:"))
                    str_route_end = str(input("Ingrese el final de la ruta:"))
                    es_continental = str(input("Ingrese si el servicio es continental (AERONAVE): "))
                    if service.provider_module.save(str_name, str_type, str_route_start, str_route_end,
                                                    es_continental):
                        print("Proveedor se ha guardo con éxito")
                    else:
                        print("Proveedor no se ha logrado guardar")
                elif selection_scoped == 2:
                    int_id = get_id_selection()
                    str_name = str(input("Ingrese el nombre: "))
                    str_type = str(input("Ingrese el tipo: "))
                    str_route_start = str(input("Ingrese el inicio de la ruta:"))
                    str_route_end = str(input("Ingrese el final de la ruta:"))
                    es_continental = str(input("Ingrese si el servicio es continental (AERONAVE): "))
                    if service.provider_module.update(int_id, str_name, str_type, str_route_start, str_route_end,
                                                      es_continental):
                        print("Proveedor se ha actualizado con éxito")
                    else:
                        print("Proveedor no se ha logrado actualizar")
                elif selection_scoped == 3:
                    int_id = get_id_selection()
                    if service.provider_module.delete(int_id):
                        print("Proveedor se ha eliminado con éxito")
                    else:
                        print("Proveedor no se ha logrado eliminar")
                else:
                    break_flag = True
        elif selection == 4:
            print("\n-- PRODUCTOS --\n")
            if len(service.product_module.find_all()) != 0:
                for product_row in service.product_module.find_all():
                    print("ID: " + str(product_row[service.product_module.ID_COL]) +
                          ", NOMBRE: " + str(product_row[service.product_module.PRODUCT_NAME_COL]) +
                          ", TIPO: " + product_row[service.product_module.PRODUCT_TYPE_COL] +
                          ", DESCRIPCIÓN: " + product_row[service.product_module.PRODUCT_DESCRIPTION_COL] +
                          ", FECHA DISPONIBLE: " + product_row[service.product_module.PRODUCT_SCHEDULE_COL] +
                          ", PRECIO: " + str(product_row[service.product_module.PRODUCT_PRICE_COL])
                          )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UN NUEVO PRODUCTO")
            print("\t2. ACTUALIZAR UN PRODUCTO")
            print("\t3. ELIMINAR UN PRODUCTO")
            print("\t4. SALIR")
            selection_scoped = get_selection()
            if 1 <= selection_scoped <= 4:
                if selection_scoped == 1:
                    str_name = str(input("Ingrese el nombre: "))
                    str_type = str(input("Ingrese el tipo de producto: "))
                    str_description = str(input("Ingrese la descripción del producto: "))
                    str_schedule = str(input("Ingrese la fecha de disponibilidad del producto: "))
                    flt_price = float(input("Ingrese el precio del producto: "))
                    if service.product_module.save(str_name, str_type, str_description, str_schedule,
                                                   flt_price):
                        print("Producto se ha guardo con éxito")
                    else:
                        print("Producto no se ha logrado guardar")
                elif selection_scoped == 2:
                    int_id = get_id_selection()
                    str_name = str(input("Ingrese el nombre: "))
                    str_type = str(input("Ingrese el tipo de producto: "))
                    str_description = str(input("Ingrese la descripción del producto: "))
                    str_schedule = str(input("Ingrese la fecha de disponibilidad del producto: "))
                    flt_price = float(input("Ingrese el precio del producto: "))
                    if service.product_module.update(int_id, str_name, str_type, str_description, str_schedule,
                                                     flt_price):
                        print("Producto se ha actualizado con éxito")
                    else:
                        print("Producto no se ha logrado actualizar")
                elif selection_scoped == 3:
                    int_id = get_id_selection()
                    if service.product_module.delete(int_id):
                        print("Producto se ha eliminado con éxito")
                    else:
                        print("Producto no se ha logrado eliminar")
                else:
                    break_flag = True
        elif selection == 5:
            print("\n-- VENTAS --\n")
            if len(service.sales_module.find_all()) != 0:
                for sales_row in service.sales_module.find_all():
                    print("ID de la venta: " + str(str(sales_row[service.sales_module.ID_COL])) +
                          ", monto facturado: " + str(sales_row[service.sales_module.SALES_TOTAL_COL]) +
                          ", productos adquiridos: " + sales_row[service.sales_module.SALES_PRODUCTOS_ADQUIRIDOS_COL] +
                          ", método de pago: " + sales_row[service.sales_module.SALES_METODO_PAGO_COL] +
                          ", información del comprador: " + sales_row[service.sales_module.SALES_INFO_COMPRADOR_COL] +
                          ", información del vendedor: " + sales_row[service.sales_module.SALES_INFO_VENDEDOR_COL] +
                          ", Fecha de la venta: " + sales_row[service.sales_module.SALES_FECHA_VENTA_COL]
                          )
            print("Por favor, seleccione una de las siguientes opciones:")
            print("\t1. AGREGAR UNA NUEVA VENTA")
            print("\t2. ELIMINAR UNA VENTA")
            print("\t3. ACTUALIZAR UNA VENTA")
            print("\t4. SALIR")
            selection_scoped = get_selection()
            if 1 <= selection_scoped <= 4:
                if selection_scoped == 1:
                    flt_total = float(input("Ingrese el total: "))
                    str_productos_adquiridos = str(input("Ingrese los productos adquiridos separados por coma (,): "))
                    str_metodo_de_pago = str(input("Ingrese el método de pago: "))
                    int_employee_id = int(input("Ingrese el id del empleado que realizo la venta: "))
                    int_customer_id = int(input("Ingrese el id del cliente que formo parte de la venta: "))
                    str_fecha = str(input("Ingrese la fecha en la que se formalizó la venta: "))
                    if service.sales_module.save(flt_total, str_productos_adquiridos, str_metodo_de_pago,
                                                 int_customer_id, int_employee_id, str_fecha):
                        print("Venta se ha guardo con éxito")
                    else:
                        print("Venta no se ha logrado guardar")
                elif selection_scoped == 2:
                    int_id = get_id_selection()
                    flt_total = float(input("Ingrese el total: "))
                    str_productos_adquiridos = str(input("Ingrese los productos adquiridos separados por coma (,): "))
                    str_metodo_de_pago = str(input("Ingrese el método de pago: "))
                    int_employee_id = int(input("Ingrese el id del empleado que realizo la venta: "))
                    int_customer_id = int(input("Ingrese el id del cliente que formo parte de la venta: "))
                    str_fecha = str(input("Ingrese la fecha en la que se formalizó la venta: "))
                    if service.sales_module.update(int_id, flt_total, str_productos_adquiridos, str_metodo_de_pago,
                                                   int_customer_id, int_employee_id, str_fecha):
                        print("Venta se ha actualizado con éxito")
                    else:
                        print("Venta no se ha logrado actualizar")
                elif selection_scoped == 3:
                    int_id = get_id_selection()
                    if service.sales_module.delete(int_id):
                        print("Venta se ha eliminado con éxito")
                    else:
                        print("Venta no se ha logrado eliminar")
                else:
                    break_flag = True
        elif selection == 6:
            break_flag = True
            return "EXIT"


def get_selection():
    return int(input("Ingrese una opción: "))


def get_id_selection():
    return int(input("Ingrese el identificador: "))
