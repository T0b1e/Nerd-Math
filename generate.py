import random
import time
import math
import quotes as q

def play():

    play: str = input('Wanna play some fun game (Y/N) : ')
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


class Generator:

    def generate_number(rank):

        number = []

        if rank == 'Bronze 1':
            Limit = 10
        if rank == 'Bronze 2':
            Limit = 15
        if rank == 'Silver 1':
            Limit = 20
        if rank == 'Silver 2':
            Limit = 25
        if rank == 'Silver 3':
            Limit = 30
        if rank == 'Gold 1':
            Limit = 35
        if rank == 'Gold 2':
            Limit = 40
        if rank == 'Gold 3':
            Limit = 45
        if rank == 'Platinum 1':
            Limit = 50
        if rank == 'Platinum 2':
            Limit = 55
        if rank == 'Platinum 3':
            Limit = 80
        else:
            pass

        for x in range(2):
            num = random.randint(1, Limit)
            number.append(num)

        return number

    def generate_operator(rank):

        operator_list = ['+', '-', '*', '/', '^', '!']

        for X in range(10):

            if rank == 'Bronze 1':
                Limit = 0
            if rank == 'Bronze 2':
                Limit = 1
            if rank == 'Silver 1':
                Limit = 2
            if rank == 'Silver 2':
                Limit = 2
            if rank == 'Silver 3':
                Limit = 3
            if rank == 'Gold 1':
                Limit = 3
            if rank == 'Gold 2':
                Limit = 3
            if rank == 'Gold 3':
                Limit = 3
            if rank == 'Platinum 1':
                Limit = 4
            if rank == 'Platinum 2':
                Limit = 4
            if rank == 'Platinum 3':
                Limit = 4

            operate = operator_list[random.randint(0,Limit)]

        return operate


    def check_num(number, operator):
        if operator == '+':
            pass
        if operator == '-':
            pass
        if operator == '*':
            pass
        if operator == '/':
            if number[1] == 0:
                temp = random.randint(1,10)  # NEED TO FIX
                number[1] = temp
        if operator == '^':
            if number[1] > 3:
                temp = random.randint(1,3)
                number[1] = temp

        return number

    def generate_equation(number, operate, No):

        Equation = f'{No}: {number[0]} {operate} {number[1]} = '

        print(Equation)

        return Equation


def bonus_equation(number, No):
    bonus_list = ['Factorial','Sqrt']
    s = random.randint(0,1)

    if number[0] > 10:
        temp = random.randint(1,10)
        number[0] = temp

    if bonus_list[s] == 'Factorial':
        Equation = f'{No}: {bonus_list[s]} {number[0]} = '
    if bonus_list[s] == 'Sqrt':
        Equation = f'{No}: {bonus_list[s]} {number[0]} = (!Round down digit Answer!)'

    print(Equation)
    return bonus_list[s]


def bonus_ans(number, symbol):

    letter = ['Keys']

    answer = 0

    if symbol == 'Factorial':
        answer = math.factorial(number[0])
    if symbol == 'Sqrt':
        answer = math.sqrt(number[0])

    letter.append(int(math.floor(answer)))

    return letter


class Answer:
    @staticmethod
    def get_answer():  # TODO

        answer = input('Answer : ')

        try:
            ans = int(answer)
        except ValueError:
            try:
                ans = float(answer)
            except ValueError:
                ans = str(answer)

        return ans

    def answer(number, operator, letter):

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

        random_answer.append(answer)

        f1 = answer + (random.randint(0,2))
        random_answer.append(f1)
        f2 = answer - (random.randint(0,2))
        random_answer.append(f2)

        random.shuffle(random_answer)

        return random_answer

    @staticmethod
    def check_answer(answer, answers):

        check = True

        if int(answers) == int(answer):
            check = True

        if int(answers) != int(answer):
            check = False
            print(f'Correct answer is {answer} ')

        return check


row = []


