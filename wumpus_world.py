import tkinter as tk
from tkinter import messagebox
import random

ROWS = 4

# --- GLOBAL STATE ---
agent = [3, 0]
gold = None
wumpus = None
pit = None

wumpus_alive = True
arrow_used = False
game_over = False

visited = set()

# Colors
COLORS = {
    "agent": "yellow",
    "visited": "orange",
    "empty": "lightblue"
}

# --- GUI SETUP ---
root = tk.Tk()
root.title("Wumpus World - Final Version")

frame = tk.Frame(root)
frame.pack()

cells = [[None for _ in range(ROWS)] for _ in range(ROWS)]

# ---------------- LOGIC ----------------
def generate_world():
    global gold, wumpus, pit

    positions = [(i, j) for i in range(ROWS) for j in range(ROWS)]
    positions.remove((3, 0))  # agent start

    gold = random.choice(positions)
    positions.remove(gold)

    wumpus = random.choice(positions)
    positions.remove(wumpus)

    pit = random.choice(positions)

def neighbors(pos):
    x, y = pos
    moves = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < ROWS:
            moves.append((nx, ny))
    return moves

def percept(pos):
    breeze = any(n == pit for n in neighbors(pos))
    stench = any(n == wumpus for n in neighbors(pos) if wumpus_alive)
    glitter = (pos == gold)
    return breeze, stench, glitter

# ---------------- GUI ----------------
def update_grid():
    for i in range(ROWS):
        for j in range(ROWS):
            if (i, j) == tuple(agent):
                color = COLORS["agent"]
            elif (i, j) in visited:
                color = COLORS["visited"]
            else:
                color = COLORS["empty"]

            cells[i][j].config(bg=color)

    show_info()

def show_info():
    breeze, stench, glitter = percept(tuple(agent))

    hints = []
    if breeze:
        hints.append("🌬 Breeze")
    if stench:
        hints.append("👃 Stench")
    if glitter:
        hints.append("✨ Gold here")
    if not hints:
        hints.append("✅ Safe")

    info_text.set(
        f"Pos: {tuple(agent)} | " +
        " | ".join(hints) +
        f" | Arrow Used: {arrow_used}"
    )

# ---------------- GAME ----------------
def move(dx, dy):
    global game_over

    if game_over:
        return

    x, y = agent
    nx, ny = x + dx, y + dy

    if 0 <= nx < ROWS and 0 <= ny < ROWS:
        agent[0], agent[1] = nx, ny
        visited.add(tuple(agent))

        update_grid()
        check_game()

def shoot(dx, dy):
    global arrow_used, wumpus_alive

    if game_over:
        return

    if arrow_used:
        messagebox.showinfo("Arrow", "Already used!")
        return

    arrow_used = True

    x, y = agent
    while 0 <= x < ROWS and 0 <= y < ROWS:
        if (x, y) == wumpus:
            wumpus_alive = False
            messagebox.showinfo("Arrow", "🎯 Wumpus killed!")
            update_grid()
            return
        x += dx
        y += dy

    messagebox.showinfo("Arrow", "❌ Missed!")

def end_game(msg, title):
    global game_over
    game_over = True

    messagebox.showinfo(title, msg)

    for btn in all_buttons:
        btn.config(state="disabled")

def check_game():
    pos = tuple(agent)

    if pos == gold:
        end_game("🎯 You found GOLD!", "WIN")

    elif pos == pit:
        end_game("💀 Fell into PIT!", "GAME OVER")

    elif pos == wumpus and wumpus_alive:
        end_game("💀 Eaten by Wumpus!", "GAME OVER")

# ---------------- RESTART ----------------
def restart_game():
    global agent, visited, game_over, arrow_used, wumpus_alive

    agent = [3, 0]
    visited = set()
    visited.add(tuple(agent))

    game_over = False
    arrow_used = False
    wumpus_alive = True

    generate_world()

    for btn in all_buttons:
        btn.config(state="normal")

    update_grid()

# ---------------- GRID ----------------
for i in range(ROWS):
    for j in range(ROWS):
        lbl = tk.Label(frame, width=10, height=5, borderwidth=1, relief="solid")
        lbl.grid(row=i, column=j)
        cells[i][j] = lbl

# ---------------- CONTROLS ----------------
controls = tk.Frame(root)
controls.pack(pady=10)

all_buttons = []

def add_btn(text, cmd, r, c, parent):
    btn = tk.Button(parent, text=text, width=5, command=cmd)
    btn.grid(row=r, column=c)
    all_buttons.append(btn)

add_btn("UP", lambda: move(-1,0), 0,1, controls)
add_btn("LEFT", lambda: move(0,-1), 1,0, controls)
add_btn("RIGHT", lambda: move(0,1), 1,2, controls)
add_btn("DOWN", lambda: move(1,0), 2,1, controls)

arrow_frame = tk.Frame(root)
arrow_frame.pack()

tk.Label(arrow_frame, text="Shoot Arrow").grid(row=0, column=1)

add_btn("↑", lambda: shoot(-1,0), 0,2, arrow_frame)
add_btn("←", lambda: shoot(0,-1), 1,1, arrow_frame)
add_btn("→", lambda: shoot(0,1), 1,3, arrow_frame)
add_btn("↓", lambda: shoot(1,0), 2,2, arrow_frame)

# Restart button
restart_btn = tk.Button(root, text="🔄 Restart", font=("Arial", 12), command=restart_game)
restart_btn.pack(pady=10)

# Info
info_text = tk.StringVar()
tk.Label(root, textvariable=info_text, font=("Arial", 12)).pack()

# Init
generate_world()
visited.add(tuple(agent))
update_grid()

root.mainloop()
