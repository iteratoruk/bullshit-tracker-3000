import json
from datetime import datetime, timedelta
from pathlib import Path

LOG_FILE = Path.home() / ".bst3000" / "log.json"


class BullshitTracker:
    def __init__(self):
        self.sessions = []
        self.current_session = None
        self.load_sessions()

    def start_session(self):
        if self.current_session is None:
            self.current_session = {"start": datetime.now().isoformat()}
        else:
            print("Session already in progress.")

    def stop_session(self):
        if self.current_session is not None:
            self.current_session["end"] = datetime.now().isoformat()
            self.sessions.append(self.current_session)
            self.current_session = None
            self.save_sessions()
        else:
            print("No session in progress.")

    def load_sessions(self):
        if LOG_FILE.exists():
            with open(LOG_FILE, "r") as f:
                data = json.load(f)
                self.sessions = data.get("sessions", [])
        else:
            self.sessions = []

    def save_sessions(self):
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "w") as f:
            json.dump({"sessions": self.sessions}, f, indent=4)

    def get_total_time(self):
        total = timedelta()
        for session in self.sessions:
            start = datetime.fromisoformat(session["start"])
            end = datetime.fromisoformat(session["end"])
            total += end - start
        return total

    def get_time_by_period(self, period: str):
        now = datetime.now()
        total = timedelta()
        for session in self.sessions:
            start = datetime.fromisoformat(session["start"])
            end = datetime.fromisoformat(session["end"])
            if period == "day" and start.date() == now.date():
                total += end - start
            elif period == "week" and start.isocalendar()[1] == now.isocalendar()[1]:
                total += end - start
            elif period == "month" and start.month == now.month:
                total += end - start
        return total
