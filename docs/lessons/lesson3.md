
---

## Урок 3 — Кольори та заливка (`lesson3.md`)  

# 🎨 Урок 3 — Кольори та заливка

## 🎯 Мета уроку
Навчитися використовувати кольори та заливку фігур.

## 📝 Завдання
1. Створити файл `lesson3.py`.
2. Написати код:

```python
from turtle import *

color("blue")
fillcolor("yellow")
begin_fill()

for _ in range(3):
    forward(100)
    left(120)

end_fill()
done()
```