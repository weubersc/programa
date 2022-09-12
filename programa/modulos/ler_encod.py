import chardet

def LER_ENCOD(ARQ):
    with open(ARQ, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
        encod=(result["encoding"])
        return(encod)
    
