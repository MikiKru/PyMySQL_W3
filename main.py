# cli - command line interface aplikacji
# gui - graphical user interface
from controller.tm_controller import TaskManagerController

class CLI:
    def __init__(self):
        self.tmc = TaskManagerController()
        while(True):
            print("Witaj w aplikacji TASK MANAGER")
            decision = input("(L) - logowanie \n(R) - rejestracja \n(Q) - wyjście").upper()
            if(decision == "L"):
                if(self.tmc.login(input("podaj email:"), input("podaj password"))):
                    self.menu()
            elif(decision == "R"):
                print("Jeszcze nie jest aktywna rejestrcja")
            else:
                print("Wyjście")
                break               # gdy program napotka break wychodzi z aktualnie wykonywanej pętli
    def menu(self):
        while(True):
            decision = input("(1) - dodaj zadanie \n(2) - wypisz zadania "
                             "\n(3) - usuń zadanie \n(4) - zmień hasło \n(Q) - cofnij").upper()
            if(decision == "1"):
                pass
            elif(decision == "2"):
                pass
            elif (decision == "3"):
                pass
            elif (decision == "4"):
                pass
            elif (decision == "Q"):
                break
            else:
                print("błędny wybor")


cli = CLI()   # utworznie obiektu klasy CLI