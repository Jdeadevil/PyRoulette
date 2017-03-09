import random
import pprint
import sys

bankroll = 0
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

def instructions(x):

    print("Enter the number of credits you want to play with\n")

    try:
        x = int(input())
    except ValueError or NameError:
        print("This isn't a number\n")
        instructions(bankroll)
  
def calculate(x):
    print('') # Literally just a placeholder for now

def spin_wheel_and_modify_board(x):
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
    print("Bankroll: " + str(x))

    next_move = input('Your move: ')

    calculate()
    if next_move == '':
        spin_wheel_and_modify_board()
    elif next_move == 'leave':
        sys.exit()


instructions(bankroll)
spin_wheel_and_modify_board(bankroll)
calculate(bankroll)
