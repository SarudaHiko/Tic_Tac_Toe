game_field = [[' '] * 3 for i in range(3)]


def welcome():
    print('---------------------------')
    print('  Добро пожаловать в игру')
    print("      Крестики-Нолики")
    print('---------------------------')
    print('Вводить нужно только цифры')
    print('---------------------------')
    print('     x - номер строки')
    print('     у - номер столбца')
    print('---------------------------\n')
    print("Готовы начать игру?")
    print('Если да - введите "Y"')
    y = input('Вводить здесь: ')
    if y == 'Y':
        start_game()
    else:
        print('\nЗакрытие программы')


def move():
    num = 0
    while True:
        num += 1

        show_field()

        if num % 2 == 1:
            print('Ходят крестики')
        else:
            print('Ходят нолики')

        x, y = ask()

        if num % 2 == 1:
            game_field[x][y] = 'X'
        else:
            game_field[x][y] = 'O'

        if check_win():
            break

        if num == 9:
            print('Ничья!')
            break


def show_field():
    print()
    print('   | 0 | 1 | 2 | ')
    print(' ----------------')
    for i, row in enumerate(game_field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print(' ----------------')
    print()


def ask():
    while True:
        cords = input('     Ваш ход: ').split()

        if len(cords) != 2:
            print('Введите 2 координаты!')
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Таких координат нет!')
            continue

        if game_field[x][y] != ' ':
            print('Клетка занята!')
            continue

        return x, y


def check_win():
    win_pos = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_pos:
        symbols = []

        for c in cord:
            symbols.append(game_field[c[0]][c[1]])

        if symbols == ['X', 'X', 'X']:
            show_field()
            print('Выиграли Крестики!')
            return True
        if symbols == ['O', 'O', 'O']:
            show_field()
            print('Выиграли Нолики!')
            return True
    return False


def start_game():
    print('\nЗапускаю игру:')
    move()


welcome()
