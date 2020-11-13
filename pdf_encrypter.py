import PyPDF2
import tkinter as tk
import os.path
from os import path

def output():
    if path.exists(pdf_path_ent.get()) == False:

        err_var.set("Error, given file path does not exist")
    else:
        try:
            pdf_file = open(pdf_path_ent.get(), "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))

            pdf_writer.encrypt(password_ent.get())
            output_pdf = open(pdf_out_ent.get(), "wb")
            pdf_writer.write(output_pdf)
            output_pdf.close()
            err_var.set("Output complete")
        except:
            err_var.set("An error occured :(")

mainwindow = tk.Tk()
mainwindow.title("Pdf Encrypter")
mainwindow.geometry("300x180")

err_var = tk.StringVar()
err_var.set("")
err_lbl = tk.Label(textvariable=err_var)

pdf_path_lbl = tk.Label(text="Enter pdf path",width=40)
pdf_path_ent = tk.Entry()

pdf_out_lbl = tk.Label(text="Enter pdf of encrypted pdf",width=40)
pdf_out_ent = tk.Entry()

password_lbl = tk.Label(text="Enter password",width=40)
password_ent = tk.Entry(show="*")

encrypt_button = tk.Button(text="Encrypt",command=output)

pdf_path_lbl.grid(column=1,row=1)
pdf_path_ent.grid(column=1,row=2)
pdf_out_lbl.grid(column=1,row=3)
pdf_out_ent.grid(column=1,row=4)
password_lbl.grid(column=1,row=5)
password_ent.grid(column=1,row=6)
encrypt_button.grid(column=1,row=7)
err_lbl.grid(column=1,row=8)

mainwindow.mainloop()
