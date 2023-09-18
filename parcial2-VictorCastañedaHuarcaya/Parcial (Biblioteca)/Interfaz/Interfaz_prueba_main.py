import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextBrowser, QPushButton, QLineEdit, QDateEdit

from autor_negocio import AutorNegocio
from libro_negocio import LibroNegocio
from categoria_negocio import CategoriaNegocio

listado_autor = []
registros_autor = "Python/Parcial (Biblioteca)/listado_autor.xlsx"
negocio1 = AutorNegocio()

listado_categorias = []
registros_categorias = 'Python/Parcial (Biblioteca)/listado_categorias.xlsx'
negocio = CategoriaNegocio()

listado_libros=[]
registros_libros = 'Python/Parcial (Biblioteca)/listado_libros.xlsx'
negocio2 = LibroNegocio()

class dialogo(QMainWindow):
    def __init__(self):
        super(dialogo, self).__init__()
        uic.loadUi('Python/Parcial (Biblioteca)/Interfaz/Interfaz1.ui', self)
        self.setWindowTitle("Interfaz_prueba")

    # Conecta el botón a la función que muestra la segunda interfaz (registrar)
        self.registrar = self.findChild(QPushButton, 'registrar')
        self.registrar.clicked.connect(self.mostrar_segunda_interfaz)

    # Conecta el botón a la función que muestra la tercera interfaz (editar)
        self.editar = self.findChild(QPushButton, 'editar')
        self.editar.clicked.connect(self.mostrar_tercera_interfaz)
    
    # Conecta el botón a la función que muestra la cuarta interfaz (eliminar)
        self.eliminar = self.findChild(QPushButton, 'eliminar')
        self.eliminar.clicked.connect(self.mostrar_cuarta_interfaz)
    
    # Conecta el botón a la función que muestra la quinta interfaz (reporte)
        self.reporte = self.findChild(QPushButton, 'reporte')
        self.reporte.clicked.connect(self.mostrar_quinta_interfaz)
    
    # Conecta el botón a la función que muestra la sexta interfaz (reactivar)
        self.reactivar = self.findChild(QPushButton, 'reactivar')
        self.reactivar.clicked.connect(self.mostrar_sexta_interfaz)
    
    #Conectamos el boton a la funcion que listara los libros (listar)
        self.listar = self.findChild(QPushButton, 'listar')
        self.listar.clicked.connect(self.listar_libros)
    
    def mostrar_segunda_interfaz(self):
        # Carga y muestra la segunda interfaz desde el archivo .ui
        self.segunda_interfaz = uic.loadUi('Python/Parcial (Biblioteca)/Interfaz/Interfaz2.ui')
        
        # Conecta el botón de "Aceptar" en la segunda interfaz a la función de captura
        aceptar = self.segunda_interfaz.findChild(QPushButton, 'aceptar')
        aceptar.clicked.connect(self.capturar_datos_2)

        # Conecta el botón de "Cancelar" en la segunda interfaz a la función de cancelar
        cancelar = self.segunda_interfaz.findChild(QPushButton, 'cancelar')
        cancelar.clicked.connect(self.cancelar_2)

        self.segunda_interfaz.show()
    
    def cancelar_2(self):
        # Cerrar la segunda interfaz
        self.segunda_interfaz.close()

    def capturar_datos_2(self):
        lista_autor_temporal=negocio1.obtener_autor()
        id_persona = len(lista_autor_temporal)+1
        cod_persona = f"P00{len(lista_autor_temporal)+1}"
        id_autor = len(lista_autor_temporal)+1
        cod_autor = f"A00{len(lista_autor_temporal)+1}"
        estado_autor = True
        #Autor
        # Obtén los textos ingresados por el usuario desde los QLineEdits
        nombre = self.segunda_interfaz.findChild(QLineEdit, 'nombre').text()
        apellido_paterno = self.segunda_interfaz.findChild(QLineEdit, 'apellido_paterno').text()
        apellido_materno = self.segunda_interfaz.findChild(QLineEdit, 'apellido_materno').text()
        fecha_nacimiento = self.segunda_interfaz.findChild(QDateEdit, 'fecha_nacimiento').date()
        #codigo_autor = self.segunda_interfaz.findChild(QLineEdit, 'codigo_autor').text()
        pais = self.segunda_interfaz.findChild(QLineEdit, 'pais').text()
        editorial = self.segunda_interfaz.findChild(QLineEdit, 'editorial').text()
        # Convierte la fecha a una cadena en el formato deseado
        fecha_formateada = fecha_nacimiento.toString("dd/MM/yyyy")
        negocio1.registrar_autor(id_persona,cod_persona,id_autor,cod_autor,nombre,apellido_paterno,apellido_materno,fecha_formateada,pais,editorial,estado_autor)
        negocio1.guardar_autor()

        #Libro
        lista_libro_temporal= negocio2.obtener_libro()
        id_libro = len(lista_libro_temporal) + 1
        titulo = self.segunda_interfaz.findChild(QLineEdit, 'titulo').text()
        codigo_libro = f"L00{len(lista_libro_temporal)+1}"
        #codigo_libro = self.segunda_interfaz.findChild(QLineEdit, 'codigo_libro').text()
        tomo = self.segunda_interfaz.findChild(QLineEdit, 'tomo').text()
        fecha_publicacion = self.segunda_interfaz.findChild(QDateEdit, 'fecha_publicacion').date()
        # Convierte la fecha a una cadena en el formato deseado
        fecha_formateada2 = fecha_publicacion.toString("dd/MM/yyyy")
        estado_libro = True
        negocio2.registrar_libro(id_libro, codigo_libro,titulo,fecha_formateada2,tomo,estado_libro)
        negocio2.guardar_libro()

        #Categoria
        lista_categoria_temporal=negocio.obtener_categorias()
        cod_categoria = f"C00{len(lista_categoria_temporal)+1}"
        genero = self.segunda_interfaz.findChild(QLineEdit, 'genero').text()
        estado_categoria = True
        negocio.registrar_categoria(cod_categoria, genero, estado_categoria)
        negocio.guardar_categorias()

        self.segunda_interfaz.close()

    def mostrar_tercera_interfaz(self):
        # Carga y muestra la tercera interfaz desde el archivo .ui
        self.tercera_interfaz = uic.loadUi('Python/Parcial (Biblioteca)/Interfaz/Interfaz3.ui')

        #Edita los datos
        #Conectar el boton "Buscar" en la tercera interfaz a la funcion de buscar_id
        buscar = self.tercera_interfaz.findChild(QPushButton, 'buscar')
        buscar.clicked.connect(self.buscar_id) 

        # Conecta el botón de "Aceptar" en la tercera interfaz a la función de captura
        aceptar = self.tercera_interfaz.findChild(QPushButton, 'aceptar')
        aceptar.clicked.connect(self.capturar_datos_3)

        # Conecta el botón de "Cancelar" en la tercera interfaz a la función de cancelar
        cancelar = self.tercera_interfaz.findChild(QPushButton, 'cancelar')
        cancelar.clicked.connect(self.cancelar_3)

        self.tercera_interfaz.show()

    def buscar_id(self):
        pass

    def cancelar_3(self):
        # Cerrar la tercera interfaz
        self.tercera_interfaz.close()

    def capturar_datos_3(self):

        id_texto = self.tercera_interfaz.findChild(QLineEdit, 'id').text()
        # Convierte la cadena de texto a un número entero
        id_entero = int(id_texto)
        # Resta 1 al número entero
        indice = id_entero - 1

        #Autor
        # Obtén los textos ingresados por el usuario desde los QLineEdits
        nombre = self.tercera_interfaz.findChild(QLineEdit, 'nombre').text()
        apellido_paterno = self.tercera_interfaz.findChild(QLineEdit, 'apellido_paterno').text()
        apellido_materno = self.tercera_interfaz.findChild(QLineEdit, 'apellido_materno').text()
        fecha_nacimiento = self.tercera_interfaz.findChild(QDateEdit, 'fecha_nacimiento').date()
        #codigo_autor = self.tercera_interfaz.findChild(QLineEdit, 'codigo_autor').text()
        pais = self.tercera_interfaz.findChild(QLineEdit, 'pais').text()
        editorial = self.tercera_interfaz.findChild(QLineEdit, 'editorial').text()
        # Convierte la fecha a una cadena en el formato deseado
        fecha_formateada = fecha_nacimiento.toString("dd/MM/yyyy")
        print(negocio1.editar_autor(indice,nombre,apellido_paterno, apellido_materno,fecha_formateada,pais,editorial))

        #Libro
        id_libro = id_entero - 1 
        titulo = self.tercera_interfaz.findChild(QLineEdit, 'titulo').text()
        #codigo_libro = self.tercera_interfaz.findChild(QLineEdit, 'codigo_libro').text()
        tomo = self.tercera_interfaz.findChild(QLineEdit, 'tomo').text()
        fecha_publicacion = self.tercera_interfaz.findChild(QDateEdit, 'fecha_publicacion').date()
        # Convierte la fecha a una cadena en el formato deseado
        fecha_formateada2 = fecha_publicacion.toString("dd/MM/yyyy")
        print(negocio2.editar_libro(id_libro,titulo,fecha_formateada2,tomo))

        #Categoria
        id_categoria = id_entero - 1
        genero = self.tercera_interfaz.findChild(QLineEdit, 'genero').text()
        #codigo_genero = self.tercera_interfaz.findChild(QLineEdit, 'codigo_genero').text()
        print(negocio.editar_categoria(id_categoria, genero))

        self.tercera_interfaz.close()

    def mostrar_cuarta_interfaz(self):
        # Carga y muestra la cuarta interfaz desde el archivo .ui
        self.cuarta_interfaz = uic.loadUi('Python/Parcial (Biblioteca)/Interfaz/Interfaz4.ui')

        # Conecta el botón de "Aceptar" en la cuarta interfaz a la función de captura
        aceptar = self.cuarta_interfaz.findChild(QPushButton, 'aceptar')
        aceptar.clicked.connect(self.capturar_datos_4)

        # Conecta el botón de "Cancelar" en la cuarta interfaz a la función de cancelar
        cancelar = self.cuarta_interfaz.findChild(QPushButton, 'cancelar')
        cancelar.clicked.connect(self.cancelar_4)

        self.cuarta_interfaz.show()

    def cancelar_4(self):
        # Cerrar la cuarta interfaz
        self.cuarta_interfaz.close()

    def capturar_datos_4(self):
        # Obtén los textos ingresados por el usuario desde los QLineEdits
        id_texto = self.cuarta_interfaz.findChild(QLineEdit, 'id').text()
        id_entero = int(id_texto)

        #Autor
        indice = id_entero - 1
        estado_autor = False
        print(negocio1.eliminar_autor(indice,estado_autor))

        #Libro
        id_libro = id_entero - 1
        estado_libro = False
        print(negocio2.eliminar_libro(id_libro,estado_libro))

        #Categoria
        id_categoria = id_entero - 1
        estado_categoria = False
        print(negocio.eliminar_categoria(id_categoria, estado_categoria))

        self.cuarta_interfaz.close()

    def mostrar_quinta_interfaz(self):
        # Carga y muestra la quinta interfaz desde el archivo .ui
        self.quinta_interfaz = uic.loadUi('Python/Parcial (Biblioteca)/Interfaz/Interfaz5.ui')

        # Conecta el botón de "aceptar" en la quinta interfaz a la función de cancelar
        aceptar_1 = self.quinta_interfaz.findChild(QPushButton, 'aceptar_1')
        aceptar_1.clicked.connect(self.cancelar_5)

        self.quinta_interfaz.show()

    def cancelar_5(self):
        print(negocio.generar_reporte())
        print(negocio1.generar_reporte())
        print(negocio2.generar_reporte())
        # Cerrar la quinta interfaz
        self.quinta_interfaz.close()
    

    def mostrar_sexta_interfaz(self):
        # Carga y muestra la quinta interfaz desde el archivo .ui
        self.sexta_interfaz = uic.loadUi('Python/Parcial (Biblioteca)/Interfaz/Interfaz6.ui')

        # Conecta el botón de "aceptar" en la quinta interfaz a la función de cancelar
        aceptar = self.sexta_interfaz.findChild(QPushButton, 'aceptar')
        aceptar.clicked.connect(self.cancelar_6)

        cancelar = self.sexta_interfaz.findChild(QPushButton, 'cancelar')
        cancelar.clicked.connect(self.sexta_interfaz.close)

        self.sexta_interfaz.show()

    def cancelar_6(self):
        # Obtén los textos ingresados por el usuario desde los QLineEdits
        id_texto = self.sexta_interfaz.findChild(QLineEdit, 'id').text()
        id_entero = int(id_texto)

        #Autor
        indice = id_entero - 1
        estado_autor = True
        print(negocio1.eliminar_autor(indice,estado_autor))

        #Libro
        id_libro = id_entero - 1
        estado_libro = True
        print(negocio2.eliminar_libro(id_libro,estado_libro))

        #Categoria
        id_categoria = id_entero - 1
        estado_categoria = True
        print(negocio.eliminar_categoria(id_categoria, estado_categoria))

        # Cerrar la sexta interfaz
        self.sexta_interfaz.close()

    def listar_libros(self):
        listado_autor = negocio1.obtener_autor()
        for autor in listado_autor:
            print(autor.imprimir())

        listado_libros = negocio2.obtener_libro()
        for libro in listado_libros:
            print(libro.imprimir())

        listado_categorias = negocio.obtener_categorias()
        for categoria in listado_categorias:
            print(categoria.imprimir())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlog = dialogo()
    dlog.show()
    sys.exit(app.exec())
