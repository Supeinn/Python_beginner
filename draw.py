import tkinter
print("動かすには、マウスの左側のボタンをクリックしてください。")
print("筆の色を変えるには、どれか一つの色をクリックします")
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=750, height=530, bg="white")
canvas.pack()
lastx,lasty = 0,0
colour = "black"
def store_position(event):
    global lastx,lasty
    lastx = event.x
    lasty = event.y
def on_click(event):
    store_position(event)
def on_drag(event):
    canvas.create_line(lastx,lasty,event.x,event.y,fill=colour,width=3)
    store_position(event)
red_id = canvas.create_rectangle(10,10,30,30,fill="red")
blue_id = canvas.create_rectangle(10,35,30,55,fill="blue")
black_id = canvas.create_rectangle(10,60,30,80,fill="black")
white_id = canvas.create_rectangle(10,85,30,105,fill="white")
def set_colour_red(event):
    global colour
    colour = "red"
def set_colour_blue(event):
    global colour
    colour = "blue"
def set_colour_black(event):
    global colour
    colour = "black"
def set_colour_white(event):
    global colour
    colour = "white"
canvas.bind("<Button-1>",on_click)
canvas.bind("<B1-Motion>",on_drag)
canvas.tag_bind(red_id,"<Button-1>",set_colour_red)
canvas.tag_bind(blue_id,"<Button-1>",set_colour_blue)
canvas.tag_bind(black_id,"<Button-1>",set_colour_black)
canvas.tag_bind(white_id,"<Button-1>",set_colour_white)



window.mainloop()
    
    
