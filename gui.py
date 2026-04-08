import tkinter as tk
from ai import best_move, check_winner, is_draw
from game import create_board

board = create_board()

def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i].config(text="X", fg="blue")

        if check_winner(board, "X"):
            status.config(text="You Win!")
            disable()
            return
        if is_draw(board):
            status.config(text="Draw!")
            return

        ai = best_move(board)
        board[ai] = "O"
        buttons[ai].config(text="O", fg="red")

        if check_winner(board, "O"):
            status.config(text="AI Wins!")
            disable()
        elif is_draw(board):
            status.config(text="Draw!")

def disable():
    for b in buttons:
        b.config(state="disabled")

def reset():
    global board
    board = create_board()
    for b in buttons:
        b.config(text=" ", state="normal")
    status.config(text="Your Turn")

def start_gui():
    global buttons, status

    root = tk.Tk()
    root.title("Tic Tac Toe AI")

    buttons = []
    for i in range(9):
        b = tk.Button(root, text=" ", font=("Arial", 20),
                      width=5, height=2,
                      command=lambda i=i: on_click(i))
        b.grid(row=i//3, column=i%3)
        buttons.append(b)

    status = tk.Label(root, text="Your Turn", font=("Arial", 14))
    status.grid(row=3, column=0, columnspan=3)

    tk.Button(root, text="Restart", command=reset).grid(row=4, column=0, columnspan=3)

    root.mainloop()