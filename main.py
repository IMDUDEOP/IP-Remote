import tkinter as tk
import subprocess
import threading

DEFAULT_IP = "0.0.0.0:5555"

def threaded_adb(cmd):
    threading.Thread(target=lambda: subprocess.run(["adb", "shell"] + cmd.split(),
                                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL),
                     daemon=True).start()

def connect_adb():
    ip = ip_entry.get().strip() or DEFAULT_IP
    connect_btn.config(state="disabled")
    status_label.config(text="🔄 Connecting...", fg="yellow")

    def attempt_connection():
        result = subprocess.run(["adb", "connect", ip],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if b"connected" in result.stdout or b"already connected" in result.stdout:
            status_label.config(text=f"🟢 Connected to {ip}", fg="#3fa34d")
        else:
            status_label.config(text="🔴 Connection Failed", fg="red")
        connect_btn.config(state="normal")

    threading.Thread(target=attempt_connection, daemon=True).start()

def send_text():
    text = text_entry.get()
    if text:
        safe_text = text.replace(" ", "%s")
        threaded_adb(f'input text "{safe_text}"')
        threaded_adb("input keyevent 66")

def send(cmd_key):
    threaded_adb(commands[cmd_key])

def hover_effect(button, hover_color, default_color):
    button.bind("<Enter>", lambda e: button.config(bg=hover_color))
    button.bind("<Leave>", lambda e: button.config(bg=default_color))

def mouse_gesture(event):
    direction = None
    if abs(event.x - 75) > abs(event.y - 75):
        direction = "Right" if event.x > 75 else "Left"
    else:
        direction = "Down" if event.y > 75 else "Up"
    if direction:
        send(direction)

commands = {
    "Power": "input keyevent 26",
    "Up": "input keyevent 19",
    "Down": "input keyevent 20",
    "Left": "input keyevent 21",
    "Right": "input keyevent 22",
    "OK": "input keyevent 66",
    "Back": "input keyevent 4",
    "Home": "input keyevent 3",
    "Volume +": "input keyevent 24",
    "Volume -": "input keyevent 25",
    "Mute": "input keyevent 164"
}

style = {
    "padx": 10, "pady": 6,
    "bd": 0, "font": ("Segoe UI", 10),
    "bg": "#2e2d2d", "fg": "white",
    "activebackground": "#444", "activeforeground": "white",
    "relief": "flat"
}

root = tk.Tk()
root.title("Android TV Remote")
root.configure(bg="#1e1e1e")
root.geometry("420x600")
root.resizable(False, False)

for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# IP Entry
ip_entry = tk.Entry(root, font=("Consolas", 10), width=30, relief="flat",
                    bg="#2e2d2d", fg="white", insertbackground="white", justify="center")
ip_entry.insert(0, DEFAULT_IP)
ip_entry.grid(row=0, column=0, columnspan=3, pady=(10, 4))

# Connect Button
connect_btn = tk.Button(root, text="Connect", command=connect_adb, bg="#3fa34d", fg="white",
                        font=("Segoe UI", 10, "bold"), relief="flat")
connect_btn.grid(row=1, column=0, columnspan=3, pady=4)

# Status Label
status_label = tk.Label(root, text="", bg="#1e1e1e", fg="white", font=("Segoe UI", 9))
status_label.grid(row=2, column=0, columnspan=3, pady=2)

# Navigation Buttons
nav = [
    ("Power", 3, 1),
    ("Up", 4, 1),
    ("Left", 5, 0), ("OK", 5, 1), ("Right", 5, 2),
    ("Down", 6, 1),
    ("Back", 7, 0), ("Home", 7, 2),
    ("Volume +", 8, 0), ("Mute", 8, 1), ("Volume -", 8, 2)
]
for label, r, c in nav:
    btn = tk.Button(root, text=label, command=lambda l=label: send(l), **style)
    btn.grid(row=r, column=c, padx=4, pady=4)
    hover_effect(btn, "#3d3d3d", style["bg"])

# Keyboard Input
tk.Label(root, text="Keyboard:", bg="#1e1e1e", fg="white", font=("Segoe UI", 9)).grid(row=9, column=0, columnspan=3, sticky="w", padx=8)
text_entry = tk.Entry(root, width=32, font=("Consolas", 10), relief="flat", bg="#2e2d2d", fg="white", insertbackground="white")
text_entry.grid(row=10, column=0, columnspan=3, padx=8, pady=4)

# Send Button
tk.Button(root, text="Send", command=send_text, bg="#3fa34d", fg="white", font=("Segoe UI", 9, "bold"), relief="flat").grid(row=11, column=0, columnspan=3, pady=4)

# Gesture Area
canvas = tk.Canvas(root, bg="#2e2d2d", width=150, height=150, highlightthickness=0)
canvas.grid(row=12, column=0, columnspan=3, pady=10)
canvas.bind("<Button-1>", mouse_gesture)

root.mainloop()
