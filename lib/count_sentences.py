class MyString:
    def __init__(self, value=""):
        self._value = ""  # internal storage for the value
        self.value = value  # will call the setter below

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) == str:
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        text = self.value.replace("!", ".")
        text = text.replace("?", ".")
        parts = text.split(".")
        count = 0
        for part in parts:
            if part.strip() != "":
                count += 1
        return count
