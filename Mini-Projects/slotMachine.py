import random as rm

# Restrictions
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Number of rows and columns in the slot machine
ROWS = 3
COLUMNS = 3

# Possible symbols in each column in the slot machine
symbol_count = {
    "A": 2, "B": 4, "C": 6, "D": 8
}

# Value of each symbol in the slot machine
symbol_value = {
    "A": 4, "B": 3, "C": 2, "D": 1
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Adding all the available symbols from the symbol_count dictionary to the all_symbols list
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # Nested list which stores the symbols of all columns
    columns = []


    for _ in range(cols):
        # List which stores the symbols of each column
        column = []
        # A copy of all_symbols for choosing symbols fairly
        current_symbols = all_symbols[:]
        # Randomly choosing a symbol from current_symbols and appending it to the column list
        for _ in range(rows):
            value = rm.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        # Appending each column to the columns list
        columns.append(column)

    return columns

# Function to print the slot machine in a readable manner
def print_slot_machine(columns):
    print("----------\n|  SLOTS |\n----------")
    # Similar to transposing a matrix
    for row in range(len(columns[0])):
        # Enumerate provides the index and the value of a particular element
        for i, column in enumerate(columns):
            if i != len(columns) - 1: # Condition for the pipe (|) operator to only be present in between two values and not at the end
                print(column[row], end = " | ")
            else:
                print(column[row], end = " ")
        print()
    print("----------")

# Function to check if the user won anything (checking if all the columns in a line are same)
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = [] # List to store the lines the user won on
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Function to get the deposit amount from the player
def deposit():
    while True:
        amount = input("Enter the deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Invalid input! Try again.")
    
    return amount

# Function to get the number of bet lines from the user (within restrictions)
def get_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Lines must range from 1 to {MAX_LINES}!")
        else:
            print("Invalid input! Try again.")

    return lines

# Function to get the bet amount on each line from the user
def get_bet():
    while True:
        bet = input(f"Enter the bet on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must range from ${MIN_BET} to ${MAX_BET}!")
        else:
            print("Invalid input! Try again.")

    return bet

# Function which runs the slot machine
def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

# Function which handles the entire game
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to spin or 'Q' to quit. ").lower()
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

main()