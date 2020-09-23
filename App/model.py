
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
                'id': None,
                'production_companies': None,
                'original_title': None,
                'vote_average': None,
                'vote_count': None,
                'genres': None,
                'production_countries':None,
                'actor1_name': None,
                'actor2_name': None,
                'actor3_name': None,
                'actor4_name': None,
                'actor5_name': None,
                'director_name':None}


    catalog['movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['casting'] = lt.newList('ARRAY_LIST', compareDirectorIds)
    #lt.newList("SINGLE_LINKED")

    catalog['id'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareproductionCompanies)
    catalog['production_companies'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareproductionCompanies)
    catalog['genres'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareproductionCompanies)
    catalog['production_countries'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareproductionCompanies)
    catalog['directors'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareActors)
    catalog['movieIds'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareActors)
    catalog['actors1'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareActors)

#HERE WE CAN ADD ACTORS 2-4



    return catalog 





# Funciones para agregar informacion al catalogo


def addMovie(catalogo,movie):
    """
    Esta funcion adiciona un pelicula a la lista de movie,
    adicionalmente lo guarda en un Map usando como llave su production_companies_I.
    """
    lt.addLast(catalogo['movies'], movie)



def newPelicula(name):
    """
    Crea una nueva estructura para modelar los pelicuales de un productora
    y su promedio de ratings
    """
    productora = {'production_companies': "", "movies": None,  "average_rating": 0}
    productora['production_companies'] = name
    productora['movies'] = lt.newList('SINGLE_LINKED', comparePeliculasByName)
    return productora


def newProd(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    company= {'production_companies': "", "movies": None,  "average_rating": 0}
    company['production_companies'] = name
    company['movies'] = lt.newList('SINGLE_LINKED', compareprodComs)    
    return company











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



#pretty sure this one is referenced by nothing and can be deleted
#dont delete without validating it is in fact useless
def addProductionCompany(catalog, companyName, movie):

    nombrePelicula = catalog['original_title']
    print ("")
    print ("\n", nombrePelicula)
    input (" Clic para continuar despues de nombre pelicula...")

    #existePelicula = mp.contains(nombrePelicula, companyName)
    existePelicula = mp.contains(catalog['production_companies_ID'], companyName)

    if existePelicula:
        entry = mp.get(catalog['production_companies_ID'], companyName)
        nombrePelicula = me.getValue(entry)
    else:
        mp.put(catalog['production_companies_ID'], companyName, nombrePelicula)
    








def addDirector(catalog, director):
#each row builds a catal;ogue entry from csv2

#this row corresponds to the rows in the CSV
    newdic = newDirector(director['director_name'], director['actor1_name'], director['id'])

#these rows are the names assigned in the catalogue. note first item in brackest is the assigned name of the new catalogue, second one is the reference matching CSV and first line
    mp.put(catalog['directors'], director['director_name'], newdic)
    mp.put(catalog['actors1'], director['actor1_name'], newdic)
    mp.put(catalog['movieIds'], director['id'], newdic)




def newDirector(director, actor1, id):

    casting= {'director': '',
            'actor1': '',
            'movieId': '',
            'total_movies': 0,
            'movies': None,
            'count': 0.0}
    casting['director'] = director
    casting['actor1'] = actor1
    casting['movieIds'] = id
    casting['movies'] = lt.newList()
    return casting




def addId(catalogo1,id):

    lt.addLast(catalogo1['id'], id)




# ==============================
# Funciones de consulta
# ==============================

def addProdCompany(catalog, prodcom, movie):

    companies = catalog['production_companies']
    existincompany = mp.contains(companies, prodcom)
    if existincompany:
        entry = mp.get(companies, prodcom)
        companyadd = me.getValue(entry)
    else:
        companyadd = newProd(prodcom)
        mp.put(companies, prodcom, companyadd)
    lt.addLast(companyadd['movies'], movie)


def addGenre(catalog, genre, movie):

    newgenre = catalog['genres']
    existgenre = mp.contains(newgenre, genre)
    if existgenre:
        entry = mp.get(newgenre, genre)
        genreToAdd = me.getValue(entry)
    else:
        genreToAdd = newProd(genre)
        mp.put(newgenre, genre, genreToAdd)
    lt.addLast(genreToAdd['movies'], movie)



def addDirectorId(catalog1, director, id):

    moviesID = catalog1['directors']
    existinID = mp.contains(moviesID, director)
    if existinID:
        entry = mp.get(moviesID, director)
        movieAdd = me.getValue(entry)
    else:
        movieAdd= newMoviedirect(director)
        mp.put(moviesID, director, movieAdd)
    lt.addLast(movieAdd['id'], id)




def newMoviedirect(nameDirector):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    directorCast= {'director': "","id":None, "movies": None,  "average_rating": 0}
    directorCast['director'] = nameDirector
    directorCast['id'] = lt.newList('SINGLE_LINKED', compareprodComsCast)    
    directorCast['movies'] = lt.newList('SINGLE_LINKED', compareprodComsCast)    
    return directorCast

# ==============================
# Funciones de Comparacion
# ==============================
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


def compareproductionCompanies(keyname, company):
    authentry = me.getKey(company)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareActors(keyname, actor):
    authentry = me.getKey(actor)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareprodComsCast(keyname, directorCat):

    authentry = me.getKey(directorCat)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1



def compareDirectorIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1



def moviesSize(catalog):
    return lt.size(catalog['movies'])


def getMoviesProdCompany (cat, company):
    compania = mp.get(cat['production_companies'], company)
    if compania:
        return me.getValue(compania)
    return None



def getMoviesByDirector(catalog, nameInput):
    #this function searches with the name defined in the catalogue, not the name in the CS

    directorsearched = mp.get(catalog['directors'], nameInput)
    if directorsearched:
        return me.getValue(directorsearched)
    return None



def getMoviesGenre(cat, genre):
    genreresult = mp.get(cat['genres'], genre)
    if genreresult:
        return me.getValue(genreresult)
    return None







"""
    directorsearched = mp.get(catalog['directors'], nameInput)
    if directorsearched:
        return me.getValue(directorsearched)
    return None


    result = mp.get(catalog['directors'], nameInput)
    movies = None
    if result:
        movies = me.getValue(result)['movies']
    return movies
"""

