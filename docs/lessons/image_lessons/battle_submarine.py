import tkinter as tk
import random

# =========================
# НАЛАШТУВАННЯ ПОЛЯ
# =========================
CELL_SIZE = 50
GRID_WIDTH = 15
GRID_HEIGHT = 15


# =========================
# КЛАС КОРАБЛЯ
# =========================
class Ship:
    def __init__(self, x, y, length, direction):
        self.length = length
        self.positions = []
        self.hits = set()

        for i in range(length):
            if direction == "H":
                self.positions.append((x + i, y))
            else:
                self.positions.append((x, y + i))

    def draw(self, canvas):
        for (x, y) in self.positions:
            px, py = Game.to_screen_coords(x, y)

            color = "red" if (x, y) in self.hits else "green"

            canvas.create_rectangle(
                px, py,
                px + CELL_SIZE, py + CELL_SIZE,
                fill=color,
                outline="black",
                width=2,
                tags="objects"
            )

    def hit(self, x, y):
        if (x, y) in self.positions:
            self.hits.add((x, y))
            return True
        return False

    def destroyed(self):
        return len(self.hits) == self.length

    def reset_hits(self):
        self.hits.clear()

    def air_zone(self):
        zone = set()
        for (x, y) in self.positions:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    zone.add((x + dx, y + dy))
        return zone


# =========================
# ПІДВОДНИЙ ЧОВЕН
# =========================
class Submarine:
    def __init__(self):
        self.x = None
        self.y = None
        self.lives = 3

    def draw(self, canvas):
        if self.x is not None:
            px, py = Game.to_screen_coords(self.x, self.y)
            canvas.create_oval(
                px + 5, py + 5,
                px + CELL_SIZE - 5,
                py + CELL_SIZE - 5,
                fill="#2bb3ff",
                outline="white",
                width=2,
                tags="objects"
            )


# =========================
# ГРА
# =========================
class Game:
    def __init__(self, root):
        self.root = root
        self.root.game = self

        self.canvas = tk.Canvas(
            root,
            width=CELL_SIZE * GRID_WIDTH,
            height=CELL_SIZE * GRID_HEIGHT,
            bg="#0a1f44"
        )
        self.canvas.pack()

        self.submarine = Submarine()
        self.ships = []
        self.score = 0
        self.last_hit_ship = None

        self.draw_background()
        self.draw_grid()
        self.create_ships()

        self.random_surface()
        self.draw_all()
        self.create_controls()

    # =========================
    # КООРДИНАТИ
    # =========================
    @staticmethod
    def to_screen_coords(x, y):
        px = x * CELL_SIZE
        py = (GRID_HEIGHT - 1 - y) * CELL_SIZE
        return px, py

    # =========================
    # ФОН
    # =========================
    def draw_background(self):
        for i in range(GRID_HEIGHT):
            shade = 40 + i * 3
            shade = min(shade, 255)
            color = f"#0a1f{shade:02x}"
            self.canvas.create_rectangle(
                0,
                i * CELL_SIZE,
                GRID_WIDTH * CELL_SIZE,
                (i + 1) * CELL_SIZE,
                fill=color,
                outline=""
            )

    def draw_grid(self):
        for i in range(GRID_WIDTH + 1):
            self.canvas.create_line(
                i * CELL_SIZE, 0,
                i * CELL_SIZE, GRID_HEIGHT * CELL_SIZE,
                fill="#1f4e79"
            )

        for i in range(GRID_HEIGHT + 1):
            self.canvas.create_line(
                0, i * CELL_SIZE,
                GRID_WIDTH * CELL_SIZE, i * CELL_SIZE,
                fill="#1f4e79"
            )

    # =========================
    # СТВОРЕННЯ КОРАБЛІВ
    # =========================
    def create_ships(self):
        while len(self.ships) < 4:
            length = random.randint(2, 3)
            direction = random.choice(["H", "V"])
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)

            ship = Ship(x, y, length, direction)

            if all(0 <= px < GRID_WIDTH and 0 <= py < GRID_HEIGHT
                   for px, py in ship.positions):
                self.ships.append(ship)

    # =========================
    # БЕЗПЕЧНІ ПОЗИЦІЇ
    # =========================
    def safe_positions(self):
        forbidden = set()
        for ship in self.ships:
            forbidden |= ship.air_zone()

        all_cells = {
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
        }

        return list(all_cells - forbidden)

    def random_surface(self):
        safe = self.safe_positions()
        if safe:
            self.submarine.x, self.submarine.y = random.choice(safe)

    # =========================
    # МАЛЮВАННЯ
    # =========================
    def draw_all(self):
        self.canvas.delete("objects")
        for ship in self.ships:
            ship.draw(self.canvas)
        self.submarine.draw(self.canvas)

    # =========================
    # ІНТЕРФЕЙС
    # =========================
    def create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        tk.Label(frame, text="X + :").grid(row=0, column=0)
        tk.Label(frame, text="Y + :").grid(row=0, column=2)

        self.dx_entry = tk.Entry(frame, width=5)
        self.dy_entry = tk.Entry(frame, width=5)

        self.dx_entry.grid(row=0, column=1)
        self.dy_entry.grid(row=0, column=3)

        tk.Button(frame, text="🔥 Вогонь!", command=self.fire)\
            .grid(row=1, column=0, columnspan=4)

        self.info_label = tk.Label(
            self.root,
            text="🎯 0",
            font=("Arial", 12, "bold")
        )
        self.info_label.pack()

    def update_info(self):
        self.info_label.config(text=f"🎯 {self.score}")

    # =========================
    # ПОСТРІЛ
    # =========================
    def fire(self):
        try:
            dx = int(self.dx_entry.get())
            dy = int(self.dy_entry.get())
        except:
            return

        tx = self.submarine.x + dx
        ty = self.submarine.y + dy

        if not (0 <= tx < GRID_WIDTH and 0 <= ty < GRID_HEIGHT):
            return

        self.animate_torpedo(tx, ty)

    def animate_torpedo(self, tx, ty):
        sx, sy = self.submarine.x, self.submarine.y
        steps = 20
        dx = (tx - sx) / steps
        dy = (ty - sy) / steps

        def step(i=0):
            if i > steps:
                self.resolve_shot(tx, ty)
                return

            cx = sx + dx * i
            cy = sy + dy * i

            self.draw_all()

            px, py = Game.to_screen_coords(cx, cy)
            self.canvas.create_oval(
                px + 10, py + 10,
                px + 20, py + 20,
                fill="yellow",
                outline="orange",
                width=2,
                tags="objects"
            )

            self.root.after(25, lambda: step(i + 1))

        step()

    # =========================
    # ЛОГІКА ПОСТРІЛУ
    # =========================
    def resolve_shot(self, tx, ty):
        hit_ship = None

        for ship in self.ships:
            if ship.hit(tx, ty):
                hit_ship = ship
                break

        # Логіка регенерації
        if self.last_hit_ship and self.last_hit_ship != hit_ship:
            self.last_hit_ship.reset_hits()

        if hit_ship:
            self.score += 10
            self.last_hit_ship = hit_ship

            if hit_ship.destroyed():
                self.ships.remove(hit_ship)
                self.last_hit_ship = None
        else:
            if self.last_hit_ship:
                self.last_hit_ship.reset_hits()
                self.last_hit_ship = None

        self.random_surface()
        self.update_info()
        self.draw_all()


# =========================
# ЗАПУСК
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Морський бій – підводного човна")
    game = Game(root)
    root.mainloop()