from unicodedata import normalize



class Eliminar_Acentos():

    def __init__(self,lista):
        self.dicTrans={}
        self.novalista=[]
        for ll in lista:
            novo=normalize('NFKD', ll).encode('ASCII', 'ignore').decode('ASCII')
            self.dicTrans[novo]=ll
            self.novalista.append(novo)

    def ordenar(self):
        lista_esp=[]
        dic_esp={}
        for ll in self.novalista:
            var=ll.upper().replace(' ','')
            var=ll.upper().replace('-',' ')
            lista_esp.append(var)
            dic_esp[var]=ll
            #print(var)
        lista_esp.sort()
        novalista=[]
        for ll in lista_esp:
            novalista.append(self.dicTrans[dic_esp[ll]])
        return(novalista)

            
            

if __name__=="__main__":
      lista=["Brasil",
            "Rondônia",
            "Acre",
            "Amazonas",
            "Roraima",
            "Pará",
            "Amapá",
            "Tocantins",
            "Maranhão",
            "Piauí",
            "Ceará",
            "Rio Grande do Norte",
            "Paraíba",
            "Pernambuco",
            "Alagoas",
            "Sergipe",
            "Bahia",
            "Minas Gerais",
            "Espírito Santo",
            "Rio de Janeiro",
            "São Paulo",
            "Paraná",
            "Santa Catarina",
            "Rio Grande do Sul",
            "Mato Grosso do Sul",
            "Mato Grosso",
            "Goiás",
            "Distrito Federal"
               ]
      EL=Eliminar_Acentos(lista)
      EL.ordenar()
