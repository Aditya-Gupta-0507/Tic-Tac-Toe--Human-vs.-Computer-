board = [' ' for x in range(10)]

def shabd_dalo(shabd, jagah):
    board[jagah] = shabd

def khali_jagah(jagah):
    return board[jagah] == ' '

def print_board(board):
    print()
    print(' ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('---+----+---')
    print(' ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('---+----+---')
    print(' ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print()

def kon_jeeta(board, shabd):
    return (board[7] == shabd and board[8] == shabd and board[9] == shabd) or (board[4] == shabd and board[5] == shabd and board[6] == shabd) or (board[1] == shabd and board[2] == shabd and board[3] == shabd) or (board[1] == shabd and board[4] == shabd and board[7] == shabd) or (board[2] == shabd and board[5] == shabd and board[8] == shabd) or (board[3] == shabd and board[6] == shabd and board[9] == shabd) or (board[1] == shabd and board[5] == shabd and board[9] == shabd) or (board[3] == shabd and board[5] == shabd and board[7] == shabd)

def khiladi_ki_chaal():
    chalao = True
    while chalao:
        chaal = input('Please \'X\' ke liye ek jagah type karein (1-9): ')
        try:
            chaal = int(chaal)
            if chaal > 0 and chaal < 10:
                if khali_jagah(chaal):
                    chalao = False
                    shabd_dalo('X', chaal)
                else:
                    print('Sorry, yah jagah bhari hui hai!')
            else:
                print('Please number ko is range ke andar hi dale!')
        except:
            print('Please ek number type karein!')


def computer_ki_chaal():
    chalne_ki_jagah = [x for x, shabd in enumerate(board) if shabd == ' ' and x != 0]
    chaal = 0

    for mano in ['O', 'X']:
        for i in chalne_ki_jagah:
            board_ki_copy = board[:]
            board_ki_copy[i] = mano
            if kon_jeeta(board_ki_copy, mano):
                chaal = i
                return chaal

    corner_kholo = []
    for i in chalne_ki_jagah:
        if i in [1,3,7,9]:
            corner_kholo.append(i)


    if len(corner_kholo) > 0:
        chaal = kuch_bhi_select_karo(corner_kholo)
        return chaal

    if 5 in chalne_ki_jagah:
        chaal = 5
        return chaal

    edge_kholo = []
    for i in chalne_ki_jagah:
        if i in [2,4,6,8]:
            edge_kholo.append(i)
            
    if len(edge_kholo) > 0:
        chaal = kuch_bhi_select_karo(edge_kholo)
        
    return chaal

def kuch_bhi_select_karo(li):
    import random
    lambai = len(li)
    kuch_bhi = random.randrange(0,lambai)
    return li[kuch_bhi]
    

def board_bhara_kya(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def jaruri_function():
    print('Tic Tac Toe game me aapka swagat hai!')
    print_board(board)

    while not(board_bhara_kya(board)):
        if not(kon_jeeta(board, 'O')):
            khiladi_ki_chaal()
            print_board(board)
        else:
            print('Sorry, is baar \'O\' jeet gaya !')
            break

        if not(kon_jeeta(board, 'X')):
            chaal = computer_ki_chaal()
            if chaal == 0:
                print('Arrey Game draw ho gaya bhai!')
            else:
                shabd_dalo('O', chaal)
                print('Computer ne \'O\' ko position', chaal , 'par rakha hai :')
                print_board(board)
        else:
            print('Bahut-Bahut Congratulations \'X\' jeet gaya! Good Job!')
            break

    if board_bhara_kya(board):
        print('Arrey Game Draw ho gaya bhai!')

while True:
    uttar = input('Dubara Kheloge ? (Y/N)')
    if uttar.lower() == 'y' or uttar.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------')
        jaruri_function()
        print('-----------------------')
    else:
        break