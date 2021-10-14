import os 

class Servicio:
    ruta_archivo='peliculas.txt'


    #para acceder a los atributos de clases
    @classmethod
    def agregar_peliculas(cls,pelicula):
        with open(cls.ruta_archivo,'a',encoding='utf8') as archivo:
            archivo.write(f"{pelicula.nombre}\n")
    
    @classmethod
    def listar_metodo(cls):
        with open(cls.ruta_archivo,'r',encoding='utf8') as archivo:
            print('Catalogo de peliculas'.center(50,'-'))
            print(archivo.read())
    
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f"Archivo eliminado: {cls.ruta_archivo}")
    