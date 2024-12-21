#CREAR
def crear_registro(nombre, edad):
    conn = mysql.connector.connect(user='usuario', password='contraseña', host='localhost', database='mi_base_de_datos')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO registros (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    conn.commit()
    cursor.close()
    conn.close()

#LEER
def leer_registros():
    conn = mysql.connector.connect(user='usuario', password='contraseña', host='localhost', database='mi_base_de_datos')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registros")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

#ACTUALIZAR
def actualizar_registro(id, nuevo_nombre, nueva_edad):
    conn = mysql.connector.connect(user='usuario', password='contraseña', host='localhost', database='mi_base_de_datos')
    cursor = conn.cursor()
    cursor.execute("UPDATE registros SET nombre=%s, edad=%s WHERE id=%s", (nuevo_nombre, nueva_edad, id))
    conn.commit()
    cursor.close()
    conn.close()

#ELIMINAR
def eliminar_registro(id):
    conn = mysql.connector.connect(user='usuario', password='contraseña', host='localhost', database='mi_base_de_datos')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM registros WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

