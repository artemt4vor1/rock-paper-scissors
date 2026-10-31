import random

def get_computer_choice():
    """Компьютер выбирает случайным образом."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Получаем выбор пользователя с проверкой."""
    while True:
        choice = input("Ваш ход (rock/paper/scissors) или 'quit' для выхода: ").strip().lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        print("Неверный ввод. Попробуйте снова.")

def determine_winner(user, computer):
    """Определяет победителя."""
    if user == computer:
        return "draw"
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "user"
    return "computer"

def main():
    print("Игра Камень-Ножницы-Бумага")
    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            print("До свидания!")
            break
        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        if result == "draw":
            print("Ничья!")
        elif result == "user":
            print("Вы победили!")
        else:
            print("Компьютер победил!")

if __name__ == "__main__":
    main()
