#This libraries bring me the control of cadency in code with Time, and a randomized number to the central mecanichy in the game 
import random
import time 
import json 

#nessa func eu mostro o ranking dos vencedores
def show_ranking():
    try:
        with open("players.json", "r") as arquivo:
            players = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum ranking encontrado.")
        return
    
    # difficulty to score
    difficulty_scores = {
        "EasyBooooy": 1,
        "Médiunidade Aflorada": 2,
        "Mãe Diná?": 3
    }
    
    # Sort players: first by attempts ascending, then by difficulty score descending
    players.sort(key=lambda p: (p['attempts'], -difficulty_scores.get(p['difficulty'], 0)))
    
    print("------------------------------ \n RANKING \n------------------------------")
    for i, player in enumerate(players, 1):
        print(f"{i}.  {player['username']} \n Tentativas: {player['attempts']} \n  Dificuldade: {player['difficulty']}")

    print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
    try:
        ret_menu = int(input("APERTE ENTER PARA VOLTAR AO MENU\n"))
    except:
        init_menu()
    if ret_menu == 0:
        init_menu()
    else:
        init_menu()

#this func. save the winner on mini db (json) for the players ranking feature
def save_player(user, attempts_on, difficulty1):
    try:
        with open("players.json", "r") as arquivo:
            players = json.load(arquivo)
    except:
       players = []

    new_player = {
        "username": user,
        "attempts": attempts_on,
        "difficulty": difficulty1
    }

    # add new player
    players.append(new_player)

    with open("players.json", "w") as arquivo:
        json.dump(players, arquivo, indent=4)

def init_menu():
    print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
    print(f"Seja bem vindo {user}!")
    print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
    try:
        action = int(input("1 - Ver Ranking \n2 - Jogar \n3 - Sair \n ------------------------------ \n"))
    except:
        print("Digite um numero válido")
    if action == 1:
        print("CARREGANDO...")
        time.sleep(2)
        show_ranking()
    elif action == 2:
        print("CARREGANDO...")
        time.sleep(2)
        dificulty_change()
    elif action == 3:
        print("CARREGANDO...")
        time.sleep(2)
        print("Obrigado, encerrando jogo...")

#difficulty change here
def dificulty_change():
    print("AS DIFICULDADES SÃO: \n 1 - FACIL (0 a 100) \n 2 - MEDIUM (0 a 300) \n 3 - MÃE DINÁ (0 a 1000)")
    while True:
        try:
            change = int(input("Qual Dificuldade você deseja jogar? 1 / 2 / 3: \n"))
        except:
             print("Você NÃO é o Steve Jobs e NÃO vai quebrar o código, digite um NÚMERO")
             continue 
        if change == 1:
            difficulty1 = "EasyBooooy"
            print("CARREGANDO...")
            time.sleep(2)
            easy_mode(difficulty1)
            break
        elif change == 2:
            difficulty1 = "Médiunidade Aflorada"
            print("CARREGANDO...")
            time.sleep(2)
            medium_mode(difficulty1)
            break
        elif change == 3:
            difficulty1 = "Mãe Diná?"
            print("CARREGANDO...")
            time.sleep(2)
            hard_mode(difficulty1)
            break
        else:
            print("Leia com ATENCAO e escolha uma dificuldade para jogar!")
            continue

#this function is responsable to start the game 
def play_game(secret_number, attempts_chance, difficulty1):
    print("------------------------------ \n ADIVINHATOR2000 ESTÁ PENSANDO EM UM NÚMERO \n------------------------------")
    time.sleep(1.5)
    attempts_on = 0
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
            if attempts_on == 1:
                easter_egg1()
            try:
                option = input("Deseja tentar novamente? (S \ N):  ").upper()
            except:
                 print("Não entendi.")
                 continue
            if option == "S":
                print("CARREGANDO...")
                time.sleep(2)
                print("Selecione a dificuldade do próximo jogo.")
                save_player(user, attempts_on, difficulty1)
                dificulty_change()
            else:
                save_player(user, attempts_on, difficulty1)
                print("Encerrando jogo...")
                exit()
        print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")        
        print(f"Restam {attempts_chance - attempts_on} tentativas!! \n------------------------------")
    print("YOU LOST, jovem pirata... TENTE NOVAMENTE!!")
    save_player(user, attempts_on, difficulty1)
    dificulty_change()