def boost(check):

    global row
    
    key_lock = []
    
    row.append(check)
    
    if row.count(True) == 10:
        key_lock.append('keys')
        row.clear()

    else:
        key_lock.append('key')

    return key_lock


point = 1


class Adding:

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

    rank = 'Iron'

    def rank(point, level): # RW = Right or Wrong

        if point <= 0:
            rank = 'Bronze 1'
        if 0 < point <= 160:
            rank = 'Bronze 2'
        if point > 160 and point <= 320:
            rank = 'Silver 1'
        if point > 320 and point <= 480:
            rank = 'Silver 2'
        if point > 480 and point <= 640:
            rank = 'Silver 3'
        if point > 640 and point <= 800:
            rank = 'Gold 1'
        if point > 800 and point <= 960:
            rank = 'Gold 2'
        if point > 960 and point <= 1120:
            rank = 'Gold 3'
        if point > 1120 and point <= 1280:
            rank = 'Platinum 1'
        if point > 1280 and point <= 1440:
            rank = 'Platinum 2'
        if point > 1440 and point < 1600:
            rank = 'Platinum 3'

        print(f'Point {point},Ranking {rank},Level {level[0]}')

        return rank


    def leveling(point):

        level = 1
        levels = []

        if point <= 0:
            level = 0
        if 0 < point <= 100:
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
    
        levels.append(level)

        if len(levels) == 2:
            del levels[0]

        return levels


health = ['*', '*', '*', '*', '*', '*']  # Start at 6 hearth


def healths(ca, boost):

    global health

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


class Time:
    @staticmethod
    def time_using():
        START = time.time()
        return START

    def exit_time(start):
        end = time.time()
        exits = end - start

        return round(exits,2)


def game_over(Health, No, Time, Level, Ranking):  # No, Time,Level ,Ranking

    gameovertime = time.time()

    time_using = Time - gameovertime

    if len(Health) <= 0:
        print(f'Game Over,You have been reach Ranking : {Ranking} and Level : {Level} by doing {No} and using {round(time_using)} sec to ')

    return None


def try_again():
    trys = input('Wanna play again (y/n) : ')
    
    return trys


file = open('rule.txt')  # Open file rule.txt
print(file.read())
file.close()
print('='*50)

no = 1


def main():
    
    player = user()
    print('..... Loading user data .....')
    time.sleep(2)
    print('='*50)

    for n in range(len(player)):

        t = Time.time_using()
        
        print(f'Hi {player[n]} have fun')

        while point < 1000:

            global no

            luck = random.uniform(1,100)

            l = Adding.leveling(point)  # Global point
            r = Adding.rank(point, l)  # Global point
            n = Generator.generate_number(r)  # Ranking
            o = Generator.generate_operator(r)  # Rainking
            cn = Generator.check_num(n, o)  # Number, Operator
            Generator.generate_equation(cn, o, no)  # Number, Operator, No
            no += 1

            if len(health) <= 3:

                if luck < 90:
                    le = ['key']

                if luck >= 90:
                    sy = bonus_equation(cn, no)
                    no += 1
                    le = bonus_ans(cn, sy)

            if len(health) > 3:
                le = ['key']

            a = Answer.answer(cn, o, le)  # Number, Operator, key
            Answer.possible_answer(a)  # Answer
            b = Answer.get_answer()
            e = Time.exit_time(t)  # Start time
            ca = Answer.check_answer(a, b)  # Answer, Get_answer
            ad = Adding.add_point(ca)  # Check_answer
            bo = boost(ca)  # Check_answer
 
            h = healths(ca, bo)  # Check_answer, boost
        
            if len(h) == 0:
                game_over(h, no, t, l, r)  # (Health,No,Time,Level,Ranking):
                break

            if ad < 0:
                q.generate_quotes()  # Quotes
                break

            if e == 0:
                break

            print('='*50)


    print('Game Has been over now')
    print('='*50)


if __name__ == 'main':
    main()

wp : str = play()
if wp == 'y':
    main()

else:
    print('See ya Have an nice day')


