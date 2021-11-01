import difflib

def clearCompara(nArquivos = 2, byts = bytearray()): #nArquivos= numero de arquivos clear na pasta
    d = difflib.Differ()
    x = open("clear"+str(nArquivos)+".bin", encoding = "ISO-8859-1").read()
    y = open("clear"+str(nArquivos-1)+".bin", encoding = "ISO-8859-1").read()
    e = d.compare(x,y)
    print(list(e))    
    # for i in range(0,len(list(e))):
    #    if i.startswith("-"):
    #        print(i + " <- index diferente")

    if nArquivos < 2:
        clearCompara(nArquivos-2, byts)



clearCompara()