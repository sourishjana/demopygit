class pycharm:
    def execute(self):
        print("execute")
        print("run")

class mycharm:
    def execute(self):
        print("spell check")
        print("condition check")
        print("execute")
        print("run")
class laptop:
    def code(self,ide):
        ide.execute()

ide=pycharm()
lap=laptop()
lap.code(ide)
print("changing the ide-------------")
ide=mycharm()
lap.code(ide)