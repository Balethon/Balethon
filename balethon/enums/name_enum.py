from enum import Enum


class NameEnum(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    def __repr__(self):
        return super().__str__()

    def __eq__(self, other):
        return self.value == other
