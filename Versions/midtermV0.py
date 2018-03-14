## Program : Study Questions
## Developer : Trevor Murphy
## Date : 03/03/2017
## Description : Asks questions randomly based on chapters in Invent Games with
## Python book.

import valid
import fp
import random

# Randomly select a question that has not been asked yet.
# qs is the list of numbers that represent q numbers for each file.
def q_select(qs, numqs):
    q = -1
    while q not in qs:
        q = random.randint(0, numqs)
    return q

# Chooses the type of question to ask.
def q_type(tfqs, mcqs):
    '''if one list has more questions than the other,'''
    '''or the opposite list has no questions left,'''
    '''ask a question from that list.'''
    if len(tfqs) > len(mcqs) or len(mcqs) == 0:
        qtype = 'tfq'
    elif len(tfqs) < len(mcqs) or len(tfqs) == 0:
        qtype = 'mcq'
    else:
        '''If the lists have the same amount of questions,'''
        '''randomly decide which list to ask from.'''
        if random.randint(0, 1) == 1:
            qtype = 'tfq'
        else:
            qtype = 'mcq'
    return qtype

# Asks the question based on type and q number
def q_ask(qtype, tfqloc, q, mcqloc):
    '''q -= 1 because index starts at 0'''
    q -= 1
    '''If it is a T/F question,'''
    if qtype == 'tfq':
        '''Call prnt_line() function from fp to print question'''
        '''Pass respective fileloc. and q number'''
        print()
        fp.prnt_line(tfqloc, q)
        print()
    else:
        '''Prints MC question instead'''
        print()
        fp.prnt_line(mcqloc, q)
        print()

# Display the question possible answers for either type of question
def q_ans_build(q, qtype):
    if qtype == 'mcq':
        ans = fp.get_ctnt('subjects\\python\\mc\\as\\mca' + str(q))
        # mca.txt files begin with the answer to the question(on the first line)
        correct = ans[0]
        '''Remove the correct answer from the list'''
        ans.remove(correct)
        '''Shuffle the answers in the list'''
        random.shuffle(ans)
        '''Remove excess false answers from list until there are 3 left'''
        while len(ans) > 3:
            '''Removes last item in list'''
            ans.pop()
        '''All of the above MCqs place the ans last in the list'''
        if correct == 'All of the above.\n':
            ans.append(correct)
            cans = 3
        else:
            '''Normal MCqs randomly insert the correct ans in any spot'''
            cans = random.randint(0, 3)
            ans.insert(cans, correct)
    else:
        ans = fp.get_ctnt('subjects\\python\\tf\\as\\tfcs')
        # T/F ans file retrieved here. r .read()s file
        tfqans = fp.get_ctnt('subjects\\python\\tf\\as\\tfas')
        # T/F correct ans chosen by q index here
        q -= 1
        if tfqans[q] == 'True\n':
            cans = 0
        else:
            cans = 1
    return ans, cans

# Takes properly formatted ans and prints them
def q_ans_disp(ans):
    '''i is initialized at 0 to increment during while loop'''
    i = 0
    '''Prints each item(answer) in ans list'''
    while i < len(ans):
        '''Prints option A(0)/B(1)/C(2)/D(3), followed by a possible answer'''
        print(chr(ord('A') + i) + ') ' + ans[i])
        '''increment i by 1 to print next letter/answer'''
        i += 1
    print()


# Retrieves the user's answer based on the question type.
def get_usr_ans(qtype):
    '''Sets the possible choices(tuple) depending on question type'''
    if qtype == 'tfq':
        choices = ('A', 'B')
    else:
        choices = ('A', 'B', 'C', 'D')
    '''Calls in_choices() func from valid module'''
    '''Pass a list/tuple, ask for input until input is in that list/tuple'''
    uans = valid.in_choices(choices)
    '''Change validated char into proper num for compare'''
    if uans == 'A':
        uans = 0
    elif uans == 'B':
        uans = 1
    elif uans == 'C':
        uans = 2
    else:
        uans = 3
    return uans

# Compares the user's answer against the correct answer returns True or False
def ans_compare(uans, cans):
    if uans == cans:
        correct = True
    else:
        correct = False
    return correct

def prnt_score(correct, totalqs, tfwrong, mcwrong):
    # Score is correct/TOTALQS
    score = (correct/totalqs) * 100
    print('You scored: ' + str(round(score, 1)) + '%!')
    print('You got these T/F questions wrong: ' + str(tfwrong))
    print('You got these multiple choice questions wrong: ' + str(mcwrong))

def ask_q_set(tfqs, mcqs, TFQS, MCQS, tfqloc, mcqloc):
    # Number answered correctly
    correct = 0
    # Question numbers play answered incorrectly
    tfwrong = []
    mcwrong = []
    '''Run until all questions are asked.'''
    while len(tfqs) > 0 or len(mcqs) > 0:
        '''Get type of q'''
        qtype = q_type(tfqs, mcqs)
        if qtype == 'tfq':
            '''select the nxtq number,'''
            nxtq = q_select(tfqs, TFQS)
            '''remove the nxtq number from the respective q list'''
            tfqs.remove(nxtq)
        else:
            nxtq = q_select(mcqs, MCQS)
            mcqs.remove(nxtq)

        '''Ask the question'''
        q_ask(qtype, tfqloc, nxtq, mcqloc)
        '''Build and return possible/correct answer'''
        answers, cans = q_ans_build(nxtq, qtype)
        '''Print the answers'''
        q_ans_disp(answers)
        '''Get the user's answer'''
        uans = get_usr_ans(qtype)
        '''Compare answers, if user answer is correct, increment correct'''
        if ans_compare(uans, cans):
            correct += 1
        elif qtype == 'tfq':
            tfwrong.append(nxtq)
        elif qtype == 'mcq':
            mcwrong.append(nxtq)
    return correct, tfwrong, mcwrong
    
def main():
    run = 'y'
##    # Location of the mcqs.txt file
    mcqloc = 'subjects\\python\\mc\\mcqs'
##    # Total number of multiple choice questions
    MCQS = fp.lines_in(mcqloc)
##    # Location of the tfqs.txt file
    tfqloc = 'subjects\\python\\tf\\tfqs'
##    # Total number of T/F questions
    TFQS = fp.lines_in(tfqloc)
##    # Total number of questions constant
    TOTALQS = MCQS + TFQS
    # Questions list, remove num once asked
    mcqs = list(range(1, MCQS + 1))
    tfqs = list(range(1, TFQS + 1))

    while run == 'y':

        ask_q_set(tfqs, mcqs, TFQS, MCQS, tfqloc, mcqloc)

        '''When player is out of questions print the % correct'''
        prnt_score(correct, TOTALQS, tfwrong, mcwrong)
        
        '''Ask to review incorrect questions'''
        review = valid.yes_no('Review the questions answered incorrectly')
        
        '''Ask to run again'''
        run = valid.yes_no('Run Again')
            
main()
