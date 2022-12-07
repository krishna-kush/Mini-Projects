import time, keyboard, requests, json, random, sys

def print_with_delay(curr_time, delay, ques, options, num, all_q_len):
    backword = 3 + 4 # 3 for ques and 4 for options

    while curr_time > 0:
        # for printing time
        print(f'{str(curr_time).split(".")[0]}.{str(curr_time).split(".")[1][:2]}')
        time.sleep(delay)
        curr_time -= delay

        # for printing question and options
        print(f'Total Questions => {all_q_len}')
        print(f'Question No. {num+1}. {ques}')
        for i, e in enumerate(options):
            print(f'{i+1}. {e}', ' '*10)
        # for going back to time string
        print(f'\033[{backword}A', end='')

        # for returning input
        if keyboard.is_pressed('1'):
            return 1
        elif keyboard.is_pressed("2"):
            return 2
        elif keyboard.is_pressed("3"):
            return 3
        elif keyboard.is_pressed("4"):
            return 4
        elif keyboard.is_pressed("e"):
            clear()
            print(f'Your RESULT is => {score} out of {len(qanda)}')
            print('THANKS FOR PLAYING!!!')
            sys.exit()
    return 0

def check(options, answer, index):
    if options[index-1] == answer:
        return True
    else:
        return False

def clear():
    print('\033[2J')

def welcome_and_rules():
    print('Welcome to the game of Guess the Question')
    print('''
        Rules: 1. You have 10 seconds to answer each question. \U0001F609
               2. You will get 1 point for each correct answer.
               3. Press E for Exiting the Game.
        ''')


# API
api = 'https://opentdb.com/api.php?amount=10&type=multiple'
def get_qanda(api):
    dataAll = requests.get(api)
    data = json.loads(dataAll.text)['results']

    # print(data)

    ls = []

    for i in data:
        ans = i['incorrect_answers']
        c = i['correct_answer']
        ans.insert(random.randint(0, len(c)), c)

        import html
        ques = html.unescape(i['question'])
    
        ls.append([ques, ans, i['correct_answer']])

    return(ls)

qanda = get_qanda(api)


# qanda = [
#     ['What is the capital of India?', ['New Delhi', 'Punjab', 'Uttar Pradesh', 'Tamil Nadu'], 'New Delhi'],
#     ['What is the capital of USA?', ['New Delhi', 'Washington DC', 'Uttar Pradesh', 'Tamil Nadu'], 'Washington DC'],
#     ['What is the capital of Australia?', ['New Delhi', 'Canberra', 'Uttar Pradesh', 'Tamil Nadu'], 'Canberra'],

# ]

score = 0

time_limit = 10.00
delay = 0.01

run = 'y'

while run[0].lower() == 'y':
    clear()

    for num, [question, options, answer] in enumerate(qanda):
        welcome_and_rules()
        ans = print_with_delay(time_limit, delay, question, options, num, len(qanda))

        clear()
        if ans != 0:
            print('Calculating Your Result')
            time.sleep(2)
        clear()

        if ans == 0:
            print()
            print('Sorry, Times Up\U0001F915\n Please Try Next Question...')
        
        else:
            if check(options, answer, ans):
                score += 1
                print('CONGRATULATION, Your Answer is Correct,\U0001F918\n Please Try Next Question...')
            else:
                print('Your Answer is Wrong,\n Please Try Next Question...\U0001F915')
        
        time.sleep(2)
        clear()

            
        
    print(f'Your RESULT is => {score} out of {len(qanda)}')
    if score == len(qanda):
        print('Your Every Answer Was Correct,\nAnd for that here is a Realisation for you,\nYou have wasted your precious time on playing this game, Go Learn Something!!!')

    run = input('Do you want to play again?(y/n) : ')

print('THANKS FOR PLAYING!!!')

time.sleep(1)
# clear()
            

