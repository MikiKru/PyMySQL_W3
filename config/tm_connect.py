import pymysql

def connection(user = "tm_user", passwd= "qwe123"):
    global conn     # zakres widoczności obiektu conn dotyczy całego skryptu
    conn = pymysql.connect("localhost", user, passwd, "tm_db")
    if(conn):
        print("...połączono z bazą danych...")
    else:
        print("błąd połączenia")
    return conn

def closeConnection():
    conn.close()
    print("...połączenie zakmniete...")

connection()
closeConnection()