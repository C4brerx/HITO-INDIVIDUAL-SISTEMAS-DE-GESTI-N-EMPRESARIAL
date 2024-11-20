from tkinter import *
from database.consultas import insertar_encuesta, obtener_encuestas, actualizar_encuesta, eliminar_encuesta
from database.conexion import crear_conexion

# Configuración de la ventana principal
ventana = Tk()
ventana.title("Encuesta de Consumo de Alcohol")
ventana.geometry("400x600")

# Frame para organizar los widgets
frame = Frame(ventana)
frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Variables para los campos de entrada
edad_entry = None
bebidas_semana_entry = None
cervezas_semana_entry = None
bebidas_fin_semana_entry = None
bebidas_destiladas_semana_entry = None
vinos_semana_entry = None

# Variables para los campos booleanos
perdidas_control_var = None
diversion_dependencia_var = None
problemas_digestivos_var = None
tension_alta_var = None
dolor_cabeza_var = None
sexo_var = None  # Variable para sexo (Mujer/Hombre)

# Listbox para mostrar las encuestas
lista_encuestas = Listbox(ventana, width=50, height=10)
lista_encuestas.pack(pady=10)

# Función para insertar encuesta
def insertar_encuesta_gui():
    conn = None
    try:
        conn = crear_conexion()
        if not conn:
            resultado_label.config(text="Error: No se pudo conectar a la base de datos", fg="red")
            return
        
        # Verificar que los campos no estén vacíos
        if not edad_entry.get() or not bebidas_semana_entry.get() or not cervezas_semana_entry.get():
            resultado_label.config(text="Error: Algunos campos están vacíos", fg="red")
            return
        
        # Obtener los valores de los campos
        edad = int(edad_entry.get())
        sexo = sexo_var.get()
        bebidas_semana = int(bebidas_semana_entry.get())
        cervezas_semana = int(cervezas_semana_entry.get())
        bebidas_fin_semana = int(bebidas_fin_semana_entry.get())
        bebidas_destiladas_semana = int(bebidas_destiladas_semana_entry.get())
        vinos_semana = int(vinos_semana_entry.get())
        perdidas_control = perdidas_control_var.get() == "Sí"
        diversion_dependencia_alcohol = diversion_dependencia_var.get() == "Sí"
        problemas_digestivos = problemas_digestivos_var.get() == "Sí"
        tension_alta = tension_alta_var.get() == "Sí"
        dolor_cabeza = dolor_cabeza_var.get() == "Sí"

        # Imprimir los valores para verificar
        print(f"Insertando encuesta con los siguientes valores: {edad}, {sexo}, {bebidas_semana}, ...")

        insertar_encuesta(
            conn, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
            bebidas_destiladas_semana, vinos_semana, perdidas_control, 
            diversion_dependencia_alcohol, problemas_digestivos, 
            tension_alta, dolor_cabeza
        )
        resultado_label.config(text="Encuesta insertada correctamente", fg="green")
    except ValueError:
        resultado_label.config(text="Error: Datos inválidos", fg="red")
    except Exception as e:
        resultado_label.config(text=f"Error: {e}", fg="red")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

# Función para mostrar encuestas
def mostrar_encuestas():
    lista_encuestas.delete(0, END)  # Limpiar el Listbox antes de insertar los nuevos resultados
    encuestas = obtener_encuestas(orden="edad")
    for encuesta in encuestas:
        lista_encuestas.insert(END, f"ID: {encuesta[0]}, Edad: {encuesta[1]}, Sexo: {encuesta[2]}")

