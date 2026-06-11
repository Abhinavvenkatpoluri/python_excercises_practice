def is_valid(isbn):
    digits = isbn.replace("-", "")
    return (
        len(digits) == 10
        and digits[:-1].isdigit()
        and (digits[-1].isdigit() or digits[-1] == "X")
        and sum((10 if c == "X" else int(c)) * (10 - i)
                for i, c in enumerate(digits)) % 11 == 0
    )
        
            
       
    