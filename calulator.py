import tkinter as tk
from math import *

answer="NULL"

def calculate():
    try:
        res_lbl.configure(text="Output: " + str(eval(eqn_ent.get())))
        global answer
        answer = str(eval(eqn_ent.get()))
    except:
        eqn_ent.delete(0, len(eqn_ent.get()))
        eqn_ent.insert(0, "Syntax error")

def insert_sqr_brk_left():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"[")


def insert_sqr_brk_right():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"]")

def insert_comma():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,",")
def insert_del():
    eqn_ent.delete(len(eqn_ent.get())-1,len(eqn_ent.get()))

def insert_sin():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"sin(")

def insert_cos():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"cos(")

def insert_tan():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"tan(")

def insert_log10():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"log10(")

def insert_exp():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"exp(")

def insert_logx():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "log([,")

def insert_pow():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "pow(,")

def insert_sqrt():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "sqrt(")

def insert_clear():
    eqn_ent.delete(0,len(eqn_ent.get()))

def insert_left_bracket():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "(")

def insert_right_bracket():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, ")")

def insert_divide():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "/")

def insert_seven():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "7")

def insert_eight():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "8")

def insert_nine():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len,"9")

def insert_multi():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "*")

def insert_four():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "4")

def insert_five():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "5")

def insert_six():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "6")

def insert_minus():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "-")

def insert_one():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "1")

def insert_two():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "2")

def insert_three():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "3")

def insert_plus():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "+")

def insert_zero():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, "0")

def insert_point():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, ".")
def insert_answer():
    insrt_len = len(eqn_ent.get())
    eqn_ent.insert(insrt_len, answer)
window = tk.Tk()
window.title("Calculator")
window.geometry("170x280")

eqn_lbl = tk.Label(text="Enter: ")
eqn_ent = tk.Entry()

text = ["[","]","DEL",",","sin()","cos()","tan()","log10","exp()","log([])","pow","sqrt","CLR","(",")",
        "/","7","8","9","*","4","5","6","-","1","2","3","+","0",".","ANS","="
        ]
command = ["insert_sqr_brk_left","insert_sqr_brk_right","insert_del","insert_comma","insert_sin",
           "insert_cos","insert_tan","insert_log10","insert_exp","insert_logx","insert_pow","insert_sqrt",
           "insert_clear","insert_left_bracket","insert_right_bracket","insert_divide","insert_seven","insert_eight",
           "insert_nine","insert_multi","insert_four","insert_five","insert_six","insert_minus","insert_one",
           "insert_two","insert_three","insert_plus","insert_zero","insert_point","insert_answer","calculate"]
row_var = 2
col_var = 0

tk.Label(window, text="Enter: ").grid(row=0,column=0,columnspan=4)
eqn_ent_grid = eqn_ent.grid(row=1,column=0,columnspan=4)
res_lbl = tk.Label(text="Output: ")

for i in range(0,len(text)):
    if col_var == 3:
        tk.Button(text=text[i],command=eval(command[i])).grid(column=col_var,row=row_var,sticky=tk.NSEW)
        col_var = 0
        row_var += 1
    else:
        tk.Button(text=text[i], command=eval(command[i])).grid(column=col_var, row=row_var,sticky=tk.NSEW)
        col_var += 1

res_lbl_grid = res_lbl.grid(row=10,column=0,columnspan=4)

window.mainloop()