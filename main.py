import tkinter as tk
from tkinter import filedialog
from os.path import abspath, basename

window = tk.Tk()
window.title("simple Editor")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

# 함수 처리부
def open_text():
    filename = filedialog.askopenfilename(
        initialdir=abspath(__file__),
        title="골라 골라~",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
    )
    if not filename: return
    text_edit.delete("1.0", "end")
    with open(filename, 'r') as fs:
        text = fs.read()
        text_edit.insert("end", text)
    window.title(f'simple Editor - {basename(filename)}')

def save_as():
    filename = filedialog.asksaveasfilename(
        initialdir=abspath(__file__),
        title="저장",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*"))
    )
    if not filename: return
    with open(filename, 'w') as fs:
        text = text_edit.get("1.0", "end")
        fs.write(text)
    window.title(f'simple Editor - {basename(filename)}')

text_edit = tk.Text(window)
frm_btn = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_btn, text="open", command=open_text)
btn_save = tk.Button(frm_btn, text="save as", command=save_as)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_btn.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
