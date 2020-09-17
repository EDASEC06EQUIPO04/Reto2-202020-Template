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

import config as cf
from App import model
import csv
from DISClib.ADT import map as mp




"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    print ("Voy a inicializar el catalogo")
    catalog = model.newCatalog()

    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, moviesfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadMovies(catalog, moviesfile) 
    


def loadMovies(catalog, moviesfile):
    """
    Carga cada una de las lineas del archivo de peliculas.
    - Se agrega cada pelicula al catalogo de movies
    - Por cada movie se encuentran sus productor y por cada
    productor, se crea una lista con sus peliculas
    """
    moviesfile = cf.data_dir + moviesfile
    #input_file = csv.DictReader(open(moviesfile))
    input_file = csv.DictReader(open(moviesfile, encoding='utf-8-sig'),delimiter=";")
    for movie in input_file:
        model.addMovie(catalog, movie)
        companies = movie['production_companies'].split(";")  # Se obtienen las productoras
        for production in companies:
            model.addProdCompany(catalog, production.strip(), movie)
        
        
        #average = movie['vote_average'].split(";")  # Se obtienen promedio  
        #nameMovie = movie['original_title'].split(";")  # Se obtienen nombre de peicula   
        #for j in companies:
            #print (j)
    #       model.addProductionCompany(catalog, j.strip(), nameMovie)
        #for j in average:
            #print (j) 
        #for j in nameMovie:
            #print (j)              
            

    #input (" El nombre de la compania y el tamano del Map. Clic para continuar")


# ___________________________________________________
#  Consultas
# ___________________________________________________

def getBooksByAuthor(catalog, authorname):
    """
    Retorna los libros de un autor
    """
    authorinfo = model.getBooksByAuthor(catalog, authorname)
    return authorinfo

