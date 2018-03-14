## Program : Study Questions MC/TF
## Developer : Trevor Murphy
## Date : 03/03/2017
## Description : Asks multiple choice and T/F questions 

import valid
import fp
import random
import os

# Randomly select a question that has not been asked yet.
# qs is the list of numbers that represent q numbers for each file.
def q_select(qs, numqs):
    q = int
    while q not in qs:
        q = random.randint(1, numqs)
    return q

# Chooses the type of question to ask.
def q_list(x, y):
    '''if one list has more questions than the other,'''
    '''or the opposite list has no questions left,'''
    '''ask a question from that list.'''
    if len(x) > len(y) or len(y) == 0:
        qlist = 0
    elif len(x) < len(y) or len(x) == 0:
        qlist = 1
    else:
        '''If the lists have the same amount of questions,'''
        '''randomly decide which list to ask from.'''
        if random.randint(0, 1) == 1:
            qlist = 0
        else:
            qlist = 1
    return qlist

# 'Randomly' build multiple choice answers
def mc_ans_build(xloc, q):
    xansloc = xloc + '\\as\\mca'
    ans = fp.get_ctnt(xansloc + str(q))
    choices = ('A', 'B', 'C', 'D')
    # mca.txt files begin with the answer to the question(on the first line)
    c = ans[0]
    '''Remove the correct answer from the list'''
    ans.remove(c)
    '''Shuffle the answers in the list'''
    random.shuffle(ans)
    '''Remove excess false answers from list until there are 3 left'''
    while len(ans) > 3:
        '''Removes last item in list'''
        ans.pop()
    '''All of the above MCqs place the ans last in the list'''
    if c == 'All of the above.\n':
        ans.append(c)
        cans = 3
    else:
        '''Normal MCqs randomly insert the correct ans in any spot'''
        cans = random.randint(0, 3)
        ans.insert(cans, c)
    return ans, choices, cans

# Build/return T/F possible answers/correct answer 
def tf_ans_build(yloc, q):
    yansloc = yloc + '\\as\\tf'
    choices = ('A', 'B')
    # T/F print answers
    ans = fp.get_ctnt(yansloc + 'cs')
    # T/F ans file retrieved here. r .read()s file
    tfqans = fp.get_ctnt(yansloc + 'as')
    # T/F correct ans chosen by q index here
    q -= 1
    # I DO NOT like how I have to compare this.
    # I could not find a way to remove the \n.
    if tfqans[q] == 'True\n':
        cans = 0
    else:
        cans = 1
    return ans, choices, cans

# Asks the question based on type and q number
def q_ask(q, qloc):
    print()
##    print('Question Number: ' + str(q))
    fp.prnt_line(qloc, q - 1)
    print()

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
def get_usr_ans(choices):
    '''Passes argument choices to func in_choices in the valid module'''
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

# I feel as if this function should be split up a little bit more
# But I also feel it actually makes the most sense like this.
def ask_q_set(sub, qz, rev = 'n', xrlist = [], yrlist = []):
    # Questions answeres incorrectly from corresponding lists.
    xwrong = []
    ywrong = []
    # Current question
    currQ = 1
    # Number answered correctly
    c = 0
    # Set location of subject question type folder.
    xloc = 'subjects\\' + sub + '\\' + qz + '\\mc'
    yloc = 'subjects\\' + sub + '\\' + qz + '\\tf'
    if os.path.exists(xloc):
    # Set number of questions in each file
        xLines = fp.lines_in(xloc + '\\mcqs')
    if os.path.exists(yloc):
        yLines = fp.lines_in(yloc + '\\tfqs')    

    if rev == 'y':
        '''Use the questions answered incorrectly as the question list'''
        x = xrlist
        y = yrlist
        totQs = len(xrlist) + len(yrlist)
    else:
        # Create lists of range of nums according to qs in file
        x = list(range(1, xLines + 1))
        y = list(range(1, yLines + 1))
        # Add qs to total number of questions
        totQs = xLines + yLines
        
    '''Run until all questions are asked.'''
    while len(x) > 0 or len(y) > 0:
        '''Print Q# out of totQs'''
        fp.s_txt(24)
        print('Question ' + str(currQ), 'out of ' + str(totQs) + ':')
        fp.s_txt(24)
        
        '''Get list to choose q from'''
        qlist = q_list(x, y)
    
        if qlist == 0:
            '''select the nxtq number,'''
            nxtq = q_select(x, xLines)
            '''remove the nxtq number from the respective q list'''
            x.remove(nxtq)
            qloc = xloc + '\\mcqs'
            answers, choices, cans = mc_ans_build(xloc, nxtq)
        else:
            nxtq = q_select(y, yLines)
            y.remove(nxtq)
            qloc = yloc + '\\tfqs'
            answers, choices, cans = tf_ans_build(yloc, nxtq)
