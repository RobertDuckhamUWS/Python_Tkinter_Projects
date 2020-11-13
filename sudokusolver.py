import tkinter as tk
import random

window = tk.Tk()
window.title("Sudoku solver")

row_count = 0
column_count=0

var_list = []
num_count = 0
con_list = [None,None,None]
var_loc_list = []

loc = 0
test_var = "0"
inc_count = 0

err_var = tk.StringVar()

for i in range(0,81):
    var = tk.StringVar()
    var_list.append(var)

def numbers():
    var_list[0].set("5")
    var_list[1].set("6")
    var_list[3].set("8")
    var_list[4].set("4")
    var_list[5].set("7")
    var_list[9].set("3")
    var_list[11].set("9")
    var_list[15].set("6")
    var_list[20].set("8")
    var_list[28].set("1")
    var_list[31].set("8")
    var_list[34].set("4")
    var_list[36].set("7")
    var_list[37].set("9")
    var_list[39].set("6")
    var_list[41].set("2")
    var_list[43].set("1")
    var_list[44].set("8")
    var_list[46].set("5")
    var_list[49].set("3")
    var_list[52].set("9")
    var_list[60].set("2")
    var_list[65].set("6")
    var_list[69].set("8")
    var_list[71].set("7")
    var_list[75].set("3")
    var_list[76].set("1")
    var_list[77].set("6")
    var_list[79].set("5")
    var_list[80].set("9")


def test_cmd():
    global var_loc_list
    for i in range(0,81):
        if var_list[i].get() != "1" or var_list[i].get() != "2" or var_list[i].get() != "3" or var_list[i].get() != "4" or var_list[i].get() != "5" or var_list[i].get() != "6" or var_list[i].get() != "7" or var_list[i].get() != "8" or var_list[i].get() != "9":
            err_var.set("")
            err_var.set("Error, invalid input")

    for i in range(0, 81):
        if var_list[i].get() != "":
            var_loc_list.append(i)
    while True:
        global loc
        global test_var
        global inc_count
        if loc == 81:
            err_var.set("")
            err_var.set("sudoku solved")

            break

        test_var = str(int(test_var) + 1)
        hor_col_cmd()
        vert_col_cmd()
        box_cmd()
        print(con_list, "var:"+test_var,"loc:"+str(loc))
        if int(test_var) > 9:
            var_list[loc].set("")
            loc -= 1
            #problem, maybe fix with while loop
            while loc in var_loc_list and loc > 0:
                loc -= 1

            test_var = str(int(var_list[loc].get()))

        if False in con_list:
            continue

        if con_list == [True,True,True]:
            var_list[loc].set(test_var)
            loc += 1
            #problem maybe fix with while loop
            while loc in var_loc_list and loc > -1:
                loc += 1
            test_var = "0"

def hor_col_cmd():
    horz_var_list = []
    check_horz_var_list = []
    loc2 = loc
    for i in range(0,9):
        loc2 += 9
        if loc2 > 80:
            break

        horz_var_list.append(var_list[loc2])


    loc2 = loc
    for i in range(0,9):
        loc2 -= 9
        if loc2 < 0:
            break

        horz_var_list.append(var_list[loc2])


    for i in range(0,8):
        check_horz_var_list.append(horz_var_list[i].get())
    #print(check_horz_var_list)

    if test_var in check_horz_var_list or int(test_var) > 9:
        con_list[0] = False
    else:
        con_list[0] = True
def vert_col_cmd():
    vert_var_list = []
    check_vert_var_list = []
    loc2 = loc
    upper_limit = 0

    for i in range(0,9):
        loc2 += 1
        if loc2 % 9 == 0:
            upper_limit = loc2
            break

        vert_var_list.append(var_list[loc2])


    loc2 = loc
    for i in range(0,9):
        loc2 -= 1
        if loc2 == upper_limit - 10:
            break

        vert_var_list.append(var_list[loc2])

    for i in range(0,8):
        check_vert_var_list.append(vert_var_list[i].get())
    #print(check_vert_var_list)


    if test_var in check_vert_var_list or int(test_var) > 9:
        con_list[1] = False
    else:
        con_list[1] = True
def box_cmd():
    box_list = []
    check_box_list = []
    boxes = [[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23],
             [6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47],
             [30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53],
             [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77],
             [60, 61, 62, 69, 70, 71, 78, 79, 80]]
    for list in boxes:
        for element in list:
            if element == loc:
                for element in list:
                    if element != loc:
                        box_list.append(var_list[element])

    for i in range(0,8):
        check_box_list.append(box_list[i].get())
    #print(check_box_list)

    if test_var in check_box_list or int(test_var) > 9:
        con_list[2] = False
    else:
        con_list[2] = True


for i in range(0,len(var_list)):

    tk.Entry(width=5,textvariable=var_list[i]).grid(column=column_count,row=row_count)
    row_count += 1
    if row_count > 8:
        row_count = 0
        column_count += 1
button = tk.Button(text="solve",command=test_cmd).grid(column=4,row=9,columnspan=2)
button1 = tk.Button(text="puzzle",command=numbers).grid(column=2,row=9,columnspan=2)
err_lbl = tk.Label(textvariable=err_var).grid(column=1,row=10,columnspan=5)


window.mainloop()