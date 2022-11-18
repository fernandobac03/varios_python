import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = 'localhost',
        port=3306,
        user = 'root',
        passwd = 'root',
        database = 'master_python'
    )

    #print(database)
    #buffered=True, me permite hacer varias consultas con el mismo cursor
    cursor = database.cursor(buffered=True)
    return [database, cursor]