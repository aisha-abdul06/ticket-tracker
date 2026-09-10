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
    while True:
        title = input("Ticket title: ").strip()

        if title:
            break

        print("Ticket title cannot be empty. Please try again.")

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

    print("\nOPEN TICKETS")
    found_open = False

    for index, ticket in enumerate(tickets, start=1):
        if ticket["status"] == "open":
            print(f"{index}. [{ticket['priority']}] {ticket['title']} — {ticket['status']}")
            found_open = True

    if not found_open:
        print("No open tickets.")

    print("\nCLOSED TICKETS")
    found_closed = False

    for index, ticket in enumerate(tickets, start=1):
        if ticket["status"] == "closed":
            print(f"{index}. [{ticket['priority']}] {ticket['title']} — {ticket['status']}")
            found_closed = True

    if not found_closed:
        print("No closed tickets.")

def main():
    tickets = load_tickets()

    while True:
        print("\n1. New ticket 2. List tickets 3. Quit 4. close ticket")
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

        elif choice == "4":
            list_tickets(tickets)
            ticket_number = int(input("Which ticket number do you want to close? "))
            ticket_index = ticket_number - 1
            if 0 <= ticket_index < len(tickets):
                tickets[ticket_index]["status"] = "closed"
                save_tickets(tickets)
                print("Ticket closed.")
            else:
                print("Invalid ticket number.")

        else:
            print("Invalid choice, try again.")


main()