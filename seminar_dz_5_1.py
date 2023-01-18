#  Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

#  Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

#  В качестве дополнительного усложнения можно:
#   a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#   b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
from random import randint
count_sweets = 221
max_take_sweets=28
curent_player=randint(1, 3)
player_1=player_2=0
bot_playing=True



def player_takes_candy(curent_player,count_sweets,max_take_sweets):
    print('Ходит игрок ->',curent_player)
    taken_sweets=False
    while taken_sweets!=True:
        print('Возьмите конфеты (не больше ',max_take_sweets,') конфет осталось ->',count_sweets)
        take=int(input())
        if take<1 or take>max_take_sweets or  take>count_sweets:
            taken_sweets=False
            print('Вы можете взять только от 1 до ',max_take_sweets,' конфе и не больше ->',count_sweets)
        else:
            taken_sweets=True
    return take

def bot_takes_candy(count_sweets,max_take_sweets):
    print('Ходит бот игрок ->',curent_player)
    if count_sweets<=max_take_sweets:
        take=count_sweets
    else:
        take=randint(1, 29)
    print('Бот взял ->',take,' конфет ')
    return take

while count_sweets!=0:
    if curent_player==1:
        taken_sweets=player_takes_candy(curent_player,count_sweets,max_take_sweets)
        player_1+=taken_sweets
        count_sweets-=taken_sweets
        curent_player=2
    elif curent_player==2:
        if bot_playing == False:
            taken_sweets=player_takes_candy(curent_player,count_sweets,max_take_sweets)
        elif bot_playing== True:
            taken_sweets=bot_takes_candy(count_sweets,max_take_sweets)
        player_2+=taken_sweets
        count_sweets-=taken_sweets
        curent_player=1
print(player_1)
print(player_2)
if curent_player==1:
    print('Победил игрок 2')
elif curent_player==2:
    print('Победил игрок 1')


