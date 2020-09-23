# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@             VIEW                   @@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


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
    if prodCompany:
        
        #print('Promedio: ' + str(prodCompany['vote_average']))
        #print('Peliculas totales: ' + str(lt.size(prodCompany['movies'])))
        iterator = it.newIterator(prodCompany['movies'])
        cuenteTotal=0
        while it.hasNext(iterator):
            cuenteTotal=cuenteTotal+1
            movie = it.next(iterator)
            print('Titulo: ' + movie['original_title'] + '  Vote average: ' + movie['vote_average'])
    else:
        print('No se encontro la compañia buscada')
    return cuenteTotal

def printPeliculasDirector(director):

    if director:
        
        iterator = it.newIterator(director['id'])
        cuenteTotal=0
        while it.hasNext(iterator):
            cuenteTotal=cuenteTotal+1
            direct = it.next(iterator)
        print('\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('\nId_Director: ', " ", director['id'])


    else:
        print('No se encontro el director seleccionado')
    return cuenteTotal
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
        print ("Se han cargado", mp.size(cont["production_companies"]), "peliculas: ")
        print("")
        print("\n**************************************************************************************")
        print (lt.getElement(cont['movies'],0))
        ultimo=int(lt.size(cont['movies']))-1
        print ("el tamano de la lista es", len(cont['movies']))
        print("")
        print (lt.getElement(cont['movies'],ultimo))
        print("")
        input ("De pruenba se imprime primera y 'ultima pelicula. Clic para continuar")

        pass
    
    elif int(inputs[0]) == 3:
        nameInput = input("Nombre de compañia productora: ")
        nombreCompanias = controller.getMoviesProdCompany(cont, nameInput)
        print("")
        print("\n**************************************************************************************")
        cuenteTotal=printProductionCompany(nombreCompanias)
        print("\n**************************************************************************************")
        # print(" Se encontraron  [ ", cuenteTotal, " ] peliculas de la productora")
        input ("Clic para continuar")
        pass

    elif int(inputs[0]) == 4:
        #cont1 = controller.initCatalogCast()
        #print (cont1)
        input ("Se creo el catalogo. Clic para continuar   ....")
        print("Cargando información de los archivos ....")
        #controller.loadData(cont, booksfile, tagsfile, booktagsfile)
        controller.loadDataCast(cont, castingSmall)
        print ("")
        nameInput = input("Nombre de director: ")
        nombreDirectores = controller.getMoviesDirector(cont, nameInput)
        print("")
        print("\n**************************************************************************************")
        cuenteTotal=printPeliculasDirector(nombreDirectores)
        print("\n**************************************************************************************")
        print(" Se encontraron  [ ", cuenteTotal, " ] peliculas del director selecionado")
        input ("Clic para continuar")
        
        pass

    elif int(inputs[0]) == 5:
        #print (mp.get(cont,'director_Movies'))
        print (mp.size(cont['production_companies']))

        print (mp.size(cont['director_Movies']))
        input ("Mapa de directores.. clic")
        pass
    else:
        sys.exit(0)
sys.exit(0)