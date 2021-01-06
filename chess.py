"""
This is my first self project, completed after my first semester of learning to code.

I created the game of chess from scratch, aiming to improve my OOP skill and hopefully learn a bit of GUI.
"""

import copy, sys

class Game:
    """ Game abstraction that contains player names, a board object, and whose turn it is.
        It also checks for certain game conditions such as checkmate, all legal moves, etc."""
    
    def __init__(self, player1, player2, board):
        self.player1, self.player2 = player1, player2
        self.board = board
        self.turn = 1
        self.board.game = self

    def get_score(self):
        """ Gives scores of both players based on pieces remaining """
        p1_score = sum([x.points for x in self.board.white_pieces])
        p2_score = sum([x.points for x in self.board.black_pieces])
        print('P1 score: ', p1_score)
        print('P2 score: ', p2_score)

    def in_check(self, player):
        """ Given a player, returns whether or not they're in check """
        player_pieces = self.board.white_pieces if player == 1 else self.board.black_pieces
        opp_pieces = self.board.black_pieces if player == 1 else self.board.white_pieces
        target_place = [piece.place for piece in player_pieces if isinstance(piece, King)][0]
        opp_moves = []
        for p in opp_pieces:
            opp_moves.extend(p.get_moves())
        return any(list(filter(lambda x: x == target_place, opp_moves)))

    def get_all_moves(self, color):
        """ Given a color, returns all possible moves they can make """
        moves = []
        for piece in eval('self.board.{0}_pieces'.format(color.lower())):
            for move in piece.get_moves():
                moves.append(move)
        return moves 


    def in_checkmate(self, player):
        """ Given a player, returns whether or not they're in checkmate """
        if self.in_check(player):
            bu = copy.deepcopy(self)
            for piece in eval('bu.board.{0}_pieces[:]'.format('white' if player == 1 else 'black')):
                moves = piece.get_moves()
                for move in moves:
                    piece2 = move.piece
                    place1, place2 = piece.place, move
                    piece.direct_move(move)
                    if not bu.in_check(player):
                        return False
                    piece.direct_move(place1)
                    if piece2:
                        piece2.direct_move(place2)
                        eval("bu.board.{0}_pieces.append(piece2)".format(piece2.color.lower()))
            return True
        return False

    def in_stalemate(self, player):
        """ Given a player, returns whether or not they're in stalemate """
        if not self.in_check(player):
            bu = copy.deepcopy(self)
            for piece in eval('bu.board.{0}_pieces[:]'.format('white' if player == 1 else 'black')):
                moves = piece.get_moves()
                for move in moves:
                    piece2 = move.piece
                    place1, place2 = piece.place, move
                    piece.direct_move(move)
                    if not bu.in_check(player):
                        return False
                    piece.direct_move(place1)
                    if piece2:
                        piece2.direct_move(place2)
                        eval("bu.board.{0}_pieces.append(piece2)".format(piece2.color.lower()))
            return True
        return False

