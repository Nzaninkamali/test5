import tkinter as tk
from tkinter import messagebox

def button_click(button):
    global player
    if button["text"] == " " and player == "X":
        button["text"] = "X"
        player = "O"
    elif button["text"] == " " and player == "O":
        button["text"] = "O"
        player = "X"

    check_winner()

def check_winner():
    winning_combinations = [
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9],
        [button1, button4, button7],
        [button2, button5, button8],
        [button3, button6, button9],
        [button1, button5, button9],
        [button3, button5, button7]
    ]

    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != " ":
            for button in combo:
                button.config(bg="green")
            messagebox.showinfo("بازی دوز", f"بازیکن {combo[0]['text']} برنده شد!")
            reset_game()

def reset_game():
    global player
    player = "X"
    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    for button in buttons:
        button["text"] = " "
        button.config(bg="SystemButtonFace")

root = tk.Tk()
root.title("بازی دوز")

player = "X"

button1 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button1))
button1.grid(row=0, column=0)
button2 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button2))
button2.grid(row=0, column=1)
button3 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button3))
button3.grid(row=0, column=2)
button4 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button4))
button4.grid(row=1, column=0)
button5 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button5))
button5.grid(row=1, column=1)
button6 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button6))
button6.grid(row=1, column=2)
button7 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button7))
button7.grid(row=2, column=0)
button8 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button8))
button8.grid(row=2, column=1)
button9 = tk.Button(root, text=" ", font="Arial 20", height=3, width=6, command=lambda: button_click(button9))
button9.grid(row=2, column=2)

tk.Button(root, text="شروع مجدد", font="Arial 15", command=reset_game).grid(row=3, column=0, columnspan=3)

root.mainloop()
