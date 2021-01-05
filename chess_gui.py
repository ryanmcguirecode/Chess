""" This is my first attempt at anything GUI related. In order for this to work on your computer you must have python3 and the pillow library installed. 
You can install this by running 'pip install pillow' in the terminal. If the pictures aren't loading make sure the directory below is correct. 
If not you can move the folder with the images or change the directory accessed below.

Most functions and logic can be found the chess.py file, but there are a few functions here that need to
interact directly with the GUI

To run the GUI: type 'python3 chess_gui.py' in the terminal
"""
import tkinter as tk
from pathlib import Path
from PIL import ImageTk, Image
from chess import *

root = tk.Tk()
root.title('Chess')
root.configure(background='#ffeacd')

dir_name = str(Path.cwd()) #Current directory of this file

# These are all of the necessary images for the game to work. 
# Color before underscore corresponds with the color of the square, and w or b before the piece corresponds with the color of the piece
white_wking = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_wking.jpg").resize((70, 70), Image.ANTIALIAS))
white_wqueen = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_wqueen.jpg").resize((70, 70), Image.ANTIALIAS))
white_wrook = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_wrook.png").resize((70, 70), Image.ANTIALIAS))
white_wbishop = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_wbishop.png").resize((70, 70), Image.ANTIALIAS))
white_wknight = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_wknight.png").resize((70, 70), Image.ANTIALIAS))
white_wpawn = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_wpawn.png").resize((70, 70), Image.ANTIALIAS))

black_wking = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_wking.jpg").resize((70, 70), Image.ANTIALIAS))
black_wqueen = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_wqueen.jpg").resize((70, 70), Image.ANTIALIAS))
black_wrook = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_wrook.png").resize((70, 70), Image.ANTIALIAS))
black_wbishop = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_wbishop.png").resize((70, 70), Image.ANTIALIAS))
black_wknight = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_wknight.png").resize((70, 70), Image.ANTIALIAS))
black_wpawn = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_wpawn.png").resize((70, 70), Image.ANTIALIAS))

white_bking = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_bking.jpg").resize((70, 70), Image.ANTIALIAS))
white_bqueen = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_bqueen.png").resize((70, 70), Image.ANTIALIAS))
white_brook = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_brook.png").resize((70, 70), Image.ANTIALIAS))
white_bbishop = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_bbishop.png").resize((70, 70), Image.ANTIALIAS))
white_bknight = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_bknight.png").resize((70, 70), Image.ANTIALIAS))
white_bpawn = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_bpawn.png").resize((70, 70), Image.ANTIALIAS))

black_bking = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_bking.jpg").resize((70, 70), Image.ANTIALIAS))
black_bqueen = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_bqueen.png").resize((70, 70), Image.ANTIALIAS))
black_brook = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_brook.png").resize((70, 70), Image.ANTIALIAS))
black_bbishop = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_bbishop.png").resize((70, 70), Image.ANTIALIAS))
black_bknight = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_bknight.png").resize((70, 70), Image.ANTIALIAS))
black_bpawn = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_bpawn.png").resize((70, 70), Image.ANTIALIAS))

white_blank = ImageTk.PhotoImage(Image.open(dir_name + "/Images/white_blank.png").resize((70, 70), Image.ANTIALIAS))
black_blank = ImageTk.PhotoImage(Image.open(dir_name + "/Images/black_blank.png").resize((70, 70), Image.ANTIALIAS))

# 64 buttons defined, one for each square on the board
ButtonA1 = tk.Button(root, text='A1', image=black_blank, highlightthickness=0)
ButtonA2 = tk.Button(root, text='A2', image=black_blank, highlightthickness=0)
ButtonA3 = tk.Button(root, text='A3', image=black_wking, highlightthickness=0)
ButtonA4 = tk.Button(root, text='A4', image=black_wking, highlightthickness=0)
ButtonA5 = tk.Button(root, text='A5', image=black_wking, highlightthickness=0)
ButtonA6 = tk.Button(root, text='A6', image=black_wking, highlightthickness=0)
ButtonA7 = tk.Button(root, text='A7', image=black_wking, highlightthickness=0)
ButtonA8 = tk.Button(root, text='A8', image=black_wking, highlightthickness=0)

