# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
#  последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def player(name, sum, max):
    valid = False
    while not valid:
        move = input(f'{name}, Ваш ход... ')
        try:
            move = int(move)
            if move > 0 and move <= max and move <= sum:
                sum -= move
                print(f'Осталось {sum}')
                valid = True
            else:
                print(f'Количество  от 1 до {max} или не больше оставшегося количества конфет')
        except:
            print('Ведите целое число.')
    return sum


def bot1(sum, max):
    move = randint(1, max) if sum >= max else randint(1, sum)
    sum -= move
    print(f'Осталось {sum}')
    return sum

def bot2(sum, max):
    move = sum % (max + 1)
    if move == 0:
        move = randint(1, max) if sum >= max else sum
    sum -= move
    print(f'Осталось {sum}')
    return sum

def winer(sum, determing_moves, name_1, name_2):
    if sum == 0:
        return name_1 if determing_moves % 2 == 0 else name_2
    else:
        return False


def VSbot1 ():
    name = input('Введите свое имя: ')
    sum = 2021
    max = 28
    count_for_check_win = sum // max
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            sum = player(name, sum, max)
        else:
            sum = bot1(sum, max)
        if determing_moves >= count_for_check_win - 1:
            temp = winer(sum, determing_moves, name, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1


def VSbot2 ():
    name = input('Введите свое имя: ')
    sum = 2021
    max = 28
    count_for_check_win = sum // max
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            sum = player(name, sum, max)
        else:
            sum = bot2(sum, max)
        if determing_moves >= count_for_check_win - 1:
            temp = winer(sum, determing_moves, name, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def VSplayer ():
    name_1_player = input('Введите имя первого игрока: ')
    name_2_player = input('Введите имя второго игрока: ')
    sum = 2021
    max = 28
    count_for_check_win = sum // max
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            sum = player(name_1_player, sum, max)
        else:
            sum = player(name_2_player, sum, max)
        if determing_moves >= count_for_check_win - 1:
            temp = winer(sum, determing_moves, name_1_player, name_2_player)
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

VSbot2 ()
