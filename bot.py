import random
import pyjokes
import emoji
from prettytable import PrettyTable
from colorama import init, Fore
import time

# Ініціалізація Colorama
init(autoreset=True)

# Меню бота
def show_menu():
    print(Fore.CYAN + "\n--- Головне меню ---")
    print("1. Рекомендувати фільм")
    print("2. Рекомендувати музику")
    print("3. Розповісти анекдот")
    print("4. Розказати цікаву історію")
    print("5. Пограти в гру (Камінь-ножиці-папір)")
    print("6. Вийти")

def recommend_movie():
    movies = ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Pulp Fiction']
    print(Fore.YELLOW + f"Ми рекомендуємо вам переглянути: {random.choice(movies)}")

def recommend_music():
    music = ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-hop']
    print(Fore.YELLOW + f"Ми рекомендуємо вам прослухати жанр: {random.choice(music)}")

def tell_joke():
    print(Fore.GREEN + pyjokes.get_joke())

def tell_story():
    stories = [
        "Історія про успіх Ілона Маска...",
        "Історія створення Google...",
        "Як Netflix став гігантом..."
    ]
    print(Fore.BLUE + f"Цікава історія: {random.choice(stories)}")

def play_game():
    choices = ['Камінь', 'Ножиці', 'Папір']
    while True:
        user_choice = input("Виберіть: Камінь, Ножиці або Папір (або вийти для завершення): ").capitalize()
        if user_choice == "Вийти":
            break
        if user_choice not in choices:
            print(Fore.RED + "Невірний вибір, спробуйте ще раз.")
            continue

        computer_choice = random.choice(choices)
        print(f"Ви вибрали: {user_choice}, Комп'ютер вибрав: {computer_choice}")

        if user_choice == computer_choice:
            print(Fore.CYAN + "Нічия!")
        elif (user_choice == 'Камінь' and computer_choice == 'Ножиці') or \
             (user_choice == 'Ножиці' and computer_choice == 'Папір') or \
             (user_choice == 'Папір' and computer_choice == 'Камінь'):
            print(Fore.GREEN + "Ви виграли!")
        else:
            print(Fore.RED + "Ви програли!")
while True:
    show_menu()
    choice = input("Оберіть опцію (1-6): ")

    if choice == '1':
        recommend_movie()
    elif choice == '2':
        recommend_music()
    elif choice == '3':
        tell_joke()
    elif choice == '4':
        tell_story()
    elif choice == '5':
        play_game()
    elif choice == '6':
        print(emoji.emojize("Дякую за використання бота! :waving_hand:", language="alias"))
        break
    else:
        print(Fore.RED + "Невірний вибір, спробуйте ще раз.")
