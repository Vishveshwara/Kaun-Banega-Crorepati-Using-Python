print('========================================================WELCOME TO KAUN BANEGA CROREPATI=================================================')
print('Rules:')
print('#There are a total of 16 questions from 4 topics(Science,Sports,History and Geography) in this quiz.                                     ')
print('#There are 3 lifelines(50/50,Double Chance and Skip)which will help you win but can be used only once each.                              ')
print('#You are guaranteed some money if you lose after reaching 4th question or you can secure the money till where you won and quit in between')
print('#To use the lifelines first we need to enter the option "e" and choose from the available lifelines by choosing 1,2 or 3                 ')
print('#Refer to the documentation for a sample output                                                                                          ')
print('=========================================================================================================================================')
print('                                                               ALL THE BEST!!!                                                           ')
print('=========================================================================================================================================')
import json
Fifthy=0
Double=0
Skip=0
ctr_sci=0
ctr_sports=0
ctr_history=0
ctr_geo=0
z1=[0]
z2=[0]
z3=[0]
Money={1:'1000',2:'3000',3:'10,000',4:'20,000',5:'50,000',6:'1,00,000',7:'3,00,000',8:'5,00,000',9:'10,00,000',10:'15,00,000',11:'25,00,000',12:'40,00,000',13:'65,00,000',14:'80,00,000',15:'90,00,000',16:'1,00,00,000'}

def money():
    z=ctr_sci+ctr_sports+ctr_history+ctr_geo
    y=Money[z]
    Money[z]='==>'+y
    for key, value in Money.items():
        print("{}) {}".format(key, value))
    Money[z]=y
def guaranteedmoney():
    v=ctr_sci+ctr_sports+ctr_history+ctr_geo
    if v<4:
        print('Sorry You did not reach any guaranteed option')
    elif v>=4 and v<8:
        print('CONGRATULATIONS YOU HAVE WON THE GUARANTEED MONEY OF 20,000 RUPEES')
    elif v>=8 and v<12:
        print('CONGRATULATIONS YOU HAVE WON THE GUARANTEED MONEY OF 5,00,000 RUPEES')
    elif v>=12 and v<16:
        print('░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗')
        print('██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝')
        print('██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░')
        print('██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗')
        print('╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝')
        print('░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░')
        print('CONGRATULATIONS YOU HAVE WON 40,00,000 RUPEES')
    elif v==16:
        print('░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗')
        print('██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝')
        print('██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░')
        print('██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗')
        print('╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝')
        print('░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░')
        
        print('██╗░░░██╗░█████╗░██╗░░░██╗  ░█████╗░██████╗░███████╗  ░█████╗░')
        print('╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██╔══██╗██╔════╝  ██╔══██╗')
        print('░╚████╔╝░██║░░██║██║░░░██║  ███████║██████╔╝█████╗░░  ███████║')
        print('░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██║██╔══██╗██╔══╝░░  ██╔══██║')
        print('░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░██║██║░░██║███████╗  ██║░░██║')
        print('░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝')

        print('░█████╗░██╗░░██╗░█████╗░███╗░░░███╗██████╗░██╗░█████╗░███╗░░██╗')
        print('██╔══██╗██║░░██║██╔══██╗████╗░████║██╔══██╗██║██╔══██╗████╗░██║')
        print('██║░░╚═╝███████║███████║██╔████╔██║██████╔╝██║██║░░██║██╔██╗██║')
        print('██║░░██╗██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝░██║██║░░██║██║╚████║')
        print('╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░░░░██║╚█████╔╝██║░╚███║')
        print('░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝')
                

