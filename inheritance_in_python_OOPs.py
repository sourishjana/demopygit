
class A:
    def feature1(self):
        print("feature 1 woring:")
    def feature2(self):
        print("feature 2 woring:")

class B(A):
    def feature3(self):
        print("feature 3 woring:")
    def feature4(self):
        print("feature 4 woring:")

class C(B):
    def feature5(self):
        print("feature 5 woring:")
    def feature6(self):
        print("feature 6 woring:")

a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature3()
b1.feature4()
b1.feature2()
b1.feature1()
c1=C()
c1.feature5()
c1.feature3()
c1.feature4()
c1.feature2()
c1.feature1()
c1.feature6()
class Q:
    def feature7(self):
        print("feature 7 woring:")
class S:
    def feature8(self):
        print("feature 8 woring:")
class R(S,Q):
    def feature9(self):
        print("feature 9 woring:")
r1=R()
r1.feature7()
r1.feature8()
r1.feature9()