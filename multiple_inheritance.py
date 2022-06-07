class dog():
    def speak1(self):
        print("bow")
class puppy():
    def speak2 (self):
        print("bow")
class calf(puppy,dog):
    def speak3 (self):
        print("bow")
dog1=calf()
dog1.speak1()