Topics=['A)SCIENCE','B)SPORTS','C)HISTORY','D)GEOGRAPHY','E)EXIT']
LIFELINES=['1)50/50','2)DOUBLE CHANCE','3)SKIP']
while True:
    if ctr_sci==4:
        Topics[0]='DELETED'
    if ctr_sports==4:
        Topics[1]='DELETED'
    if ctr_history==4:
        Topics[2]='DELETED'
    if ctr_geo==4:
        Topics[3]='DELETED'        
    for l in Topics:
        print(l.strip('"'))
    print('=========================================================================================================================================')
    T=input('Enter any option: ')
    if ctr_sci==0:
        if T.lower()=='a':
            import sciquestions
            print('Your Available lifelines are:')
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sci=ctr_sci+1
            from sciquestions import q1
            q1()
            from sciquestions import a
            from sciquestions import L1
            from sciquestions import L2
            from sciquestions import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
    
                break
            print('=========================================================================================================================================')
    elif ctr_sci==1:
        if T.lower()=='a':
            import sciquestions
            print('Your Available lifelines are:')
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sci=ctr_sci+1
            from sciquestions import q1
            q1()
            from sciquestions import a
            from sciquestions import L1
            from sciquestions import L2
            from sciquestions import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_sci==2:
        if T.lower()=='a':
            import sciquestions
            print('Your Available lifelines are:')
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sci=ctr_sci+1
            from sciquestions import q1
            q1()
            from sciquestions import a
            from sciquestions import L1
            from sciquestions import L2
            from sciquestions import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')

    elif ctr_sci==3:
        if T.lower()=='a':
            import sciquestions
            print('Your Available lifelines are:')
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sci=ctr_sci+1
            from sciquestions import q1
            q1()
            from sciquestions import a
            from sciquestions import L1
            from sciquestions import L2
            from sciquestions import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    if ctr_sports==0:
        if T.lower()=='b':
            import sports
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sports=ctr_sports+1
            from sports import q1
            q1()
            from sports import a
            from sports import L1
            from sports import L2
            from sports import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
            
    elif ctr_sports==1:
        if T.lower()=='b':
            import sports
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sports=ctr_sports+1
            from sports import q1
            q1()
            from sports import a
            from sports import L1
            from sports import L2
            from sports import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
                
    elif ctr_sports==2:
        if T.lower()=='b':
            import sports
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sports=ctr_sports+1
            from sports import q1
            q1()
            from sports import a
            from sports import L1
            from sports import L2
            from sports import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
                

    elif ctr_sports==3:
        if T.lower()=='b':
            import sports
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_sports=ctr_sports+1
            from sports import q1
            q1()
            from sports import a
            from sports import L1
            from sports import L2
            from sports import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    if ctr_history==0:
        if T.lower()=='c':
            import history
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_history=ctr_history+1
            from history import q1
            q1()
            from history import a
            from history import L1
            from history import L2
            from history import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_history==1:
        if T.lower()=='c':
            import history
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_history=ctr_history+1
            from history import q1
            q1()
            from history import a
            from history import L1
            from history import L2
            from history import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_history==2:
        if T.lower()=='c':
            import history
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_history=ctr_history+1
            from history import q1
            q1()
            from history import a
            from history import L1
            from history import L2
            from history import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_history==3:
        if T.lower()=='c':
            import history
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_history=ctr_history+1
            from history import q1
            q1()
            from history import a
            from history import L1
            from history import L2
            from history import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    if ctr_geo==0:
        if T.lower()=='d':
            import geo
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_geo=ctr_geo+1
            from geo import q1
            q1()
            from geo import a
            from geo import L1
            from geo import L2
            from geo import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_geo==1:
        if T.lower()=='d':
            import geo
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_geo=ctr_geo+1
            from geo import q1
            q1()
            from geo import a
            from geo import L1
            from geo import L2
            from geo import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_geo==2:
        if T.lower()=='d':
            import geo
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_geo=ctr_geo+1
            from geo import q1
            q1()
            from geo import a
            from geo import L1
            from geo import L2
            from geo import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    elif ctr_geo==3:
        if T.lower()=='d':
            import geo
            for l in LIFELINES:
                print(l.strip('"'))
            print('=========================================================================================================================================')
            ctr_geo=ctr_geo+1
            from geo import q1
            q1()
            from geo import a
            from geo import L1
            from geo import L2
            from geo import L3
            z1[0]=L1[0]
            z2[0]=L2[0]
            z3[0]=L3[0]
            if z1[0]==1:
                LIFELINES[0]='LIFELINE HAS BEEN USED'
            if z2[0]==1:
                LIFELINES[1]='LIFELINE HAS BEEN USED'
            if z3[0]==1:
                LIFELINES[2]='LIFELINE HAS BEEN USED'            
            if a==1:
                print('CONGRATULATIONS')
                money()
            else:
                print('Sorry you lost')
                print('=========================================================================================================================================')
                break
            print('=========================================================================================================================================')
    if T.lower()=='e':
        print('you have quit the game')
        z=ctr_sci+ctr_sports+ctr_history+ctr_geo
        print('CONGRATULATIONS!!! YOU HAVE WON',Money[z],'RUPEES')
        print('THANK YOU FOR PLAYING')
        print('=========================================================================================================================================')
        break
    if ctr_sci+ctr_sports+ctr_history+ctr_geo==16:
        break
if T!='e':
    guaranteedmoney()
    print('THANK YOU FOR PLAYING')
    print('=========================================================================================================================================')


