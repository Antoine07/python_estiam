# Programme Python E1, E2, E3, E4, E5

## Programme E1

- Jour 1 & 2

[chapitre introduction](https://antoine07.github.io/python_estiam/)

- Jour 3

[qcm](https://antoine07.github.io/python_estiam/qcm_introduction.html)

[chapitre structure](https://antoine07.github.io/python_estiam/02_structure.html)
[chapitre structure](https://antoine07.github.io/python_estiam/03_fichier.html)


Bibio

[Fun Mooc ](https://www.fun-mooc.fr/fr/cours/python-3-des-fondamentaux-aux-concepts-avances-du-langage/)

[pdf ](https://python.sdv.u-paris.fr/cours-python.pdf?utm_source=chatgpt.com)

## Programme E4


## Pratique

```bash
for f in *.html; do pandoc "$f" -o "pdf/${f%.html}.pdf" --pdf-engine=weasyprint; done

for f in *.md; do pandoc "$f" -o "pdf/${f%.md}.pdf" --pdf-engine=xelatex --standalone; done

for file in PythonE1/Work/Slides/*.md; do
  marp "$file" --html --allow-local-files -o "docs/$(basename "${file%.md}.html")"
done

```