class corretor():
    def __init__(self,lista,ntab,vlabel):
        self.lista=lista
        self.tam=(len(lista))
        self.saida=[]
        self.vlabel=vlabel
        if ntab==89:
            self.cor89()
        if ntab==10:
            self.cor10()
        if ntab==11:
            self.cor11()        
    def cor89(self):
        if self.tam>=2 and len(self.lista[self.tam-1])==6:
           nova_lista=[]
           LP0=self.lista[self.tam-2][:]
           LP1=self.lista[self.tam-1][:]
           m=0
           for ll in LP0:
               if m==1:
                   temp=[]
                   for k in range(0,len(ll)-1):
                       temp.append(ll[k])
                   if  self.tam==2:
                       temp.append("")
                   else:
                       temp.append("conclusão")
                   nova_lista.append(temp)
               else:
                   nova_lista.append(ll)
               m+=1
           nova_lista.append(LP1[len(LP1)-1])
           self.saida.append(nova_lista)
        else:
           self.saida=self.lista[:]
            
    def cor10(self):
        if self.tam>=2 and len(self.lista[self.tam-1])==5:
           nova_lista=[]
           LP0=self.lista[self.tam-2][:]
           LP1=self.lista[self.tam-1][:]
           m=0
           for ll in LP0:
               if m==1:
                   temp=[]
                   for k in range(0,len(ll)-1):
                       temp.append(ll[k])
                   if  self.tam==2:
                       temp.append("")
                   else:
                       temp.append("conclusão")
                   nova_lista.append(temp)
               else:
                   nova_lista.append(ll)
               m+=1
           nova_lista.append(LP1[len(LP1)-1])
           self.saida.append(nova_lista)
        else:
           self.saida=self.lista[:]       

    def cor11(self):
        print("TAMANHO")
        print(self.tam)
        print("TAMANHO2")
        print(len(self.lista[self.tam-1]))
        if self.tam>=2 and len(self.lista[self.tam-1])==5:
           LP0=self.lista[self.tam-2][:]
           LP1=self.lista[self.tam-1][:]
           nova_lista=[]
           m=0
           for ll in LP0:
               if m==1:
                   temp=[]
                   for k in range(0,len(ll)-1):
                       temp.append(ll[k])
                   temp.append(self.vlabel)
                   nova_lista.append(temp)
               else:
                   nova_lista.append(ll)
               m+=1
           nova_lista.append(LP1[len(LP1)-1])
           self.saida.append(nova_lista)
        else:
           self.saida=self.lista[:]     
