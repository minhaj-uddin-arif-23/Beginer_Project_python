# dictionary
quize = {
    "Question:-01":{
        "Q":"What is the capital of Bangladesh",
        "Ans": "Dhaka ctg",
    },
    "Question:-02":{
        "Q":"What is your name",
        "Ans":"Arif",
    },
    "Question:-03":{
        "Q":"What is the prime Number ",
        "Ans":"2,3,5,",
    }
}

score = 0

for key,value in quize.items():
    print(value['Q'])
    answer = input("Answer is? ")

    if answer.lower() == value['Ans'].lower():
        print("Correct")
        score +=1
        print("your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value['Ans'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " Out of 3 quiestion ")
