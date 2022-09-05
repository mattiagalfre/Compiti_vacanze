#Bob 

def response(hey_bob):
    msg = hey_bob.strip()
    if msg.isupper():
        if msg.endswith('?'):
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif msg.endswith('?'):
        return "Sure."
    elif msg == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