ButtonB1 = tk.Button(root, text='B1', image=white_wknight, highlightthickness=0)
ButtonB2 = tk.Button(root, text='B2', image=black_wpawn, highlightthickness=0)
ButtonB3 = tk.Button(root, text='B3', image=black_wking, highlightthickness=0)
ButtonB4 = tk.Button(root, text='B4', image=black_wking, highlightthickness=0)
ButtonB5 = tk.Button(root, text='B5', image=black_wking, highlightthickness=0)
ButtonB6 = tk.Button(root, text='B6', image=black_wking, highlightthickness=0)
ButtonB7 = tk.Button(root, text='B7', image=black_wbishop, highlightthickness=0)
ButtonB8 = tk.Button(root, text='B8', image=black_wking, highlightthickness=0)

ButtonC1 = tk.Button(root, text='C1', image=black_wbishop, highlightthickness=0)
ButtonC2 = tk.Button(root, text='C2', image=white_wpawn, highlightthickness=0)
ButtonC3 = tk.Button(root, text='C3', image=black_wking, highlightthickness=0)
ButtonC4 = tk.Button(root, text='C4', image=black_wking, highlightthickness=0)
ButtonC5 = tk.Button(root, text='C5', image=black_wking, highlightthickness=0)
ButtonC6 = tk.Button(root, text='C6', image=black_wking, highlightthickness=0)
ButtonC7 = tk.Button(root, text='C7', image=black_wking, highlightthickness=0)
ButtonC8 = tk.Button(root, text='C8', image=black_wking, highlightthickness=0)

ButtonD1 = tk.Button(root, text='D1', image=white_wqueen, highlightthickness=0)
ButtonD2 = tk.Button(root, text='D2', image=black_wpawn, highlightthickness=0)
ButtonD3 = tk.Button(root, text='D3', image=black_wking, highlightthickness=0)
ButtonD4 = tk.Button(root, text='D4', image=black_wking, highlightthickness=0)
ButtonD5 = tk.Button(root, text='D5', image=black_wking, highlightthickness=0)
ButtonD6 = tk.Button(root, text='D6', image=black_wking, highlightthickness=0)
ButtonD7 = tk.Button(root, text='D7', image=black_wking, highlightthickness=0)
ButtonD8 = tk.Button(root, text='D8', image=black_wking, highlightthickness=0)

ButtonE1 = tk.Button(root, text='E1', image=black_wking, highlightthickness=0)
ButtonE2 = tk.Button(root, text='E2', image=white_wpawn, highlightthickness=0)
ButtonE3 = tk.Button(root, text='E3', image=black_wking, highlightthickness=0)
ButtonE4 = tk.Button(root, text='E4', image=black_wking, highlightthickness=0)
ButtonE5 = tk.Button(root, text='E5', image=black_wking, highlightthickness=0)
ButtonE6 = tk.Button(root, text='E6', image=black_wking, highlightthickness=0)
ButtonE7 = tk.Button(root, text='E7', image=black_wking, highlightthickness=0)
ButtonE8 = tk.Button(root, text='E8', image=black_wking, highlightthickness=0)

ButtonF1 = tk.Button(root, text='F1', image=white_wbishop, highlightthickness=0)
ButtonF2 = tk.Button(root, text='F2', image=black_wpawn, highlightthickness=0)
ButtonF3 = tk.Button(root, text='F3', image=black_wking, highlightthickness=0)
ButtonF4 = tk.Button(root, text='F4', image=black_wking, highlightthickness=0)
ButtonF5 = tk.Button(root, text='F5', image=black_wking, highlightthickness=0)
ButtonF6 = tk.Button(root, text='F6', image=black_wking, highlightthickness=0)
ButtonF7 = tk.Button(root, text='F7', image=black_wking, highlightthickness=0)
ButtonF8 = tk.Button(root, text='F8', image=black_wking, highlightthickness=0)


