🧩 GUI Word Unscrambler Game
A sleek, desktop-based vocabulary and brain training game built with Python and Tkinter. This application challenges players to unscramble jumbled words against a 5-minute countdown clock, providing a clean, modern card-based user interface and real-time performance tracking.

✨ Features
Dual-Interface Flow: Features a dedicated Start Menu outlining game rules, transitioning seamlessly into a responsive gameplay arena.

Smart Word Parser: Automatically reads custom word lists from a local text file while intelligently stripping out punctuation. Includes a robust fallback word list if the external file is missing.

Robust Scrambling Engine: Shuffles word letters dynamically, ensuring the generated scrambled string never accidentally matches the original word.

Intelligent Timer System: Implements a strict 5-minute (300-second) countdown timer that dynamically turns red during the final 30 seconds to heighten tension.

Immediate Response Feedback: Provides instant visual validation (Correct! 🎉 or Wrong!) alongside automated text input focusing and keyboard binding (Enter key submission).

Detailed Post-Game Analytics: Calculates and displays your total score, question count, and overall accuracy percentage when time expires or the player voluntarily exits.

🛠️ Tech Stack
Language: Python 3.x

GUI Framework: Tkinter (Python's standard built-in GUI package)

Libraries Used: random, string, tkinter.messagebox
