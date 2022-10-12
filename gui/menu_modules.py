import tkinter as tk
from tkinter import ttk

# # método para leer datos de un archivo
# def csv_read(file, csv_rows):
#     try:
#         with open(file, mode="r") as csv_file:
#             csv_reader = csv.reader(csv_file, delimiter=";")
#             for scoped_row in csv_reader:
#                 csv_rows.append(scoped_row)
#     except(AttributeError, TypeError, AssertionError):
#         raise AssertionError("Variables no cuenta con el tipo de dato esperado!!!")
#
#
# # método para escribir cosas en un archivo
# def csv_write(file, csv_rows):
#     try:
#         with open(file, mode="m") as csv_file:
#             csv_writer = csv.writer(csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             for scoped_row in csv_rows:
#                 csv_writer.writerow(scoped_row)
#     except(AttributeError, TypeError, AssertionError):
#         raise AssertionError("Variables no cuentan con el tipo de dato esperado!!!")


"""
#iniciando al usuario
def draw_screen(master):
    # Grids init
    frm = ttk.Frame(master, padding=20)
    frm.grid()
    msg_frm = ttk.Frame(frm, padding=10)
    msg_frm.grid()
    data_frm = ttk.Frame(frm, padding=10)
    data_frm.grid()
    btn_frm = ttk.Frame(frm, padding=10)
    btn_frm.grid()

    # Entries init
    scoped_user = ttk.Entry(data_frm)
    scoped_password = ttk.Entry(data_frm)

    # Gui
    ttk.Label(msg_frm, text="Por favor ingrese credenciales").grid(column=0, row=0)
    ttk.Label(data_frm, text="Usuario: ", justify="left").grid(column=0, row=1)
    scoped_user.grid(column=2, row=1)
    ttk.Label(data_frm, text="Clave: ", justify="left").grid(column=0, row=2)
    scoped_password.grid(column=2, row=2)
"""


# creación ventanas y con un botón para cerrar
def ventana(master):
    master.title('Toplevel Window')
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    ttk.Button(frm,
               text='Cerrar',
               command=master.destroy).pack(expand=True)


# ventana de empleados
def ventana_empleados(master):
    master.title('Módulo de empleados')
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    ttk.Button(frm,
               text='Cerrar',
               command=master.destroy).pack(expand=True)


# ventana de clientes
def ventana_clientes(master):
    master.title('Módulo de clientes')
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    ttk.Button(frm,
               text='Cerrar',
               command=master.destroy).pack(expand=True)


# ventana de proovedores
def ventana_proveedores(master):
    master.title('Módulo de proovedores')
    frm = ttk.Frame(master, padding=40)
    frm.grid()

    ttk.Button(frm,
               text='Cerrar',
               command=master.destroy).pack(expand=True)


# ventana de productos
def ventana_productos(master):
    master.title('Módulo de productos ')
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    ttk.Button(frm,
               text='Cerrar',
               command=master.destroy).pack(expand=True)


# ventana ventas y botones para cerrar
def ventana_ventas(master):
    master.title('Ventana de ventas')
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    ttk.Button(frm,
               text='número de venta',
               command=master.destroy).grid(column=0, row=0, pady=10, padx=10)

    # consultar ventas en el sistema
    ttk.Button(frm,
               text='Consultar ventas registradas', ).grid(column=0, row=1, pady=10, padx=10)
    # numero de venta
    ttk.Button(frm,
               text='Cerrar',
               command=master.destroy).grid(column=0, row=2, pady=10, padx=10)
    # despliegue de textos
    ttk.Label(frm).grid(column=0, row=3, pady=10, padx=10)
    # input boxes


def ventana_principal(master):
    master.title('Ventana principal')
    frm = ttk.Frame(master, padding=20)
    frm.grid()

    # Botón de empleados
    def on_click_ventas():
        frm.destroy()
        open_ventas(master)

    def on_click_empleados():
        frm.destroy()
        open_empleados(master)

    def on_click_proveedores():
        frm.destroy()
        open_proveedores(master)

    def on_click_productos():
        frm.destroy()
        open_productos(master)

    def on_click_clientes():
        frm.destroy()
        open_clientes(master)

    ttk.Button(frm, text="Módulo de empleados", command=on_click_empleados).grid(column=0, row=0, pady=10, padx=10)

    # Botón de clientes
    ttk.Button(frm, text="Módulo de clientes", command=on_click_clientes).grid(column=0, row=1, pady=10, padx=10)

    # Botón de proveedores
    ttk.Button(frm, text="Módulo de proveedores", command=on_click_proveedores).grid(column=0, row=2, pady=10, padx=10)

    # Botón de productos
    ttk.Button(frm, text="Módulo de productos", command=on_click_productos).grid(column=0, row=3, pady=10, padx=10)

    # Botón de ventas
    ttk.Button(frm, text="Módulo de ventas", command=on_click_ventas).grid(column=0, row=4, pady=10, padx=10)


# funciones para abrir las ventanas
def open_empleados(master):
    ventana_empleados(master)


def open_clientes(master):
    ventana_clientes(master)


def open_proveedores(master):
    ventana_proveedores(master)


def open_productos(master):
    ventana_productos(master)


# creación del método para crear la ventana de ventas
def open_ventas(master):
    ventana_ventas(master)


def open_window(master):
    ventana(master)
