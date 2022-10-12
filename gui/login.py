import service.login
from tkinter import *
from tkinter import ttk


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

    # def
    def on_click_create():
        print(service.login.create_user(scoped_user.get(), scoped_password.get()))

    def on_click_login():
        user = scoped_user.get()
        id_user = service.login.validate_user(scoped_user.get(), scoped_password.get())
        if id_user is not None:
            frm.destroy()
            draw_success(master, user, id_user)
        else:
            frm.destroy()
            draw_error(master, "Clave o usuario no encontrados")

    print(scoped_user.get(), str(scoped_password.get()))
    ttk.Button(btn_frm, text="Iniciar Sesión", command=on_click_login).grid(column=0, row=0, padx=1, pady=3)
    ttk.Button(btn_frm, text="Crear Usuario", command=on_click_create).grid(column=1, row=0, padx=1, pady=3)


def draw_success(master, user, id_user):
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    ttk.Label(frm, text="Bienvenido, " + user + " - " + id_user).grid(column=0, row=0)
    ttk.Button(frm, text="ok", command=print("Do on next")).grid(column=0, row=1, padx=1, pady=3)


def draw_error(master, reason):
    frm = ttk.Frame(master, padding=40)
    frm.grid()
    msg_frm = ttk.Frame(frm, padding=10)
    msg_frm.grid()
    btn_frm = ttk.Frame(frm, padding=10)
    btn_frm.grid()

    def on_click_retry():
        frm.destroy()
        draw_screen(master)

    ttk.Label(msg_frm, text="Error al ingresar - Razón: " + reason).grid(column=0, row=0)
    ttk.Button(btn_frm, text="Volver a intentar", command=on_click_retry).grid(column=0, row=1, padx=1, pady=3)
    ttk.Button(btn_frm, text="Cancelar", command=master.destroy).grid(column=1, row=1, padx=1, pady=3)
