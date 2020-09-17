"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller 
#import controller
assert config
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________



castingLarge='themoviesdb/MoviesCastingRaw-large.csv'
castingSmall='themoviesdb/MoviesCastingRaw-small.csv'
moviesLarge='themoviesdb/MoviesDetailsCleaned-large.csv'
moviesSmall='themoviesdb/MoviesDetailsCleaned-small.csv'
booksfile = 'GoodReads/books-small.csv'
tagsfile = 'GoodReads/tags.csv' 
booktagsfile = 'GoodReads/book_tags-small.csv'



# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printProductionCompany(prodCompany):
 #output pelicula de una compañia de producción
 #output =: imprime peliculas de una compañoia de producción
    if author:
        print('compañia encontrada: ' + prodCompany['production_company'])
        print('Promedio: ' + str(prodCompany['vote_average']))
        print('Peliculas totales: ' + str(lt.size(prodCompany['movies'])))
        iterator = it.newIterator(prodCompany['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'] + movie['vote_average'])
    else:
        print('No se encontro la compañia buscada')





# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n********************************  Grupo 04  ******************************************")
    print("\n*********** CONSOLA DEL RETO 2 @@@ EXPLORANDO LA MAGIA DEL CINE RECARGADO @@@  *******")
    print("\n**************************************************************************************")
    print(" ")
    print("(1) Inicializar Catálogo de movies y casting")
    print("(2) Cargar información en el catálogo de movies y casting")
    print("(3)   REQ. 1: Consultar las productoras de cine")
    print("(4)   REQ. 2: Consultar a un director")
    print("(5)   REQ. 3: Consultar a un actor")
    print("(6)   REQ. 4: Entender un genero cinematografico")
    print("(7)   REQ. 5: Consultar peliculas por pais")
    print("(0) Salir")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar ? ')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo  Movies y Casting ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()
        #print (cont)
        input ("Se creo el catalogo. Clic para continuar   ....")

    

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        #controller.loadData(cont, booksfile, tagsfile, booktagsfile)
        controller.loadData(cont, moviesSmall)
        print ("Se han cargado tanas peliculas: ", lt.size(cont['movies']))
        #input ("dar clic par ver lo cargado...")
        #for i in range (0,10):
            #print("\n**************************************************************************************")
            # print (lt.getElement(cont['movies'],i))
        
        #print('Peliculas cargadas: ' + str(lt.size(cont)))
        
        input ("clic para coninuar")
        #print('Géneros cargados: ' + str(controller.tagsSize(cont)))

        
        pass
    
    elif int(inputs[0]) == 3:
        name = input("Nombre de compañia: ")
        prodInfo = controller.getBooksByAuthor(cont, name)
        printProductionCompany(prodInfo)
        pass

    elif int(inputs[0]) == 4:
        input ("Opcion en construccion")
        pass

    elif int(inputs[0]) == 5:
        input ("Opcion en construccion")
        pass
    else:
        sys.exit(0)
sys.exit(0)