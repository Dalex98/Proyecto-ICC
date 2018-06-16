from screen import *
from candidatos
from mesas2
from simulacion
from escrutinio import *
from estadisticas import *

## Menu de opciones ##
def menu():
    op = '0'
    while int(op) > 5 or int(op) < 1:
        clearScreen()
        print()    
        print(Cursor.FORWARD(17) +  "-------------------------------")
        print(Cursor.FORWARD(17) +  "| ELECCIONES MUNICIPALES 2018 |")
        print(Cursor.FORWARD(17) +  "-------------------------------")
        print(Fore.GREEN)
        print(Cursor.FORWARD(17) + "1) Registrar candidatos")
        print(Cursor.FORWARD(17) + "2) Registrar mesas de sufragio")
        print(Cursor.FORWARD(17) + "3) Empieza la votación")
        print(Cursor.FORWARD(17) + "4) Escrutinio  de votos")
        print(Cursor.FORWARD(17) + "5) Estadísticas")
        print(Cursor.FORWARD(17) + Fore.YELLOW + "Eliga una opcion ( )" + Back.RESET)
        op = input(Cursor.UP(1) + Cursor.FORWARD(35))   
    print(Style.RESET_ALL)
    return op

## Funcion principal que llamara cada requerimiento ##
def main():
    #cargarPrograma()
    #otro comentario
    op = menu()
    if op == '1':
        print("LLamar funcion principal que registra candidatos")
    elif op == '2':
        print("LLamar funcion principal que registra mesas de sufragio") 
    elif op == '3':
        print("LLamar funcion principal que inicia simulación")   
    elif op == '4':
        print("LLamar funcion principal que realiza el escrutinio de votos")    
    elif op == '5':
        print("LLamar funcion principal que muestra estadisticas de votación")      
        
main()
