print("-------------constructors-------------------")
class A:
    def __init__(self):
        print("init in A")
    def feature1(self):
        print("feature 1 woring:")
    def feature2(self):
        print("feature 2 woring:")

class B(A):
    def __init__(self):
        super().__init__()
        print("init in B")
    def feature3(self):
        print("feature 3 woring:")
    def feature4(self):
        print("feature 4 woring:")


b1=B()
print("-------------multiple inheritance /MOR---------------------")
class Q:
    def __init__(self):
        print("init in Q")
    def feature5(self):
        print("feature 5-Q woring:")
class W:
    def __init__(self):
        print("init in W")
    def feature5(self):
        print("feature 5-W woring:")
class E(Q,W):
    def __init__(self):
        super().__init__()
        print("init in E")
    def feature7(self):
        print("feature 7 woring:")
e=E()
print("--------------MOR---------------")
e.feature5()