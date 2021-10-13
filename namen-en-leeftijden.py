stopped = False



questionsInfo = {
    "question": {
        "name": "Wat is uw naam?: ",
        "age": "Wat is uw leeftijd?: "
    },

    "answer": {}
}

questionsKeys = list (questionsInfo['question'].keys() )




def welcomesUser(name, age):
    print("Hallo " + name + " je leeftijd is " + age)




while not stopped:

    for num, key in enumerate( questionsInfo['question'] ):
    
        answerKey = questionsKeys[num] 

        question = questionsInfo['question'][key]

        answer = input(question)

        

        questionsInfo['answer'].setdefault(answerKey, answer)

        if answer == "stop":
            stopped = True
            break


    else:
        name = questionsInfo['answer']['name']
        age = questionsInfo['answer']['age']

        welcomesUser(name, age)