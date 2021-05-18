class TicTacToe:

    # To declare the variables we have to use in other methods
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        self.result = False

    # To start and the process of the game 'XO'
    def game_on(self):
        while True:
            self.show_grid()
            self.ask_coordinate("X")
            if self.result:
                break
            self.ask_coordinate("O")
            if self.result:
                break
        exit()

    def ask_coordinate(self, player):
        coordinates = input("Enter the coordinates: ").replace(" ", "")
        return self.check_coordinate(coordinates, player)

    def show_grid(self):
        print(f"""
        ---------
        | {self.grid[0][0]} {self.grid[0][1]} {self.grid[0][2]} |
        | {self.grid[1][0]} {self.grid[1][1]} {self.grid[1][2]} |
        | {self.grid[2][0]} {self.grid[2][1]} {self.grid[2][2]} |
        ---------
        """)
        return None

    def check_coordinate(self, coordinate, player):
        if len(coordinate) == 0 or len(coordinate) > 2:
            print("Coordinates should be from 1 to 3!")
            return self.ask_coordinate(player)
        for i in coordinate:
            if i in "123":
                pass
            elif i in "0456789":
                print("Coordinates should be from 1 to 3!")
                return self.ask_coordinate(player)
            else:
                print("You should enter numbers!")
                return self.ask_coordinate(player)
        return self.add_cell(coordinate, player)

    def add_cell(self, coordinate, player):
        row = int(coordinate[0]) - 1
        column = int(coordinate[1]) - 1
        if self.grid[row][column] == "O" or self.grid[row][column] == "X":
            print("This cell is occupied! Choose another one!")
            return self.ask_coordinate(player)
        else:
            self.grid[row][column] = player
            self.show_grid()
            return self.check_winner(row, column, player)

    def check_winner(self, row, column, player):
        # For shorter the line code
        grid = self.grid
        if all(cell == player for cell in grid[row]) or all(cell == player for cell in [x[column] for x in grid]):
            print(f"{player} wins")
            self.result = True
        elif grid[0][0] == grid[1][1] == grid[2][2] and grid[1][1] == player:
            print(f"{player} wins")
            self.result = True
        elif grid[0][2] == grid[1][1] == grid[2][0] and grid[1][1] == player:
            print(f"{player} wins")
            self.result = True
        check_draw = list()
        for i in range(3):
            for j in range(3):
                check_draw.append(grid[i][j])
        if all(value != " " for value in check_draw) and not self.result:
            print("Draw")
            self.result = True


start = TicTacToe()
start.game_on()
