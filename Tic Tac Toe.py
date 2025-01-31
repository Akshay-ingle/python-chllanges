board={'7': ' ', '8': ' ', '9': ' ',
       '4': ' ', '5': ' ', '6': ' ',
       '1': ' ', '2': ' ', '3': ' '}

board_key=[]

for key in board :
    board_key.append(key)
def print_board(theboard):
    print(theboard['7']+'|'+theboard['8']+'|'+theboard['9'])
    print('-+-+-')           
    print(theboard['4']+'|'+theboard['5']+'|'+theboard['6'])
    print('-+-+-') 
    print(theboard['1']+'|'+theboard['2']+'|'+theboard['3'])
def game():
    ten='X'
    count=0
                   