import difflib
import os

def comparaEndereco(listaDeListas, endereco):
    arr = list()
    for lista in listaDeListas:
        arr.append(lista[endereco])
    retorno = arr.count(arr[0]) == len(arr)
    # if retorno == False:
    #     print(arr)
    return retorno

def montaArray(nArquivos = 2, byts = list()): #nArquivos= numero de arquivos clear na pasta
    x = open(os.getcwd()+"/clear"+str(nArquivos)+".bin", "rb").read()
    e = list()
    for i in list(x):
        e.append(hex(i))
    
    byts.append(e)
    if nArquivos > 1:
        retorno = montaArray(nArquivos-1, byts)
        return retorno
    else:
        indexesFixos = list()
        for i, hexa in enumerate(e):
            if comparaEndereco(byts, i):
                indexesFixos.append(i)
        # print(indexesFixos)
        return indexesFixos

retorno = montaArray()
print(retorno)