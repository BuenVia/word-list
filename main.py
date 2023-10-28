from tkinter import *
import database
import datetime

def add_word():
    spa_text = spa_entry.get()
    eng_text = eng_entry.get()
    created_at = datetime.datetime.now()
    database.insert_word(spa_text, eng_text, created_at)

def show_all_words():
    row_index = 4
    print("---WORD LIST---")
    results = database.show_all_words()
    for result in results:
        print(f"{result}\n")
        result_label = Label(text=result, justify="left", anchor="w").grid(row=row_index)
        row_index += 1
        

database.create_tables()

tk = Tk()
tk.title("Word List")
tk.config(bg="#883399", padx=20, pady=20)

spa_label = Label(text="Spanish").grid(row=0)
eng_label = Label(text="English").grid(row=1)

spa_entry = Entry(width=100)
spa_entry.grid(row=0, column=1, padx=20, pady=20)

eng_entry = Entry(width=100)
eng_entry.grid(row=1, column=1, padx=20, pady=20)

add_btn = Button(text="Add", command=add_word).grid(row=2)

show_btn = Button(text="Show", command=show_all_words).grid(row=3)


tk.mainloop()