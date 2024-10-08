from application import Application

class ProblemSituation:
    ERROR_USAGE = 1

    def __init__(self):
        self.application = Application()

    def run(self):
        try:
            self.application.run()
        except ValueError as e:  
            print(str(e))
            exit(self.ERROR_USAGE)

situation = ProblemSituation()
situation.run()
