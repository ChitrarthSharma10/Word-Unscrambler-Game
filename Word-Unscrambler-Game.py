import random
import tkinter as tk
from tkinter import messagebox
import string
import os

class WordUnscramblerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Unscrambler Game")
        self.root.geometry("500x530") 
        self.root.configure(bg="#F3F4F6")  
        self.root.resizable(False, False)
        
        # Game variables
        self.word_list = []
        self.current_word_index = 0
        self.score = 0
        self.total_questions = 0
        self.original_word = ""
        
        # Timer variables (300 seconds = 5 minutes)
        self.time_left = 300
        self.timer_id = None  
        
        # UI Frames containers
        self.start_frame = None
        self.game_frame = None
        
        self.load_words()
        self.show_start_screen()

    def load_words(self):
        """Loads words and strips out commas or punctuation automatically"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'words.txt')
        try:
            with open(file_path, 'r') as file:
                text = file.read()
                self.word_list = [word.strip(string.punctuation) for word in text.split() if word.strip(string.punctuation)]


        except FileNotFoundError:
            print(f"Error: The file '{file_path}' could not be found. Using fallback words.")
            self.word_list = ["python", "programming", "frontend", "developer", "scramble", "interface", "aesthetic"]
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.word_list = []

    def scramble_word(self, word):
        """Word scrambling logic"""
        word_letters = list(word)
        for _ in range(5):
            random.shuffle(word_letters)
            scrambled = "".join(word_letters)
            if scrambled != word:
                return scrambled
        return "".join(word_letters)

    def clear_window(self):
        """Helper to clear frames and reset ongoing active timers"""
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        if self.start_frame:
            self.start_frame.pack_forget()
        if self.game_frame:
            self.game_frame.pack_forget()

    # ==================== INTERFACE 1: START MENU ====================
    def show_start_screen(self):
        self.clear_window()
        
        self.start_frame = tk.Frame(self.root, bg="#F3F4F6")
        self.start_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Main Title Banner
        title_label = tk.Label(
            self.start_frame, text="WORD UNSCRAMBLER", 
            font=("Segoe UI", 24, "bold"), bg="#F3F4F6", fg="#4F46E5"
        )
        title_label.pack(pady=(10, 5))
        
        subtitle = tk.Label(
            self.start_frame, text="Train your brain & test your vocabulary!", 
            font=("Segoe UI", 11, "italic"), bg="#F3F4F6", fg="#6B7280"
        )
        subtitle.pack(pady=(0, 20))
        
        # Rules Card Frame
        rules_frame = tk.LabelFrame(
            self.start_frame, text=" HOW TO PLAY ", font=("Segoe UI", 10, "bold"),
            bg="#FFFFFF", fg="#374151", bd=1, relief="solid", padx=15, pady=15
        )
        rules_frame.pack(fill="x", pady=10)
        
        rules_text = (
            "• You will see a jumbled/scrambled word.\n\n"
            "• Unscramble and type your answer in the entry box.\n\n"
            "• Press 'Submit' or hit 'Enter' to confirm your guess.\n\n"
            "• ⏱️ TIMED GAME: You have exactly 5 MINUTES to solve as many words as possible!\n\n"
            "• Click 'Exit Game' anytime to wrap up and see your final accuracy."
        )
        
        rules_label = tk.Label(
            rules_frame, text=rules_text, font=("Segoe UI", 10), 
            bg="#FFFFFF", fg="#4B5563", justify="left", wraplength=380
        )
        rules_label.pack()

        # Start Button
        start_btn = tk.Button(
            self.start_frame, text="START GAME", font=("Segoe UI", 13, "bold"),
            bg="#4F46E5", fg="#FFFFFF", activebackground="#4338CA", activeforeground="#FFFFFF",
            bd=0, cursor="hand2", width=20, height=2, command=self.start_game
        )
        start_btn.pack(pady=(25, 10), ipady=6, expand=True)

    # ==================== INTERFACE 2: GAMEPLAY ====================
    def start_game(self):
        if not self.word_list:
            messagebox.showerror("Error", "No words loaded. Cannot start game.")
            return
            
        random.shuffle(self.word_list)
        self.current_word_index = 0
        self.score = 0
        self.total_questions = 0
        self.time_left = 300  
        
        self.clear_window()
        
        self.game_frame = tk.Frame(self.root, bg="#F3F4F6")
        self.game_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Top Header Score & Timer Bar
        stats_bar = tk.Frame(self.game_frame, bg="#F3F4F6")
        stats_bar.pack(fill="x", pady=(10, 20))
        
        self.question_label = tk.Label(stats_bar, text="Q: 1", font=("Segoe UI", 11, "bold"), bg="#F3F4F6", fg="#4B5563")
        self.question_label.pack(side="left")
        
        self.timer_label = tk.Label(stats_bar, text="Time: 05:00", font=("Segoe UI", 11, "bold"), bg="#F3F4F6", fg="#D97706")
        self.timer_label.pack(side="left", expand=True)
        
        self.score_label = tk.Label(stats_bar, text="Score: 0", font=("Segoe UI", 11, "bold"), bg="#F3F4F6", fg="#4B5563")
        self.score_label.pack(side="right")
        
        # Word Box Wrapper
        word_card = tk.Frame(self.game_frame, bg="#FFFFFF", bd=1, relief="solid")
        word_card.pack(fill="x", pady=10)
        
        self.scrambled_label = tk.Label(
            word_card, text="XXXXX", font=("Courier New", 28, "bold"), 
            bg="#FFFFFF", fg="#1F2937", pady=25
        )
        self.scrambled_label.pack()
        
        # Input Section
        input_label = tk.Label(self.game_frame, text="Type your answer below:", font=("Segoe UI", 10), bg="#F3F4F6", fg="#6B7280")
        input_label.pack(pady=(15, 5))
        
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            self.game_frame, textvariable=self.entry_var, font=("Segoe UI", 14), 
            justify="center", width=22, bd=1, relief="solid", highlightthickness=1, highlightbackground="#D1D5DB"
        )
        self.entry.pack(pady=5, ipady=6) 
        self.entry.bind("<Return>", lambda event: self.check_answer()) 
        self.entry.focus()
        
        # Dynamic Response Feedback line
        self.feedback_label = tk.Label(self.game_frame, text="", font=("Segoe UI", 12, "bold"), bg="#F3F4F6")
        self.feedback_label.pack(pady=10)

        # Control Buttons (Lifted upwards, padding streamlined)
        btn_container = tk.Frame(self.game_frame, bg="#F3F4F6")
        btn_container.pack(pady=(10, 0))

        self.submit_btn = tk.Button(
            btn_container, text="Submit", font=("Segoe UI", 11, "bold"),
            bg="#10B981", fg="#FFFFFF", activebackground="#059669", activeforeground="#FFFFFF",
            bd=0, cursor="hand2", width=12, height=1, command=self.check_answer
        )
        self.submit_btn.pack(side="left", padx=10, ipady=4)

        self.exit_btn = tk.Button(
            btn_container, text="Exit Game", font=("Segoe UI", 11, "bold"),
            bg="#EF4444", fg="#FFFFFF", activebackground="#DC2626", activeforeground="#FFFFFF",
            bd=0, cursor="hand2", width=12, height=1, command=self.game_over
        )
        self.exit_btn.pack(side="right", padx=10, ipady=4)
        
        self.update_timer()
        self.next_question()

    # ==================== TIMER ENGINE ====================
    def update_timer(self):
        if self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
            
            if self.time_left <= 30:
                self.timer_label.config(fg="#EF4444")
            else:
                self.timer_label.config(fg="#D97706")
                
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time: 00:00")
            messagebox.showwarning("Time's Up!", "⏰ 5 minutes are up! Let's check how you did.")
            self.game_over(time_expired=True)

    # ==================== GAME LOGIC EXECUTIONS ====================
    def next_question(self):
        if self.current_word_index >= len(self.word_list):
            self.game_over()
            return

        self.feedback_label.config(text="")
        self.entry_var.set("") 
        self.entry.config(state="normal")
        self.submit_btn.config(state="normal")

        self.original_word = self.word_list[self.current_word_index]
        scrambled = self.scramble_word(self.original_word)
        
        self.total_questions += 1
        self.question_label.config(text=f"Q: {self.total_questions}")
        self.scrambled_label.config(text=" ".join(scrambled.upper())) 
        self.entry.focus()

    def check_answer(self):
        if self.submit_btn['state'] == 'disabled':
            return

        user_guess = self.entry_var.get().strip().lower()
        if not user_guess:
            return

        self.entry.config(state="disabled")
        self.submit_btn.config(state="disabled")

        if user_guess == self.original_word.lower():
            self.feedback_label.config(text="Correct! 🎉", fg="#10B981")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.feedback_label.config(text=f"Wrong! Correct: '{self.original_word}'", fg="#EF4444")

        self.current_word_index += 1
        
        if self.time_left > 0:
            self.root.after(2000, self.next_question)

    def game_over(self, time_expired=False):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        if not time_expired and self.feedback_label.cget("text") == "" and self.total_questions > 0:
            self.total_questions -= 1

        accuracy = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        
        summary_msg = f"--- Game Over ---\n\nYour final score: {self.score}/{self.total_questions}\nAccuracy: {accuracy:.1f}%\n\nThanks for playing!"
        messagebox.showinfo("Results", summary_msg)
        
        self.show_start_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordUnscramblerGUI(root)
    root.mainloop()
