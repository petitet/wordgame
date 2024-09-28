import random
import tkinter as tk
from tkinter import messagebox

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
attempts = 6

# Create the main window
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("400x400")

# Create a label to display instructions
instructions = tk.Label(root, text="Guess the 5-letter word!")
instructions.pack()

# Create an entry widget for user input
guess_entry = tk.Entry(root)
guess_entry.pack()

# Create a frame to hold the result boxes
result_frame = tk.Frame(root)
result_frame.pack()

# Create labels to display correct and incorrect letters
correct_spot_label = tk.Label(root, text="Correct spot: ")
correct_spot_label.pack()
wrong_spot_label = tk.Label(root, text="Wrong spot: ")
wrong_spot_label.pack()
not_in_word_label = tk.Label(root, text="Not in word: ")
not_in_word_label.pack()

# Create a label to display remaining attempts
attempts_label = tk.Label(root, text="Attempts remaining: 6")
attempts_label.pack()

# Function to check the guess
def check_guess():
    global attempts
    guess = guess_entry.get().upper()
    if len(guess) != 5:
        messagebox.showerror("Error", "Please enter a 5-letter word.")
        return
    
    # Clear previous result
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    correct_spot = []
    wrong_spot = []
    not_in_word = []
    for i in range(len(guess)):
        letter_label = tk.Label(result_frame, text=guess[i], width=2, height=1, font=('Helvetica', 18))
        if guess[i] == secret_word[i]:
            letter_label.config(bg='green', fg='white')  # Correct letter in the correct position
            correct_spot.append(guess[i])
        elif guess[i] in secret_word:
            letter_label.config(bg='yellow', fg='black')  # Correct letter in the wrong position
            wrong_spot.append(guess[i])
        else:
            letter_label.config(bg='grey', fg='white')  # Incorrect letter
            not_in_word.append(guess[i])
        letter_label.pack(side=tk.LEFT)
    
    correct_spot_label.config(text=f"Correct spot: {', '.join(correct_spot)}")
    wrong_spot_label.config(text=f"Wrong spot: {', '.join(wrong_spot)}")
    not_in_word_label.config(text=f"Not in word: {', '.join(not_in_word)}")
    
    if guess == secret_word:
        messagebox.showinfo("Congratulations!", "You've guessed the word correctly!")
        root.quit()
    else:
        attempts -= 1
        attempts_label.config(text=f"Attempts remaining: {attempts}")
        if attempts == 0:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The word was {secret_word}.")
            root.quit()

# Create a button to submit the guess
submit_button = tk.Button(root, text="Submit Guess", command=check_guess)
submit_button.pack()

# Run the application
root.mainloop()