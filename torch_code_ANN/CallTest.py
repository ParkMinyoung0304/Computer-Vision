class Person:
    def hello(self, name):
        print("hello"+name)
        
    def __call__(self, name):
        print("__call__"+"HELLO"+name)
    

        
person = Person()
person("Tom")
person.hello("Tom")