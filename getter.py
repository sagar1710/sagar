class property_fun_demo:

    def __init__(self):
        self._age = 0

    def get_age(self):
        print 'getter method called'
        return self_age

    def set_age(self, a):
        print 'setter method called'
        self._age = a

    def del_age(self):
        del self._age
        age = property(get_age, set_age, del_age)


mark = property_fun_demo()
mark.age = 10
print mark.age
