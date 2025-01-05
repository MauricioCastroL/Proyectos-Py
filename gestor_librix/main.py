# Autor: Mauricio Castro Leal
# Fecha: 30/12/2024
# Objetivo: Gestor Librix GUI

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import csv

dict_students = {} # Varialble Global

def users(CSV_users):
    # Guarda los accesos de usuarios permitidos
    dict_users = {}

    file = open(CSV_users, 'r', encoding='UTF-8')

    for linea in file:
        data = linea.rstrip().split(',')
        dict_users[data[0]] = data[1]
    
    file.close()

    return dict_users

def students(CSV_students):
    # Guarda los estudiantes

    file = open(CSV_students, 'r', encoding='UTF-8')

    reader = csv.DictReader(file)
    for row in reader:
        name = row['nombre']
        notas = row['notas'].split(',')  
        curso = row['curso']
        dict_students[name] = {"notas": notas, "curso": curso}

    file.close()
    
    return dict_students


# Verifica cadenas como el nombre
def is_name(string):
    if isinstance(string, str) and string.replace(' ', '').isalpha():
        return True
    else:
        messagebox.showerror('ERORR', 'Ingrese bien su nombre')
        return False


# Muestra u oculta la contraseña 
def show_disabled_enabled(password_user):
    if check.get():
        password_user.configure(show='')
    else:
        password_user.configure(show='*')


# Da inicio al programa 
def init(name, password, file_user):
    name = name.get()
    password = password.get()

    if name and password:

        is_name(name) # Validación de nombre
    
        if name in file_user:
            real_password = file_user[name]
            if password == real_password:
                menu_option() # Inicio a la siguiente ventana
            else:
                messagebox.showerror('ERORR', 'Ingrese bien su contraseña')
        else:
            messagebox.showerror('ERORR', 'No se encuentra registrado')
    else:
        messagebox.showerror('ERORR', 'Ingrese todos los campos')


# Ventana menu opciones
def menu_option():

    # Configuraciones ventana menu de opciones
    menu = tk.Toplevel()
    menu.title('Librix')
    menu.resizable(False, False)
    menu.geometry('1500x800')
    menu.configure(background='#f4b324')

    # Contenido del menu de opciones
    Frame(
        menu,
        width=300,
        height=1000,
        background='#f4a324'
    ).place(x=0, y=0)

    Label(
        menu,
        text='Menú de Opciones',
        font='RoxboroughCF, 20',
        background='#f4a324'
    ).place(x=25, y=100)

    Button(
        menu, 
        height=2,
        width=15,
        background='green',
        text='Agregar',
        command=lambda: add(menu)
    ).place(x=60, y=200)

    Button(
        menu,
        height=2,
        width=15,
        background='green',
        text='Mostrar',
        command=lambda: show(menu)
    ).place(x=60, y=300)

    Button(
        menu,
        height=2,
        width=15,
        background='green',
        text='Eliminar',
        command=lambda: delete(menu)
    ).place(x=60, y=400)

    Button(
        menu,
        height=2,
        width=15,
        background='green',
        text='Modificar',
        command=lambda: modify(menu)
    ).place(x=60, y=500)


    menu.mainloop()


def cancel_button(lista):
    for wid in lista:
        wid.destroy()

def clean_button(lista):
    for wid in lista:
        wid.delete(0, tk.END)
        if isinstance(wid, Text):
            wid.configure(state='normal')
            wid.delete("1.0", "end")
            wid.configure(state='disabled')