##        print('CANS = ' + str(cans))
        '''Ask the question'''
        q_ask(nxtq, qloc)
        '''Print the answers'''
        q_ans_disp(answers)
        '''Get the user's answer'''
        uans = get_usr_ans(choices)
        
        '''Compare answers, if user answer is correct, increment correct'''
        if uans == cans:
            c += 1
        elif qlist == 0:
            xwrong.append(nxtq)
        else:
            ywrong.append(nxtq)
        currQ += 1
    return c, totQs, xwrong, ywrong

# Prints score and numbers of questions user answered incorrectly
def prnt_score(c, totQs, xwrong, ywrong):
    score = (c/totQs) * 100
    fp.s_txt()
    print('You answered ' + str(c) + '/' + str(totQs) + ' correctly.')
    print('Your score is: ' + str(round(score, 1)) + '%!')
    fp.s_txt()
    # If the score is perfect, dont ask to review, dont show qs wrong
    if score == 100:
        rev = 'n'
    else:
        print('You answered', len(xwrong), 'multiple choice questions',
          'incorrectly:\n', str(xwrong))
        fp.s_txt()
        print('You answered', len(ywrong), 'T/F questions incorrectly:\n',
          str(ywrong))
        fp.s_txt()
        rev = valid.yes_no('Review the questions answered incorrectly')
        fp.s_txt()
    return rev

# Gets the subject choices from the folder subjects using os
def get_subjects():
    subs = os.listdir('subjects\\')
    for i in range(len(subs)):
        subs[i] = subs[i].lower().capitalize()
    return subs

def get_quizzes(sub):
    quizzes = os.listdir('subjects\\' + sub + '\\')
    for i in range(len(quizzes)):
        quizzes[i] = quizzes[i].lower().capitalize()
    return quizzes

# Simple Menu, Asks for study subject, validates choice, passes subject
def menu():
    subs = get_subjects()
    fp.s_txt()
    print('Choose which subject you would like to study:')
    fp.s_txt(46)
    sub = valid.in_choices(subs)
    fp.s_txt()
    return sub

def new_menu(sub = ' ', qz = 0, erev = 'review'):
    if qz == 0:
        subs = get_subjects()
        subs.append('New')
        fp.s_txt()
        print('Choose which subject you would like to ' + erev + ':')
        print('Type new for new subject.')
        fp.s_txt(46)
        sub = valid.in_choices(subs)
        fp.s_txt()
        return sub
    else:
        quizzes = get_quizzes(sub)
        quizzes.append('New')
        fp.s_txt()
        print('Choose which quiz you would like to ' + erev + ':')
        print('Type new for new quiz.')
        fp.s_txt(46)
        quiz = valid.in_choices(quizzes)
        fp.s_txt()
        return quiz
    
def main():
    # Run until broken, I think this may be my fav method of keeprunning
    tfa1 = open("tfa1.txt", "w")
    tfa1.write("True")
    tfa1.close()
    while True:
        '''Use the menu to choose the subject to study'''
        #sub = menu()
        while 1:
            sub = new_menu()
            if sub == 'New':
                sub = new_sub()
            else:
                break
        while 1:
            quiz = new_menu(sub, 1)
            if quiz == 'New':
                quiz = new_quiz(sub)
            else:
                break
        '''Ask all questions from that subject's folders'''
        c, totQs, xwrong, ywrong = ask_q_set(sub, quiz)
        
        '''When player is out of questions print the % correct'''
        '''Ask to review incorrect questions'''
        rev = prnt_score(c, totQs, xwrong, ywrong)
        if rev == 'y':
            while len(xwrong) > 0 or len(ywrong) > 0:
                c, totQs, xwrong, ywrong = ask_q_set(sub, rev, xwrong, ywrong)
                rev = prnt_score(c, totQs, xwrong, ywrong)
                if rev == 'n':
                    break

        '''Ask to run again'''
        run = valid.yes_no('Continue studying')
        fp.s_txt()
        if run == 'n':
            break
            sys.exit()

main()