ButtonG1 = tk.Button(root, text='G1', image=black_wknight, highlightthickness=0)
ButtonG2 = tk.Button(root, text='G2', image=white_wpawn, highlightthickness=0)
ButtonG3 = tk.Button(root, text='G3', image=black_wking, highlightthickness=0)
ButtonG4 = tk.Button(root, text='G4', image=black_wking, highlightthickness=0)
ButtonG5 = tk.Button(root, text='G5', image=black_wking, highlightthickness=0)
ButtonG6 = tk.Button(root, text='G6', image=black_wking, highlightthickness=0)
ButtonG7 = tk.Button(root, text='G7', image=black_wking, highlightthickness=0)
ButtonG8 = tk.Button(root, text='G8', image=black_wking, highlightthickness=0)

ButtonH1 = tk.Button(root, text='H1', image=white_wrook, highlightthickness=0)
ButtonH2 = tk.Button(root, text='H2', image=black_wpawn, highlightthickness=0)
ButtonH3 = tk.Button(root, text='H3', image=black_wking, highlightthickness=0)
ButtonH4 = tk.Button(root, text='H4', image=black_wking, highlightthickness=0)
ButtonH5 = tk.Button(root, text='H5', image=black_wking, highlightthickness=0)
ButtonH6 = tk.Button(root, text='H6', image=black_wking, highlightthickness=0)
ButtonH7 = tk.Button(root, text='H7', image=black_wking, highlightthickness=0)
ButtonH8 = tk.Button(root, text='H8', image=black_wking, highlightthickness=0)

# These labels enumerate each column and row
LabelA = tk.Label(root, text='A', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 0)
LabelB = tk.Label(root, text='B', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 1)
LabelC = tk.Label(root, text='C', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 2)
LabelD = tk.Label(root, text='D', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 3)
LabelE = tk.Label(root, text='E', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 4)
LabelF = tk.Label(root, text='F', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 5)
LabelG = tk.Label(root, text='G', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 6)
LabelH = tk.Label(root, text='H', fg='black', bg='#ffeacd', padx=27).grid(row=9, column = 7)

Label1 = tk.Label(root, text='1', fg='black', bg='#ffeacd', pady=25).grid(row=8, column = 8)
Label2 = tk.Label(root, text='2', fg='black', bg='#ffeacd', pady=25).grid(row=7, column = 8)
Label3 = tk.Label(root, text='3', fg='black', bg='#ffeacd', pady=25).grid(row=6, column = 8)
Label4 = tk.Label(root, text='4', fg='black', bg='#ffeacd', pady=25).grid(row=5, column = 8)
Label5 = tk.Label(root, text='5', fg='black', bg='#ffeacd', pady=25).grid(row=4, column = 8)
Label6 = tk.Label(root, text='6', fg='black', bg='#ffeacd', pady=25).grid(row=3, column = 8)
Label7 = tk.Label(root, text='7', fg='black', bg='#ffeacd', pady=25).grid(row=2, column = 8)
Label8 = tk.Label(root, text='8', fg='black', bg='#ffeacd', pady=25).grid(row=1, column = 8)



buttons = []
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
for c in columns:
    for r in range(1, 9):
        eval("Button{0}{1}.grid(row={2}, column={3})".format(c, r, 9 - r, columns.index(c))) # Add squares to their positions on board
        eval("Button{0}{1}.configure(command=lambda: receive_input('{2}{3}'))".format(c, r, c, r)) # Each square (button) passes its position as a string into the receive_input function
        buttons.append(eval("Button{0}{1}".format(c, r))) # Create a list of buttons so they can be iterated over
        

# Create labels for game status updates and errors
Labelp1 = tk.Label(root, text='White \u2605', fg='black', bg='#ffeacd', font=("Calibri", 16))
Labelp2 = tk.Label(root, text='Black', fg='black', bg='#ffeacd', font=("Calibri", 16))
Labelgame_status = tk.Label(root, text='Choose white piece to move', fg='black', bg='#ffeacd', font=("Calibri", 16))
Labelerror = tk.Label(root, text='', fg='red', bg='#ffeacd', font=("Calibri", 16))
# Add them to the board
Labelp1.grid(row=0, column=0, columnspan=2)
Labelp2.grid(row=0, column=6, columnspan=2)
Labelgame_status.grid(row=0, column=2, columnspan=4)
Labelerror.grid(row=11, column=2, columnspan=4)


