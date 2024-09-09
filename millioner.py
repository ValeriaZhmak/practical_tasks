import random

# Створюємо список словників питань і відповідей 
questions = [
    {
        "question": "Столиця України?",
        "answers": ["A: Київ", "B: Львів", "C: Харків", "D: Одеса"],
        "correct": "A"
    },
    {
        "question": "Найдовша річка в світі?",
        "answers": ["A: Ніл", "B: Амазонка", "C: Міссісіпі", "D: Янцзи"],
        "correct": "B"
    },
    {
        "question": "Який рік був оголошений роком Незалежності України?",
        "answers": ["A: 1989", "B: 1990", "C: 1991", "D: 1992"],
        "correct": "C"
    }
]

# Спсок для нагород за правильну відповідь
prizes = [1000, 5000, 10000]

# Використані підказки
hints_used = {"5050": False, "call_friend": False, "crowd_help": False}

# Функція для виведення питання і варіантів відповідей
def ask_question(player_name, question_data, prize_amount):
    print(f"На кону: {prize_amount} грн")
    print(f"{player_name}, ось ваше питання:")
    print(question_data["question"])
    for ans in question_data["answers"]:
        print(ans)
    print("Підказки: 1 - 50/50, 2 - Дзвінок другу, 3 - Допомога залу")
    answer = input("Ваша відповідь (A, B, C, D або 1, 2, 3 для підказок): ").upper()  # Переводимо в верхній регістр
    return answer

# Підказки
def use_hint_5050(question_data):
    correct_answer = question_data["correct"]
    wrong_answers = [ans for ans in ["A", "B", "C", "D"] if ans != correct_answer]
    removed_answers = random.sample(wrong_answers, 2)
    print("Залишились варіанти:")
    for ans in question_data["answers"]:
        if ans[0] not in removed_answers:
            print(ans)

def use_hint_audience():
    print("Зал голосує...")
    percentages = random.choices(range(10, 50), k=4)
    percentages[random.randint(0, 3)] += 50  # Гарантований високий відсоток для однієї відповіді
    for i, option in enumerate(["A", "B", "C", "D"]):
        print(f"{option}: {percentages[i]}%")

def use_hint_friend(question_data):
    print("Ваш друг вважає, що відповідь:", question_data["answers"][random.randint(0, 3)])

# Цикл гри
def play_game(player_name):
    prize_total = 0
    game_continue = True

    question_index = 0
    while game_continue and question_index < len(questions):
        question_data = random.choice(questions)  # Вибір випадкового питання
        prize = prizes[question_index]

        while True:
            answer = ask_question(player_name, question_data, prize)

            if answer == "1" and not hints_used["5050"]:
                use_hint_5050(question_data)
                hints_used["5050"] = True
            elif answer == "2" and not hints_used["call_friend"]:
                use_hint_friend(question_data)
                hints_used["call_friend"] = True
            elif answer == "3" and not hints_used["crowd_help"]:
                use_hint_audience()
                hints_used["crowd_help"] = True
            elif answer in ["A", "B", "C", "D"]:
                if answer == question_data["correct"]:
                    print("Правильно!")
                    prize_total += prize
                    break
                else:
                    print(f"Неправильно, {player_name}. Правильна відповідь: {question_data['correct']}")
                    print(f"Ви виграли: {prize_total} грн")
                    game_continue = False
                    break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

        question_index += 1

    if game_continue:
        print(f"Вітаємо, {player_name}! Ви виграли {prize_total} грн")

# Запуск гри з привітанням
print("Вітаємо в грі 'Хто хоче стати мільйонером?'")
player_name = input("Як вас звати? ")

while True:
    play_game(player_name)
    restart = input(f"{player_name}, бажаєте зіграти ще раз? (так/ні): ").lower()
    if restart != "так":
        print(f"Дякуємо за гру, {player_name}!")
        break
