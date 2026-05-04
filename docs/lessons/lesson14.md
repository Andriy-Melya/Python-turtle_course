# 🎲 Випадкові кольори у Python Turtle 🐢

## 🔹 Що таке випадковий колір?

Випадковий колір — це коли комп’ютер **сам обирає колір**, і кожного разу він може бути іншим 🎨

---

## Підключаємо “магію випадковості”

```python
import random
```

👉 Це спеціальна бібліотека, яка вміє генерувати випадкові числа

---

## 🔹 Спосіб №1. Випадковий колір зі списку

Найпростіший спосіб 👇

```python
from turtle import *
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

color(random.choice(colors))
pensize(5)
forward(100)

done()
```

---

### 💡 Як це працює:

```python
random.choice(colors)
```

👉 обирає випадковий елемент зі списку кольорів

---

## 🔹 Спосіб №2. Повністю випадковий колір (RGB) 🔥

```python
from turtle import *
import random

colormode(255)  # дозволяє використовувати RGB

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

color(r, g, b)
pensize(5)
forward(100)

done()
```

---

### 💡 Що таке RGB?

Кожен колір складається з трьох компонентів:

* 🔴 Red (червоний)
* 🟢 Green (зелений)
* 🔵 Blue (синій)

Кожен компонент має значення від **0 до 255**

---

## 🔥 Крок 4. Випадковий колір у циклі

Найцікавіший варіант 😎

```python
from turtle import *
import random

colormode(255)

pensize(3)

for i in range(20):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color(r, g, b)
    forward(100)
    right(100)

done()
```

