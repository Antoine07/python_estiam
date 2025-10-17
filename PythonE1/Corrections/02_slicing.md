---
marp: true
theme: default
paginate: true
class: lead
---

# **Corrections – Exercices sur le slicing**

---

## **Exercice 1 – Inverser une chaîne de caractères en une ligne**

### **Énoncé**
> Inverser une chaîne de caractères en une seule ligne grâce au slicing.

### **Solution**

```python
"bonjour"[::-1]
````

Résultat :

```
'ruojnob'
```

---

### **Autre approche (avec variable)**

```python
content = "bonjour"
print(content[::-1])
```

Résultat identique :

```
ruojnob
```

> **Explication :**
> Le slicing `[::-1]` indique à Python de parcourir la chaîne de droite à gauche (pas = -1).

---

## **Exercice 2 – Extraire le mot "Python" d'une phrase**

### **Énoncé**

> Extraire le mot `"Python"` de la chaîne `"Je code en Python tous les jours"`.

### **Solution 1 – Avec slicing direct (indices connus)**

```python
message = "Je code en Python tous les jours"
print(message[11:17])  # 'Python'
```

> Ici, on découpe la chaîne du caractère 11 au caractère 17 (exclus).
> Attention : cette approche dépend de la position fixe du mot.

---

### **Solution 2 – Avec compréhension de liste**

```python
message = "Je code en Python tous les jours"
mot = [word for word in message.split(" ") if word == "Python"]
print(mot)
```

Résultat :

```
['Python']
```

---

### **Solution 3 – En combinant compréhension et jointure**

```python
"".join(word for word in message.split(" ") if word == "Python")
```

Résultat :

```
'Python'
```

---

### **Solution 4 – Recherche par slicing dynamique**

```python
message = "Je code en Python tous les jours"
search = "Python"

for i in range(0, len(message) - len(search)):
    if message[i:len(search) + i] == search:
        print(f"Le mot '{search}' a été trouvé à l'indice {i}")
```

Résultat :

```
Le mot 'Python' a été trouvé à l'indice 11
```

---

## **Exercice 3 – Supprimer les éléments d'indice pair d'une liste**

### **Énoncé**

> À partir d'une liste donnée, supprimer les éléments d'indice pair.

### **Solution**

```python
l = [14, 18, 21, 24, 100, 78, 57]
# Indices : 0, 1, 2, 3, 4, 5, 6

pairs = l[::2]   # éléments d'indice pair
impairs = l[1::2]  # éléments d'indice impair

print("Indices pairs :", pairs)
print("Indices impairs :", impairs)
```

Résultat :

```
Indices pairs : [14, 21, 100, 57]
Indices impairs : [18, 24, 78]
```

> **Explication :**
>
> * `l[::2]` : commence à 0 et saute un élément à chaque fois.
> * `l[1::2]` : commence à 1 (deuxième élément) et saute un élément.

---

## **Exercice 4 – Copier et modifier une liste**

### **Énoncé**

> Créer une copie d'une liste, modifier la copie et vérifier que l'originale n'est pas affectée.

### **Solution**

```python
a = [1, 2]
b = a[:]  # copie superficielle de la liste

b.append(3)

print("a =", a)  # [1, 2]
print("b =", b)  # [1, 2, 3]
```

Résultat :

```
a = [1, 2]
b = [1, 2, 3]
```

> **Explication :**
>
> * `a[:]` crée une **nouvelle liste** en mémoire (copie de surface).
> * Modifier `b` n’a donc aucun effet sur `a`.
> * C’est la méthode la plus rapide pour dupliquer une liste simple.

---

### ✅ **Récapitulatif des notions utilisées**

| Notion                       | Syntaxe            | Description                |
| ---------------------------- | ------------------ | -------------------------- |
| Inversion d’une séquence     | `[::-1]`           | Parcours à rebours         |
| Extraction d’une sous-chaîne | `[start:end]`      | Coupe entre deux indices   |
| Pas (step)                   | `[::2]`            | Sauter des éléments        |
| Copie de liste               | `[:]`              | Crée une nouvelle liste    |
| Compréhension de liste       | `[x for x in ...]` | Filtrage et transformation |

---

