def create_ticket():
    title = input("Ticket title: ")
    reporter = input("Reported by: ")
    priority = input("priority (low/medium/high): ")

    ticket = {
        "title": title,
        "reporter": reporter,
        "priority": priority
    }
    return ticket

new_ticket = create_ticket()
print(new_ticket)