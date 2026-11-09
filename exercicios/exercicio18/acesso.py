import sqlite3

with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()
        cur.execute("SELECT * FROM amigos")
        # lista = cur.fetchall()
        # print(lista)

        for amigo in cur:
            print(f"{amigo['nome']} nasceu em {amigo['nascimento']}")


cur.close()
banco.close()