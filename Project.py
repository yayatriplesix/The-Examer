'''
This program can help you create the examination
How to use:
1.Enter the number of your question
2.Enter your question
3.Enter you answer choices
4.Enter the correct answer


Author : Yaya & Tonpho @ITKMITL
Last Modified Date : 14/12/2014 Time : 11:21 AM
Language : Python 2.7.8

'''
import Tkinter as tk
import tkMessageBox

class App:
    def __init__(self, root):
        tk.Label(root, text='Welcome To The Examer', font = "Helvetica 32 bold italic", fg = "red").grid(padx=20, pady=10)
        howto = 'How to use:\n1.Enter the number of your question\n2.Enter your question\n3.Enter you answer choices\n4.Enter the correct answer\n5.Do the test'
        tk.Label(root, text=howto, font = "Helvetica 14").grid(padx=20, pady=10)
        tk.Button(root, text='Begin!', command=self.start).grid(pady=10)

    def start(self):
        self.first = tk.Toplevel()
        self.first.resizable(True, True)
        tk.Label(self.first, text='Please Enter The Number of Your Question :', font = "Helvetica 14").grid(padx=20, pady=5)
        self.num = tk.IntVar()
        entry = tk.Entry(self.first, textvariable=self.num)
        entry.grid(pady=5)
        tk.Button(self.first, text='Create', command=self.question).grid(pady=5)
        
    def restart(self):
        self.root6.destroy()
        self.start()
        
    def again(self):
        self.root6.destroy()
        self.main_do_exam()
        
    def submit(self):
        if self.num_choice.get() == self.ans_list[self.j-1]:
            self.score += 1
        self.root4.destroy()
        self.root6 = tk.Toplevel()
        label1 = tk.Label(self.root6, text='Congratulation', font = "Helvetica 32 bold italic", fg = "red")
        score_label = tk.Label(self.root6, text='Your Score is : %d / %d' % (self.score, self.num.get()), font = "Helvetica 16 bold italic")
        label1.grid(padx = 100, pady = 20)
        score_label.grid(padx = 100, pady = 20)
        tk.Button(self.root6, text='Create New Test', command=self.restart).grid(row=3, pady=5)
        tk.Button(self.root6, text='Do the Exam Again', command=self.again).grid(row=4, pady=5)
               
    def sub_do_exam(self):
        if self.num_choice.get() == self.ans_list[self.j-1]:
            self.score += 1
        num = self.num.get()
        value = self.values.get()
        self.j += 1
        self.num_choice = tk.IntVar()
        next_button = tk.Button(self.root4, text='Next', command=self.sub_do_exam)
        submit_button = tk.Button(self.root4, text='Submit', command=self.submit)
        question_label = tk.Label(self.root4, text='%d.'%self.j+self.quest_list[self.j-1].get(), font='Helvetica 16 bold', width = 50, anchor='w')
        question_label.grid(sticky='W', row=0, column=0)
        for i in xrange(1, value+1):
            tk.Radiobutton(self.root4, text='(%d) : '% i+self.all_choice[self.j-1][i-1].get(), variable=self.num_choice, value=i, width = 50, anchor='w').grid(sticky='W', row=i, column=0, padx=10, pady=3)
        if self.j == len(self.quest_list):
            submit_button.grid(column=0, row=value+2)
        else:
            next_button.grid(column=0, row=value+2, pady=10)

        
    def main_do_exam(self):
        self.root5.destroy()
        self.root4 = tk.Toplevel()
        self.root4.resizable(True, True)
        num = self.num.get()
        value = self.values.get()
        self.score = 0
        self.j = 1
        self.num_choice = tk.IntVar()
        next_button = tk.Button(self.root4, text='Next', command=self.sub_do_exam) 
        question_label = tk.Label(self.root4, text='%d.'%self.j+self.quest_list[self.j-1].get(), font='Helvetica 16 bold', width = 50, anchor='w')
        question_label.grid(sticky='W', row=0, column=0)
        for i in xrange(1, value+1):
            tk.Radiobutton(self.root4, text='(%d) : '% i+self.all_choice[self.j-1][i-1].get(), variable=self.num_choice, value=i, width = 50, anchor='w').grid(sticky='W', row=i, column=0, padx=10, pady=3)
        next_button.grid(column=0, row=value+2, pady=10)
        
    
    def finish_create(self):
        self.ans_list.append(self.correct_choice.get())
        self.root3.destroy()
        self.root5 = tk.Toplevel()
        self.root5.resizable(True, True)
        label1 = tk.Label(self.root5, text='Your Examination are Ready to Use', font = "Helvetica 32 bold italic")
        label1.grid(pady = 100, padx = 300)
        do_exam_button = tk.Button(self.root5, text='Do the Exam Now !!!', font = "Helvetica 16 bold italic", fg = "red", command=self.main_do_exam)
        do_exam_button.grid(pady = 20, padx = 300)
        
    def sub_add_choice(self):
        self.ans_list.append(self.correct_choice.get())
        self.i += 1
        value = self.values.get()
        self.correct_choice = tk.IntVar(value='Select Answer')
        tk.Label(self.root3, width = 50, text=str(self.i)+'.'+self.quest_list[self.i-1].get()+' : ').grid(pady=3, row=0, columnspan=3)
        for i in xrange(value):
            self.choice_list.append('choice'+str(i))
        for j in xrange(1, value+1):
            self.choice_list[j-1] = tk.StringVar()
            tk.Label(self.root3, text='('+str(j)+') :').grid(pady=3, row = j+1, column=1)
            tk.Entry(self.root3, width=50, textvariable=self.choice_list[j-1]).grid(pady=3, padx=10, row = j+1, column=2)
        self.all_choice.append(self.choice_list)
        self.choice_list = []
        if value == 2:
            option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2)
        elif value == 3:
            option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2, 3)
        elif value == 4:
            option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2, 3, 4)
        elif value == 5:
            option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2, 3, 4, 5)
        option.grid(pady=3, column=2, row=value+2)
        button_next = tk.Button(self.root3, text='Next', command=self.sub_add_choice)
        button_submit = tk.Button(self.root3, text='Submit', command=self.finish_create)
        if self.i == len(self.quest_list):
            button_submit.grid(column=2, row=value+3)
        else:
            button_next.grid(column=2, row=value+3)

    def main_add_choice(self):
        try:
            self.root2.destroy()
            self.root3 = tk.Toplevel()
            self.root3.resizable(True,True)
            value = self.values.get()
            self.correct_choice = tk.IntVar(value='Select Answer')
            self.ans_list = []
            self.choice_list = []
            self.all_choice = []
            self.i = 1
            tk.Label(self.root3, width = 50, text=str(self.i)+'.'+self.quest_list[self.i-1].get()+' : ').grid(pady=3, row=0, columnspan=3)
            for i in xrange(value):
                self.choice_list.append('choice'+str(i))
            for j in xrange(1, value+1):
                self.choice_list[j-1] = tk.StringVar()
                tk.Label(self.root3, text='('+str(j)+') :').grid(pady=3, row = j+1, column=1)
                tk.Entry(self.root3, width=50, textvariable=self.choice_list[j-1]).grid(pady=3, padx=10, row = j+1, column=2)
            self.all_choice.append(self.choice_list)
            self.choice_list = []
            if value == 2:
                option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2)
            elif value == 3:
                option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2, 3)
            elif value == 4:
                option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2, 3, 4)
            elif value == 5:
                option = tk.OptionMenu(self.root3, self.correct_choice, 1, 2, 3, 4, 5)
            option.grid(pady=3, column=2, row=value+2)
            tk.Button(self.root3, text='Next', command=self.sub_add_choice).grid(column=2)
        except:
            tkMessageBox.Showerror(title='as;dlkjfa;sdkjfsd;f', message='a;sldkjf;aslkdjf')

    def choice(self):
        self.root1.destroy()
        self.root2 = tk.Toplevel()
        self.root2.resizable(True, True)
        tk.Label(self.root2, text='Please Enter The Number of Your Choices').grid(pady=5)
        self.values = tk.IntVar(value='Please Select')
        tk.OptionMenu(self.root2, self.values, 2, 3, 4, 5).grid(pady=2)
        tk.Button(self.root2, text='Submit', command=self.main_add_choice).grid(pady=5)
    def question(self):
        try:
            if self.num.get() == 1:
                raise ValueError

            self.first.destroy()
            self.root1 = tk.Toplevel()
            self.root1.resizable(True, True)
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
                entry.grid(row=(row*2)-1, column=col, padx=20)
                row += 1
                if i%10 == 0:
                    if num % 2 == 0:
                        col += 2
                    else:
                        col += 1
                    row = 1
            tk.Button(self.root1, text='Submit', command=self.choice).grid(columnspan = col + 1, pady = 5)
        except:
            tkMessageBox.showerror(title='Error', message='Plase select more than one')


root = tk.Tk()
app = App(root)
root.title('The Examer')
root.resizable(True,True)
root.mainloop()
