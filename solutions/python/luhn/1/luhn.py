class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = self.card_num.replace(" ", "")
        if len(num) <= 1 or not num.isdigit():
            return False
        digits = [int(d) for d in num]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0
               
