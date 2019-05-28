def getConversa():
    conversa = []

    cumprimento = open('Assuntos/Cumprimento.txt', 'r')
    despedida = open('Assuntos/Despedida.txt', 'r')
    esporte = open('Assuntos/Esporte.txt', 'r')
    comida = open('Assuntos/Comida.txt', 'r')
    livro = open('Assuntos/Livro.txt', 'r')
    filme = open('Assuntos/Filme.txt', 'r')
    jogo = open('Assuntos/Jogo.txt', 'r')

    conversa += cumprimento.readlines()
    conversa += despedida.readlines()
    conversa += esporte.readlines()
    conversa += comida.readlines()
    conversa += livro.readlines()
    conversa += filme.readlines()
    conversa += jogo.readlines()

    return conversa
