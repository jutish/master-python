from tkinter import *

ventana = Tk()
ventana.title('Frames en master Python')
ventana.geometry('600x600')

marco_padre1 = Frame(ventana,height=200,width=200)
# marco_padre1.config(bg = "yellow")
marco_padre1.pack(anchor = N, fill = X, expand = YES)

marco_padre2 = Frame(ventana,height=200,width=200)
# marco_padre2.config(bg = 'red')
marco_padre2.pack(anchor = S,fill = X, expand = YES)

# Marco 1
marco = Frame(marco_padre1, width = 200, height = 200)
marco.config(
	bg = 'orange', #Background
	bd = 5, #Border
	relief = SOLID
)
marco.pack(side = LEFT)
marco.pack_propagate(False) #Evita que cuando agrego el label, se achique el marco.
texto = Label(marco,text='Label Marco 1')
texto.config(bg="orange",fg="white")
texto.pack(fill=Y,expand=YES,anchor=CENTER) #Centro el Texto

#Marco2
marco = Frame(marco_padre1, width = 200, height = 200)
marco.config(
	bg = 'green', #Background
	bd = 5, #Border
	relief = SOLID
)
marco.pack(side = RIGHT)

#Marco 3
marco = Frame(marco_padre2, width = 200, height = 200)
marco.config(
	bg = 'yellow', #Background
	bd = 5, #Border
	relief = SOLID
)
marco.pack(side=LEFT)

#Marco 4
marco = Frame(marco_padre2, width = 200, height = 200)
marco.config(
	bg = 'pink', #Background
	bd = 5, #Border
	relief = SOLID
)
marco.pack(side = RIGHT)

ventana.mainloop()