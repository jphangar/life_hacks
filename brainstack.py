import csv





class Question:

    def __init__(self, name="Unknown", answer="Unknown"):

        self.name = name

        self.answer = answer



    def getName(self):

        return self.name



    def getAnswer(self):

        return self.answer





class Category:

    def __init__(self, name):

        self.name = name

        self.listOfQuestion = []



    def getName(self):

        return self.name



    def addQuestion(self, question):

        self.listOfQuestion.append(question)





class Subject:

    def __init__(self, name):

        self.name = name

        self.listOfCategory = []



    def getName(self):

        return self.name



    def addCategories(self, category):

        self.listOfCategory.append(category)





path = "questions and answers - Sheet1.csv"

file = open(path, newline='')

reader = csv.reader(file)

subjectList = []

for row in reader:

    subject = Subject(row[0])

    category = Category(row[1])

    rowSize = 0

    x = False

    added_subject = Subject(row[0])

    for AddedElement in subjectList:

        if subject.getName() == AddedElement.getName():

            x = True

            added_subject = AddedElement

    if x:

        for rowElement in row:

            rowSize += 1

        for i in range(2, rowSize - 1, 2):

            question = Question(row[i], row[i + 1])

            category.addQuestion(question)

        added_subject.listOfCategory.append(category)

    else:

        for rowElement in row:  # get the size

            rowSize += 1

        for i in range(2, rowSize - 1, 2):

            question = Question(row[i], row[i + 1])  # create question object

            category.addQuestion(question)

        subject.listOfCategory.append(category)

        subjectList.append(subject)





print("Welcome to Brain Stack!\nThis app is here to help motivate you with your studying needs. ")

print("Please enter your name: ")

name = input()

print("\nAwesome ", name,

      ", we have uploaded your courses and have study notes for your Math, Science, and Economics courses.\nYou must "

      "select one course to study first to unlock study notes for the next class.")







# while 1:

#     for SubjectElement in subjectList:

#         if selection == SubjectElement.getName():

#             print("Please make a selection:")

#             categoryNum = 0

#             for CategoryElement in SubjectElement.listOfCategory:

#                 print(str(categoryNum) + ". " + CategoryElement.getName())

#                 categoryNum += 1

#             categoryChoice = input()

#             for j in range(0,len(SubjectElement.listOfCategory)):

#                 if categoryChoice == str(j):

#                     for QuestionElement in CategoryElement.listOfQuestion:

#                         print(QuestionElement.getName())

#                         print("Your Answer/or press x to quit: ")

#                         your_answer = input()

#                         if your_answer == 'x':

#                             break

#                         if your_answer == QuestionElement.getAnswer():

#                             print("Excellent!!")

#                         else:

#                             print("Wrong!!")

#                         print(QuestionElement.getAnswer())

#                 else:

#                     break

while 1:

    print("Which course did you want to study? ")

    selection = input().capitalize()  # Math, Science, Economics

    if selection == 'x':

        continue

    for SubjectElement in subjectList:

        if selection == SubjectElement.getName():

            print("Please make a selection:")

            categoryNum = 0

            for CategoryElement in SubjectElement.listOfCategory:

                print(str(categoryNum) + ". " + CategoryElement.getName())

                categoryNum += 1

            print("Please choose category")

            Choice = input()

            if Choice != 'x':

                QuestionList = SubjectElement.listOfCategory[int(Choice)].listOfQuestion

                for QuestionElement in QuestionList:

                    print(QuestionElement.getName())

                    print("Your Answer/or press x to quit: ")

                    your_answer = input()

                    if your_answer == 'x':

                        break

                    print(QuestionElement.getAnswer())

            else:

                break



