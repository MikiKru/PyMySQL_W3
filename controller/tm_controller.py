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
    def insertTaskByUser(self, task_name, task_description, task_category, user_id):
        self.c.execute("insert into task values(default, %s, %s, %s, %s)",
                       (task_name, task_description, task_category, user_id))
        # ?
        decision = input("potwierdź dodanie taska (T/N)").upper()
        if(decision == 'T'):
            self.conn.commit()      # zatwierdź i wprowadź do bazy danych
            print("dodano nowego taska: " + task_name)
            self.selectTasks()      # wywołanie metody selectTasks() w metodzie insertTaskByUser()
        else:
            self.conn.rollback()    # odrzuć dane i nie wprowadzaj do bazy danych
            print("nic nie dodano")
        # ?
    def selectTasks(self):
        self.c.execute("SELECT * FROM task")
        tasks = self.c.fetchall()
        for task in tasks:    # iteruje po rekordach
            # %s -> w to miejsce wprowadzam string
            # %15s -> w to miejsce wprowadzam string ale rezerwuje 15 znaków na jego reprezentacje
            task_name = task[1]
            task_description = task[2]
            task_category = task[3]
            user_id = task[4]
            print("| %15s | %30s | %15s | %15s |" %
                  (task_name, task_description, task_category, self.selectUserById(user_id)))
    def selectUserById(self, user_id):
        self.c.execute("SELECT name, lastname FROM user WHERE user_id = %s", str(user_id))
        selectedUser = self.c.fetchone()
        return selectedUser[0] + " " + selectedUser[1]
    def deleteTaskById(self, task_id):
        self.c.execute("DELETE FROM task WHERE task_id = %s", str(task_id))
        self.conn.commit()
        self.selectTasks()

tmc = TaskManagerController()
# tmc.login('mk@mk.pl', 'mk')         # ok
# tmc.insertTaskByUser("test111","test111","Python",1)
tmc.deleteTaskById(16)

