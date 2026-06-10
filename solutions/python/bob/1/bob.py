def response(hey_bob):
    hey_bob_1="".join(hey_bob.split())
    if hey_bob_1=="":
       return "Fine. Be that way!"
    if hey_bob_1[len(hey_bob_1)-1]=='?' and hey_bob_1.isupper():
       return "Calm down, I know what I'm doing!" 
    if hey_bob_1[len(hey_bob_1)-1]=='?':
       return "Sure."
    if hey_bob_1.isupper():
       return "Whoa, chill out!"
    return "Whatever."