import random


pb = {
    0 : 25,
    1 : 20,
    2 : 20,
    4 : 10,
    6 : 10,
    "wicket" : 5,
    "wide" : 5,
    "no ball" : 5
}

pb_nob = {
    0 : 60,
    1 : 80,
    2 : 80,
    4 : 50,
    6 : 30,
}

def choose(num  : int , nob = False , prob = pb , prob_nob = pb_nob):
    if(nob):
        return random.choices(list(pb_nob.keys()), list(pb_nob.values()) , k = num)
    return random.choices(list(pb.keys()), list(pb.values()) , k = num)