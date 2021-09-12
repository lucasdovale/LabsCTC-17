import numpy

tabuleiro = numpy.zeros((7, 7), dtype=str)

'''
    LEGENDA
    0, 1, 2, 3, 4: Quantidade de lâmpadas adjacentes
    L: lâmpada
    I: iluminado
    P: preto
    X: proibido
'''

'''
# JOGO 1: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html#7x7:dBiBb4e4aBeBb3i0d
tabuleiro[0][4] = 'P'
tabuleiro[2][0] = 'P'
tabuleiro[2][3] = '4'
tabuleiro[3][2] = '4'
tabuleiro[3][4] = 'P'
tabuleiro[4][3] = 'P'
tabuleiro[4][6] = '3'
tabuleiro[6][2] = '0'
'''

# JOGO 2: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html#7x7:d1c1aBaBa1g1c1gBa4aBa2c3d
tabuleiro[0][4] = '1'
tabuleiro[1][1] = '1'
tabuleiro[1][3] = 'P'
tabuleiro[1][5] = 'P'
tabuleiro[2][0] = '1'
tabuleiro[3][1] = '1'
tabuleiro[3][5] = '1'
tabuleiro[4][6] = 'P'
tabuleiro[5][1] = '4'
tabuleiro[5][3] = 'P'
tabuleiro[5][5] = '2'
tabuleiro[6][2] = '3'

'''
# JOGO 3: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html#7x7:dBiBb4e4aBeBb3i0d
tabuleiro[1][1] = '0'
tabuleiro[1][5] = 'P'
tabuleiro[2][3] = '4'
tabuleiro[3][2] = 'P'
tabuleiro[3][4] = '4'
tabuleiro[4][3] = 'P'
tabuleiro[5][1] = '3'
tabuleiro[5][5] = '2'
'''


def iluminar(board):
    for line in range(0, 7):
        for column in range(0, 7):
            if board[line][column] == 'L':

                j = column
                # Iluminar linha à esquerda
                while j > 0 and (board[line][j - 1] == '' or board[line][j - 1] == 'I'):
                    board[line][j - 1] = 'I'
                    j = j - 1

                j = column
                # Iluminar linha à direita
                while j < 6 and (board[line][j + 1] == '' or board[line][j + 1] == 'I'):
                    board[line][j + 1] = 'I'
                    j = j + 1

                i = line
                # Iluminar coluna acima
                while i > 0 and (board[i - 1][column] == '' or board[i - 1][column] == 'I'):
                    board[i - 1][column] = 'I'
                    i = i - 1

                i = line
                # Iluminar coluna abaixo
                while i < 6 and (board[i + 1][column] == '' or board[i + 1][column] == 'I'):
                    board[i + 1][column] = 'I'
                    i = i + 1

    return board


def vazios_e_lampadas(line, column, board):
    vazios_vizinhos = 0
    lampadas_vizinhas = 0

    if line + 1 <= 6 and board[line + 1][column] == '':
        vazios_vizinhos += 1
    if column + 1 <= 6 and board[line][column + 1] == '':
        vazios_vizinhos += 1
    if line >= 1 and board[line - 1][column] == '':
        vazios_vizinhos += 1
    if column >= 1 and board[line][column - 1] == '':
        vazios_vizinhos += 1

    if line + 1 <= 6 and board[line + 1][column] == 'L':
        lampadas_vizinhas += 1
    if column + 1 <= 6 and board[line][column + 1] == 'L':
        lampadas_vizinhas += 1
    if line >= 1 and board[line - 1][column] == 'L':
        lampadas_vizinhas += 1
    if column >= 1 and board[line][column - 1] == 'L':
        lampadas_vizinhas += 1

    return vazios_vizinhos, lampadas_vizinhas


def preenchimento_adjacencias(number, board):
    mudou = False
    for linha in range(0, 7):
        for coluna in range(0, 7):
            [v, l] = vazios_e_lampadas(linha, coluna, board)
            if board[linha][coluna] == number and v == int(tabuleiro[linha][coluna]) - l:
                if linha + 1 < 7 and tabuleiro[linha + 1][coluna] == '':
                    board[linha + 1][coluna] = 'L'
                    mudou = True
                if coluna + 1 < 7 and tabuleiro[linha][coluna + 1] == '':
                    board[linha][coluna + 1] = 'L'
                    mudou = True
                if linha - 1 >= 0 and tabuleiro[linha - 1][coluna] == '':
                    board[linha - 1][coluna] = 'L'
                    mudou = True
                if coluna - 1 >= 0 and tabuleiro[linha][coluna - 1] == '':
                    board[linha][coluna - 1] = 'L'
                    mudou = True
                board = iluminar(board)
    return board, mudou


def finalizacao_preenchimento(board):
    mudou1 = True
    mudou2 = True
    mudou3 = True
    mudou4 = True
    while mudou1 or mudou2 or mudou3 or mudou4:
        [board, mudou1] = preenchimento_adjacencias('4', board)
        [board, mudou2] = preenchimento_adjacencias('3', board)
        [board, mudou3] = preenchimento_adjacencias('2', board)
        [board, mudou4] = preenchimento_adjacencias('1', board)
    return board


