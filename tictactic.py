import tkinter as tk
from tkinter import messagebox
board=[""]*9
player="😊"
def winning():
    wc=[(0,1,2),(3,4,5) ,(6,7,8), (0,3,6) ,(1,4,7) ,(2,5,8) ,(0,4,8),(2,4,6)]
    for a,b,c in wc:
        if board [a]==board[b]==board[c]!="":
            return board[a]
    if "" not in board:
        return "Draw"
    return None
def onclick(i):
    global player
    if board [i]=="" and not winning():
        board [i]=player
        allbuttons [i].config(text=player)
        if winning():
            if winning()=="Draw":
                messagebox.showinfo("Tictactoe","Draw Match")
            else:
                messagebox.showinfo("Tictactoe",f"Player {winning()} wins" )
        if player=="😊":
            player="👿"
        else:
            player="😊"
def resetboard():
    global player,board
    board=[""]*9
    player="😊"
    for i in allbuttons:
        i.config(text="")



    

 










root=tk.Tk()
root.title("Welcome to Tictacto")
allbuttons=[]
for i in range (9):
    x_or_o=tk.Button(root,text="",font=("Goudy Stout",20),width=5,height=3,command=lambda i=i:onclick(i))
    x_or_o.grid(row=i//3,column=i%3)
    allbuttons.append(x_or_o)
reset=tk.Button(root,text="Reset Game",font=("Impact",20),width=13,height=3,command=resetboard)
reset.grid(row=4,column=1)




root.mainloop()