def myDecorator(func):
    def nestedFunc():
        print('Before')
        func()
        print('After')
    return nestedFunc

@myDecorator
def sayHello():
    print('Hello Fatma from the python learning journey!')

@myDecorator
def sayHowAreYou():
    print('Hello Fatma from say how are you function!')

sayHello()
sayHowAreYou()



#we use @decorator_name instead of this
# decoration = myDecorator(sayHello)
# decoration()
