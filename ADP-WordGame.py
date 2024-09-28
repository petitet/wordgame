import random

# Custom list of five-letter words
# word_list = ['APPLE', 'BERRY', 'CHERRY', 'DATES', 'ELDER']
word_list = [
    'AUDIT', 'ALLOW', 'ADMIN', 'APPLY', 'ALIGN',
    'BONUS', 'BATCH', 'BILLS', 'BREAK', 'BENCH',
    'CHECK', 'CLOCK', 'CLAIM', 'COUNT', 'CODES',
    'DEDUCT', 'DRAFT', 'DUES', 'DAILY', 'DELAY',
    'EARNS', 'ENTRY', 'EXEMPT', 'EXTRA', 'EFILE',
    'FILER', 'FORMS', 'FIXED', 'FINES', 'FLOAT',
    'GROSS', 'GRANT', 'GOALS', 'GUIDE', 'GROUP',
    'HOURS', 'HIRED', 'HUMAN', 'HONOR', 'HASTE',
    'INPUT', 'ISSUE', 'INDEX', 'INCUR', 'INPAY',
    'JOINT', 'JOBS', 'JUDGE', 'JIFFY', 'JUMPS',
    'KEYED', 'KIOSK', 'KNOWN', 'KEEPS', 'KINDS',
    'LEAVE', 'LABOR', 'LOANS', 'LIMIT', 'LEDGER',
    'MATCH', 'MERIT', 'MONEY', 'MONTH', 'MEMOS',
    'NETED', 'NEEDS', 'NOTES', 'NAMED', 'NICHE',
    'ORDER', 'OPTED', 'OWING', 'OFFER', 'ONSET',
    'PAYEE', 'PRINT', 'PLANS', 'POSTS', 'PAYER',
    'QUOTA', 'QUERY', 'QUICK', 'QUALS', 'QUIET',
    'RATES', 'RECUR', 'RAISE', 'REIMB', 'ROLES',
    'SHIFT', 'STAFF', 'SALES', 'STOCK', 'SCHED',
    'TAXES', 'TRACK', 'TOTAL', 'TERMS', 'TRUST',
    'UNION', 'USERS', 'UNPAID', 'UNITS', 'UPSET',
    'VALUE', 'VOUCH', 'VALID', 'VAULT', 'VOTES',
    'WAGES', 'WORKS', 'WRITE', 'WORTH', 'WORRY',
    'XEROX', 'XRATE', 'XPERT', 'XPATH', 'XPORT',
    'YIELD', 'YEARN', 'YOKED', 'YARDS', 'YOUTH',
    'ZONAL', 'ZIPPY', 'ZONED', 'ZEALS', 'ZESTS'
]



# Choose a random word from the list
secret_word = random.choice(word_list)

# Function to check the guess
def check_guess(guess, secret_word):
    result = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result.append('🟩')  # Correct letter in the correct position
        elif guess[i] in secret_word:
            result.append('🟨')  # Correct letter in the wrong position
        else:
            result.append('⬜')  # Incorrect letter
    return ''.join(result)

# Main game loop
def play_game():
    attempts = 6
    print("Welcome to ADP Word Game!")
    print("Guess the 5-letter word.")
    
    while attempts > 0:
        guess = input("Enter your guess: ").upper()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        result = check_guess(guess, secret_word)
        print(result)
        
        if guess == secret_word:
            print("Congratulations! You've guessed the word!")
            break
        
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was {secret_word}.")

# Start the game
play_game()
