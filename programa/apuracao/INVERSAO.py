from programa.modulos.apuracao.FORMATO_NUMERO import inteiro as formato
from programa.modulos.apuracao.FORMATO_NUMERO import flutuante as tonelada

def INVERTER(LISTA,VAR1,VAR2):
    
    temporario=[]
    for j in range(0,len(VAR2)):
        temp=[]
        temp.append(VAR2[j])
        for pp in VAR1:
            for ll in LISTA:
                if ll[0]==pp and j==ll[1]:
                    temp.append(formato(ll[2]))
                    temp.append(tonelada(ll[3]))
        temporario.append(temp)
    return(temporario)

def FORMATAR(listatemp,VAR1,VAR2,num):
    LISTAFORMAT=[]
    for j in range(1,len(VAR1)*2+1,num):
        temp=[]
        for k in range(0,len(VAR2)):
            for te in listatemp:    
                if VAR2[k]==te[0]:
                    temp.append([te[0],te[j],te[1+j],te[2+j],te[3+j],te[4+j],te[5+j],
                                 te[6+j],te[7+j],te[8+j],te[9+j],te[10+j],te[11+j]])
        LISTAFORMAT.append(temp)

    return(LISTAFORMAT)
        

    
