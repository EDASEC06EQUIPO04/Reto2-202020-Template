
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
               'vote_count': None}


    catalog['movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    #lst = lt.newList("ARRAY_LIST")
    #lst = lt.newList("SINGLE_LINKED")

    print (  catalog['movies'])
    #input ("@@@@ Clic para continuar @@@@ ")

    catalog['production_companies'] = mp.newMap(2000,
                                    maptype='PROBING',
                                    #PROBING, CHAINING
                                    loadfactor=0.4,
                                    comparefunction=compareproductionCompanies)

    return catalog 
    





# Funciones para agregar informacion al catalogo


def addMovie(catalogo,movie):
    """
    Esta funcion adiciona un pelicula a la lista de movie,
    adicionalmente lo guarda en un Map usando como llave su production_companies_I.

    """
    lt.addLast(catalogo['movies'], movie)
    #mp.put(catalogo['production_companies_ID'], movie['id'], movie)
    #mp.put(catalog['id'], movies['id'], movies)
    #print (mp.get(catalogo['production_companies_ID'], movie['id']))
    #print (mp.get(catalog['id'],movies['id']))
  

    # input ("Ya estoy aqui.. y voy adicionar un book ....Clic para continuar")
   
    
""" 
def addBook(catalog, book):
    
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    
    lt.addLast(catalog['books'], book)
    mp.put(catalog['bookIds'], book['goodreads_book_id'], book)
    #print (mp.get(catalog['bookIds'],book['authors']))
    print (mp.get(catalog['bookIds'],book['goodreads_book_id']))
    #input ("Ya estoy aqui.. y voy adicionar un book ....Clic para continuar")
    print ("===============================================================================================================")

    addBookYear(catalog, book)
    
"""
    #addProductionCompany(catalog, j.strip(), j)

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




def addProductionCompany(catalog, companyName, movie):
    """
    Esta función adiciona una pelicula a la lista de pelicualas de una cierta productora
    Cuando se adiciona el la pelicula se actualiza el promedio de de la ,is,a
    """
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
#        nombrePelicula = newPelicula(companyName) 
        # aqui debo continuar con el codigo, pero no habia podido..
        mp.put(catalog['production_companies_ID'], companyName, nombrePelicula)
    
    """ aqui hay que asegurar que el map cargue bien, algo me esta pasando que no lo logro """
    """ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

    #for i in  catalog['production_companies_ID']:   
    #     print (mp.get(catalog['production_companies_ID'], companyName))
    #input("dar clic")
    #lt.addLast(nombrePelicula['vote_average'], movie)

    #authavg = nombrePelicula['vote_average']
    #PelAvg = movie['vote_average']
    #if (authavg == 0.0):
    #    nombrePelicula['vote_average'] = float(PelAvg)
    #else:
    #    nombrePelicula['vote_average'] = (authavg + float(PelAvg)) / 2



# ==============================
# Funciones de consulta
# ==============================

def addProdCompany(catalog, prodcom, movie):
    """
    Esta función adiciona un libro a la lista de libros publicados
    por un autor.
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
