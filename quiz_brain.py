class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f" Q.{self.question_number}: {current_question.text}, (true /false):  ")  
        self.check_answer(user, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Yay you guessed it right your score is {self.score} / {self.question_number}")
        else:
            print(f"You are wrong and the total score is {self.score}/ {self.question_number}") 
 
        print(f"The correct answer is {correct_answer} ")  
        print("\n")

            
        