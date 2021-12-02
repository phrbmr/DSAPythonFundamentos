#Aula 6
import os
import sqlite3

import random
import time
import datetime

import matplotlib.pyplot as plt

## Aula 2
# Remove o arquivo com o banco de dados SQLite (caso exista)
os.remove("dsa.db") if os.path.exists("dsa.db") else None

# Criando uma conexão
conn = sqlite3.connect('dsa.db')   

# Criando um cursor
c = conn.cursor()
 
# Função para criar uma tabela
def create_table():
  c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')
    
# Função para inserir uma linha
def data_insert():
  c.execute("INSERT INTO produtos VALUES(10, '2020-05-02 14:32:11', 'Teclado', 90 )")
  conn.commit()

##Aula 3
# Usando variáveis para inserir dados    
def data_insert_var():
  new_date = datetime.datetime.now()
  new_prod_name = 'Monitor'
  new_valor = random.randrange(50,100)
  c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
  conn.commit()

##Aula 4
# Leitura de dados
def leitura_todos_dados():
  c.execute("SELECT * FROM PRODUTOS")
  for linha in c.fetchall():
    print(linha)
        
# Leitura de registros específicos
def leitura_registros():
  c.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
  for linha in c.fetchall():
    print(linha)      
        
# Leitura de colunas específicos
def leitura_colunas():
  c.execute("SELECT * FROM PRODUTOS")
  for linha in c.fetchall():
    print(linha[3])       

##Aula 5
# Update
def atualiza_dados():
  c.execute("UPDATE produtos SET valor = 70.00 WHERE valor = 98.0")
  conn.commit()
    
# Delete
def remove_dados():
  c.execute("DELETE FROM produtos WHERE valor = 62.0")
  conn.commit()

##Aula 6
# Gerar gráfico com os dados no banco de dados
def dados_grafico():
    c.execute("SELECT id, valor FROM produtos")
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
        
    plt.bar(ids, valores)
    plt.show()

# Criar tabela
create_table()

# Inserir dados
data_insert()

# Gerando valores e inserindo na tabela
for i in range(10):
  data_insert_var()
  time.sleep(1)

# Select nos dados
print("-> Todos os dados:")
leitura_todos_dados()

# Leitura de registros específicos
print("-> Registros específicos:")
leitura_registros()

# Leitura de colunas específicas
print("-> Colunas específicas:")
leitura_colunas()

# Atualiza dados
print("-> Atualiza dados")
atualiza_dados()
leitura_todos_dados()

# Remove dados
print("-> Remove dados")
remove_dados()
leitura_todos_dados()

# Gerando gráficos
dados_grafico()

# Encerrando a conexão
c.close()
conn.close()