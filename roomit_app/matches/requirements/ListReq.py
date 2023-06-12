from .Requirement import Requirement


class ListReq(Requirement):
    def __init__(self, disqualifies, weight, text, desired_answer):
        super().__init__(disqualifies, weight, text)
        self._desired_answer = desired_answer

    def calculate_score(self, answer):
        # print("List - \n\tanswer  -\t", answer, "\n\tdesired answer:  -\t", self._desired_answer)
        # if there is no desired answer
        if self._desired_answer is None or self._desired_answer == []:
            return None
        # if desired answer is don't care -> grade = weight
        # todo: check id D is don't care
        elif self._desired_answer == 'D' or self._desired_answer == 'empty':
            return self._weight
        # if there is a desired answer for the requirement but there is no answer
        elif answer is None:
            return self._weight / 2
        # if there is a desired answer and an answer
        else:
            # if the answer is in the desired answer options -> grade = weight
            if not set(answer).isdisjoint(self._desired_answer):
                return self._weight
            # if the answer is not in the desired answer list -> grade = zero
            else:
                return 0

    def convert_answer_to_str(self, answer):
        return ', '.join(answer) if answer is not None else "-"
