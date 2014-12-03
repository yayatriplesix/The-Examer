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
Last Modified Date : 03/12/2014 Time : 03:40
Language : Python 2.7.8

'''
import Tkinter as tk
class App:
    def __init__(self, root):
        tk.Label(root, text='Please Enter The Number of Your Question :').grid()
        self.num = tk.IntVar()
        entry = tk.Entry(root, textvariable=self.num)
        entry.grid(pady=5)
        tk.Button(root, text='Create', command=self.question).grid(pady=5)
        
    def sub_add_choice(self):
        self.i += 1
        value = self.values.get()
        tk.Label(self.root3, width = 50, text=str(self.i)+'.'+self.quest_list[self.i-1].get()+' : ').grid(pady=3, row=0, columnspan=3)
        for j in xrange(1, value+1):
            tk.Label(self.root3, text='('+str(j)+') :').grid(pady=3, row = j+1, column=1)
            tk.Entry(self.root3, width=50).grid(pady=3, padx=10, row = j+1, column=2)
        button_next = tk.Button(self.root3, text='Next', command=self.sub_add_choice)
        button_submit = tk.Button(self.root3, text='Submit')
        if self.i == len(self.quest_list):
            button_submit.grid(column=2, row=value+2)
        else:
            button_next.grid(column=2, row=value+2)

    def main_add_choice(self):
        self.root2.destroy()
        self.root3 = tk.Toplevel()
        self.root3.resizable(True,True)
        value = self.values.get()
        self.i = 1
        tk.Label(self.root3, width = 50, text=str(self.i)+'.'+self.quest_list[self.i-1].get()+' : ').grid(pady=3, row=0, columnspan=3)
        for j in xrange(1, value+1):
            tk.Label(self.root3, text='('+str(j)+') :').grid(pady=3, row = j+1, column=1)
            tk.Entry(self.root3, width=50).grid(pady=3, padx=10, row = j+1, column=2)
        tk.Button(self.root3, text='Next', command=self.sub_add_choice).grid(column=2)

    def choice(self):
        self.root1.destroy()
        self.root2 = tk.Toplevel()
        self.root2.resizable(True, True)
        tk.Label(self.root2, text='Please Enter The Number of Your Choices').grid(pady=5)
        self.values = tk.IntVar(value='Please Select')
        tk.OptionMenu(self.root2, self.values, 2, 3, 4, 5).grid(pady=2)
        tk.Button(self.root2, text='Submit', command=self.main_add_choice).grid(pady=5)
        
    def question(self):
        self.root1 = tk.Toplevel()
        self.root1.resizable(True, True)
        self.root1.title('The-Examer')
        self.quest_list = []
        num = self.num.get()
        col = 0
        row = 1
        for j in xrange(1, num+1):
            self.quest_list.append('quest'+str(j))
        for i in xrange(1, num+1):
            self.quest_list[i-1] = tk.StringVar()
            tk.Label(self.root1, text='Please Enter Your Question %d :' % i).grid(pady=5, row=(row-1)*2, column=col)
            entry = tk.Entry(self.root1, width=50, textvariable=self.quest_list[i-1])
            entry.grid(row=(row*2)-1, column=col)
            row += 1
            if i%10 == 0:
                if num % 2 == 0:
                    col += 2
                else:
                    col += 1
                row = 1
        tk.Button(self.root1, text='Submit', command=self.choice).grid(columnspan = col + 1, pady = 5)


root = tk.Tk()
app = App(root)
root.title('The Examer')
root.resizable(True,True)
root.mainloop()