def add(menu):
    # Agrega el estudiante al diccionario
    def add_student():
        if entry_name.get() and  entry_curso.get() and entry_notas.get():
            name = entry_name.get()
            if is_name(name):
                notas = entry_notas.get()
                curso = entry_curso.get()

                if name in dict_students:
                    messagebox.showinfo('Acción Invalida', 'El estudiante ya se encuentra en la lista')
                else:
                    dict_students[name] = {"notas": notas.split(','), "curso": curso}
                    file = open('students.csv', 'a', encoding='UTF-8')
                    writer = csv.DictWriter(file, fieldnames=['nombre', 'notas', 'curso'])
                    if file.tell() == 0:  
                        writer.writeheader()
                    writer.writerow({'nombre': name, 'notas': notas, 'curso': curso})
                    file.close()
        else:
            messagebox.showinfo('Acción Invalida', 'Ingrese todos los campos')
            

    # Crea las instancias de agregado
    encabezado = Label(
        menu,
        text='Agregar Estudiante',
        background='#f4b324',
        font='RoxboroughCF, 30',
    )
    encabezado.place(x=600, y=100)

    label_name = Label(
        menu,
        text='Ingrese el nombre del estudiante',
        background='#f4b324',
        font='RoxboroughCF, 13',
    )
    label_name.place(x=400, y=300)

    name = StringVar()
    entry_name = Entry( # Nombre estudiante
        menu,
        width=30,
        font='RoxboroughCF, 12',
        textvariable=name
    )
    entry_name.place(x=400, y=330)

    label_curso = Label(
        menu,
        text='Curso',
        background='#f4b324',
        font='RoxboroughCF, 13',
        )
    label_curso.place(x=800, y=300)

    curso = StringVar()
    entry_curso = Entry( # Curso estudiante
            menu, 
            width=10,
            font='RoxboroughCF, 12',
            takefocus=curso
        )
    entry_curso.place(x=800, y=330)

    label_notas = Label(
        menu,
        text='Ingrese las notas separadas por coma',
        background='#f4b324',
        font='RoxboroughCF, 13',
    )
    label_notas.place(x=1000, y=300)

    notas = StringVar()
    entry_notas = Entry(
        menu,
        width=20,
        textvariable=notas,
        font='RoxboroughCF, 12',

    )
    entry_notas.place(x=1000, y=330)

    agregar = Button(
        menu,
        text='Confirmar',
        background='green',
        font='RoxboroughCF, 13',
        command=add_student
    )
    agregar.place(x=600, y=500)

    limpiar = Button(
        menu,
        text='Limpiar Todo',
        background='#5e17eb',
        font='RoxboroughCF, 13',
        command=lambda: clean_button([entry_curso, entry_name, entry_notas])
    )
    limpiar.place(x=800, y=500)

    cancelar = Button(
        menu, 
        text='Cancelar',
        background='red',
        font='RoxboroughCF, 13',
        command=lambda: cancel_button([entry_notas, entry_curso, entry_name, limpiar, agregar, cancelar, label_curso, label_name, label_notas, encabezado])
    )
    cancelar.place(x=1000, y=500)    

def show(menu):
    
    encabezado = Label(
        menu,
        text='Mostrar Listado de Estudiantes',
        background='#f4b324',
        font='RoxboroughCF, 30'
    )
    encabezado.place(x=600, y=100)

    listado_insert = Text(
        menu,
        state='normal',
        width=100,
        height=30
    )
    listado_insert.place(x=500, y=200)

    cancelar = Button(
        menu, 
        text='Cancelar',
        background='red',
        font='RoxboroughCF, 12',
        command=lambda: cancel_button([encabezado, listado_insert, cancelar])
    )
    cancelar.place(x=1350, y=700)

    for nombre, info in dict_students.items():
        notas_str = ', '.join(map(str, info['notas']))  
        listado_insert.insert('end', f'Nombre: {nombre}, Notas: {notas_str}, Curso: {info["curso"]}\n')
    listado_insert.configure(state='disabled')


