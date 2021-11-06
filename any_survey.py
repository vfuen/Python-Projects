class SurveyOptions:
    def __init__(self, question):
        self.question = question
        self.results = []

    def ask_questions(self):
        print(self.question)

    def store_answer(self, answer):
        self.results.append(answer)

    def show_results(self):
        """"Show the results of the survey"""
        print("Survey results:")
        for result in self.results:
            print(f"- {result}")


