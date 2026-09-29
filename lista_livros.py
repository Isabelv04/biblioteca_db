import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")

resultados = cursor.fetchall()

for linha in resultados:
    print(f"id: {linha[0]} | titulo: {linha[1]} | autor: {linha[2]} | editora: {linha[3]} | ano_publicacao: {linha[4]} | \
edicao: {linha[5]} | disponivel: {linha[6]}")

conn.close()
##