#game in easy mode
def easy_mode(difficulty1):
    secret_number = random.randint(0, 100)
    attempts_chance = 15
    play_game(secret_number, attempts_chance, difficulty1)

#game in medium mode
def medium_mode(difficulty1):
    secret_number = random.randint(0, 300)
    attempts_chance = 10
    play_game(secret_number, attempts_chance, difficulty1)

#game in HAAAARDDDD MODE, ITS IMPOSSIBLE TO TAKE THE RIGTH NUMBER HERE... i thinking...
def hard_mode(difficulty1):
    attempts_on = 0
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
                attempts_on += 1
        elif attempt < secret_number:
                print("Errou!! é MAIS")
                attempts_on += 1
        elif attempt == secret_number:
                attempts_on += 1
                print("...")
                print("Ok, isso foi...")
                print("muito supeito!!")
                print("Mas parabens, você é O NOVO CAMPEÃO DO ADIVINHATOR2000!!!")
                option = input("Deseja tentar novamente? (S \ N):  ").upper()
                if option == "S":
                    save_player(user, attempts_on, difficulty1)
                    dificulty_change()
                else:
                    print("Encerrando jogo...")
                    save_player(user, attempts_on, difficulty1)
                    exit()
        print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")        
        print(f"Restam {attempts_chance - attempts_on} tentativas!! \n------------------------------")
    print("Como esperado, você não advinhou :( \n Mas relaxa, é você, uma máquina e 1000 números, você não achou mesmo que fosse vencer né?")
    final_lose = input("Deseja tentar novamente?  (S) / (N):  ").upper()
    if final_lose == "S" or final_lose == "SIM":
         dificulty_change()
    else:
         print("Encerrando Jogo...")
         exit()

#legend mode easter egg
def easter_egg1():
        print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
        print("WOW!! De primeira!")
        print("VOCÊ DESBLOQUEOU O MODO LENDA!")
        print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
        legend_mode_option()

#option to start legend mode or not
def legend_mode_option():
    try:
        decision = int(input(f"Olá {user}, você liberou o modo LENDA. Você deseja:\n(1)- TENTAR   ou  (2)- FUNGIR? \n"))
    except:
        print("Digite um número válido")
    if decision == 1:
        print("CARREGANDO...")
        time.sleep(2)
        legend_mode_play(30)
    elif decision == 2:
        print("Boa escolha...")
        exit()

#legend mode play 
def legend_mode_play(tempo):
    secret_number = random.randint(0, 300)
    inicio = time.time()
    attempts_on = 0
    while True:
        time_pass = time.time() - inicio
        if time_pass >= tempo:
            print("Como imaginado... NÃO DEU!\nACERTE DE PRIMEIRA OUTRA VEZ PARA VOLTAR AO MODO LENDA NOVAMENTE.")
            break
        try:
            attempt = int(input("Digite seu palpite: "))
        except:
            print("Digite um número válido!")
            continue

        attempts_on += 1

        if attempt > secret_number:
            print("Errou!! é MENOS")
        elif attempt < secret_number:
            print("Errou!! é MAIS")
        elif attempt == secret_number:
            print("\n💀 LENDÁRIO!!! VOCÊ ACERTOU!!!")
            print(f"Tentativas: {attempts_on}")
            
            save_player(user, attempts_on, "MODO LENDA")
            return
        time_remaining = tempo - time_pass
        print(f"Tempo restante: {int(time_remaining)} segundos.")

#username input here 
print("------------------------------ \n ADIVINHATOR2000 \n------------------------------")
user = input("Olá jogador! Como devo te chamar?: \n")

#tis function starts initial menu
init_menu()

