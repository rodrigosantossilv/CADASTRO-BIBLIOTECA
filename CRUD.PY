
livros = []

while True:
    print("\n--- BIBLIOTECA ---")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = input("Escolha uma opçao: ")

    if opcao == "1":
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")

        livro = {
            "codigo": len(livros) + 1,
            "titulo": titulo,
            "autor": autor,
            "status": "Disponível"
        }

        livros.append(livro)
        print("Livro cadastrado com sucesso")

    elif opcao == "2":
        if not livros:
            print("Ainda não há livros cadastrados.")
        else:
            print("\n--- LIVROS CADASTRADOS ---")

            for livro in livros:
                print(f"\nCódigo: {livro['codigo']}")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Status: {livro['status']}")

    elif opcao == "3":
        print("Programa encerrado. Até mais!")
        break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")
