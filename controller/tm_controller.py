# klasa obsługująca żądania użytkownika aplikacji
# ALT + Enter -> auto-podpowiedź
from config.tm_connect import ConnectionConfig

'''
        result = [
        [id_0,name_0,lastname_0, email_0, password_0,registration_0, enable_0],
        [id_1,name_1,lastname_1, email_1, password_1,registration_1, enable_1],
        [id_2,name_2,lastname_2, email_2, password_2,registration_2, enable_2],
        [id_3,name_3,lastname_3, email_3, password_3,registration_3, enable_3]
        ]
'''

class TaskManagerController:
    def __init__(self):
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()
    def login(self, email, passwd):
        # wykonanie zapytania
        self.c.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, passwd))
        # pobranie wyniku zwracanego przez zapytanie (resultset)
        result = self.c.fetchone()
        if(result):
            print("zalogowano: " + result[3])
        else:
            print("niezalogowano")
    

tmc = TaskManagerController()
tmc.login('mk@mk.pl', 'mk')         # ok
tmc.login('mk@mk.pl', 'mk111')      # błąd logowania
tmc.login('mk@mk.pll', 'mk111')     # błąd logowania
