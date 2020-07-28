import tkinter as tk

window = tk.Tk()
window.title('simple Editor')

#크기 변경하기
frm = tk.Frame(window, width=300, height=500)
frm.pack()

#텍스트 집어넣기
txt = tk.Label(window, text='Hi people')
txt.grid(row=0,column=0)

#버튼 집어넣기
btn = tk.Button(window, text='submit', width=15)
btn.grid(row=15,column=0)

window.mainloop()
