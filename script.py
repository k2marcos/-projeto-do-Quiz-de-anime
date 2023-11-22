from tkinter import *
from PIL import Image, ImageTk

imagem_path = "protagonistas.jpg"

def bg_Botao():
    imagem = Image.new("RGBA", (165, 16), (0,0,0,0))
    return ImageTk.PhotoImage(imagem)


root = Tk()
root.geometry("1400x1200")
root.title("Quiz")

imagem = Image.open(imagem_path)
imagem = imagem.resize((1400, 1100), Image.LANCZOS)
bg = ImageTk.PhotoImage(imagem)

canvas = Canvas(root, width=1400, height=1200)
canvas.pack(fill=BOTH, expand=YES)
canvas.create_image(0, 0, anchor=NW, image=bg)

anal = Label(root, text="pergunta", image=bg_Botao(), foreground="red", width=165, height=16, )
anal.place(x=140, y=250)

btn1 = Button(root, text="ale", width=55, height=3)
btn1.place(x=140, y=650)

btn2 = Button(root, text="stf", width=55, height=3)
btn2.place(x=140, y=850)

btn3 = Button(root, text="flv", width=55, height=3)
btn3.place(x=900, y=850)

btn4 = Button(root, text="cls", width=55, height=3)
btn4.place(x=900, y=650)

root.mainloop()
