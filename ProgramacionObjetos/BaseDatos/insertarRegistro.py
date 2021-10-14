import psycopg2


conexion = psycopg2.connect(
    user = 'postgres',
    password='91021663366',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try: 
    with conexion:
        #Cursor es un objto para realizar sentencia de SQL desde python
        with conexion.cursor() as cursor:

            #Definir la sentencia que se quiere ejecutar en SQL
                #Sentencia para realizar un resgitro en la base de datos
            sentencia ="INSERT INTO personas(nombre,apellido,email) VALUES(%s, %s, %s)"
            #sustituir los valores
            valores=("Carlos Piñeros","Lara Gutierrez","carlos@gmail.com")
            cursor.execute(sentencia,valores)

            registrosIncertados=cursor.rowcount
            print(f"Registros Incertados: {registrosIncertados}")



            #Cerrar la base de datos
except Exception as e:
    print(f"Ocurrio un error {e}")
finally:   
    conexion.close()
