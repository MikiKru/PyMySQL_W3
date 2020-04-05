# cli - command line interface aplikacji
# gui - graphical user interface
from controller.tm_controller import TaskManagerController

class CLI:
    def __init__(self):
        tmc = TaskManagerController()
        while(True):
            print("Witaj w aplikacji TASK MANAGER")
            decision = input("(L) - logowanie \n(R) - rejestracja \n(Q) - wyjście").upper()
            if(decision == "L"):
                pass
            elif(decision == "R"):
                print("Jeszcze nie jest aktywna rejestrcja")
            else:
                print("Wyjście")
                break               # gdy program napotka break wychodzi z aktualnie wykonywanej pętli

cli = CLI()   # utworznie obiektu klasy CLI