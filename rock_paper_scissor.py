import random

# Definir opciones y mensajes
LANGUAGES = {
    "español": {
        "options": ["piedra", "papel", "tijeras"],
        "messages": {
            "choose": "Elige Piedra, Papel o Tijeras, o Q para salir: ",
            "invalid": "Palabra inválida. Por favor, intenta de nuevo.",
            "computer_pick": "La computadora eligió",
            "win": "¡Ganaste!",
            "lose": "¡Perdiste!",
            "tie": "Es un empate.",
            "user_wins": "Ganaste",
            "computer_wins": "La computadora ganó",
            "goodbye": "¡Adiós!",
            "times": "veces",
        },
    },
    "english": {
        "options": ["rock", "paper", "scissors"],
        "messages": {
            "choose": "Choose Rock, Paper, or Scissors, or Q to quit: ",
            "invalid": "Invalid word. Please try again.",
            "computer_pick": "Computer picked",
            "win": "You won!",
            "lose": "You lost!",
            "tie": "It's a tie.",
            "user_wins": "You won",
            "computer_wins": "Computer won",
            "goodbye": "Goodbye!",
            "times": "times",
        },
    },
}

# ASCII Art para piedra, papel y tijeras
ASCII_ART = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """,
    "piedra": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "papel": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "tijeras": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

# Preguntar al usuario si quiere jugar en inglés o en español
while True:
    language = input("¿Quieres jugar en inglés o en español? (inglés/español): ").lower()
    if language in ["español", "espanol"]:
        language = "español"
        break
    elif language in ["inglés", "ingles", "english"]:
        language = "english"
        break
    else:
        print("Opción no válida. Por favor, elige 'inglés' o 'español'.")

# Configurar opciones y mensajes según el idioma
options = LANGUAGES[language]["options"]
messages = LANGUAGES[language]["messages"]

# Inicializar contadores de victorias
user_wins = 0
computer_wins = 0

# Lógica del juego
while True:
    user_input = input(messages["choose"]).lower()
    if user_input == 'q':
        break
    if user_input not in options:
        print(messages["invalid"])
        continue

    random_num = random.randint(0, 2)
    computer_pick = options[random_num]

    # Mostrar elección del usuario en ASCII
    print(f"\nTú elegiste: {user_input.capitalize()}")
    print(ASCII_ART[user_input])

    # Mostrar elección de la computadora en ASCII
    print(f"{messages['computer_pick']} {computer_pick.capitalize()}:")
    print(ASCII_ART[computer_pick])

    # Determinar el resultado
    if user_input == computer_pick:
        print(messages["tie"])  # Empate
    elif (
        (user_input == "rock" and computer_pick == "scissors") or
        (user_input == "paper" and computer_pick == "rock") or
        (user_input == "scissors" and computer_pick == "paper") or
        (user_input == "piedra" and computer_pick == "tijeras") or
        (user_input == "papel" and computer_pick == "piedra") or
        (user_input == "tijeras" and computer_pick == "papel")
    ):
        print(messages["win"])
        user_wins += 1
    else:
        print(messages["lose"])
        computer_wins += 1

# Mostrar resultados finales
print(f"{messages['user_wins']} {user_wins} {messages['times']}.")
print(f"{messages['computer_wins']} {computer_wins} {messages['times']}.")
print(messages["goodbye"])
