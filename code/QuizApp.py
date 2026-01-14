import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import json
import time

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        # Liste der Fragen mit Antwortmöglichkeiten und der richtigen Antwort
        self.questions = [
            {"question": "Was ist die Hauptstadt von Frankreich?", "options": ["Berlin", "Madrid", "Paris", "Rom"], "answer": "Paris"},
            {"question": "Was ist 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
            {"question": "In welcher Programmiersprache ist dieses Quiz geschrieben?", "options": ["Python", "Java", "C++", "Ruby"], "answer": "Python"},
        ]

        self.current_question_index = 0
        self.selected_answer = tk.StringVar(value=None)
        self.timer_label = None
        self.timer_thread = None
        self.timer_running = False
        self.time_left = 30
        self.results = []

        # GUI-Elemente erstellen
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        # Frage-Label
        self.question_label = tk.Label(self.root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        # Frame für die Antwortmöglichkeiten
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack()

        # Radiobuttons für die Antwortmöglichkeiten
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame, text="", variable=self.selected_answer, value=None, anchor="w"
            )
            rb.pack(fill="x", padx=20, pady=5, anchor="w")
            self.radio_buttons.append(rb)

        # Timer-Label
        self.timer_label = tk.Label(self.root, text="Verbleibende Zeit: 30 Sekunden", fg="red")
        self.timer_label.pack(pady=10)

        # Button für die nächste Frage
        self.next_button = tk.Button(self.root, text="Nächste Frage", command=self.next_question)
        self.next_button.pack(pady=5)

        # Button zum Speichern der Ergebnisse
        self.save_button = tk.Button(self.root, text="Ergebnisse speichern", command=self.save_results)
        self.save_button.pack(pady=5)

    def load_question(self):
        # Lädt die aktuelle Frage und die Antwortmöglichkeiten
        if self.current_question_index < len(self.questions):
            self.time_left = 30
            self.timer_label.config(text=f"Verbleibende Zeit: {self.time_left} Sekunden")

            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            self.selected_answer.set(None)

            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option, value=option)

            # Startet den Timer für die Frage
            self.start_timer()
        else:
            # Beendet das Quiz, wenn keine Fragen mehr übrig sind
            self.end_quiz()

    def start_timer(self):
        # Startet den Timer-Thread
        self.timer_running = True
        self.timer_thread = threading.Thread(target=self.update_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def update_timer(self):
        # Aktualisiert den Timer jede Sekunde
        while self.time_left > 0 and self.timer_running:
            time.sleep(1)
            self.time_left -= 1
            self.timer_label.config(text=f"Verbleibende Zeit: {self.time_left} Sekunden")

        # Behandelt den Fall, wenn die Zeit abgelaufen ist
        if self.time_left == 0:
            self.timer_running = False
            messagebox.showinfo("Zeit abgelaufen!", "Die Zeit für diese Frage ist vorbei.")
            self.next_question()

    def next_question(self):
        # Stoppt den Timer und lädt die nächste Frage
        self.timer_running = False

        if self.current_question_index < len(self.questions):
            selected = self.selected_answer.get()
            correct = self.questions[self.current_question_index]["answer"]
            self.results.append({
                "question": self.questions[self.current_question_index]["question"],
                "selected": selected,
                "correct": correct,
                "is_correct": selected == correct,
            })

        self.current_question_index += 1
        self.load_question()

    def save_results(self):
        # Speichert die Ergebnisse in einer JSON-Datei
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON-Dateien", "*.json"), ("Alle Dateien", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                json.dump(self.results, file, indent=4)
            messagebox.showinfo("Erfolg", "Ergebnisse erfolgreich gespeichert!")

    def load_results(self):
        # Lädt gespeicherte Ergebnisse aus einer JSON-Datei
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON-Dateien", "*.json"), ("Alle Dateien", "*.*")]
        )
        if file_path:
            with open(file_path, "r") as file:
                self.results = json.load(file)
            messagebox.showinfo("Erfolg", "Ergebnisse erfolgreich geladen!")

    def end_quiz(self):
        # Beendet das Quiz und zeigt eine Abschlussnachricht an
        self.timer_running = False
        messagebox.showinfo("Quiz beendet", "Sie haben das Quiz abgeschlossen.")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