def delete(menu):
    def kill():
        if entry_name.get():
            name = entry_name.get()
            if name in dict_students:
                notas_str = ', '.join(map(str, dict_students[name]['notas']))
                listado_insert.configure(state='normal')
                listado_insert.insert('end', f'Nombre: {name}, Notas: {notas_str}, Curso: {dict_students[name]["curso"]}\n')
                listado_insert.configure(state='disabled')
                confirmar.configure(state='normal')
            else:
                messagebox.showinfo('ERROR', 'El estudiante no se encuentra registrado')
        else:
            messagebox.showwarning('ERROR', 'Ingrese el nombre del estudiante a eliminar')

    def confirm_delete():

        name = entry_name.get()
        notas_str = ', '.join(map(str, dict_students[name]['notas']))
        curso = dict_students[name]['curso']

        del dict_students[name]
        messagebox.showinfo('Éxito', f'El estudiante "{name}" ha sido eliminado.')

        file = open('students.csv', 'w', encoding='UTF-8')

        writer = csv.DictWriter(file, fieldnames=['nombre', 'notas', 'curso'])
    
        writer.writeheader()
        
        for estudiante, datos in dict_students.items():
            writer.writerow({
                'nombre': estudiante,
                'notas': ','.join(map(str, datos['notas'])),
                'curso': datos['curso']
            })
        file.close()

        entry_name.delete(0, 'end')
        if listado_insert is not None:
            listado_insert.configure(state='normal')
            listado_insert.delete("1.0", "end")
            listado_insert.configure(state='disabled')

        confirmar.configure(state='disabled')
    
    encabezado = Label(
        menu,
        text='Eliminar Estudiante',
        background='#f4b324',
        font='RoxboroughCF, 30'
    )
    encabezado.place(x=750, y=100)

    label_name = Label(
        menu,
        text='Nombre Estudiante',
        background='#f4b324',
        font='RoxboroughCF, 13'
    )
    label_name.place(x=800, y=250)

    name = StringVar()
    entry_name = Entry(
        menu,
        width=25,
        textvariable=name,
        font='RoxboroughCF, 12'
    )
    entry_name.place(x=800, y=280)

    info = Button(
        menu,
        text='Desplegar información',
        background='green',
        width=15,
        height=2,
        command=kill 
    )
    info.place(x=850, y=350)

    listado_insert = Text(
        menu,
        width=80,
        height=20,
        state='disabled'
    )
    listado_insert.place(x=600, y=400)

    limpiar = Button(
            menu,
            text='Limpiar',
            background='#5e17eb',
            width=15,
            height=2,
            command=lambda: clean_button([entry_name, listado_insert]) 
        )
    limpiar.place(x=1100, y=265)

    confirmar = Button(
        menu,
        text='Confirmar',
        background='green',
        width=15,
        height=2,
        state='disabled',  
        command=confirm_delete
    )
    confirmar.place(x=800, y=800)

    cancelar = Button(
        menu,
        text='Cancelar',
        background='red',
        width=15,
        height=2,
        command=lambda: cancel_button([entry_name, label_name, encabezado, limpiar, cancelar, info, confirmar, listado_insert]) 
    )
    cancelar.place(x=1300, y=700)

