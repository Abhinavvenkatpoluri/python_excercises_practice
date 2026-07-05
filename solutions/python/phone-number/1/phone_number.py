import string

class PhoneNumber:
    def __init__(self, number):
        # 1. Check for illegal character types first
        for char in number:
            if char in string.ascii_letters:
                raise ValueError("letters not permitted")
            if char in string.punctuation and char not in "+-(). ":
                raise ValueError("punctuations not permitted")

        # 2. Extract only digit characters
        num1 = []
        for char in number:
            if char.isdigit():
                num1.append(char)

        # 3. Length checks
        if len(num1) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(num1) > 11:
            raise ValueError("must not be greater than 11 digits")

        # 4. Handle 11-digit numbers starting with 1
        if len(num1) == 11:
            if num1[0] != "1":
                raise ValueError("11 digits must start with 1")
            num1.pop(0)  # Strip country code to normalize to 10 digits

        # 5. Extract Area Code and Exchange Code positions
        # Index 0 is Area Code start, Index 3 is Exchange Code start
        if num1[0] == "0":
            raise ValueError("area code cannot start with zero")
        if num1[0] == "1":
            raise ValueError("area code cannot start with one")

        if num1[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if num1[3] == "1":
            raise ValueError("exchange code cannot start with one")

        # 6. Assign the cleaned 10-digit string to self.number
        # This allows the test's `.number` property lookup to work perfectly!
        self.number = "".join(num1)
        self.area_code=self.number[:3]
    def pretty(self):
        self.pretty="("+self.area_code+")"+"-"+self.number[3:6]+"-"+self.number[6:10]
        return self.pretty

