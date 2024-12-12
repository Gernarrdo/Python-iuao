import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
 
def funzioneandrea():
    numerorandom = random.randint(0, 5)
    if numerorandom == 0:
        print("Francesco Totti è tornato")
        return
    if numerorandom == 2:
        print("Ciao!")
        return        
    else:
        print("Ciao Andrea")
        return