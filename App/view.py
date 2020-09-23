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
from DISClib.ADT import map as mp
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


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printProductionCompany(prodCompany):
    if prodCompany:

        iterator = it.newIterator(prodCompany['movies'])

        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'] + '  Vote average: ' + movie['vote_average'])
    else:
        print('No se encontro la compañia buscada')



def printMoviesbyDirector(directorInput):
    iterator = it.newIterator(directorInput['casting'])

    while it.hasNext(iterator):
        movie = it.next(iterator)
    print(directorInput['id']['first'])


def printgenre(ginput):
    if ginput:
        iterator = it.newIterator(ginput['movies'])
        while it.hasNext(iterator):
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'] + '  Vote average: ' + movie['vote_average'])
    else:
        print('No se encontro el genero buscado')



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n*********************** RETO 2 @@@ EXPLORANDO LA MAGIA DEL CINE RECARGADO @@@  *******")
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


    #input 1 and input 2 could be merged to create the catalogue and load it with movies in one input
    if int(inputs[0]) == 1:
        cont = controller.initCatalog()
        input ("presione una tecla para continuar...")


    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, moviesSmall, castingSmall)
        print ("Se han cargado: ")
        print(str(controller.moviesSize(cont)), "peliculas: ")

        #these functions can be rewritten to follow the model-> controller distribution. use the moviessize print as a reference
        print (mp.size(cont["production_companies"]), "  compañias de producción ")
        print (mp.size(cont["genres"]), "  generos ")
        print (mp.size(cont["directors"]), "  directores ")
        print (mp.size(cont["actors1"]), "  actores")
        input ("presione una tecla para continuar...")

    #-------------requerimiento 1-----------------
    #input:     nombre compania de producción
    # output1: lista de todas las peliculas
    # output2: total de peliculas 
    # output3: vote average de las peliculas 
    elif int(inputs[0]) == 3:
    
        nameInput = input("Nombre de compañia a buscar: ")
        nombreCompanias = controller.getMoviesProdCompany(cont, nameInput)
        printProductionCompany(nombreCompanias)
        input ("presione una tecla para continuar...") 

    #-------------requerimiento 2-----------------
    #input:    nombre de un director
    # output1: lista de todas las peliculas dirigidas  
    # output2: total de peliculas 
    # output3: vote average de las peliculas
    elif int(inputs[0]) == 4:

        print (mp.size(cont["directors"]), "  directores ")

        nameInput = input("Nombre de director: ")
        directors = controller.getMoviesDirector(cont, nameInput)
        printMoviesbyDirector(directors)
        input ("presione una tecla para continuar...") 

    #-------------requerimiento 3-----------------
    #input:     nombre actor
    # output1:  lista peliculas que participo
    # output2:  total de peliculas
    # output3:  vote average de las peliculas
    # output 4: nombre de director con mas collabs (peliculas que incluyen actor + director)
    elif int(inputs[0]) == 5:
        input ("Opcion en construccion")
        pass

    #-------------requerimiento 4-----------------
    #input:     genero cinematografico
    # output1: lista de peliculas asociadas
    # output2: total de peliculas
    # output3: promedio de votos
    elif int(inputs[0]) == 6:
        nameInput = input("Nombre de genero a buscar: ")
        result = controller.getMoviesGenre(cont, nameInput)
        printgenre(result)
        input ("presione una tecla para continuar...") 

    #-------------requerimiento 5-----------------
    #input:     pais
    # output1:  lista de peliculas producidas en el pais
    # output2:  titulo y año de produccion (por pelicula)
    # output3:  nombre del director que la dirigio
    elif int(inputs[0]) == 7:
        input ("Opcion en construccion")
        pass



    else:
        sys.exit(0)
sys.exit(0)