import tkinter
window = tkinter.Tk()
button = tkinter.Button(window,text="押さないでね",width=40)
button.pack(padx=10,pady=10)
clickCount = 0

def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1 :
        button.configure(text="押さないでよ")
    elif clickCount == 2 :
        button.configure(text="次やったらボタンは消す")
    else:
        button.pack_forget()
        
button.bind("<ButtonRelease-1>",onClick)
window.mainloop()
