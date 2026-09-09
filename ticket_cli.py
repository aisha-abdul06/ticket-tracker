import json
import os

TICKET_FILE = "tickets.json"


def load_tickets():
    if not os.path.exists(TICKET_FILE):
        return []

    with open(TICKET_FILE, "r") as f:
        return json.load(f)


def save_tickets(tickets):
    with open(TICKET_FILE, "w") as f:
        json.dump(tickets, f, indent=2)


def create_ticket():
    title = input("Ticket title: ")
    reporter = input("Reported by: ")
    priority = input("Priority (low/medium/high): ")

    return {
        "title": title,
        "reporter": reporter,
        "priority": priority,
        "status": "open"
    }


def list_tickets(tickets):
    if not tickets:
        print("No tickets yet.")
        return

    for index, ticket in enumerate(tickets, start=1):
        print(f"{index}. [{ticket['priority']}] {ticket['title']} — {ticket['status']}")


def main():
    tickets = load_tickets()

    while True:
        print("\n1. New ticket 2. List tickets 3. Quit")
        choice = input("Choose: ")

        if choice == "1":
            tickets.append(create_ticket())
            save_tickets(tickets)
            print("Ticket saved.")

        elif choice == "2":
            list_tickets(tickets)

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid choice, try again.")


main()