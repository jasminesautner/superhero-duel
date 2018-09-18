# message = "Hello World"

#     def greeting():
#         print(message)

# class Dog:
#     def bark(object):
#         print("Woof")

# # mydog = Dog()
# # mydog.bark()

# if __name__ == "__main__":
#     my_dog = Dog()
#     my_dog.bark()

class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration
    
    def sleep(self):
        print(
            "{} sleeps for {} hours ".format(
                self.name,
                self.sleep_duration))

# dog = Animal("Sophie", 12)
# dog.sleep()

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()


