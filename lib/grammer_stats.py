import pytest

class GrammarStats:
    def __init__(self):
        self.text = None
        self.invalid = 0
        self.passed = 0

    def add_text(self, text):
        self.text = text
        self.check()

    def check(self):
        if self.text[0].isupper() and self.text[-1] in ".!?":
            self.passed +=1
            return True
        else:
            self.invalid += 1
            return False
            
    def percentage_good(self):
        total_tested = self.passed / (self.passed + self.invalid) * 100
        return total_tested

        







        # counter = []
        # for item in self.text:
        #     if item == True:
        #         number_counted = counter.append(1) 
        #         return number_counted



        # for self.text in self.check == True:
        #     self.counter[True] = self.check_so_far + 1
        # else:
        #     return self.check_so_far

        # if self.text is True:
        #     return self.check_so_far + 1
        # else:
        #     return self.check_so_far + 0
        

    # def reading_chunk(self, wpm, minutes):
    #     words_user_can_read = wpm * minutes
    #     words = self._contents.split()
    #     if self._read_so_far >= len(words):
    #         self._read_so_far = 0
    #     chunk_start = self._read_so_far
    #     chunk_end = self._read_so_far + words_user_can_read
    #     chunk_words = words[chunk_start:chunk_end]
    #     self._read_so_far = chunk_end
    #     return " ".join(chunk_words)