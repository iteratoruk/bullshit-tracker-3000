from datetime import datetime
from tkinter import ttk

from .tracker import BullshitTracker


class BullshitTrackerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bullshit Tracker 3000")
        self.tracker = BullshitTracker()
        self.running = False
        self.start_time = None
        self.start_stop_button = ttk.Button(self.root, text="Start", command=self.toggle_session)
        self.start_stop_button.pack(pady=10)
        self.current_session_label = ttk.Label(self.root, text="Current Session: 00:00:00")
        self.current_session_label.pack(pady=5)
        self.today_label = ttk.Label(self.root, text="Today's Bullshit: 00:00:00")
        self.today_label.pack(pady=5)
        self.week_label = ttk.Label(self.root, text="This Week's Bullshit: 00:00:00")
        self.week_label.pack(pady=5)
        self.month_label = ttk.Label(self.root, text="This Month's Bullshit: 00:00:00")
        self.month_label.pack(pady=5)
        self.update_stats()

    def toggle_session(self):
        if not self.running:
            self.tracker.start_session()
            self.start_time = datetime.now()
            self.running = True
            self.start_stop_button.config(text="Stop")
            self.update_current_session()
        else:
            self.tracker.stop_session()
            self.running = False
            self.start_stop_button.config(text="Start")
            self.current_session_label.config(text="Current Session: 00:00:00")
            self.update_stats()

    def update_current_session(self):
        if self.running:
            elapsed = datetime.now() - self.start_time
            self.current_session_label.config(text=f"Current Session: {str(elapsed).split('.')[0]}")
            self.root.after(1000, self.update_current_session)

    def update_stats(self):
        today = self.tracker.get_time_by_period("day")
        week = self.tracker.get_time_by_period("week")
        month = self.tracker.get_time_by_period("month")

        self.today_label.config(text=f"Today's Bullshit: {str(today).split('.')[0]}")
        self.week_label.config(text=f"This Week's Bullshit: {str(week).split('.')[0]}")
        self.month_label.config(text=f"This Month's Bullshit: {str(month).split('.')[0]}")
