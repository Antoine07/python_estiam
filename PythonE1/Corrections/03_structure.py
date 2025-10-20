def selection_sort(liste):
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    return liste

print(selection_sort([5, 3, 8, 1]))
# [1, 3, 5, 8]

def find_min(liste):
    min_idx = 0
    for i in range(1, len(liste)):
        if liste[i] < liste[min_idx]:
            min_idx = i
    return min_idx

print(find_min([8, 3, 9, 2]))  # 3


from math import sqrt

def nearest_point(points):
    return min(points, key=lambda p: sqrt(p[0]**2 + p[1]**2))

points = [(1, 2), (3, 4), (0, 5)]
print(nearest_point(points))  # (1, 2)


def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for x in lst:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 1]))  # {1, 2}


A = {"Python", "Java", "C"}
B = {"Python", "Rust"}
C = {"C", "Python", "Go"}

communs = A & B & C
uniques_A = A - (B | C)

print(communs)   # {'Python'}
print(uniques_A) # {'Java'}

def word_frequency(texte):
    freqs = {}
    for mot in texte.split():
        freqs[mot] = freqs.get(mot, 0) + 1
    return freqs

print(word_frequency("le chat et le chien et le chat"))
# {'le': 3, 'chat': 2, 'et': 2, 'chien': 1}


stock = {
    "pomme": {"prix": 1.2, "quantité": 10},
    "banane": {"prix": 0.8, "quantité": 15}
}

def add_article(stock, nom, prix, quantite):
    stock[nom] = {"prix": prix, "quantité": quantite}

def modifier_quantite(stock, nom, delta):
    if nom in stock:
        stock[nom]["quantité"] += delta

def valeur_totale(stock):
    return sum(item["prix"] * item["quantité"] for item in stock.values())

add_article(stock, "orange", 1.5, 8)
modifier_quantite(stock, "banane", -5)
print(valeur_totale(stock))  # 31.5