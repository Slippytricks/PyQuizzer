## Program : Study Questions MC/TF
## Developer : Trevor Murphy
## Date : 03/03/2017
## Description : Asks multiple choice and T/F questions 

import valid
import fp
import random
import os

def new_sub():
    name = input('Input subject name: ')
    fp.s_txt()
    name = name.lower().capitalize()
    if valid.yes_no('Is "' + name + '" the correct subject name') == 'y':
        os.mkdir('subjects\\' + name + '\\')
    return name

def new_quiz(sub):
    while 1:
        name = input('Input quiz name: ')
        if valid.yes_no('Is "' + name + '" the correct quiz name') == 'y':
            os.mkdir('subjects\\' + sub + '\\' + name)
            os.mkdir('subjects\\' + sub + '\\'  + name + '\\mc')
            f = open('subjects\\' + sub + '\\'  + name + '\\mc\\mcqs.txt', 'w')
            f.close()
            os.mkdir('subjects\\' + sub + '\\'  + name + '\\mc\\as')
            os.mkdir('subjects\\' + sub + '\\'  + name + '\\tf')
            f = open('subjects\\' + sub + '\\'  + name + '\\tf\\tfqs.txt', 'w')
            f.close()
            os.mkdir('subjects\\' + sub + '\\'  + name + '\\tf\\as')
            f = open('subjects\\' + sub + '\\'  + name + '\\tf\\as\\tfcs.txt', 'w')
            f.write('True\nFalse\n')
            f.close()
            f = open('subjects\\' + sub + '\\'  + name + '\\tf\\as\\tfas.txt', 'w')
            f.close()
            break
    return name

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

#rewrite
def menu(erev, sub = ' ', qz = 0):
    if qz == 0:
        subs = get_subjects()
        if erev == 'Edit':
            subs.append('New')
        fp.s_txt()
        print('Choose which subject you would like to ' + erev.lower() + ':')
        erev.capitalize()
        print('Type new for new subject.')
        fp.s_txt(46)
        sub = valid.in_choices(subs)
        fp.s_txt()
        return sub
    else:
        quizzes = get_quizzes(sub)
        if erev == 'Edit':
            quizzes.append('New')
        fp.s_txt()
        print('Choose which quiz you would like to ' + erev.lower() + ':')
        erev.capitalize()
        print('Type new for new quiz.')
        fp.s_txt(46)
        quiz = valid.in_choices(quizzes)
        fp.s_txt()
        return quiz

def addAnswer(sub, qz, qType):
    if qType == 'Tf':
        print('Enter the Answer(T/F)')
        with open('subjects\\' + sub +  '\\' + qz + '\\tf\\as\\tfas.txt', 'a') as f:
            f.write(valid.in_choices(['True', 'False']) + '\n')
            f.close()
    else:
        qNum = fp.lines_in('subjects\\' + sub + '\\'+ qz + '\\' + qType + '\\' + qType.lower() + 'qs')
        f = open('subjects\\' + sub + '\\' + qz + '\\' + qType + '\\as\\' + qType.lower() + 'a' + str(qNum) + '.txt', 'w')
        for i in range(4):
            while 1:
                if i == 0:
                    fp.s_txt()
                    ans = input ('Enter the CORRECT answer:')
                    fp.s_txt()
                else:
                    fp.s_txt()
                    ans = input('Enter a FALSE answer:')
                    fp.s_txt()
                if valid.yes_no('Is "' + ans + '" the answer you want to add') == 'y':
                    f.write(ans + '\n')
                    break
        f.close()

def addQuestion(sub, qz, qType):
    while 1:
        q = input('Type ' + qType + ' question: ')
        fp.s_txt()
        if valid.yes_no('Is "' + q + '" the question you want to add') == 'y':
            with open('subjects\\' + str(sub) + '\\' + str(qz) + '\\' + str(qType.lower()) + '\\' + str(qType.lower()) + 'qs.txt', 'a') as f:
                f.write(str(q) + '\n')
                f.close()
            break
    addAnswer(sub, qz, qType)

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
    random.shuffle(ans)
    '''All of the above MCqs place the ans last in the list'''
    if c == 'All of the above.\n':
        ans.append(c)
        cans = 3
    else:
        for i in range(len(ans)):
            if ans[i] == c:
                cans = i
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

def edit_study():
    fp.s_txt()
    if valid.in_choices(['Study', 'Edit']) == 'Study':
        return 'Study'
    else:
        return 'Edit'
    
def main():
    samesub, sameqz = 'n', 'n'
    while 1:
        erev = edit_study()
        if samesub == 'n':
            sub = menu(erev)
            if sub == 'New':
                sub = new_sub()
        if sameqz == 'n':
            qz = menu(erev, sub, 1)
            if qz == 'New':
                qz = new_quiz(sub)
        if erev == 'Edit':
            while 1:
                addQuestion(sub, qz, valid.in_choices(['Mc', 'Tf']))
                if valid.yes_no('Add another question') == 'n':
                    break
        else:
            c, totQs, xwrong, ywrong = ask_q_set(sub, qz)
            rev = prnt_score(c, totQs, xwrong, ywrong)
            if rev == 'y':
                while len(xwrong) > 0 or len(ywrong) > 0:
                    c, totQs, xwrong, ywrong = ask_q_set(sub, qz, rev, xwrong, ywrong)
                    rev = prnt_score(c, totQs, xwrong, ywrong)
                    if rev == 'n':
                        break
        if valid.yes_no('Continue studying') == 'n':
            break
        else:
            samesub = valid.yes_no('Study same subject')
            sameqz = valid.yes_no('Study same quiz')
main()
