import json


score = 0

with open('test.json', 'r') as f:

    quizData = json.load(f)

    for x in quizData['quiz']:
        total = x
    
    print("There are a total of " + total + " questions\n")

    for i in quizData['quiz']:
        print(i + '. ' + quizData['quiz'][i]['question'])
        print('\n'.join(quizData['quiz'][i]['options']))
        
        answer = input("Answer: ").upper()

        if answer == quizData['quiz'][i]['answer']:
            score+=1
            print("Correct!\n")
        else:
            print("Incorrect!\n")

f.close()

final = (score / int(total)) * 100

_ = "Your score is: " + str(round(final, 1)) + "%"

print(_)
