# 📺 Android TV Remote

A simple and intuitive GUI application for controlling your Android TV using ADB (Android Debug Bridge). This application allows you to connect to your Android TV over the network and send commands such as navigation, volume control, and text input. From anywhere in the world if connected to Tailscale IP.

---

## 🚀 Features

- Connect to Android TV via ADB over Wi-Fi or Tailscale
- Send navigation commands (Up, Down, Left, Right, OK, Back, Home)
- Control volume (Volume Up, Volume Down, Mute)
- Input text using the on-screen keyboard
- Gesture-based controls for navigation
- User-friendly interface built with Tkinter

---

## 🛠 Minimum Software Requirements

- Python 3.x (≥ 3.6 recommended)
- ADB (Android Debug Bridge) installed and configured in PATH
- Tkinter (bundled with Python on most systems)

---

## 💻 Supported Operating Systems

- Windows
- macOS
- Linux

---

## ⚙️ How to Set Up (All OS) – Code-Only Instructions

# 🪟 Windows (CMD / PowerShell)

:: 1. Install Python from https://www.python.org/downloads/
:: 2. Download and extract Platform Tools from:
::    https://developer.android.com/studio/releases/platform-tools

:: 3. Add ADB to PATH (replace with actual path)

```bash
setx PATH "%PATH%;C:\Path\To\platform-tools"
```
:: 4. Clone and run the project

```bash
git clone https://github.com/IMDUDEOP/IP-Remote.git
cd IP-Remote
python main.py
```

# 🍎 macOS (Terminal)

# 1. Install Python, Tkinter, and ADB

# 1. Install Python & ADB

```bash
brew install python
brew install android-platform-tools
```

# 2. Clone and run the project

```bash
git clone https://github.com/IMDUDEOP/IP-Remote.git
cd IP-Remote
python3 main.py
```

# 🐧 Linux (Debian/Ubuntu)
  
```bash
sudo apt-get update
sudo apt-get install python3 python3-tk android-tools-adb -y
```
  
# 2. Clone and run the project

```bash
git clone https://github.com/IMDUDEOP/IP-Remote.git
cd IP-Remote
python3 main.py
```
</details>

---

## 🕹️ How to Use
Launch the application.

Enter the IP address of your Android TV. Tailscale works too. (e.g., 192.168.0.102:5555).

Click Connect to establish the ADB connection.

Use the navigation buttons or gesture area to control your TV.

Use the text box to send keyboard input.

---

## NOTE: I'm a linux user, so if you encounter any problem on different OS please conatcct me on: dudeop672@gmail.com