move_from, move_to = None, None # These will change when users click which piece they want to move and where they want to move it
def receive_input(square):
    """ Receives positional inputs as a string from buttons on GUI so pieces can be moved """
    global move_from, move_to
    if not move_from:   # This means that the user has just clicked the piece they want to move
        move_from = square
    else:               # The user has just clicked where they want to move the previously selected piece
        move_to = square
    update_game()

def receive_promote_input(piece_code, pawn):
    """ Receives promotional inputs as a string so pawn can be promoted to user selected piece """
    global promote_piece
    if piece_code == 'Q':
        promote_piece = 'Queen'
    elif piece_code == 'R':
        promote_piece = 'Rook'
    elif piece_code == 'K':
        promote_piece = 'Knight'
    else:
        promote_piece = 'Bishop'
    promote(pawn)

def update_game():
    """ Updates gamestate after piece/square is clicked """
    global move_from, move_to, cg
    backup = copy.deepcopy(cg)  # Deep copy of game is created, in case user moves into check
    update_gui(cg)
    if move_from and not move_to:  # User has selected piece to move but not where to move it
        from_place = cg.board.places.get(move_from)
        if from_place.piece is None: # User has selected an empty square
            Labelerror.configure(text='No piece here')
            move_from, move_to = None, None
            update_gui(cg)
        elif from_place.piece.color != ('White' if cg.turn == 1 else 'Black'): # User has selected an opponent's piece
            Labelerror.configure(text="Cant move opponent's piece")
            move_from, move_to = None, None
            update_gui(cg)
        else:
            Labelgame_status.configure(text='Where to move {0} {1}'.format(from_place.piece.color, from_place.piece.kind)) # User has selected a valid piece
    elif move_from and move_to: # User has selected piece to move and where to move it
        from_place = cg.board.places.get(move_from)
        gui_move(from_place.piece, move_to) # Moves pieces on the gui
        if cg.in_check(3 - cg.turn):
            Labelerror.configure(text="Can't move into check")
            cg = backup  # If player moves into check, which is illegal, game is restored to previous state of backup taken above
        move_from, move_to = None, None
        update_gui(cg)

def update_gui(game):
    """ Updates gui to reflect changes in gamestate """
    for c in columns:  # Update board to show piece posistions
        for r in range(1, 9):
            square = c + str(r)
            eval("Button{0}{1}.configure(image={2})".format(c, r, game.board.places[square].get_img()))

    if game.in_checkmate(game.turn):
        cm_text = ('Checkmate: {0} wins'.format('Black' if game.turn == 1 else 'White'))
        Labelgame_status.configure(text=cm_text, fg='Blue')
        for button in buttons: 
            button.configure(state='disabled') # Game is over, further actions disabled

    elif game.in_stalemate(game.turn):
        Labelgame_status.configure(text='Game over: stalemate', fg='Blue')
        for button in buttons:
            button.configure(state='disabled') # Game is over, further actions disabled

    elif game.in_check(game.turn):
        ch_text = ('{0} in check'.format('Black' if game.turn == 2 else 'White'))
        Labelgame_status.configure(text=ch_text)

    elif cg.turn == 1:
        Labelp1.configure(text='White \u2605') # Shows turn is white
        Labelp2.configure(text='Black')
        Labelgame_status.configure(text='Choose white piece to move')
    else:
        Labelp1.configure(text='White')
        Labelp2.configure(text='Black \u2605')  # Shows turn is black
        Labelgame_status.configure(text='Choose black piece to move')

