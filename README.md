# 🎯 Number Guessing Game (Python)

A simple command-line Number Guessing Game built using Python. The player selects a difficulty level and tries to guess a randomly generated number in the fewest attempts possible.

---

## 📌 Features

* Multiple difficulty levels:

  * Easy (1–10)
  * Medium (1–50)
  * Difficult (1–100)
* Tracks number of attempts per round
* Maintains a **best score** during the session
* User-friendly prompts and feedback
* Replay option after each game

---

## 🎮 How to Play

1. Choose a difficulty level (1, 2, or 3).
2. Enter your guesses based on the selected range.
3. The program will guide you:

   * "HIGHER NUMBER PLEASE" if your guess is too low
   * "LOWER NUMBER PLEASE" if your guess is too high
4. Keep guessing until you find the correct number.
5. Try to beat your **best score** (least number of attempts).

---

## 🧠 Game Logic

* The computer randomly selects a number within the chosen range.
* Each guess increases the attempt counter.
* The game ends when the correct number is guessed.
* The best score is updated if the current attempt count is lower.

---

## 🔁 Replay Option

After each round, you can choose to:

* Press `y` to play again
* Press any other key to exit the game

---

## 💡 Future Improvements

* Add input validation to handle non-integer inputs
* Store best score across sessions (using file handling)
* Add a graphical interface (GUI)
* Add timer-based scoring system

---

## 📜 License

This project is open-source and free to use.

---

Enjoy the game and happy coding! 🎉
