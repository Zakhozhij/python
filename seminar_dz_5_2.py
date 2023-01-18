#  Создайте программу для игры в ""Крестики-нолики"". 
# Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает соответсвующие клетки от 1 до 9), 
# сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

board = [' ' for _ in range(1,10)]
def draw_board(board):
    print ("-------------")
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-------------")

def make_move(current_player,board):
    who_make_move='+'
    if current_player==1:
        who_make_move='0'
    wrong_ceil=True
    while wrong_ceil!=False:
        print('Введите номер ячейки (от 1 до 9) для зполнения -> ')
        ceil=int(input())
        if 0<ceil<10 and board[ceil-1]==" ":
            wrong_ceil=False 
        else:
            print('Ячейка недоступна')
    board[ceil-1]=who_make_move
    return board

def check_result(current_player,board):
    who_make_move='0'
    if current_player==1:
        who_make_move='+'
    if (board[0]==board[1]==board[2]==who_make_move or board[3]==board[4]==board[5]==who_make_move or board[6]==board[7]==board[8]==who_make_move\
        or board[0]==board[3]==board[6]==who_make_move or board[1]==board[4]==board[7]==who_make_move or board[2]==board[5]==board[8]==who_make_move\
        or board[0]==board[4]==board[8]==who_make_move or board[2]==board[4]==board[6]==who_make_move):
        print('Победили ->',who_make_move)
        return 1
    elif (board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' '):
        print('Ничья')
        return 1
    else:
        return 0


result=0
current_player=1
while result!=1:
    draw_board(board)
    result=check_result(current_player,board)
    if result!=1:
        board=make_move(current_player,board)
        if current_player==1:
            current_player=2
        elif current_player==2:
            current_player=1
draw_board(board)