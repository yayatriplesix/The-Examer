'''
This program can help you create the examination
How to use:
1.Enter the number of your question
2.Enter your question
3.Enter you answer choices
4.Enter the correct answer
You can reset your question by enter "_reset" in question
You can submit all of your question when you finish it by enter "_submit"

Author : Yaya & Tonpho @ITKMITL
Last Modified Date : 24/11/2014 Time : 14:50
Language : Python 2.7.8

'''
import Tkinter as tk
root = tk.Tk()
root.resizable(True, True)
##root.geometry('500x200')
root.title('The-Examer')
tk.Label(root, text='Please Enter The Number of Your Question :').grid()
num = tk.IntVar()
entry = tk.Entry(root, textvariable=num)
entry.grid(pady=5)
##space = tk.Label(root, text=" ")
##space.grid()


def question():
    root = tk.Tk()
    root.resizable(True, True)
##    root.geometry('500x200')
    root.title('The-Examer')
    quest = {}
    global num
    num = num.get()
    col = 0
    row = 1
    for i in xrange(1, num+1):
        quest_name = tk.StringVar()
        tk.Label(root, text='Please Enter Your Question %d :' % i).grid(pady=5, row=(row-1)*2, column=col)
        entry = tk.Entry(root, textvariable=quest_name)
        entry.grid(row=(row*2)-1, column=col)
        row += 1
        if i%10 == 0:
            if num % 2 == 0:
                col += 2
            else:
                col += 1
            row = 1
    tk.Button(root, text='Submit').grid(pady=5)


tk.Button(root, text='Create', command=question).grid(pady=5)

root.mainloop()
