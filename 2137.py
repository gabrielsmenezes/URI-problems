while True:
  try:
    livros = list()
    numero_de_livros = int(input())
    while numero_de_livros > 0:
        livros.append(input())
        numero_de_livros = numero_de_livros - 1
    livros.sort()
    for livro in livros:
        print(livro)
  except EOFError:
    break