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


class Application:
    def __init__(self):
        pass

    def run(self):
        print("HELLO")


situation = ProblemSituation()
situation.run()
