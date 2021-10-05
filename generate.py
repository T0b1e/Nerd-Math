import random
import time
import math
import quotes as q

def play():
    play = input('Wanna play some fun game (Y/N) : ')
    try:
        int(play)
    except:
        try:
            float(play)
        except:
            play.lower()

    return play

def user():
    
    player = []

    players = input('How many player : ')
    
    for n in range(int(players)):

        username = input('Player name : ')
        
        player.append(username)

    return player


def generate_number(level):

    number = []

    if level == 0:
        n = 10
    if level == 1:
        n = 10
    if level == 2:
        n = 20
    if level == 3:
        n = 30
    if level == 4:
        n = 30
    if level == 5:
        n = 40
    if level == 6:
        n = 50
    if level == 7:
        n = 60
    if level == 8:
        n = 80
    if level == 9:
        n = 100
    if level == 10:
        n = 100
        
    for x in range(2):
        num = random.randint(1,n)
        number.append(num)

    return number

def generate_operator(level):

    operator_list = ['+','-','*','/','^','!']

    for X in range(10):

        if level == 0:
            o = 0
        if level == 1:
            o = 1
        if level == 2:
            o = 2
        if level == 3:
            o = 2
        if level == 4:
            o = 3
        if level == 5:
            o = 3
        if level == 6:
            o = 3
        if level == 7:
            o = 3
        if level == 8:
            o = 4
        if level == 9:
            o = 4
        if level == 10:
            o = 4

        operate = operator_list[random.randint(0,o)]
    
    #print(operate)
    return operate

def check_num(number,operator):
    if operator == '+':
        pass
    if operator == '-':
        pass
    if operator == '*':
        pass
    if operator == '/':
        if number[1] == 0:
            temp = random.randint(1,10) #NEED TO FIX
            number[1] = temp
    if operator == '^':
        if number[1] > 3:
            temp = random.randint(1,3)
            number[1] = temp

    return number

def bonus_equation(number):
    bonus_list = ['Factorial','Sqrt']
    s = random.randint(0,1)

    if number[0] > 10:
        temp = random.randint(1,10)
        number[0] = temp

    Equation = f'{bonus_list[s]} {number[0]} = (!Round down digit Answer!)'

    print(Equation)
    return bonus_list[s]

def bonus_ans(number,symbol):

    letter = ['Keys']
    answer = 0

    if symbol == 'Factorial':
        answer = math.factorial(number[0])
    if symbol == 'Sqrt':
        answer = math.sqrt(number[0])

    letter.append(int(math.floor(answer)))

    #print(letter)
    return letter

def generate_equation(number,operate):

    Equation = f'{number[0]} {operate} {number[1]} = '

    print(Equation)

    return Equation

def get_answer():

    Answer = input('Answer : ')

    try:
        Ans = int(Answer)
    except ValueError:
        try:
            Ans = float(Answer)
        except ValueError:
            Ans = str(Answer)
            
    return Ans

def answer(number,operator,letter):
    if operator == '+':
        answer = number[0] + number[1]
    if operator == '-':
        answer = number[0] - number[1]
    if operator == '*':
        answer = number[0] * number[1]
    if operator == '/':
        answer = number[0] / number[1]
    if operator == '^':
        answer = number[0] ^ number[1]

    if letter[0] == 'Keys':
        answer = letter[1]
    
    if letter[0] != 'Keys':
        pass

    return int(answer)

def possible_answer(answer):

    random_answer = []
    
    f1 = answer + (random.randint(0,2))
    random_answer.append(f1)
    f2 = answer - (random.randint(0,2))
    random_answer.append(f2)

    #print(random_answer)
    return random_answer

def check_answer(answer,Answer,time):

    check = True

    if Answer == answer:     
        check = True
        #print(f'Correct at {time} Sec')

    if Answer != answer:
        check = False
        print(f'Correct answer is {Answer} ')
        #print(f'Wrong at {time} Sec')

    #print(check)
    return check

row = []

def boost(check):

    global row
    
    key_lock = []
    
    row.append(check)
    
    if row.count(True) == 10:
        key_lock.append('keys')
    else:
        key_lock.append('key')

    print(row,key_lock)

    return key_lock

point = 0

def add_point(check):

    global point

    if check == True:
        point = point + 20
    
    if check == False:
        point = point - 20
        if point < 0:
            point = 0
        pass

    return point

def leveling(point):#RW = Right or Wrong

    #global level
    level = 1

    if point <= 0:
        level = 0
    if point > 0 and point <= 100:
        level = 1
    if point > 100 and point <= 200:
        level = 2
    if point > 200 and point <= 300:
        level = 3
    if point > 300 and point <= 400:
        level = 4
    if point > 400 and point <= 500:
        level = 5
    if point > 500 and point <= 600:
        level = 6
    if point > 600 and point <= 700:
        level = 7
    if point > 700 and point <= 800:
        level = 8
    if point > 800 and point <= 900:
        level = 9
    if point > 900 and point < 1000:
        level = 10
    
    print(f'Point {point}, Level {level}')

    return level

health = ['*','*','*','*','*','*']

def Health(ca,boost):
    
    if boost[0] == 'keys':
        health.append('*')
    if boost[0] != 'keys':
        pass

    if ca == False:
        del health[0]
    else:
        pass

    print(f'HEALTH : {health}')

    return health

def time_count():
    start = time.time()
    return start

def exit_time(start):
    end = time.time()
    exits = end - start
    
    return round(exits,2)

file = open('rule.txt')
print(file.read())
file.close()
print('='*50)

def game():
    
    player = user()

    for n in range(len(player)):

        t = time_count()
        
        print(f'Hi {player[n]} have fun')

        while point < 1000:

            luck = random.uniform(1,100)

            l = leveling(point)
            n = generate_number(l)
            o = generate_operator(l)
            cn = check_num(n,o)

            if luck < 80:
                generate_equation(cn,o)
                le = ['key']

            if luck >= 80:
                sy = bonus_equation(cn)
                le = bonus_ans(cn,sy)

            a = answer(cn,o,le)
            possible_answer(a)
            b = get_answer()
            e = exit_time(t)
            ca = check_answer(a,b,e)
            ad = add_point(ca)
            bo = boost(ca)
 
            h = Health(ca,bo)
        
            if len(h) == 0:
                break

            if ad < 0:
                q.generate_quotes()
                break

            if e == 0:
                break

            print('='*50)
    
    print('Game Has been over now')
    print('='*50)

wp = play()
if wp == 'y':
    game()

else:
    print('See ya')

