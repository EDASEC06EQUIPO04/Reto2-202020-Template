def newCatalog():
    catalog = {'books': None,
               'bookIds': None,
               'authors': None,
               'tags': None,
               'tagIds': None,
               'years': None}

    catalog['books'] = lt.newList('SINGLE_LINKED', compareBookIds)
    catalog['bookIds'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['authors'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareAuthorsByName)
    catalog['tags'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareTagNames)
    catalog['tagIds'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareTagIds)
    catalog['years'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapYear)



def loadTags(catalog, tagsfile):
    """
    Carga en el catalogo los tags a partir de la informacion
    del archivo de etiquetas
    """
    tagsfile = cf.data_dir + tagsfile
    input_file = csv.DictReader(open(tagsfile))
    for tag in input_file:
        model.addTag(catalog, tag)




def addTag(catalog, tag):
    """
    Adiciona un tag a la tabla de tags dentro del catalogo
    """
    newtag = newTagBook(tag['tag_name'], tag['tag_id'])
    mp.put(catalog['tags'], tag['tag_name'], newtag)
    mp.put(catalog['tagIds'], tag['tag_id'], newtag)



def newTagBook(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = lt.newList()
    return tag
