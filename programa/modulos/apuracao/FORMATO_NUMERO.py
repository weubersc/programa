import csv
import os
import string
import math

def inteiro(var):
         try:
              var2=int(var)
              vf=("{:,}".format(var2).replace(",", " "))
              VS=str(vf)
         except ValueError:
             if var=="x":
                VS=var
             else:
                VS="-"
         return(VS)
     
def flutuante(var):
         multiplier = 10 ** 0        
         try:             
              vv3=(float(var)/1000)
              vv=int(math.floor(vv3*multiplier + 0.5) / multiplier)
              vf=("{:,}".format(vv).replace(",", " "))
              VS=str(vf)
         except ValueError:
             if var=="x":
                VS=var
             else:
                VS="-"
         return(VS)
