from tkinter import *
from PIL import Image, ImageTk


def criar_imagem_com_transparencia():
    # Cria uma imagem RGBA com fundo transparente
    imagem = Image.new("RGBA", (165, 16), (0, 0, 0, 0))
    return ImageTk.PhotoImage(imagem)

root = Tk()
root.geometry("1400x1200")
root.title("Quiz")

canvas = Canvas(root, width=1400, height=1200, highlightthickness=0)
canvas.pack(fill=BOTH, expand=YES)

# Cria uma imagem com transparência
bg_transparente = criar_imagem_com_transparencia()

# Cria a Label com a imagem transparente
anal = Label(root, text="pergunta", image=bg_transparente, compound='center', foreground="#fff", width=165, height=16)
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
