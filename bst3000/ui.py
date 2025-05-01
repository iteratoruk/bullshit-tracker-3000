from datetime import datetime
import tkinter as tk
from .tracker import BullshitTracker


class BullshitTrackerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bullshit Tracker 3000  v0.0.0.0.1.0.101 — Crushing Your Soul Since Today")
        self.tracker = BullshitTracker()
        self.is_running = False
        self.start_time = None
        self.launch_text = "🚀 Launch Bullshit Timer — Let the Idiocy Commence"
        self.btn = tk.Button(
            self.root,
            text=self.launch_text,
            font=("Helvetica", 16, "bold"),
            width=50, height=2,
            bg="red", fg="white",
            activebackground="darkred", activeforeground="white",
            command=self.toggle
        )
        self.btn.pack(pady=20)
        self.session_text = "⏳ Current Idiocy Session: 00:00:00"
        self.session_label = tk.Label(
            self.root,
            text=self.session_text,
            font=("Helvetica", 12)
        )
        self.session_label.pack(pady=5)
        self.stats_label = tk.Label(
            self.root,
            justify="left",
            font=("Helvetica", 10)
        )
        self.stats_label.pack(pady=10)
        self.interrupt_text = "Click the big button when someone interrupts your genius."
        self.footer = tk.Label(
            self.root,
            text=self.interrupt_text,
            font=("Helvetica", 8)
        )
        self.footer.pack(side="bottom", pady=5)
        self.update_ui()

    def toggle(self):
        if not self.is_running:
            self.tracker.start_session()
            self.start_time = datetime.now()
            self.is_running = True
            self.btn.config(text="🛑 Halt the Madness — Rescue My Sanity", bg="green", fg="white",
                            activebackground="darkgreen", activeforeground="white")
            self.footer.config(text="Recording colleagues’ absurdity… your dignity is safe.")
        else:
            self.tracker.stop_session()
            self.is_running = False
            self.btn.config(text=self.launch_text, bg="red", fg="white",
                            activebackground="darkred", activeforeground="white")
            self.session_label.config(text=self.session_text)
            self.footer.config(text=self.interrupt_text)

    def update_ui(self):
        if self.is_running and self.start_time:
            elapsed = datetime.now() - self.start_time
            elapsed_str = str(elapsed).split('.')[0]
            self.session_label.config(text=f"⏳ Current Idiocy Session: {elapsed_str}")

        today, week, month, total = self.tracker.get_stats()
        stats_text = (
            f"📅 Today’s Fiasco:    {today}\n"
            f"🗓️ This Week’s Follies: {week}\n"
            f"📊 Monthly Tragedy:   {month}\n"
            f"🔗 Lifetime Suffering: {total}"
        )
        self.stats_label.config(text=stats_text)
        delay = 1000 if self.is_running else 5000
        self.root.after(delay, self.update_ui)
