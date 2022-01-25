from tkinter import *

root = Tk()

a1 = [0,0,0]
a2 = [0,0,0]
a3 = [0,0,0]
b1 = [0,0,0]
b2 = [0,0,0]
b3 = [0,0,0]


class but():

    count = 1

    def cknDnr(self):
        if but.count == 9:
            winLabel = Label(root, text = 'Game over').grid(row = 5, column = 1)
        elif  a1[0]+a2[0]+a3[0]==3 or a1[1]+a2[1]+a3[1]==3 or a1[2]+a2[2]+a3[2]==3:
            winLabel = Label(root, text = 'Saadat Own').grid(row = 5, column = 1)
        elif a1[0]+a2[1]+a3[2]==3 or a1[2]+a2[1]+a3[0]==3:
            winLabel = Label(root, text = 'Saadat Own').grid(row = 5, column = 1)
        elif sum(a1)==3 or sum(a2)==3 or sum(a3)==3:
            winLabel = Label(root, text = 'Saadat Own').grid(row = 5, column = 1)
        if b1[0]+b2[0]+b3[0]==6 or b1[1]+b2[1]+b3[1]==6 or b1[2]+b2[2]+b3[2]==6:
            winLabel = Label(root, text = 'Ru Own').grid(row = 5, column = 1)
        elif b1[0]+b2[1]+b3[2]==6 or b1[2]+b2[1]+b3[0]==6:
            winLabel = Label(root, text = 'Ru Own').grid(row = 5, column = 1)
        elif sum(b1)==6 or sum(b2)==6 or sum(b3)==6:
            winLabel = Label(root, text = 'Ru Own').grid(row = 5, column = 1)
    def myClick00(self):
        self.count+=1
        if self.count%2 == 0:
            self.button00 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 0, column = 0)
            a1[0] = 1
            self.cknDnr()
        else:
            self.button00 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 0, column = 0)
            b1[0] = 2
            self.cknDnr()
    def myClick01(self):
        self.count+=1
        if self.count%2 == 0:
            self.button01 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 0, column = 1)
            self.cknDnr()
            a1[1] = 1
        else:
            self.button01 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 0, column = 1)
            b1[1] = 2
            self.cknDnr()
    def myClick02(self):
        self.count+=1
        if self.count%2 == 0:
            self.button02 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 0, column = 2)
            a1[2] = 1
            self.cknDnr()
        else:
            self.button02 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 0, column = 2)
            b1[2] = 2
            self.cknDnr()


    def myClick10(self):
        self.count+=1
        if self.count%2 == 0:
            self.button10 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 1, column = 0)
            a2[0] = 1
            self.cknDnr()
        else:
            self.button10 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 1, column = 0)
            b2[0] = 2
            self.cknDnr()
    def myClick11(self):
        self.count+=1
        if self.count%2 == 0:
            self.button11 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 1, column = 1)
            a2[1] = 1
            self.cknDnr()
        else:
            self.button11 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 1, column = 1)
            b2[1] = 2
            self.cknDnr()
    def myClick12(self):
        self.count+=1
        if self.count%2 == 0:
            self.button12 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 1, column = 2)
            a2[2] = 1
            self.cknDnr()
        else:
            self.button12 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 1, column = 2)
            b2[2] = 2
            self.cknDnr()

    def myClick20(self):
        self.count+=1
        if self.count%2 == 0:
            self.button20 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 2, column = 0)
            a3[0] = 1
            self.cknDnr()
        else:
            self.button20 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 2, column = 0)
            b3[0] = 2
            self.cknDnr()
    def myClick21(self):
        self.count+=1
        if self.count%2 == 0:
            self.button21 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 2, column = 1)
            a3[1] = 1
            self.cknDnr()
        else:
            self.button21 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 2, column = 1)
            b3[1] = 2
            self.cknDnr()
    def myClick22(self):
        self.count+=1
        if self.count%2 == 0:
            self.button22 = Button(root, text = 'X', state = DISABLED, padx = 10, pady = 10, bg = 'Yellow').grid(row= 2, column = 2)
            a3[2] = 1
            self.cknDnr()
        else:
            self.button22 = Button(root, text = 'O', state = DISABLED, padx = 10, pady = 10, bg = 'Violet').grid(row= 2, column = 2)
            b3[2] = 2
            self.cknDnr()




    def __init__(self):

        self.button00 = Button(root, text = '', height = 10, width = 10, command = self.myClick00).grid(row= 0, column = 0)
        self.button01 = Button(root, text = '', height = 10, width = 10, command = self.myClick01).grid(row= 0, column = 1)
        self.button02 = Button(root, text = '', height = 10, width = 10, command = self.myClick02).grid(row= 0, column = 2)

        self.button10 = Button(root, text = '', height = 10, width = 10, command = self.myClick10).grid(row= 1, column = 0)
        self.button11 = Button(root, text = '', height = 10, width = 10, command = self.myClick11).grid(row= 1, column = 1)
        self.button12 = Button(root, text = '', height = 10, width = 10, command = self.myClick12).grid(row= 1, column = 2)

        self.button20 = Button(root, text = '', height = 10, width = 10, command = self.myClick20).grid(row= 2, column = 0)
        self.button21 = Button(root, text = '', height = 10, width = 10, command = self.myClick21).grid(row= 2, column = 1)
        self.button22 = Button(root, text = '', height = 10, width = 10, command = self.myClick22).grid(row= 2, column = 2)







but()
root.mainloop()
