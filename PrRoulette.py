import random
import pprint
import sys

spin = 0
straight_ups = []
reds = []
blacks = []
evens = []
odds = []
low = []
high = []
first_column = []
second_column = []
third_column = []
first_dozen = []
second_dozen = []
third_dozen = []
streets = []
bankroll = 0

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

for i in range (0, 37):
    straight_ups.append(i)  # Straight up

    if i in [1, 3, 5, 7, 9, 12, 14, 16, 18,
             19, 21, 23, 25, 27, 30, 32, 34, 36]:
        reds.append(i)      # Red
    else:
        blacks.append(i)    # Black

for i in range(1, 37):
    if i % 2 == 0:
        evens.append(i)     # Even Numbers
    else:
        odds.append(i)      # Odd Numbers

for i in range(1, 37):
    if i < 18:
        low.append(i)       # Low Numbers
    else:
        high.append(i)      # High Numbers

for i in range(1, 35, 3):
    first_column.append(i)  # First Column

for i in range(2, 36, 3):
    second_column.append(i) # Second Column

for i in range(3, 37, 3):
    third_column.append(i)  # Third Column

for i in range(1, 37):
    if i < 12:
        first_dozen.append(i)   # First Dozen
    elif i > 12 and i < 25:
        second_dozen.append(i)  # Second Dozen
    else:
        third_dozen.append(i)   # Third Dozen

for i in range (1, 37, 3):
    
    streets.append(straight_ups[i:i+3]) # Nested Array of all
                                        # Eleven Streets (11:1)

def initial_print_board():

    print(initial_board)
  
def calculate(next_move):
            
    if next_move == '':
        spin_wheel_and_modify_board()
    elif next_move == 'leave':
        sys.exit()

    next_move = next_move.split(', ')

    temp_next_move = {}

    for i in range(len(next_move)):
        temp_next_move[next_move[i]] = i
        if list(temp_next_move.keys())[i][:6] == 'street':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][6:]
        if list(temp_next_move.keys())[i][:3] == 'odd':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][3:]
        if list(temp_next_move.keys())[i][:4] == 'even':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][4:]
        if list(temp_next_move.keys())[i][:4] == 'high':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][4:]
        if list(temp_next_move.keys())[i][:3] == 'low':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][3:]
        if list(temp_next_move.keys())[i][:9] == 'first_col':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][9:]
        if list(temp_next_move.keys())[i][:10] == 'second_col':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][10:]
        if list(temp_next_move.keys())[i][:9] == 'third_col':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][9:]
        if list(temp_next_move.keys())[i][:9] == 'first_doz':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][9:]
        if list(temp_next_move.keys())[i][:10] == 'second_doz':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][10:]
        if list(temp_next_move.keys())[i][:9] == 'third_doz':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][9:]
        if list(temp_next_move.keys())[i][:11] == 'straight_up':
            temp_next_move[next_move[i]] = list(temp_next_move.keys())[i][11:]

    bet_amount = list(temp_next_move.values())

    for i in range(len(bet_amount)):
        bet_amount[i] = int(bet_amount[i][1:-1])

    bet_amount = sum(bet_amount)

    if bet_amount > bankroll:
        print("That number is higher than your bankroll! Try again.")
        next_move = input()
        calculate(next_move)

    spin_wheel_and_modify_board()

def spin_wheel_and_modify_board():
    global spin
    spin = random.randint(0,36)

    temp_initial_board = list(initial_board)
    
    for i, o in number_dictionary.items():
        if str(o) == str(spin):
            temp_initial_board[i] = 'x'
            if spin > 9:
                temp_initial_board[i+1] = 'x'
        
    temp_initial_board = ''.join(temp_initial_board)

    print(temp_initial_board)
    print("""Instructions: Type the desired bet followed by what you're
willing to bet in parenthesis, followed by commas. For example:
first_column(20), third_column(20)

    Odds, Evens: odd(x), even(x) (1:1)
    High, Low: high(x), low(x) (1:1)
    First, Second, Third Column: first_col(x), second_col(x), third_col(x) (3:1)
    First, Second, Third Dozen: first_doz(x), second_doz(x), third_doz(x) (3:1)
    Straight Up: xx(x) (36:1)
    Street: (x, x) (11:1)

    For streets, enter which street (1 - 11) you would like to bet on,
    followed by your desired bet.

    Leave the text field blank for a free spin!
    Type 'leave' to close software.

""")
    print("\n" + "Winning Number: " + str(spin))
    print("Bankroll: " + str(bankroll) + "\n")

    global next_move
    next_move = input('Your move: ')

    calculate(next_move)


while bankroll == 0:        
    try:
        print("Enter the number of credits you want to play with\n")
        bankroll = int(input())
    except ValueError or NameError:
        print("This isn't a number\n")
    
spin_wheel_and_modify_board()
