from .Requirement import Requirement


class YNReq(Requirement):
    def __init__(self, disqualifies, weight, text, desired_answer):
        super().__init__(disqualifies, weight, text)
        self._desired_answer = desired_answer

    def calculate_score(self, answer):
        # print("YN - \n\tanswer  -\t", answer, "\n\tdesired answer  -\t", self._desired_answer)
        if type(answer) is not bool and answer is not None:
            raise TypeError("Answer should be of type bool, but got - ", answer," of type - ", type(answer))
        elif self._desired_answer is None or not self._desired_answer:
            return None
        elif answer == self._desired_answer:
            return self._weight
        else:
            return 0

    def convert_answer_to_str(self, answer):
        return answer