# Función para actualizar una encuesta
def actualizar_encuesta_gui():
    try:
        # Recibir los valores de los campos
        id_encuesta = int(id_encuesta_entry.get())
        edad = int(edad_entry.get())
        sexo = sexo_var.get()
        bebidas_semana = int(bebidas_semana_entry.get())
        cervezas_semana = int(cervezas_semana_entry.get())
        bebidas_fin_semana = int(bebidas_fin_semana_entry.get())
        bebidas_destiladas_semana = int(bebidas_destiladas_semana_entry.get())
        vinos_semana = int(vinos_semana_entry.get())
        perdidas_control = perdidas_control_var.get() == "Sí"
        diversion_dependencia_alcohol = diversion_dependencia_var.get() == "Sí"
        problemas_digestivos = problemas_digestivos_var.get() == "Sí"
        tension_alta = tension_alta_var.get() == "Sí"
        dolor_cabeza = dolor_cabeza_var.get() == "Sí"

        # Actualizar encuesta en la base de datos
        actualizar_encuesta(
            id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
            bebidas_destiladas_semana, vinos_semana, perdidas_control, 
            diversion_dependencia_alcohol, problemas_digestivos, 
            tension_alta, dolor_cabeza
        )
        resultado_label.config(text="Encuesta actualizada correctamente", fg="green")
    except Exception as e:
        resultado_label.config(text=f"Error al actualizar: {e}", fg="red")

# Función para eliminar una encuesta
def eliminar_encuesta_gui():
    try:
        id_encuesta = int(id_encuesta_entry.get())
        eliminar_encuesta(id_encuesta)
        resultado_label.config(text="Encuesta eliminada correctamente", fg="green")
    except Exception as e:
        resultado_label.config(text=f"Error al eliminar: {e}", fg="red")

# Crear campos de entrada
Label(frame, text="ID Encuesta:").grid(row=0, column=0, sticky="w")
id_encuesta_entry = Entry(frame)
id_encuesta_entry.grid(row=0, column=1)

Label(frame, text="Edad:").grid(row=1, column=0, sticky="w")
edad_entry = Entry(frame)
edad_entry.grid(row=1, column=1)

Label(frame, text="Sexo:").grid(row=2, column=0, sticky="w")
sexo_var = StringVar(value="Mujer")
OptionMenu(frame, sexo_var, "Mujer", "Hombre").grid(row=2, column=1)

# Campos numéricos
campos = [
    ("Bebidas por semana:", "bebidas_semana_entry"),
    ("Cervezas por semana:", "cervezas_semana_entry"),
    ("Bebidas fin de semana:", "bebidas_fin_semana_entry"),
    ("Bebidas destiladas por semana:", "bebidas_destiladas_semana_entry"),
    ("Vinos por semana:", "vinos_semana_entry"),
]

for i, (texto, var_name) in enumerate(campos, start=3):
    Label(frame, text=texto).grid(row=i, column=0, sticky="w")
    globals()[var_name] = Entry(frame)
    globals()[var_name].grid(row=i, column=1)

# Campos booleanos (Sí/No)
booleanos = [
    ("¿Pérdidas de control?", "perdidas_control_var"),
    ("¿Diversión/Dependencia del alcohol?", "diversion_dependencia_var"),
    ("¿Problemas digestivos?", "problemas_digestivos_var"),
    ("¿Tensión alta?", "tension_alta_var"),
    ("¿Dolores de cabeza?", "dolor_cabeza_var"),
]

for i, (texto, var_name) in enumerate(booleanos, start=8):
    Label(frame, text=texto).grid(row=i, column=0, sticky="w")
    globals()[var_name] = StringVar(value="No")
    OptionMenu(frame, globals()[var_name], "Sí", "No").grid(row=i, column=1)

# Botones
Button(ventana, text="Insertar Encuesta", command=insertar_encuesta_gui).pack(pady=5)
Button(ventana, text="Mostrar Encuestas", command=mostrar_encuestas).pack(pady=5)
Button(ventana, text="Actualizar Encuesta", command=actualizar_encuesta_gui).pack(pady=5)
Button(ventana, text="Eliminar Encuesta", command=eliminar_encuesta_gui).pack(pady=5)

resultado_label = Label(ventana)
resultado_label.pack()

ventana.mainloop()
