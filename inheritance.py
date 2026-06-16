class student:
    school_name = 'xyz'

    @classmethod
    def new_school(cls,new):
        cls.new = 'jkl'

    def __init__(self,name):
        print(name)
        print("hello")

    @staticmethod
    def adult(age):
        return age>=18

class std_info(student):

    def info(self, name,age):
        print(name,age)


# s1 = student('harry')
print(student.adult(0))
 #s2 = std_info('jkl')  # if we are not providing here name then oit is giving errror inside info(name)
# s2.info('priyanka', 0)

# 
# 1.  class methods - Call it directly using the Class name (Recommended)
student.new_school()
