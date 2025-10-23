
def upperString(content):
    return content.upper()

def lowerString(content):
    return content.lower()

def firstLetterUpper(content):
    if len(content) == 0:
        return ""
    
    return content[0].upper() # Récupère la première lettre et la met en majuscule