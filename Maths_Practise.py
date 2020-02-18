import random

def digitcheck(number_to_check):

    result = False

    while result == False:

        variable = input(number_to_check)
        
        if (variable.isdigit()): result = True
        
        else: print('!!!!! --> The character you have entered is not an interger. Please enter it again')

    return variable

questionsright = 0
questionswrong = 0

result = False
restult2 = False

match = True

answerin = False

stop_program =  False

print(' ')
print(' ')
print(' ')
print(' ')

print ('------------------------------------------------------------------------------------------------------------------------------------')
print ('Welcome to Maths Practise! Answer the question at the botom of the screen, and then check if you are correct at the top of the screen.')
print ('Type "stop" to end the program')

while match == True:

    mindigit = digitcheck('First, choose a minimum digit. ')
    maxdigit = digitcheck('Now, chose a maximum digit. ')


    if mindigit == maxdigit or mindigit > maxdigit:
        print('!!!!! --> oops, you made the maximum digit equal or less than the minimum digit. Please enter them again')
    else:
        print('Ok, lets start!')
        match = False



while  stop_program == False:
    
    Number1 = random.randrange(int(mindigit), int(maxdigit) )
    Number2 = random.randrange(int(mindigit), int(maxdigit) )

    realanswer = Number1 + Number2
    print (Number1, '+', Number2)

    
    while answerin == False:
        answer = input('= ')
        if (answer.isdigit()): answerin = True
        elif answer == ('stop'): 
            print('!!!!!! --> you typed stop, ending program after this question')
            stop_program = True
        else:
            print('!!!!! --> oops, that is an non-interger character. Enter the answer again')    

    answerin = False

    print('======Marking======')
    print(' ')
    print('The question you just did was', Number1, '+', Number2)
    print('You answered',answer)
    print(' ')
    print('The real answer is...', realanswer)  

    if int(answer) == realanswer:
        print('You are CORRECT!')
        questionsright = questionsright + 1

    else:
        print('You are WRONG!')
        questionswrong = questionswrong + 1    
    
    if stop_program == True:
        print('FINAL SCORE:', questionsright, 'questions right and', questionswrong, 'questions wrong.')

    elif questionsright == 0:
        print('you have gotten no questions right so far, and have gotten', questionswrong, 'questions wrong...')
    
    elif questionsright == 0:
        print('you have gotten', questionsright, 'questions right so far, and no questions wrong!')    

    else:
        print ('you have gotten', questionsright, 'questions right and', questionswrong, 'questions wrong so far.')

    print(' ')
    
    if stop_program == True:
        print('======ENDING PROGRAM.======')
        print(' ')

    else:
        print('====== Ok! Next question. ======')

# END #