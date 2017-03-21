import random
import pprint
import sys
import re

spin = 0
next_move = ''

landed_on_dict = {
    'straight_up': list(range(37)),
    'red': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
    'black': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 21, 22, 24, 26, 28, 29, 31, 33, 35],
    'even': list(range(2, 37, 2)),
    'odd' : list(range(1, 37, 2)),     
    'low': list(range(19)),           
    'high': list(range(19, 37)),      
    'first_col': list(range(1, 35, 3)),
    'second_col': list(range(2, 36, 3)),
    'third_col': list(range(3, 37, 3)),
    'first_doz': list(range(1, 13)),
    'second_doz': list(range(13, 26)),
    'third_doz': list(range(26,37))
    }
street = []

for i in range (1, 37, 3):
    
    street.append(list(range(37))[i:i+3]) # Nested Array of all
                                        # Eleven Streets (11:1)

landed_on_dict['street'] = street

multiply_by_dict = {'straight_up': 35,
                    'red': 2,
                    'black': 2,
                    'even': 2,
                    'odd': 2,
                    'high':2,
                    'low': 2,
                    'first_col': 3,
                    'second_col': 3,
                    'third_col': 3,
                    'first_doz': 3,
                    'second_doz': 3,
                    'third_doz': 3,
                    'street': 11}
bankroll = 0

instructions = """Instructions: Type the desired bet followed by what you're
willing to bet in parenthesis, followed by commas. For example:
first_column(20), third_column(20)
    Odds, Evens: odd(x), even(x) (1:1)
    High, Low: high(x), low(x) (1:1)
    First, Second, Third Column: first_col(x), second_col(x), third_col(x) (3:1)
    First, Second, Third Dozen: first_doz(x), second_doz(x), third_doz(x) (3:1)
    Straight Up: (x-x) (36:1)
    Street: (x-x) (11:1)
    For streets, enter which street you would like to bet on,
    followed by your desired bet.
    Leave the text field blank for a free spin!
    Type 'leave' to close software.
"""

initial_board = """     -------------------------------------- 
    | |3|6|9|12|15|18|21|24|27|30|33|36|3rd|
    | -------------------------------------|
    |0|2|5|8|11|14|17|20|23|26|29|32|35|2nd|
    | -------------------------------------|
    | |1|4|7|10|13|16|19|22|25|28|31|34|1st|
     -------------------------------------- 
      |  1st 12  |  2nd 12  |  3rd 12  |
      ----------------------------------
      |  1-18|Even|Red|Black|Odd|19-36 |
       -------------------------------- """

number_dictionary = {52: '3', 54: '6', 56: '9', 58: '12', 61: '15', 64: '18',
                     67: '21', 70: '24', 73: '27', 76: '30', 79: '33', 82: '36',
                     140: '0', 142: '2', 144: '5', 146: '8', 148: '11', 151: '14',
                     154: '17', 157: '20', 160: '23', 163: '26', 166: '29',
                     169: '32', 172: '35', 232: '1', 234: '4', 236: '7', 238: '10',
                     241: '13', 244: '16', 247: '19', 250: '22', 253: '25', 256: '28',
                     259: '31', 262: '34'}

def initial_print_board():

    print(initial_board)
  
def calculate(next_move, bankroll):
            
    if next_move == '':
        spin_wheel_and_modify_board(bankroll)
    elif next_move == 'leave':
        sys.exit()

    next_move = next_move.split(',')

    temp_next_move = {}

    try:
        for i in range(len(next_move)):
            formatRegex = re.compile(r'(\w+)(\(\d+\))|(\w+)(\(\d+-\d+\))')
            mo = formatRegex.search(next_move[i])
            mo_single_name = mo.group(1)
            mo_single_format = mo.group(2)
            mo_double_name = mo.group(3)
            mo_double_format = mo.group(4)
            if mo_single_format == None:
                temp_next_move[mo_double_name] = mo_double_format.strip('()')
            elif mo_double_format == None:
                temp_next_move[mo_single_name] = mo_single_format.strip('()')
    except AttributeError:
        print("Move not recognised, try typing your move in again in.")
        next_move = input()
        calculate(next_move, bankroll)        

    bet_amount = list(temp_next_move.values())

    for i in range(len(temp_next_move)):
        if bet_amount[i].find('-') != -1:
            bet_amount[i] = bet_amount[i][bet_amount[i].find('-')+1:]
        bet_amount[i] = int(bet_amount[i])
            
    for bet_name, bet_placed in temp_next_move.items():
        if bet_placed.find('-') > -1:         
            dashIndex = bet_placed.find('-')
            temp_next_move[bet_name] = temp_next_move[bet_name][:dashIndex]           
            
    for name, sList in landed_on_dict.items():
        if name != 'street' and name != 'straight_up':
            if name in temp_next_move.keys():
                if spin in landed_on_dict[name]:
                    bankroll += (int(temp_next_move[name]) * multiply_by_dict[name])
        elif name == 'street':
            dashIndex = bet_placed.find('-')
            if name in temp_next_move.keys():
                if spin in landed_on_dict[name][:dashIndex]:
                    bankroll += (int(temp_next_move[name][dashIndex+1:]) * multiply_by_dict[name])
        elif name == 'straight_up':
            dashIndex = bet_placed.find('-')
            if name in temp_next_move.keys():
                if temp_next_move[name][:dashIndex] == spin:
                    bankroll += (int(temp_next_move[name][dashIndex+1:]) * multiply_by_dict[name])
                
                    
                   
    if sum(bet_amount) > bankroll:
        print("That number is higher than your bankroll! Try again.")
        next_move = input()
        calculate(next_move)
    else:
        global x
        x = bankroll
        x -= sum(bet_amount)
        return bankroll
    # Example Move: high(10), low(20), street(20-100)
    
def spin_wheel_and_modify_board(bankroll):
    global spin
    spin = random.randint(0,36)

    temp_initial_board = list(initial_board)
    
    for i, o in number_dictionary.items():
        if str(o) == str(spin):
            temp_initial_board[i] = 'x'
            if spin > 9:
                temp_initial_board[i+1] = 'x'
        
    temp_initial_board = ''.join(temp_initial_board)

    global next_move
    next_move = input('Your move: ')

    try:
        print(temp_initial_board)
        print(instructions)
        print("\n" + "Winning Number: " + str(spin))
    except TypeError:
        print("Move not recognised, try typing your move in again in.")
        next_move = input()
        spin_wheel_and_modify_board(bankroll)

    calculate(next_move, bankroll)

    print("Bankroll: " + str(x) + "\n")

while bankroll == 0:        
    try:
        print("Enter the number of credits you want to play with\n")
        bankroll = int(input())
    except ValueError or NameError:
        print("This isn't a number\n")

print(instructions)

while next_move != 'leave':
    spin_wheel_and_modify_board(bankroll)
    bankroll = x