def bloqueios(board):
    for linha in range(0, 7):
        for coluna in range(0, 7):
            [v, l] = vazios_e_lampadas(linha, coluna, board)

            if board[linha][coluna] == '0':
                if linha + 1 < 7 and board[linha + 1][coluna] == '':
                    board[linha + 1][coluna] = 'X'
                if coluna + 1 < 7 and board[linha][coluna + 1] == '':
                    board[linha][coluna + 1] = 'X'
                if linha - 1 >= 0 and board[linha - 1][coluna] == '':
                    board[linha - 1][coluna] = 'X'
                if coluna - 1 >= 0 and board[linha][coluna - 1] == '':
                    board[linha][coluna - 1] = 'X'

            if board[linha][coluna] == '1' and l == 1:
                if linha + 1 < 7 and board[linha + 1][coluna] == '':
                    board[linha + 1][coluna] = 'X'
                if coluna + 1 < 7 and board[linha][coluna + 1] == '':
                    board[linha][coluna + 1] = 'X'
                if linha - 1 >= 0 and board[linha - 1][coluna] == '':
                    board[linha - 1][coluna] = 'X'
                if coluna - 1 >= 0 and board[linha][coluna - 1] == '':
                    board[linha][coluna - 1] = 'X'

            if board[linha][coluna] == '2' and l == 2:
                if linha + 1 < 7 and board[linha + 1][coluna] == '':
                    board[linha + 1][coluna] = 'X'
                if coluna + 1 < 7 and board[linha][coluna + 1] == '':
                    board[linha][coluna + 1] = 'X'
                if linha - 1 >= 0 and board[linha - 1][coluna] == '':
                    board[linha - 1][coluna] = 'X'
                if coluna - 1 >= 0 and board[linha][coluna - 1] == '':
                    board[linha][coluna - 1] = 'X'

            if board[linha][coluna] == '3' and l == 3:
                if linha + 1 < 7 and board[linha + 1][coluna] == '':
                    board[linha + 1][coluna] = 'X'
                if coluna + 1 < 7 and board[linha][coluna + 1] == '':
                    board[linha][coluna + 1] = 'X'
                if linha - 1 >= 0 and board[linha - 1][coluna] == '':
                    board[linha - 1][coluna] = 'X'
                if coluna - 1 >= 0 and board[linha][coluna - 1] == '':
                    board[linha][coluna - 1] = 'X'
    return board


# Analisar casas bloqueadas (marcadas com X)
def possibilidades_bloqueados(board):
    for linha in range(0, 7):
        for coluna in range(0, 7):
            if board[linha][coluna] == 'X':
                possibilidades = 0

                j = coluna
                # Buscar possibilidades na linha à esquerda
                while j > 0 and (board[linha][j - 1] == '' or board[linha][j - 1] == 'I' or board[linha][j - 1] == 'X'):
                    if board[linha][j - 1] == '':
                        possibilidades += 1
                        x = linha
                        y = j - 1

                j = coluna
                # Buscar possibilidades na linha à direita
                while j < 6 and (board[linha][j + 1] == '' or board[linha][j + 1] == 'I' or board[linha][j + 1] == 'X'):
                    if board[linha][j + 1] == '':
                        possibilidades += 1
                        x = linha
                        y = j + 1

                i = linha
                # Buscar possibilidades coluna acima
                while i > 0 and (
                        board[i - 1][coluna] == '' or board[i - 1][coluna] == 'I' or board[i - 1][coluna] == 'X'):
                    if board[i - 1][coluna] == '':
                        possibilidades += 1
                        x = i - 1
                        y = coluna

                i = linha
                # Buscar possibilidades coluna abaixo
                while i < 6 and (
                        board[i + 1][coluna] == '' or board[i + 1][coluna] == 'I' or board[i + 1][coluna] == 'X'):
                    if board[i + 1][coluna] == '':
                        possibilidades += 1
                        x = i + 1
                        y = coluna

                # Se houver só uma possibilidade, a lâmpada será colocada lá e X->I
                if possibilidades == 1:
                    board[x][y] = 'L'
                    board[linha][coluna] = 'I'
                    tabuleiro = iluminar(board)

    return tabuleiro


# OTIMIZAR ESSA PARTE!!!
tabuleiro = finalizacao_preenchimento(tabuleiro)
tabuleiro = bloqueios(tabuleiro)
tabuleiro = finalizacao_preenchimento(tabuleiro)
tabuleiro = bloqueios(tabuleiro)

tabuleiro = possibilidades_bloqueados(tabuleiro)

print(tabuleiro)

casas_vazias = 0
for i in range(0, 7):
    for j in range(0, 7):
        if tabuleiro[i][j] == '':
            casas_vazias += 1

if casas_vazias == 0:
    print("COMPLETO")
else:
    print("INCOMPLETO")
