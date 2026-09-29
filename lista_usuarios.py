import sqlite3 as sqlite

<<<<<<< HEAD
#abre a conexão com o banco
conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row

#cria um cursor (objeto para interagir com o banco)
cursor = conn.cursor()

#executa o sql
cursor.execute("SELECT * FROM usuarios")

#pega os registros e guarda na variável resultados
resultados = cursor.fetchall()

#percorre os registros que retornaram
for linha in resultados:
    print(f"id: {linha['id']} | nome: {linha['nome']}")
    #print(f"id: {linha[0]} | nome: {linha[1]}")

#fecha a conexão
conn.close()
=======
conn = sqlite.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

for linha in resultados:
    print(f"id: {linha[0]} | nome: {linha[1]}")

conn.close()

>>>>>>> 2feeb8e3e6a365a6837f242ddcd2ca3f91731740
