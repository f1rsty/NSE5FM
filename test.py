import json


score = 0

def get_valid_input():

    while True:
        answer = input("Answer: ").upper()
        if answer not in ('A', 'B', 'C', 'D'):
            print("\nPlease enter a valid character from a-d")
        else:
            break

    return answer

with open('test.json', 'r') as f:

    quizData = json.load(f)

    for x in quizData['quiz']:
        total = x
    
    print("There are a total of " + total + " questions\n")

    for i in quizData['quiz']:
        print(i + '. ' + quizData['quiz'][i]['question'])
        print('\n'.join(quizData['quiz'][i]['options']))
        
        answer = get_valid_input()

        if answer == quizData['quiz'][i]['answer']:
            score+=1
            print("Correct!\n")
        else:
            print("Incorrect!\n")

f.close()

final = (score / int(total)) * 100

_ = "Your score is: " + str(round(final, 1)) + "%"

print(_)

