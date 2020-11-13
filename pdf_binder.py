import PyPDF2
import tkinter as tk
import os.path
from os import path

def output():
    err_list = [path.exists(pdf_1_ent.get()),path.exists(pdf_2_ent.get())]
    err_list2 = []

    file_err_list=[path.exists(pdf_1_ent.get()),path.exists(pdf_2_ent.get())]
    file_err_list2 = []
    for i in range(0,2):
        if err_list[i]==False:
            err_list2.append(i)
    for i in range(0,2):
        if file_err_list[i]==False:
            file_err_list2.append(i)
    if len(err_list2) > 0 or len(file_err_list2) > 0:

        global test_variable
        err_var.set("A file or file path does not exist")

    else:
        try:
            print(pdf_1_ent.get() + "\n", pdf_2_ent.get() + "\n", pdf_3_ent.get() + "\n")
            pdf_1_file = open(pdf_1_ent.get(), 'rb')
            pdf_2_file = open(pdf_2_ent.get(), 'rb')
            pdf1Reader = PyPDF2.PdfFileReader(pdf_1_file)
            pdf2Reader = PyPDF2.PdfFileReader(pdf_2_file)
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf1Reader.numPages):
                page_obj = pdf1Reader.getPage(page_num)
                pdf_writer.addPage(page_obj)

            for page_num in range(pdf2Reader.numPages):
                page_obj = pdf2Reader.getPage(page_num)
                pdf_writer.addPage(page_obj)

            pdf_3_file = open(pdf_3_ent.get(), 'wb')
            pdf_writer.write(pdf_3_file)
            pdf_3_file.close()
            pdf_1_file.close()
            pdf_2_file.close()

            err_var.set("Output complete")
        except:
            err_var.set("An error occured :(")


main_window = tk.Tk()
main_window.title("Pdf Binder")
main_window.geometry("300x180")

err_var= tk.StringVar()
err_var.set("")

pdf_1_lbl = tk.Label(text="Pdf 1 file path:",width=40)
pdf_1_ent = tk.Entry()

pdf_2_lbl = tk.Label(text="Pdf 2 file path:",width=40)
pdf_2_ent = tk.Entry()

pdf_3_lbl = tk.Label(text="Binded pdf file path:",width=40)
pdf_3_ent = tk.Entry()

pdf_bind_btn = tk.Button(text="Bind files",command=output)

err_lbl = tk.Label(textvariable=err_var)

pdf_1_lbl.grid(column=1,row=0)
pdf_1_ent.grid(column=1,row=1)

pdf_2_lbl.grid(column=1,row=2)
pdf_2_ent.grid(column=1,row=3)

pdf_3_lbl.grid(column=1,row=4)
pdf_3_ent.grid(column=1,row=5)

pdf_bind_btn.grid(column=1,row=6)

err_lbl.grid(column=1,row=7)

main_window.mainloop()