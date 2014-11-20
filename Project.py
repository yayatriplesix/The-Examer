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
Last Modified Date : 20/11/2014 Time : 22:19
Language : Python 2.7.8

'''
import Tkinter as tk
root = tk.Tk()
root.geometry('500x200')
root.title('The-Examer')
tk.Label(root, text='Please Enter The Number of Your Question :').pack()
num = tk.IntVar()
entry = tk.Entry(root, textvariable=num)
entry.pack()



def question():
    root = tk.Tk()
    root.geometry('500x200')
    root.title('The-Examer')
    quest = {}
    global num
    num = num.get()
    for i in xrange(1, num+1):
        quest_name = tk.StringVar()
        tk.Label(root, text='Please Enter Your Question %d :' % i).pack()
        entry = tk.Entry(root, textvariable=quest_name)
        entry.pack()
    tk.Button(root, text='Submit').pack()
##        if quest_name == '_reset':
##            reset()
##        quest[quest_name.get()] = 0
##        choice = choice_func(input('Please Enter The Number of Your Choices :\n'), [])
##        correct = input('Please Enter Your Correct Choice :\n')
##        quest[quest_name.get()] += correct
##        print quest
##        print choice
        
##def choice_func(num, choice):
##    for i in xrange(1, num+1):
##        choice.append(raw_input('Enter Your Choice '+'('+str(i)+') :\n'))
##    return choice

##def reset():
##    question(input('Please Enter The Number of Your Question :\n'), {})

tk.Button(root, text='Create', command=question).pack()
##
##question(input('Please Enter The Number of Your Question :\n'), {})
root.mainloop()
