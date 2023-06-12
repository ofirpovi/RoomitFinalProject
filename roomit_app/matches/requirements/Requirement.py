from abc import ABC, abstractmethod


class Requirement(ABC):
    def __init__(self, disqualifies, weight, text):
        self._disqualifies = disqualifies
        self._weight = weight
        self._text = text

    @abstractmethod
    def calculate_score(self, answer):
        pass

    @abstractmethod
    def convert_answer_to_str(self, answer):
        pass
