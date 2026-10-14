import json
import os
import sqlite3

from db import get_connection
SOURCE = "tickets.json"

if not os.path.exists(SOURCE):
    print("No tickets.json found - nothing to migrate.")
    raise SystemExit

with open(SOURCE) as f:
    tickets = json.load(f)

    connection = get_connection()
    moved = 0
    skipped = 0

VALID_PRIORITIES = {"low", "medium", "high"}
VALID_STATUSES = {"open", "closed"}

def clean(raw, allowed, fallback):
    value = (raw or "").strip().lower()
    return value if value in allowed else fallback


    for ticket in tickets:
        try:
            connection.execute(
                "INSERT INTO tickets (title, reporter, priority, status) VALUES (?, ?, ?, ?)",
                (
                    ticket["title"].strip(),
                    ticket["reporter"].strip(),
                    clean(ticket.get("priority"), VALID_PRIORITIES, "medium"),
                    clean(ticket.get("status"), VALID_STATUSES, "open"),
                ),
            )
            moved += 1
        except sqlite3.IntegrityError as error:
         print(f"Skipping ticket '{ticket.get('title')}': {error}")
    skipped += 1

    connection.commit()
    connection.close()
    print(f"Migrated {moved} ticket(s). Skipped {skipped}.")
    