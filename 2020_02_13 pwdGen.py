import string
import random
spec = list(['!','@','#','$','%','^','&','*','-','=','+'])

def picksmletter():
    letter = list(string.ascii_lowercase)
    letter.remove('i')
    letter.remove('l')
    letter.remove('o')
    return random.choice(letter)

def pickupletter():
    letter = list(string.ascii_uppercase)
    letter.remove('I')
    letter.remove('L')
    letter.remove('O')
    return random.choice(letter)

def picknum():
    num = list(string.digits)
    num.remove('1')
    num.remove('0')
    return random.choice(num)

def pickspec():
    return random.choice(spec)

def passgen(plen, uletter=1, num=1, spec=1):
    res = str()

    if plen >= 30:
        return str('Choose a shorter password length')

    res = res + pickupletter()

    pos = list(range(1,plen))

    uppos = random.choice(pos)
    pos.remove(uppos)
    
    numpos = random.choice(pos)
    pos.remove(numpos)
    
    specpos = random.choice(pos)
    pos.remove(specpos)

    for i in range(1,plen):
        if (i == uppos): res = res + pickupletter()
        elif i == numpos: res = res + picknum()
        elif i == specpos: res = res + pickspec()
        else: res = res + picksmletter()
        if res[i].lower == res[i-1].lower:
            res[:-1]
            res = res + picksmletter()

    return res


class GUI():

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack()

        self.plen = tk.IntVar()
        self.plen.set(20)

        self.result = tk.StringVar()
        self.result.set('')

        self.label = tk.Label(self.frame, text='How long do you want the password to be?')
        self.label.pack()
        self.number = tk.Entry(self.frame, text=self.plen, textvariable=self.plen)
        self.number.pack()


        self.calc = tk.Button(self.frame, text='Generate', command = self.click)
        self.calc.pack()

        self.end = tk.Button(self.frame, text='Close', command = self.quit)
        self.end.pack()

        self.label = tk.Label(self.frame, text = 'Generated Password:')
        self.label.pack()
        
        self.label = tk.Entry(self.frame, width=100, textvariable = self.result)
        self.label.pack()

    def click(self):
        self.result.set(passgen(self.plen.get()))

    def quit(self):
        self.parent.destroy()



if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    window.geometry("300x250")
    myapp = GUI(window)
    window.mainloop()
