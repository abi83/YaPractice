from random import randint

class Game:
    FIELD_START = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    field = None
    SIGNS = {
        'user': 'X',
        'cpu': '0',
    }

    def __init__(self):
        self.field = self.FIELD_START

    def check_move(self, point: tuple) -> None:
        if len(point) != 2:
            raise ValueError("Point must be in '1 3' format")
        for item in point:
            if item < 1 or item > 3:
                raise ValueError('X and Y must be in [1,2,3]')
        if self.field[point[1]-1][point[0]-1] != ' ':
            raise ValueError('The point is already busy')
        return True

    def make_move(self, point: tuple, player) -> bool:
        if self.check_move(point):
            self.field[point[1]-1][point[0]-1] = self.SIGNS.get(player)
            return True
        return False

    def cpu_move(self):
        while True:
            x = randint(1, 3)
            y = randint(1, 3)
            if self.check_move((x, y)):
                return x, y

    @staticmethod
    def user_move():
        move = input("Your move in: 'X Y' format: ")
        point = tuple(int(x) for x in move.split(' '))
        return point

    def field_print(self):
        print('╔=========╗')
        for line in self.field:
            print('║', end='')
            for column in line:
                print(' ' + column + ' ', end='')
            print('║')
        print('╚=========╝')

    def check_result(self):
        lists_to_check = []
        for line in self.field:
            lists_to_check.append(line)

        left_cross = []
        right_cross = []
        for i in range(0, 3):
            lists_to_check.append([element[i] for element in self.field])
            # breakpoint()
            left_cross.append(self.field[i][i])
            right_cross.append(self.field[i][2-i])
        lists_to_check.append(left_cross)
        lists_to_check.append(right_cross)
        for key, sign in self.SIGNS.items():
            for line in lists_to_check:
                if line.count(sign) == 3:
                    return key
        count = 0
        for line in self.field:
            count += line.count(' ')
        if count == 0:
            return 'No one'
        return None



if __name__ == "__main__":
    game = Game()
    winner = None

    while not winner:
        move_done = False

        # users move
        while not move_done:
            try:
                point = game.user_move()
                # game.check_move(point)
                move_done = game.make_move(point, 'user')
                print('User move accepted')
            except ValueError as e:
                print(e)
        game.field_print()
        winner = game.check_result()
        if winner:
            break


        # cpu move
        move_done = False
        while not move_done:
            try:
                point = game.cpu_move()
                # game.check_move(point)
                move_done = game.make_move(point, 'cpu')
                print('CPU move accepted')
            except ValueError as e:
                print(e)

        game.field_print()
        winner = game.check_result()

    print(f'{winner} win!')
