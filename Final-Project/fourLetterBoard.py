# Author: Khushboo Patel
# Description: 2 player FourLetterBoard game
# Implementation decisions: Store coordinates in a list (instead of tuples as tuples cannot be replaced with strings when
# updating the game board tiles from coordinates to letters A-D).


class FourLetterBoard:

    def __init__(self):
        self.board = {"A": [[0, 0], [0, 1], [1, 0], [1, 1]],
                       "B": [[0,2], [0,3], [1,2], [1,3]],
                       "C": [[2,0], [2,1], [3,0], [3,1]],
                       "D": [[2,2], [2,3], [3,2], [3,3]]}
        #tracks/stores letters at the region level
        self.current_board = dict(self.board)
        self.valid_coordinates = self.valid_coordinates()
        self.current_state = "UNFINISHED"
        self.totalmoves = 0
        #tracks/stores letters at the player level; letter played:coordinates
        self.moves_played = {"x":
                                 {"A": [],
                                  "B": [],
                                  "C": [],
                                  "D": []},
                             "o":
                                 {"A": [],
                                  "B": [],
                                  "C": [],
                                  "D": []}}

    def get_opponent(self, player):
        if player.lower() == "x":
            return "o"
        elif player.lower() == "o":
            return "x"
        else:
            return False

    def valid_coordinates(self):
        v_coordinates = []
        for row in range(0,4):
            for column in range(0,4):
                v_coordinates.append([row, column])
        return v_coordinates

    def get_value(self, region, coordinates):
        value = None
        for code in self.current_board.keys():
            if code == region and coordinates in self.current_board[code]:
                value = coordinates
        return value

    def get_region(self, coordinates):
        for code in self.board.keys():
            if coordinates in self.board[code]:
                return code

    def get_regioncoordinates(self, region):
        coordinates = []
        for code in self.board.keys():
            if code == region:
                coordinates += self.board[code]
        return coordinates

    def get_neighbors(self, region, coordinates):
        row = coordinates[0]
        column = coordinates[1]
        row_list = [[row, n] for n in range(0,4)]
        column_list = [[n, column] for n in range(0,4)]
        region_list = self.get_regioncoordinates(region)
        temp = [row_list, column_list, region_list]
        neighbors = []
        for lst in temp:
            for item in lst:
                if item not in neighbors:
                    neighbors.append(item)
        neighbors.remove(coordinates)
        return neighbors

    def get_opponentmoves(self, opponent, player_letter):
        opponent_moves = []
        for id, info in self.moves_played.items():
            if id == opponent:
                for key in info:
                    if key == player_letter:
                        opponent_moves += info[key]
        return opponent_moves

    def checkduplicate(self, opponent_moves, neighbors):
        flag = "N"
        for coordinate in neighbors:
            if coordinate in opponent_moves:
                flag = "Y"
        return flag

    def make_move(self, row, column, letter, player):
        """If the game has already been won or drawn, or
        if letter, player and coordinates are invalid, or
        if the square is not empty, or
        if the letter duplicates an opponent letter in the same row, column, or region,
        make_move should just return False."""
        if self.current_state != "UNFINISHED":
            print("Error: Game over")
            return False
        elif letter.upper() not in ["A", "B", "C", "D"]:
            print("Error: Invalid letter")
            return False
        elif player.lower() not in ["x", "o"]:
            print("Error: Invalid player")
            return False

        coordinates = [row, column]
        if coordinates not in self.valid_coordinates:
            print("Error: Invalid coordinates")
            return False

        region = self.get_region(coordinates)
        square = self.get_value(region, coordinates)
        #i.e. if value is None
        if square != coordinates:
            print("Error: Square is not empty")
            return False

        opponent = self.get_opponent(player)
        opponent_moves = self.get_opponentmoves(opponent, letter)
        neighbors = self.get_neighbors(region, coordinates)
        is_duplicate = self.checkduplicate(opponent_moves, neighbors)
        if is_duplicate.upper() == "Y":
            print("Error: Duplicates an opponent letter in the same row, column or region")
            return False
        else:
            self.update_board(region, coordinates, letter, player)
            return True

    def update_board(self, region, coordinates, letter, player):
        self.totalmoves += 1

        #update currentboard
        for code in self.current_board.keys():
            if code == region:
                for i in range(0, len(self.current_board[code])):
                    #if value = coordinates, replace current value with player's letter
                    if self.current_board[code][i] == coordinates:
                        self.current_board[code][i] = letter

        #update moves_played
        for node, code in self.moves_played.items():
            if node == player:
                for code in self.moves_played[node]:
                    if code == letter:
                        self.moves_played[node][code].append(coordinates)

        #update currentstate
        tempstr = ''
        for code in self.current_board.keys():
            if code == region:
                for i in range(0, len(self.current_board[code])):
                    if self.current_board[code][i] in ['A', 'B', 'C', 'D']:
                        tempstr += self.current_board[code][i]
        result = sorted(str(tempstr))
        if result == ['A', 'B', 'C', 'D']:
            self.set_current_state(player)
        elif self.totalmoves >= 16:
            self.current_state = "DRAW"

    def set_current_state(self, player):
        if player == "x":
            self.current_state = "X_WON"
        elif player == "o":
            self.current_state = "O_WON"

    def get_board(self):
        return self.board

    def get_currentboard(self):
        return self.current_board

    def get_current_state(self):
        return self.current_state

    def get_movesplayed(self):
        return self.moves_played

    def get_totalmoves(self):
        return self.totalmoves



def main():
    g1 = FourLetterBoard()

    print("Player O Region A:", g1.make_move(1, 1, "B", "o"))
    print("Player X Region B:", g1.make_move(1, 2, "A", "x"))
    print("Player O Region A:", g1.make_move(0, 1, "C", "o"))
    print("Player X Region B:", g1.make_move(0, 2, "B", "x"))
    print("Player O Region B:", g1.make_move(0, 3, "A", "o"))
    print("Player X Region A:", g1.make_move(0, 0, "B", "x"))
    print("Player O Region C:", g1.make_move(2, 0, "A", "o"))
    print("Player X Region C:", g1.make_move(3, 0, "C", "x"))
    print("Player O Region C:", g1.make_move(2, 1, "D", "o"))
    print("Player X Region D:", g1.make_move(2, 2, "B", "x"))
    print("Player O Region C:", g1.make_move(3, 1, "B", "o"))
    print("Player X Region D:", g1.make_move(3, 2, "C", "x"))
    print("Total moves:", g1.get_totalmoves())
    print("Game Status:", g1.get_currentstate())
    print("Gameboard:", g1.get_currentboard())
    print("Player Level Moves:", g1.get_movesplayed())

if __name__ == '__main__':
    main()

