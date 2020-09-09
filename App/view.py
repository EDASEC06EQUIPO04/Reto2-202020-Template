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

MovieDetailsS="Data/themoviesdb/MoviesDetailsCleaned-small.csv"
MovieCastingS="Data/themoviesdb/MoviesCastingRaw-small.csv"

MovieDetailsL="Data/themoviesdb/MoviesDetailsCleaned-large.csv"
MovieCastingL="Data/themoviesdb/MoviesCastingRaw-large.csv"


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def menu():

    print("\nBienvenido")
    print ("Cargar Datos small (1)")
    print("")
    print ("Cargar Datos large (2)")
    print("")
    print("Salir (0)")


def main():
    
    while True:
        menu() 
        print("")
        inputs =input('Seleccione una opción para continuar\n') 
        if len(inputs)>0:

            if int(inputs[0])==1: #opcion 1
                controller.Mostrar_lista_s(MovieDetailsS, MovieCastingS)

            elif int(inputs[0])==2: #opcion 2
                controller.Mostrar_lista_l(MovieDetailsL, MovieCastingL)

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()