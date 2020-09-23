
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@            MODEL                   @@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config
"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""
# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    
    catalog = {'movies': None,
               'production_companies': None,
               'director_Movies': None,
               'id_Movie': None
                }
   
    catalog['production_companies'] = mp.newMap(3000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.5,
                                    comparefunction=compareproductionCompanies)
    
    catalog['director_Movies'] = mp.newMap(3000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.5,
                                    comparefunction=compareproductionDirector)
    catalog['id_Movie'] = mp.newMap(3000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.5,
                                    comparefunction=compareproductionDirector)


    catalog['movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['id'] = lt.newList('ARRAY_LIST', compareDirectorIds)
    #lst = lt.newList("ARRAY_LIST")"SINGLE_LINKED")

    #print (catalog['movies'])
    #print (catalog['id'])
    #input ("@@@@ Clic para continuar @@@@ ")


    return catalog 
    

# Funciones para agregar informacion al catalogo
def addId(catalogo1,id):
    """
    Esta funcion adiciona un pelicula a la lista de movie,
    adicionalmente lo guarda en un Map usando como llave su production_companies_I.
    """
    lt.addLast(catalogo1['id'], id)


def addMovie(catalogo,movie):
    """
    Esta funcion adiciona un pelicula a la lista de movie,
    adicionalmente lo guarda en un Map usando como llave su production_companies_I.
    """
    lt.addLast(catalogo['movies'], movie)



def newProd(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    company= {'production_companies': "", "movies": None,  "average_rating": 0}
    company['production_companies'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareprodComs)    
    return company

def newMovie(nameDirector):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    directorCast= {'director': "","id":None, "movies": None,  "average_rating": 0}
    directorCast['director'] = nameDirector
    directorCast['id'] = lt.newList('SINGLE_LINKED', compareprodComsCast)   
    
    directorCast['movies'] = lt.newList('SINGLE_LINKED', compareprodComsCast)    
    return directorCast

def compareprodComsCast(keyname, directorCat):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(directorCat)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareprodComs(keyname, company):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def addProdCompany(catalog, prodcom, movie):
    """
    Esta función adiciona una pelicula al mapa de 
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    companies = catalog['production_companies']
    existincompany = mp.contains(companies, prodcom)
    if existincompany:
        entry = mp.get(companies, prodcom)
        companyadd = me.getValue(entry)
    else:
        companyadd = newProd(prodcom)
        mp.put(companies, prodcom, companyadd)
    lt.addLast(companyadd['movies'], movie)

def addDirectorId(catalog1, director, id):
    """
    Esta función adiciona una pelicula al mapa de 
    Cuando se adiciona el libro se actualiza el promedio de dicho autor
    """
    moviesID = catalog1['director_Movies']
    existinID = mp.contains(moviesID, director)
    if existinID:
        entry = mp.get(moviesID, director)
        movieAdd = me.getValue(entry)
    else:
        movieAdd= newMovie(director)
        mp.put(moviesID, director, movieAdd)
    lt.addLast(movieAdd['id'], id)

# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones de Comparacion
# ==============================
def compareDirectorIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareMovieIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
        

def comparePeliculasByName(keyname, pelicula):
    """
    Compara dos nombres de pelicula. El primero es una cadena
    y el segundo un entry de un map
    """
    pelhentry = me.getKey(pelicula)
    if (keyname == pelhentry):
        return 0
    elif (keyname > pelhentry):
        return 1
    else:
        return -1

def compareproductionDirector(keyDirector, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(director)
    if (keyDirector == authentry):
        return 0
    elif (keyDirector> authentry):
        return 1
    else:
        return -1


def compareproductionCompanies(keyname, company):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def getMoviesProdCompany (cat, company):
    compania = mp.get(cat['production_companies'], company)
    if compania:
        return me.getValue(compania)
    return None

def getMoviesDirector (catalogo1, director):
    directorPel = mp.get(catalogo1['director_Movies'], director)
    if directorPel:
        return me.getValue(directorPel)
    return None