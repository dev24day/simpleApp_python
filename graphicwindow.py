import tkinter as tk

window = tk.Tk()
window.title("simple Editor")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

text_edit = tk.Label(window)
frm_btn = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_btn, text="open")
btn_save = tk.Button(frm_btn, text="save as")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_btn.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