class Board:
    """ Board abstraction that contains a dictionary of 64 place objects along with 2 lists that contain
        all white and black pieces that haven't been captured"""

    def __init__(self):
        self.places = {}  #Every space on board has a key (string such as 'A2') and a value (corresponding place object)
        self.white_pieces = []
        self.black_pieces = []
        self.reset_board()

    def reset_board(self):
        """ Resets board to starting conditions """
        self.places.clear()
        self.white_pieces.clear()
        self.black_pieces.clear()
        
        ### Pieces ###
        self.white_pieces.extend([Rook('White'), Knight('White'), Bishop('White'), Queen('White'), 
            King('White'), Bishop('White'), Knight('White'), Rook('White')])
        self.black_pieces.extend([Rook('Black'), Knight('Black'), Bishop('Black'), Queen('Black'), 
            King('Black'), Bishop('Black'), Knight('Black'), Rook('Black')])
        
        row, color, pieces = 1, 'White', self.white_pieces    #Placing pieces on their starting squares
        while row <= 8:
            piece = 0
            for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                self.places['{0}{1}'.format(column, row)] = Place(column, row, pieces[piece])
                piece += 1
            row, color, pieces = row + 7, 'Black', self.black_pieces

        ### Pawns ###
        self.white_pieces.extend([Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White'),
            Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White')])
        self.black_pieces.extend([Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black'),
            Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black')])
        
        row, color, pieces = 2, 'White', self.white_pieces    #Placing pawns on their starting squares
        while row <= 7:
            piece = 8
            for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                self.places['{0}{1}'.format(column, row)] = Place(column, row, pieces[piece])
                piece += 1
            row, color, pieces = row + 5, 'Black', self.black_pieces

        for p in self.white_pieces + self.black_pieces:
            p.board = self

        ### Other Places ###
        for row in range(3, 7):    #Creating place entries for all squares that pieces don't start on
            for column in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                self.places['{0}{1}'.format(column, row)] = Place(column, row)

        for p in self.places.values():
            p.board = self


class Place:
    """ Place abstraction that contains attributes for row, column, and piece contained if there is one on that square
        Also contains methods for removing a piece when it is moved or captured"""

    def __init__(self, column, row, piece=None):
        self.row, self.column = row, column
        self.piece = piece
        if piece:
            self.piece.place = self

    def __repr__(self):
        if self.piece:
            return '{0}{1}: {2} {3}'.format(self.column, self.row, self.piece.color, self.piece.kind)
        else:
            return '{0}{1}'.format(self.column, self.row)

    def move_piece(self):
        """ Used when a piece is moved (not captured / removed from game) """
        self.piece = None

    def remove_piece(self):
        """ Used when a piece is removed from game (captured, pawn promotion) """
        if self.piece:    
            eval('self.board.{0}_pieces.remove(self.piece)'.format(self.piece.color.lower()))  #removes piece from active list of pieces in Board object
            self.piece = None

    def get_img(self):
        """ Updates a given square in the GUI """
        if self.column in ['A', 'C', 'E', 'G'] and self.row % 2 == 0:
            square_color = 'white'
        elif self.column in ['B', 'D', 'F', 'H'] and self.row % 2 == 1:
            square_color = 'white'
        else:
            square_color = 'black'
        if self.piece == None:
            return '{0}_blank'.format(square_color)
        else:
            return '{0}_{1}{2}'.format(square_color, self.piece.color.lower()[0], self.piece.kind.lower())

class Piece:
    """ Piece abstraction, contains attributes for kind (eg. "King") and color. Also contains methods for moving pieces, 
        but determining legal moves is left to subclasses, as different types of pieces move in different ways """

    turns = 0  # Not needed for most pieces, used to keep track of turns for En Passant captures
    def __init__(self, kind, color):
        self.kind, self.color = kind, color
    
    def __repr__(self):
        return self.color + ' ' + self.kind

    def move_cl(self):
        """ Moves piece to square given by user in the command line version, and captures piece if there is one, 
        after checking if move is legal. Also handles special cases, such as castling and En passant """
        attempt = input('Where to move {0}: '.format(self.kind))  #User gives square to move to
        if attempt == 'Back':
            pass
        elif self.board.places.get(attempt) is None:
            print('Inavlid input')
        elif self.board.places[attempt] not in self.get_moves(True):
            print('Illegal move')
        else:  
            new_place = self.board.places[attempt]  #Place object attained from user input
            if self.kind == 'Pawn' and not new_place.piece and new_place.column != self.place.column:  #Checks for and handles En passant captures
                self.board.places[new_place.column + str(self.place.row)].remove_piece()
            self.place.move_piece() 
            new_place.remove_piece()  #Piece is captured, if relevant
            new_place.piece = self  #Piece is moved
            self.place = new_place
            
            if self.kind == 'King' and self.moved == False:  #Handles special case of castling
                row = str(1 if self.color == 'White' else 8)
                if (attempt == 'G1' and self.color == 'White') or (attempt == 'G8' and self.color == 'Black'):
                    self.board.places['H' + row].piece.direct_move(self.board.places['F' + row])
                elif (attempt == 'C1' and self.color == 'White') or (attempt == 'C8' and self.color == 'Black'):
                    self.board.places['A' + row].piece.direct_move(self.board.places['D' + row])

            if self.kind == 'Pawn':
                if self.moved == False:  #Resets turns so pawn can be captured by En passant only on next turn
                    self.turns = 0
                if self.place.row == (8 if self.color == 'White' else 1): #Checking for pawn promotion
                    self.promote()
            if self.kind == 'King' or self.kind == 'Rook' or self.kind == 'Pawn':  #King and rook can no longer castle, pawn can 
                self.moved = True                                                   #   only move 2 squares on first turn
            for p in self.board.white_pieces + self.board.black_pieces:  #Incrementing turns for En passant captures
                p.turns += 1
            self.board.game.turn = 3 - self.board.game.turn  #Changes turn

    def direct_move(self, new_place):
        """ Not normally used for piece movement, used for testing checkmate and castling """
        self.place.move_piece()
        new_place.remove_piece()
        new_place.piece = self
        self.place = new_place

    def get_long_moves(self, direction, curr_column, curr_row, color):
        """ Given a direction, row, and column, returns a list of legal moves in that direction 
            Used for pieces that can move in straight lines (Queen, Rook, Bishop)"""
        if direction == 'ru':
            curr_column, curr_row = chr(ord(curr_column) + 1), str(int(curr_row) + 1)
        elif direction == 'rd':
            curr_column, curr_row = chr(ord(curr_column) + 1), str(int(curr_row) - 1)
        elif direction == 'lu':
            curr_column, curr_row = chr(ord(curr_column) - 1), str(int(curr_row) + 1)
        elif direction == 'ld':
            curr_column, curr_row = chr(ord(curr_column) - 1), str(int(curr_row) - 1)
        elif direction == 'r':
            curr_column, curr_row = chr(ord(curr_column) + 1), str(curr_row)
        elif direction == 'l':
            curr_column, curr_row = chr(ord(curr_column) - 1), str(curr_row)
        elif direction == 'u':
            curr_column, curr_row = curr_column, str(int(curr_row) + 1)
        elif direction == 'd':
            curr_column, curr_row = curr_column, str(int(curr_row) - 1)
        else:
            print('Error: inavlid direction')

        target_place = self.board.places.get(curr_column + curr_row)
        target_places = []
        if target_place is None:
            return []
        elif target_place.piece is None:
            target_places.append(target_place)
            target_places.extend(self.get_long_moves(direction, curr_column, curr_row, color))
            return target_places
        elif target_place.piece.color != self.color:
            target_places.append(target_place)
            return target_places
        else:
            return []

class King(Piece):  
    """ King subclass of piece """

    points = 0  #Standard points in chess scoring systems

    def __init__(self, color):
        Piece.__init__(self, 'King', color)
        self.moved = False  #for castling purposes

    def get_moves(self, castle=False):   
        """ Returns a list of place objects that this king can legally move to """
        """ Castle attribute is necessary so that castle moves are only checked for under certain conditions. 
            Otherwise, endless recursion will occur when checking for checkmate. """
        curr_row, curr_column = self.place.row, self.place.column
        
        potential_squares = [curr_column + str(curr_row + 1), curr_column + str(curr_row - 1), 
        chr(ord(curr_column) + 1) + str(curr_row), chr(ord(curr_column) - 1) + str(curr_row),
        chr(ord(curr_column) + 1) + str(curr_row + 1), chr(ord(curr_column) + 1) + str(curr_row - 1),
        chr(ord(curr_column) - 1) + str(curr_row + 1), chr(ord(curr_column) - 1) + str(curr_row - 1)]
        
        potential_moves = [self.board.places.get(square) for square in potential_squares]
        can_move = lambda x: x is not None and (x.piece is None or x.piece.color != self.color)
        potential_moves = list(filter(can_move, potential_moves))
        if castle and not self.moved:    
            potential_moves.extend(self.add_castle_moves())  #Adds castle moves if applicable
        return potential_moves

    def add_castle_moves(self):
        """ Returns list of castle moves if necessary conditions are met (King and Rook haven't moved, 
            King not in check, no pieces in between, King can't move through check) """
        castle_moves = []
        row = str(1 if self.color == 'White' else 8)
        r_rook, r_knight, r_bishop = 'H' + row, 'G' + row, 'F' + row
        l_rook, l_knight, l_bishop, l_queen = 'A' + row, 'B' + row, 'C' + row, 'D' + row
        opp_moves = self.board.game.get_all_moves('Black' if self.color == 'White' else 'White')
        
        if (self.board.places[r_rook].piece and self.board.places[r_rook].piece.kind == 'Rook' and 
            not self.board.places[r_rook].piece.moved and self.board.places[r_bishop].piece is None and 
            self.board.places[r_knight].piece is None):  #castling conditions (right)
            if self.board.places[r_bishop] not in opp_moves and self.board.places[r_knight] not in opp_moves and self.place not in opp_moves: #king can't move through check
                castle_moves.append(self.board.places[r_knight])            
        if (self.board.places[l_rook].piece and self.board.places[l_rook].piece.kind == 'Rook' and 
            not self.board.places[l_rook].piece.moved and self.board.places[l_knight].piece is None and 
            self.board.places[l_bishop].piece is None and self.board.places[l_bishop].piece is None): #castling conditions (left)
            if self.board.places[l_bishop] not in opp_moves and self.board.places[l_queen] not in opp_moves and self.place not in opp_moves: #king can't move through check
                castle_moves.append(self.board.places[l_bishop])
        return castle_moves

class Queen(Piece):
    """ Queen subclass of piece """

    points = 9  #Standard points in chess scoring systems

    def __init__(self, color):
        Piece.__init__(self, 'Queen', color)

    def get_moves(self, castle=False):  #See note on castle variable under King.get_moves()
        """ Returns a list of place objects that this Queen can legally move to """
        target_places = []
        for direction in ['r', 'l', 'u', 'd', 'ru', 'rd', 'lu', 'ld']:  #directions Queen can move in
            target_places.extend(self.get_long_moves(direction, self.place.column, self.place.row, self.color))
        return target_places

class Rook(Piece):
    """ Rook subclass of piece """

    points = 5  #Standard points in chess scoring systems

    def __init__(self, color):
        Piece.__init__(self, 'Rook', color)
        self.moved = False  #for castling purposes

    def get_moves(self, castle=False):  #See note on castle variable under King.get_moves()
        """ Returns a list of place objects that this Rook can legally move to """
        target_places = []
        for direction in ['r', 'l', 'u', 'd']:  #directions Rook can move in
            target_places.extend(self.get_long_moves(direction, self.place.column, self.place.row, self.color))
        return target_places

class Bishop(Piece):
    """ Bishop subclass of piece """

    points = 3  #Standard points in chess scoring systems

    def __init__(self, color):
        Piece.__init__(self, 'Bishop', color)

    def get_moves(self, castle=False):  #See note on castle variable under King.get_moves()
        """ Returns a list of place objects that this Bishop can legally move to """
        target_places = []
        for direction in ['ru', 'lu', 'rd', 'ld']:  #directions Bishop can move in
            target_places.extend(self.get_long_moves(direction, self.place.column, self.place.row, self.color))
        return target_places

class Knight(Piece):
    """ Knight subclass of piece """

    points = 3  #Standard points in chess scoring systems

    def __init__(self, color):
        Piece.__init__(self, 'Knight', color)

    def get_moves(self, castle=False):  #See note on castle variable under King.get_moves()
        """ Returns a list of place objects that this Knight can legally move to """
        curr_row, curr_column = self.place.row, self.place.column
        
        potential_squares = [chr(ord(curr_column) + 1) + str(curr_row + 2), chr(ord(curr_column) + 1) + str(curr_row - 2),
        chr(ord(curr_column) + 2) + str(curr_row + 1), chr(ord(curr_column) + 2) + str(curr_row - 1),
        chr(ord(curr_column) - 1) + str(curr_row + 2), chr(ord(curr_column) - 1) + str(curr_row - 2),
        chr(ord(curr_column) - 2) + str(curr_row + 1), chr(ord(curr_column) - 2) + str(curr_row - 1)]

        potential_moves = [self.board.places.get(square) for square in potential_squares]
        can_move = lambda x: x is not None and (x.piece is None or x.piece.color != self.color)
        potential_moves = list(filter(can_move, potential_moves))
        return potential_moves

class Pawn(Piece):
    """ Pawn subclass of piece """

    points = 1  #Standard points in chess scoring systems

    def __init__(self, color):
        Piece.__init__(self, 'Pawn', color)
        self.moved = False

    def get_moves(self, castle=False):  #See note on castle variable under King.get_moves()
        """ Returns a list of place objects that this Pawn can legally move to """
        curr_row, curr_column = self.place.row, self.place.column
        potential_moves = []
        inc = 1 if self.color == 'White' else -1  #white pawns and black pawns move in different directions

        up1 = self.board.places.get(curr_column + str(curr_row + inc))
        up2 = self.board.places.get(curr_column + str(curr_row + 2 * inc))
        diag_l = self.board.places.get(chr(ord(curr_column) - 1) + str(curr_row + inc))
        diag_r = self.board.places.get(chr(ord(curr_column) + 1) + str(curr_row + inc))
        r1 = self.board.places.get(chr(ord(curr_column) + 1) + str(curr_row))  #r1 (right) and l1 (left) squares are checked for
        l1 = self.board.places.get(chr(ord(curr_column) - 1) + str(curr_row))  #    possible En passant captures

        if (self.place.row == 8 and self.color == 'White') or (self.place.row == 1 and self.color == 'Black'):
            return []
        if up1.piece is None:
            potential_moves.append(up1)
        if up2 and up2.piece is None and self.moved == False:  #Pawn can move 2 squares on first move
            potential_moves.append(up2)
        if diag_l and diag_l.piece and diag_l.piece.color != self.color:   #Pawn captures diagonally
            potential_moves.append(diag_l)
        elif l1 and l1.piece and l1.piece.color != self.color and l1.piece.kind == 'Pawn' and l1.piece.turns == 1:  #En passant
            potential_moves.append(diag_l)
        if diag_r and diag_r.piece and diag_r.piece.color != self.color:   #Pawn captures diagonally
            potential_moves.append(diag_r)
        elif r1 and r1.piece and r1.piece.color != self.color and r1.piece.kind == 'Pawn' and r1.piece.turns == 1:  #En passant
            potential_moves.append(diag_r)
        return potential_moves

    def promote(self):
        """ Pawn is promoted to Queen, Rook, Bishop, or Knight if it reaches the final row """
        self.place.remove_piece()
        while True:
            new_piece = input("Choose piece for promotion ('Queen', 'Knight', 'Rook', or 'Bishop'): ")  #User decides which piece to promote to
            if new_piece in ['Queen', 'Knight', 'Rook', 'Bishop']:
                break
            print('Invalid input')
        new_piece = eval("{0}('{1}')".format(new_piece, self.color))
        new_piece.place, new_piece.board = self.place, self.board
        self.place.piece = new_piece
        eval('self.board.{0}_pieces.append(new_piece)'.format(self.color.lower()))


def play_cl():
    """ When called, allows users to play a command line version of the game """
    p1 = input("Player1 name: ")
    p2 = input("Player2 name: ")
    cg = Game(p1, p2, Board())  #Game instance created
    while True:
        backup = copy.deepcopy(cg)  #Deep copy of game is created, in case user moves into check
        if cg.in_checkmate(cg.turn):
            print('Game over: {0} wins'.format(p2 if cg.turn == 1 else p1))
            break
        elif cg.in_stalemate(cg.turn):
            print('Game over: stalemate')
            break
        sq = input("Piece to move ({0}): ".format('white' if cg.turn == 1 else 'black'))  #Player inputs square of piece to move
        target_place = cg.board.places.get(sq)
        if target_place is None:
            print('Inavild input')
        elif target_place.piece is None:
            print('No piece here')
        elif target_place.piece.color != ('White' if cg.turn == 1 else 'Black'):
            print("Cant move opponent's piece")
        else:
            target_place.piece.move_cl()
        if cg.in_check(3 - cg.turn):
            print("Can't move into check")
            cg = backup  #If player moves into check, which is illegal, game is restored to previous state of backup taken above
    ng = input('Enter Y for new game or N to exit: ')
    if ng == 'N' or ng == 'n':
        sys.exit()
    else:
        cg, backup = 0, 0
        play_cl()
