
if __name__ == "__main__":

    alain = Person("Alain", "Berset")
    print(alain.get_firstname(), alain.get_lastname())


    john = Student("John", "Smith", 4.00)
    print(john.get_firstname(), john.get_lastname(), john.get_grade())
    john.study("math", 15)
