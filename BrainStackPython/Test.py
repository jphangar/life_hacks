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






# i = 0
# while i == 0:
#
#     s1 = Subject("Math")
#     s1.addCategories(Category("Algebra"))
#     s1.addCategories(Category("Calculus"))
#     s1.listOfCategory[0].addQuestion(Question("what is 3 times 5?", "15"))
#
#     s2 = Subject("English")
#     s2.addCategories(Category("EnglishForChildren"))
#     s2.addCategories(Category("EnglishForAdults"))
#     s2.listOfCategory[0].addQuestion(Question("Fill in the blank: availab__ity", "li"))
#     print("A welcome statement & the option menus will be here:")
#     print("1.Math  2.English")
#     user_prompt = input()
#     if user_prompt == '1':
#         print("You have chosen math")
#         print("Now Choose a category:")
#         print("0. " + s1.listOfCategory[0].getName())
#         print("1. " + s1.listOfCategory[1].getName())
#         category_prompt = input()
#         if category_prompt == '0':
#             print("Answer the question:")
#             print(s1.listOfCategory[0].listOfQuestion[0].getName())
#             Answer_prompt = input()
#             if Answer_prompt == s1.listOfCategory[0].listOfQuestion[0].getAnswer():
#                 print("CORRECT!!")
#             else:
#                 print("WRONG!!")








    # print(s.name);
    # print(s.listOfCategory[0].name)
    # print(s.listOfCategory[0].listOfQuestion[0].name)
    # print(s.listOfCategory[0].listOfQuestion[0].getAnswer())


