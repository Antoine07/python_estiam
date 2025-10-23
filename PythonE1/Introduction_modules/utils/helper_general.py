API_KEY="1234"

def greet(name):
    return f"Bonjour {name}!"
    
def avarage(notes):
    if len(notes) > 0 :
        return round( sum(notes)/len(notes), 2 )
    return None