import random
import json
import csv
a=0
L1=[0]
L2=[0]
L3=[0]
def Fifthy(x,n):
    L1[0]=1
    global a
    p=1
    while p==1:
        A=Answer[x]
        m=random.randint(0,n)
        o=random.randint(0,n)
        M=Answer[m]
        N=Answer[o]
        if options.index(A)!=options.index(M):
            if options.index(A)!=options.index(N):
                if m!=o:
                    p=2
                    '''print(options.index(A))
                    print(options.index(M))
                    print(options.index(N))
                    print(m,n)'''
                    choices[x][options.index(M)]='DELETED'
                    choices[x][options.index(N)]='DELETED'
                    print('=========================================================================================================================================')       
                    print('question-',questions[x])
                    print('your options-',
                          'A)',choices[x][0],
                          'B)',choices[x][1],
                          'C)',choices[x][2],
                          'D)',choices[x][3])
                    option2=input('enter Your choice')
                    if option2==A:
                        print('correct')
                        a=1
                    else:
                        print('You lost')
                        print('Correct Option was',Answer[x])
                        a=0
def double_chance(x):
    L2[0]=1
    global a
    A=Answer[x]
    print('You now have two times to answer this question')
    option2=input('enter Your choice')
    if option2==A:
        print('correct')
        a=1
    else:
        print('You get Another Try')
        option2=input('enter Your choice')
        if option2==A:
            print('correct')
            a=1
        else:
            print('you lost')
            print('Correct Option was',Answer[x])
            a=0
def skip(x):
    L3[0]=1    
    global a
    a=1
    print('You have skipped this question')
    print('Correct Option was',Answer[x])
    
        
    
l=[]
questions1=[]
Answers1=[]
choices1=[]
choices=[]
options=['a','b','c','d','e']
with open ('geo.csv','r') as f:
    data=csv.reader(f)
    for row in data:
        #print(row)
        l.append(row)
        
questions1.append(l[0])
Answers1.append(l[2])
choices1.append(l[1])
#print(questions1)
questions=questions1[0]
Answer=Answers1[0]
choicesA=choices1[0]
#print(questions)
#print(Answer)
#print(choices)

choices.append(choicesA[0:5])
choices.append(choicesA[5:10])
choices.append(choicesA[10:15])
choices.append(choicesA[15:20])
#print(Choices)
Answer = [x[1:-1] for x in Answer]
#print(Answer)

def q1():
    global a
    n=len(questions)-1
    x=random.randint(0,n)
    print('question-',questions[x])
    print('your options-',
          'A)',choices[x][0],
          'B)',choices[x][1],
          'C)',choices[x][2],
          'D)',choices[x][3],
          'E)',choices[x][4])
    print('=========================================================================================================================================')
    option=input('Enter Your choice: ')
    A=Answer[x]
    if option.lower()==A:
        print('Your Entered option is correct')
        a=1
        questions.pop(x)
        choices.pop(x)
        Answer.pop(x)
    elif option.lower()=='e':
        Option_for_Lifeline=int(input('Enter The Option From the Lifelines: '))
        if Option_for_Lifeline==1:
            Fifthy(x,n)
            questions.pop(x)
            choices.pop(x)
            Answer.pop(x)
        elif Option_for_Lifeline==2:
            double_chance(x)
            questions.pop(x)
            choices.pop(x)
            Answer.pop(x) 
        elif Option_for_Lifeline==3:
            skip(x)
            questions.pop(x)
            choices.pop(x)
            Answer.pop(x)
    elif option not in options:
        print('Invalid Entry')
        a=0
    else:
        print('Wrong Answer')
        a=0
