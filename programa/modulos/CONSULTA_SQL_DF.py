import pandas as pd
import sqlite3
import os



def DF_SQL_DF(DF,sql_query,tabela):
   conn=sqlite3.connect("banco.db")
   DF.to_sql(tabela,conn,if_exists="replace",
                         index=False)
   conn.close()
   conn=sqlite3.connect("banco.db")
   DF_SAIDA=pd.read_sql_query(sql_query,conn)
   conn.close()
   os.remove("banco.db")
   return(DF_SAIDA)
