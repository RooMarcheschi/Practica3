import csv
#import os.path
import os


path_files = "files"
archivo_net = "netflix_titles.csv"

path_arch = os.path.join(os.getcwd(), path_files)

archivo = open(os.path.join(path_arch, archivo_net), "r")
data_net = csv.reader(archivo, delimiter=',')
header, datos= next(data_net), list(data_net)
header

#for linea in datos:
#    print(linea)
#--------1----------
def tipos_show_pais(pais):
    shows_pais = [i for i in datos if pais in i[5].split(', ')]
    tipos = set([s[1] for s in shows_pais])
    return tipos

pais = "United States"
print(f"The types of show that {pais} have are: ")
for t in tipos_show_pais(pais):
    print(t)


def paises():
    ls = [p[5].split(', ') for p in datos]
    flat_ls = [item for sublist in ls for item in sublist]
    paises = set(flat_ls)
    return paises

print("The countries in this csv are: ")
for p in paises():
    print(p)

#falta la parte c q no la entiendo

#--------2----------
def paises_ordenados():
    ls = [p[5].split(', ') for p in datos]
    flat_ls = [item for sublist in ls for item in sublist]
    paises = set(flat_ls)
    return sorted(list(paises))

print("Sorted countries: ")
for p in paises_ordenados():
    print(p)


#--------3----------
def shows_anio(anio):
    shows = [p[2] for p in datos if p[7] == anio]
    return shows

print("The shows from that year are: ")
for p in shows_anio("2021"):
    print(p)