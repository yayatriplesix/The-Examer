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
class App:
    def __init__(self, root):
        tk.Label(root, text='Please Enter The Number of Your Question :').grid()
        self.num = tk.IntVar()
        entry = tk.Entry(root, textvariable=self.num)
        entry.grid(pady=5)
        tk.Button(root, text='Create', command=self.question).grid(pady=5)
    def main_add_choice(self):
        root3 = tk.Toplevel()
        root3.resizable(True,True)
        value = self.values.get()
        for i in xrange(1, self.num.get()+1):
            tk.Label(root3, text=str(i)+'.'+self.quest_list[i-1].get()+' : ').grid(pady=3)
            for j in xrange(1, value+1):
                tk.Label(root3, text='('+str(j)+') : ').grid(pady=3, column=1)
                tk.Entry(root3).grid(pady=3, column=2)

    def choice(self):
        root2 = tk.Toplevel()
        root2.resizable(True, True)
        tk.Label(root2, text='Please Enter The Number of Your Choices').grid(pady=5)
        self.values = tk.IntVar(value='Please Select')
        tk.OptionMenu(root2, self.values, 2, 3, 4, 5).grid(pady=2)
        tk.Button(root2, text='Submit', command=self.main_add_choice).grid(pady=5)
    def question(self):
        root1 = tk.Toplevel()
        root1.resizable(True, True)
        root1.title('The-Examer')
        self.quest_list = []
        num = self.num.get()
        col = 0
        row = 1
        for j in xrange(1, num+1):
            self.quest_list.append('quest'+str(j))
        for i in xrange(1, num+1):
            self.quest_list[i-1] = tk.StringVar()
            tk.Label(root1, text='Please Enter Your Question %d :' % i).grid(pady=5, row=(row-1)*2, column=col)
            entry = tk.Entry(root1, textvariable=self.quest_list[i-1])
            entry.grid(row=(row*2)-1, column=col)
            row += 1
            if i%10 == 0:
                if num % 2 == 0:
                    col += 2
                else:
                    col += 1
                row = 1
        tk.Button(root1, text='Submit', command=self.choice).grid(columnspan = col + 1, pady = 5)



root = tk.Tk()
app = App(root)
root.title('The Examer')
root.resizable(True,True)
root.mainloop()
