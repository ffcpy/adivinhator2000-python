#This libraries bring me the control of cadency in code with Time, and a randomized number to the central mecanichy in the game 
import random
import time 
import json 
#tis function starts initial menu
def init_menu():
    print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
    print(f"Seja bem vindo {user}, a seguir, selecione a dificuldade do jogo.")
    time.sleep(1)
    print("CARREGANDO...")
    time.sleep(2)
    dificulty_change()
#difficulty change here
def dificulty_change():
    print("AS DIFICULDADES SÃO: \n 1 - FACIL (0 a 100) \n 2 - MEDIUM (0 a 300) \n 3 - MÃE DINÁ (0 a 1000)")
    while True:
        try:
            change = int(input("Qual Dificuldade você deseja jogar? 1 / 2 / 3: \n"))
        except:
             print("Não quebra o código, digite um NÚMERO")
             continue 
        if change == 1:
            print("CARREGANDO...")
            time.sleep(2)
            easy_mode()
            break
        elif change == 2:
            print("CARREGANDO...")
            time.sleep(2)
            medium_mode()
            break
        elif change == 3:
            print("CARREGANDO...")
            time.sleep(2)
            hard_mode()
            break 
        else:
            print("Leia com ATENCAO e escolha uma dificuldade para jogar!")
            continue
#this function is responsable to start the game 
def play_game(secret_number, attempts_chance):
    print("------------------------------ \n ADIVINHATOR2000 ESTÁ PENSANDO EM UM NÚMERO \n------------------------------")
    time.sleep(1.5)
    attempts_on = 0
    attempts_off = attempts_chance - attempts_on
    for i in range(attempts_chance):
        #try disable the crash for jokes on the inputs 
        try:
            attempt = int(input("Digite seu palpite:  "))
        except:
             print("Digite um NÚMERO válido.")
             #continue return to the loop 
             continue
        if attempt > secret_number:
            print("VERIFICANDO...")
            time.sleep(1.5)
            print("Errou!! é MENOS \n")
            attempts_on += 1
        elif attempt < secret_number:
            print("VERIFICANDO...")
            time.sleep(1.5)
            print("Errou!! é MAIS \n")
            attempts_on += 1
        elif attempt == secret_number:
            print("VERIFICANDO...")
            time.sleep(1.5)
            print("Acertou!!...")
            attempts_on += 1
            try:
                option = input("Deseja tentar novamente? (S \ N):  ").upper()
            except:
                 print("Não entendi.")
                 continue
            if option == "S":
                print("CARREGANDO...")
                time.sleep(2)
                print("Selecione a dificuldade do próximo jogo.")
                dificulty_change()
            else:
                print("Encerrando jogo...")
                exit()
        print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")        
        print(f"Restam {attempts_off} tentativas!! \n------------------------------")
    print("YOU LOST, jovem pirata... TENTE NOVAMENTE!!")
    dificulty_change()
#game in easy mode
def easy_mode():
    secret_number = random.randint(0, 100)
    attempts_chance = 15
    play_game(secret_number, attempts_chance)
#game in medium mode
def medium_mode():
    secret_number = random.randint(0, 300)
    attempts_chance = 10
    play_game(secret_number, attempts_chance)
#game in HAAAARDDDD MODE, ITS IMPOSSIBLE TO TAKE THE RIGTH NUMBER HERE... i thinking...
def hard_mode():
    secret_number = random.randint(0, 1000)
    attempts_chance = 10
    input(f"{user} você sabe que é impossivel acertar isso né? quer MESMO continuar?:  " )
    print("OK, Tem certeza?")
    time.sleep(1.5)
    print("Tarde demais, vamos comecar!")
    time.sleep(1.5)
    print("Prepare-se...")
    time.sleep(1.5)
    for i in range(attempts_chance):
        try:
            attempt = int(input("Digite seu palpite:  "))
        except:
             print("Não quebra o código, digite um NÚMERO!")
             continue
        if attempt > secret_number:
                print("Errou!! é MENOS")
        elif attempt < secret_number:
                print("Errou!! é MAIS")
        elif attempt == secret_number:
                print("...")
                print("Ok, isso foi...")
                print("muito supeito!!")
                print("Mas parabens, você é O NOVO CAMPEÃO DO ADIVINHATOR2000!!!")
                option = input("Deseja tentar novamente? (S \ N):  ").upper()
                if option == "S":
                    dificulty_change()
                else:
                    print("Encerrando jogo...")
                    exit()
    print("Como esperado, você não advinhou :( \n Mas relaxa, é você, uma máquina e 1000 números, você não achou mesmo que fosse vencer né?")
    final_lose = input("Deseja tentar novamente?  (S) / (N):  ").upper()
    if final_lose == "S" or final_lose == "SIM":
         dificulty_change()
    else:
         print("Encerrando Jogo...")
         exit()
#username input here 
print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
user = input("Olá jogador! Como devo te chamar?: \n")

init_menu()
