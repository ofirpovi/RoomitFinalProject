from .Requirement import Requirement


class ListReq(Requirement):
    def __init__(self, disqualifies, weight, text, desired_answer):
        super().__init__(disqualifies, weight, text)
        self._desired_answer = desired_answer

    def calculate_score(self, answer):
        if answer is not None and (self._desired_answer is None or self._desired_answer == 'D' or not set(answer).isdisjoint(self._desired_answer)):
            return self._weight
        else:
            return 0

    def convert_answer_to_str(self, answer):
        return ', '.join(answer) if answer is not None else "-"
