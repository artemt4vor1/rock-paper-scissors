import random
import json

class ScoreBoard:
    def __init__(self, filename="scoreboard.json"):
        self.filename = filename
        self.user_wins = 0
        self.computer_wins = 0
        self.draws = 0
        self._load()

    def _load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.user_wins = data.get("user_wins", 0)
                self.computer_wins = data.get("computer_wins", 0)
                self.draws = data.get("draws", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            # Если файла нет или он битый — начинаем с нуля
            self.user_wins = 0
            self.computer_wins = 0
            self.draws = 0

    def update(self, result):
        if result == "user":
            self.user_wins += 1
        elif result == "computer":
            self.computer_wins += 1
        else:
            self.draws += 1

    def show(self):
        print("\n--- Текущий счёт ---")
        print(f"Вы: {self.user_wins}")
        print(f"Компьютер: {self.computer_wins}")
        print(f"Ничьи: {self.draws}")
        print("--------------------\n")

    def save(self):
        data = {
            "user_wins": self.user_wins,
            "computer_wins": self.computer_wins,
            "draws": self.draws
        }
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice():
    while True:
        choice = input("Ваш ход (rock/paper/scissors) или 'quit' для выхода: ").strip().lower()
        if choice in ["rock", "paper", "scissors", "quit"]:
            return choice
        print("Неверный ввод. Попробуйте снова.")


def determine_winner(user, computer):
    if user == computer:
        return "draw"
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "user"
    return "computer"


def main():
    print("Игра Камень-Ножницы-Бумага")
    scoreboard = ScoreBoard()
    scoreboard.show()

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            print("До свидания!")
            scoreboard.save()
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

        scoreboard.update(result)
        scoreboard.show()


if __name__ == "__main__":
    main()