def modify(menu):
    def dict_modify():
        if entry_name.get():
            name = entry_name.get()
            if name in dict_students:
                curso = dict_students[name]['curso']
                notas = dict_students[name]['notas']
                
                entry_curso.configure(state='normal')
                entry_curso.insert(0, f'{curso}')

                entry_notas.configure(state='normal')
                entry_notas.insert(0, f'{','.join(map(str, notas))}')

                confirmar.configure(state='normal')
                
            else:
                messagebox.showwarning('ERROR', 'El estudiante no esta registrado')
        else:
            messagebox.showwarning('ERROR', 'Ingrese el nombre del estudiante a eliminar')

    def confirm(): 
        #Aqui se ingresan las modificaciones
        name = entry_name.get()
        curso = entry_curso.get()
        notas = list(map(int, entry_notas.get().split(',')))

        dict_students[name]['notas'] = notas
        dict_students[name]['curso'] = curso

        file = open('students.csv', 'w', encoding='UTF-8')
        writer = csv.DictWriter(file, fieldnames=['nombre', 'notas', 'curso'])
    
        writer.writeheader()
        
        for estudiante, datos in dict_students.items():
            writer.writerow({
                'nombre': estudiante,
                'notas': ','.join(map(str, datos['notas'])),
                'curso': datos['curso']
            })
        file.close()


    encabezado = Label(
        menu,
        text='Modifiar Estudiante',
        background='#f4b324',
        font='RoxboroughCF, 30'
    )
    encabezado.place(x=700, y=100)

    label_nombre = Label(
        menu,
        text='Nombre estudiante',
        background='#f4b324',
        font='RoxboroughCF, 13'
    )
    label_nombre.place(x=400, y=270)
    
    name = StringVar()
    entry_name = Entry(
        menu,
        width=25,
        textvariable=name,
        font='RoxboroughCF, 12'
    )
    entry_name.place(x=400, y=300)

    modify_label = Label(
        menu,
        text='Modifique las Notas y Curso:',
        background='#f4b324',
        font='RoxboroughCF, 13'
    )
    modify_label.place(x=400, y=400)

    label_notas = Label(
        menu,
        text='Notas separadas por coma',
        background='#f4b324',
        font='RoxboroughCF, 13'
    )
    label_notas.place(x=400, y=430)

    notas = StringVar()
    entry_notas = Entry(
        menu,
        width=20,
        state='disabled',
        textvariable=notas,
        font='RoxboroughCF, 12'
    )
    entry_notas.place(x=400, y=460)

    label_curso = Label(
        menu,
        text='Curso',
        background='#f4b324',
        font='RoxboroughCF, 13'
    )
    label_curso.place(x=400, y=490)

    curso = StringVar()
    entry_curso = Entry(
        menu,
        width=10,
        textvariable=curso,
        state='disabled',
        font='RoxboroughCF, 12'
    )
    entry_curso.place(x=400, y=520)

    desplegar_mostrar = Button(
        menu,
        text='Desplegar',
        width=15,
        height=2,
        command=dict_modify,
        background='green'
    )
    desplegar_mostrar.place(x=900, y=290)

    limpiar = Button(
        menu,
        background='purple',
        text='Limpiar',
        width=15,
        height=2,
        command=lambda: clean_button([entry_curso, entry_name, entry_notas])
    )
    limpiar.place(x=700, y=290)

    cancelar = Button(
        menu,
        text='Cancelar',
        background='red',
        width=15,
        height=2,
        command= lambda: cancel_button([entry_curso, entry_name, entry_notas, encabezado, label_curso, label_nombre, desplegar_mostrar, label_notas, cancelar, limpiar, modify_label, confirmar])
    )
    cancelar.place(x=1300, y=700)

    confirmar = Button(
        menu,
        background='green',
        text='Confirmar',
        width=15,
        height=2,
        state='disabled',
        command=confirm
    )
    confirmar.place(x=800, y=700)

if __name__ == '__main__':

    user = users('users.csv')
    student = students('students.csv')

    root = tk.Tk() # Inicio Tk

    # Configuraciones ventana inicio de sesión
    root.resizable(False, False)
    root.geometry('800x1000+10000+0')
    root.title('Gestor Librix')
    root.configure(background='#f4b324')

    # Contenido ventana de inicio de sesión

    Label(
        text='Bienvenido a Librix!',
        font='RoxboroughCF, 25',
        background='#f4b324'
    ).place(x=275, y=150)

    Label(
        text='Inicio de Sesión',
        font='RoxboroughCF, 25',
        background='#f4b324'
    ).place(x=300, y=300)

    Label(
        text='Nombre de Usuario',
        font='RoxboroughCF, 15',
        background='#f4b324'
    ).place(x=325, y=450)

    # Nombre del usuario
    name_user = Entry(
        root,
        width=20,
        background='white',
        fg='black',
    )
    name_user.place(x=325, y=500)

    Label(
        text='Contraseña',
        font='RoxboroughCF, 15',
        background='#f4b324'
    ).place(x=325, y=600)

    # Contraseña usuario 
    password_user = Entry(
        root,
        width=20,
        show='*',
        background='white',
        fg='black',
    )
    password_user.place(x=325, y=650)

    Label(
        root,
        text='Mostrar',
        font='RoxboroughCF, 12',
        background='#f4b324'
    ).place(x=560, y=650)

    check = tk.BooleanVar() # Mostrar ocultar contraseña
    check_button = tk.Checkbutton(
        root,
        variable=check,
        background='#f4b324',
        command=lambda: show_disabled_enabled(password_user)
    )
    check_button.place(x=520, y=650)

    Button(
        text='Confirmar',
        width=6,
        height=2,
        background='green',
        fg='white',
        command=lambda: init(name_user, password_user, user)
    ).place(x=400, y=750)

    root.mainloop()
