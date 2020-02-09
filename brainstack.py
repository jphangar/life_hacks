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
        for i in range(2, rowSize - 1,2):
            question = Question(row[i], row[i+1])
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




# print(subjectList[0].getName())
# print(subjectList[0].listOfCategory[2].getName())
# print(subjectList[0].listOfCategory[2].listOfQuestion[0].getName())
# print(subjectList[0].listOfCategory[2].listOfQuestion[0].getAnswer())
# print(subjectList[0].listOfCategory[2].listOfQuestion[1].getName())
# print(subjectList[0].listOfCategory[2].listOfQuestion[1].getAnswer())

