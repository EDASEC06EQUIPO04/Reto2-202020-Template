
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@            CONTROLLER              @@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
# _____loadDataCast(cont1, castingSmall)______________________________________________

def loadDataCast(catalogo1, castingfile):
    """
    Carga los datos de los archivos en el modelo
    """
    loadIdMovies(catalogo1, castingfile) 

def loadIdMovies(catalogo1, castingfile):
    """
    Carga cada una de las lineas del archivo de peliculas.
    - Se agrega cada pelicula al catalogo de movies
    - Por cada movie se encuentran sus productor y por cada
    productor, se crea una lista con sus peliculas
    """
    castingfile = cf.data_dir + castingfile
    #input_file = csv.DictReader(open(moviesfile))
    input_file = csv.DictReader(open(castingfile, encoding='utf-8-sig'),delimiter=";")
    j=0
    for id in input_file:
        model.addId(catalogo1, id)
        director= id['director_name'].split(";")  # Se obtienen las productoras
        #j=j+1
        #print (j)
        for idDir in director:
            model.addDirectorId(catalogo1, idDir.strip(), id)
        
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
    i=0
    for movie in input_file:
        #i=i+1
        #print (i)
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



def getMoviesProdCompany (cat, company):
    infoCompania =model.getMoviesProdCompany(cat,company)
    return infoCompania

def getMoviesDirector (catalogo1, director):
    #print ("Aqui estamos")
    #input ("Dar clic para continuar")
    infoDirector =model.getMoviesDirector(catalogo1, director)
    return infoDirector