import os
import json
from datetime import datetime, timedelta


class BullshitTracker:
    def __init__(self):
        self.data_dir = os.path.expanduser('~/.bst3000')
        self.log_path = os.path.join(self.data_dir, 'log.json')
        os.makedirs(self.data_dir, exist_ok=True)
        self.sessions = self._load_sessions()
        self.current_start = None

    def _load_sessions(self):
        if not os.path.exists(self.log_path):
            return []
        with open(self.log_path, 'r') as f:
            data = json.load(f)
        sessions = []
        for s in data.get('sessions', []):
            start = datetime.fromisoformat(s['start'])
            end = datetime.fromisoformat(s['end'])
            sessions.append({'start': start, 'end': end})
        return sessions

    def _save_sessions(self):
        data = {'sessions': [
            {'start': s['start'].isoformat(), 'end': s['end'].isoformat()}
            for s in self.sessions
        ]}
        with open(self.log_path, 'w') as f:
            json.dump(data, f, indent=2)

    def start_session(self):
        if self.current_start is None:
            self.current_start = datetime.now()

    def stop_session(self):
        if self.current_start is None:
            return
        end = datetime.now()
        self.sessions.append({'start': self.current_start, 'end': end})
        self.current_start = None
        self._save_sessions()

    def _gather_durations(self):
        now = datetime.now()
        today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        week = today - timedelta(days=today.weekday())
        month = today.replace(day=1)
        d_today = timedelta()
        d_week = timedelta()
        d_month = timedelta()
        d_total = timedelta()
        for s in self.sessions:
            start, end = s['start'], s['end']
            dur = end - start
            d_total += dur
            if start >= today:   d_today += dur
            if start >= week:    d_week  += dur
            if start >= month:   d_month += dur
        return d_today, d_week, d_month, d_total

    def get_stats(self):
        d_today, d_week, d_month, d_total = self._gather_durations()
        def fmt(td):
            secs = int(td.total_seconds())
            h, rem = divmod(secs, 3600)
            m, s = divmod(rem, 60)
            return f'{h:02}:{m:02}:{s:02}'
        return fmt(d_today), fmt(d_week), fmt(d_month), fmt(d_total)
