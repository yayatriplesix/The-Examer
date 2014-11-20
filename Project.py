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

eiei jubjub
'''
def question(num, quest):
    for i in xrange(num):
        quest_name = raw_input('Please Enter Your Question :\n')
        if quest_name == '_reset':
            reset()
        quest[quest_name] = 0
        choice = choice_func(input('Please Enter The Number of Your Choices :\n'), [])
        correct = input('Please Enter Your Correct Choice :\n')
        quest[quest_name] += correct
        print quest
        print choice

def choice_func(num, choice):
    for i in xrange(1, num+1):
        choice.append(raw_input('Enter Your Choice ' + '(' + str(i) + ') :\n'))
    return choice
def reset():
    question(input('Please Enter The Number of Your Question :\n'), {})

question(input('Please Enter The Number of Your Question :\n'), {})
