"""
mini-timer v2
Student Name (Student ID)

V2 Tasks (Görevler):
1. Implement a `status` command to show the active timer and current elapsed time.
2. Implement a `cancel` command to stop the active timer WITHOUT saving it to the log.
3. Enhance the `stats` command to also calculate and display the longest session duration.
"""

import os
import sys
from datetime import datetime

DATA_DIR = ".minitimer"
ACTIVE_FILE = os.path.join(DATA_DIR, "active.txt")
SESSIONS_FILE = os.path.join(DATA_DIR, "sessions.log")


def initialize():
    if os.path.exists(DATA_DIR):
        return "Already initialized"
    os.mkdir(DATA_DIR)
    open(ACTIVE_FILE, "w", encoding="utf-8").close()
    open(SESSIONS_FILE, "w", encoding="utf-8").close()
    return "Initialized empty mini-timer in .minitimer/"


def ensure_initialized():
    return os.path.exists(DATA_DIR) and os.path.exists(ACTIVE_FILE) and os.path.exists(SESSIONS_FILE)


def read_active_session():
    if not os.path.exists(ACTIVE_FILE):
        return None
    content = open(ACTIVE_FILE, "r", encoding="utf-8").read().strip()
    if not content:
        return None
    started_at, label = content.split("|", 1)
    return {"started_at": started_at, "label": label}


def write_active_session(started_at, label):
    open(ACTIVE_FILE, "w", encoding="utf-8").write(started_at + "|" + label)


def clear_active_session():
    open(ACTIVE_FILE, "w", encoding="utf-8").close()


def start_session(label):
    if not ensure_initialized():
        return "Not initialized. Run: python solution_v2.py init"
    if read_active_session() is not None:
        return "A timer is already running."

    started_at = datetime.now().replace(microsecond=0).isoformat()
    write_active_session(started_at, label)
    return 'Started "' + label + '" at ' + started_at


def stop_session():
    if not ensure_initialized():
        return "Not initialized. Run: python solution_v2.py init"
    
    active = read_active_session()
    if active is None:
        return "No active timer found."

    started_at = active["started_at"]
    label = active["label"]
    stopped_at = datetime.now().replace(microsecond=0).isoformat()
    duration_seconds = max(0, int((datetime.fromisoformat(stopped_at) - datetime.fromisoformat(started_at)).total_seconds()))

    line = f"{started_at}|{label}|{stopped_at}|{duration_seconds}\n"
    with open(SESSIONS_FILE, "a", encoding="utf-8") as f:
        f.write(line)

    clear_active_session()
    return f'Stopped "{label}" after {duration_seconds}s'

# V2: Yeni görev - Status komutu
def status_session():
    if not ensure_initialized():
        return "Not initialized. Run: python solution_v2.py init"
    
    active = read_active_session()
    if active is None:
        return "No active timer found."
        
    started_at = active["started_at"]
    label = active["label"]
    current_time = datetime.now().replace(microsecond=0)
    elapsed = max(0, int((current_time - datetime.fromisoformat(started_at)).total_seconds()))
    
    return f'Active timer: "{label}" | Elapsed: {elapsed}s'

# V2: Yeni görev - Cancel komutu
def cancel_session():
    if not ensure_initialized():
        return "Not initialized. Run: python solution_v2.py init"
        
    active = read_active_session()
    if active is None:
        return "No active timer found."
        
    clear_active_session()
    return f'Canceled "{active["label"]}". Session was not saved.'


def show_log():
    if not ensure_initialized():
        return "Not initialized. Run: python solution_v2.py init"

    lines = open(SESSIONS_FILE, "r", encoding="utf-8").read().splitlines()
    if not lines:
        return "No sessions found."

    output = []
    for index, line in enumerate(lines, start=1):
        started_at, label, stopped_at, duration = line.split("|")
        output.append(f"[{index}] {label} | started: {started_at} | stopped: {stopped_at} | duration: {duration}s")
    return "\n".join(output)


# V2: Geliştirilmiş Stats komutu
def show_stats():
    if not ensure_initialized():
        return "Not initialized. Run: python solution_v2.py init"

    lines = open(SESSIONS_FILE, "r", encoding="utf-8").read().splitlines()
    if not lines:
        return "No sessions found."

    total_sessions = len(lines)
    total_duration = 0
    max_duration = 0

    for line in lines:
        _, _, _, duration = line.split("|")
        dur_int = int(duration)
        total_duration += dur_int
        if dur_int > max_duration:
            max_duration = dur_int

    average_duration = total_duration // total_sessions
    return (
        f"Sessions: {total_sessions}\n"
        f"Total duration: {total_duration}s\n"
        f"Average duration: {average_duration}s\n"
        f"Longest session: {max_duration}s"
    )


def main():
    if len(sys.argv) < 2:
        print("Usage: python solution_v2.py <command> [args]")
        return

    command = sys.argv[1]

    if command == "init":
        print(initialize())
    elif command == "start":
        if len(sys.argv) < 3:
            print('Usage: python solution_v2.py start "Study session"')
        else:
            print(start_session(sys.argv[2]))
    elif command == "stop":
        print(stop_session())
    elif command == "status":
        print(status_session())
    elif command == "cancel":
        print(cancel_session())
    elif command == "log":
        print(show_log())
    elif command == "stats":
        print(show_stats())
    else:
        print("Unknown command: " + command)


if __name__ == "__main__":
    main()