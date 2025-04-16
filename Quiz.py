Perguntas = ("Quanto é 2+2?",
             "Qual o nome do cachorro em vidas secas?",
             "Qual o nome do autor de Dom Casmurro?", 
             "Como Virginia wolf morreu?",
             "Qual o nome da vilã de senhora do meu destino?",
             "Qual o nome do autor de e nao sobrou nenhum?",)

Alternativas = (("a) 3", "b) 4", "c) 5", "d) 6"),
                ("a) Capitu", "b) Bentinho", "c) Escobar", "d) Baleia"),
                ("a) Machado de Assis", "b) Clarice Lispector", "c) Jorge Amado", "d) Guimarães Rosa"),
                ("a) Enforcada", "b) Afogada", "c) Queimada", "d) Cortada"),
                ("a) Maria do Carmo", "b) Nazare", "c) Maria de Fátima", "d) Maria da Luz"),
                ("a) Agatha Christie", "b) Stephen King", "c) J.K. Rowling", "d) Arthur Conan Doyle"))

Respostas_Corretas = ("b", "d", "a", "b", "b", "a")

print("Bem-vindo ao Quiz!")
print("Responda as perguntas a seguir:")

score =0

for i in range(len(Perguntas)):
    print(f"\nPergunta {i+1}:")
    print(Perguntas[i])
    print("Alternativas:")
    for alternativa in Alternativas[i]:
        print(alternativa)

    while True:  # Loop until the user provides a valid input
        guess = input("Sua resposta: ").strip().lower()

        # Check if the guess is valid
        if guess not in ("a", "b", "c", "d"):
            print("Opção inválida! Tente novamente.")
            continue  # Go back to the same question if invalid input
        else:
            # Check if the guess is correct
            if guess == Respostas_Corretas[i]:
                print("Resposta correta!")
                score += 1
            else:
                print(f"Resposta errada! A resposta correta é: {Respostas_Corretas[i]}")
            break  # Exit the loop after a valid answer
print(f"\n Você acertou:{score} de {len(Perguntas)} perguntas.") 
print("\nFim do quiz! Obrigado por participar.")