def gui_move(piece, target_sq):
    """ Moves piece to square given by user on the GUI, captures piece if there is one, after checking if move is legal
    Also handles special cases, such as castling and En passant """
    global move_from, move_to
    if not piece:
        move_from, move_to = None, None
    elif piece.board.places[target_sq] not in piece.get_moves(True): # If player tries to make an illegal move
        Labelerror.configure(text="Illegal move")
    else:  
        new_place = piece.board.places[target_sq]  # Place object attained from user input
        if piece.kind == 'Pawn' and not new_place.piece and new_place.column != piece.place.column:  # Checks for and handles En passant captures
            piece.board.places[new_place.column + str(piece.place.row)].remove_piece()
        piece.place.move_piece() 
        new_place.remove_piece()  # Piece is captured, if relevant
        new_place.piece = piece  # Piece is moved
        piece.place = new_place
        
        if piece.kind == 'King' and piece.moved == False:  # Handles special case of castling
            row = str(1 if piece.color == 'White' else 8)
            if (target_sq == 'G1' and piece.color == 'White') or (target_sq == 'G8' and piece.color == 'Black'):
                piece.board.places['H' + row].piece.direct_move(piece.board.places['F' + row])
            elif (target_sq == 'C1' and piece.color == 'White') or (target_sq == 'C8' and piece.color == 'Black'):
                piece.board.places['A' + row].piece.direct_move(piece.board.places['D' + row])

        if piece.kind == 'Pawn':
            if piece.moved == False:  # Resets turns so pawn can be captured by En passant only on next turn
                piece.turns = 0
            if piece.place.row == (8 if piece.color == 'White' else 1): # Checking for pawn promotion
                promote(piece)
        if piece.kind == 'King' or piece.kind == 'Rook' or piece.kind == 'Pawn':  # King and rook can no longer castle, pawn can 
            piece.moved = True                                                   #   only move 2 squares on first turn
        for p in piece.board.white_pieces + piece.board.black_pieces:  # Incrementing turns for En passant captures
            p.turns += 1
        piece.board.game.turn = 3 - piece.board.game.turn  # Changes turn
        Labelerror.configure(text='')
        update_gui(piece.board.game) # GUI updated

promote_piece, ButtonQ, ButtonR, ButtonK, ButtonB = None, None, None, None, None
def promote(piece):
    """ Allows user to select which piece to promote pawn to """
    global promote_piece, ButtonQ, ButtonR, ButtonK, ButtonB
    if not promote_piece: # User has not yet chose which piece to promote pawn to
        col = piece.color.lower()[0]
        # Buttons added to allow user to pick what piece to promote to
        ButtonQ = tk.Button(root, text='A1', image=eval('white_{0}queen'.format(col)), highlightthickness=0, command=lambda: receive_promote_input('Q', piece))
        ButtonR = tk.Button(root, text='A2', image=eval('white_{0}rook'.format(col)), highlightthickness=0, command=lambda: receive_promote_input('R', piece))
        ButtonK = tk.Button(root, text='A3', image=eval('white_{0}knight'.format(col)), highlightthickness=0, command=lambda: receive_promote_input('K', piece))
        ButtonB = tk.Button(root, text='A4', image=eval('white_{0}bishop'.format(col)), highlightthickness=0, command=lambda: receive_promote_input('B', piece))
        ButtonQ.grid(column=9, row=3)
        ButtonR.grid(column=9, row=4)
        ButtonK.grid(column=9, row=5)
        ButtonB.grid(column=9, row=6)
        for button in buttons:
            button.configure(state='disabled') # Disables moves until promotion piece is selected
    else: # User has chosen which piece to promote to
        # Pawn removed, new piece added
        piece.place.remove_piece()
        new_piece = eval("{0}('{1}')".format(promote_piece, piece.color))
        new_piece.place, new_piece.board = piece.place, piece.board
        piece.place.piece = new_piece
        eval('piece.board.{0}_pieces.append(new_piece)'.format(piece.color.lower()))
        promote_piece = None
        
        # Buttons used to select promotion piece are removed
        ButtonQ.destroy()
        ButtonR.destroy()
        ButtonK.destroy()
        ButtonB.destroy()
        for button in buttons:
            button.configure(state='normal') # Moves re-enabled
        update_gui(cg)


cg = Game('w', 'b', Board()) # Creates game instance
update_gui(cg) # Sets pieces to their original positions
root.mainloop()