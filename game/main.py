import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera =>')
    user_option = user_option.lower()
    
    if user_option not in options:
        print('esa opción no es válida')
        return None, None
    
    computer_option = random.choice(options)
    
    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano')
            user_wins += 1
        else: 
            print('papel gana a piedra')
            print('computer gano')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else: 
            print('tijera gana a papel')
            print('computer gano')
            computer_wins += 1 
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano')
            user_wins += 1
        else: 
            print('piedra gana a tijera')
            print('computer gano')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('--------' * 20)
        print('ROUND', rounds)
        print('--------' * 20)
        
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1
        
        user_option, computer_option = choose_options()
        if user_option is None or computer_option is None:
            continue
        
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if computer_wins == 3:
            print('el ganador es la computadora')
            break
        if user_wins == 3:
            print('el ganador es el usuario')
            break
    
run_game()