from flask import Flask, render_template, abort, request
from db import get_all_tickets, get_ticket
app = Flask(__name__)
@app.route("/")
def home():
    return "My ticket is working!"
@app.route("/about")
def about():
    return "An IT support ticket tracker for the IT Department."



@app.route("/tickets")
def tickets():
    status = request.args.get("status")
    priority = request.args.get("priority")

    all_tickets = get_all_tickets(status, priority)

    heading = "All Support Tickets"

    if status and priority:
        heading = f"{status.title()} and {priority.title()} Priority Tickets"
    elif status:
        heading = f"{status.title()} Tickets"
    elif priority:
        heading = f"{priority.title()} Priority Tickets"

    return render_template(
        "tickets.html",
        title=heading,
        tickets=all_tickets,
        active=status
    )



@app.route("/tickets/<int:ticket_id>")
def ticket_detail(ticket_id):
    ticket = get_ticket(ticket_id)

    if ticket is None:
        abort(404)
    return render_template("ticket_detail.html", ticket=ticket, number=ticket_id["id"])    
    
    return render_template("tickets_detail.html", ticket=all_tickets[ticket_id - 1],number=ticket_id, ticket_count=ticket_count)

@app.route("/ticket/<int:ticket_id>")
def ticket(ticket_id):
    return f"You asked for ticket number {ticket_id}."

@app.route("/help")
def help():
    return "This is the Ticket Tracker help page."

@app.route("/contact")
def contact():
    return "Contact us at Ticket Tracker Support."

@app.route("/stats")
def stats():
    all_tickets = load_tickets()

    total = len(all_tickets)
    open_tickets = sum(1 for ticket in all_tickets if ticket["status"] == "open")
    closed_tickets = sum(1 for ticket in all_tickets if ticket["status"] == "closed")

    low = sum(1 for ticket in all_tickets if ticket["priority"].lower() == "low")
    medium = sum(1 for ticket in all_tickets if ticket["priority"].lower() == "medium")
    high = sum(1 for ticket in all_tickets if ticket["priority"].lower() == "high")

    return render_template(
        "stats.html",
        total=total,
        open_tickets=open_tickets,
        closed_tickets=closed_tickets,
        low=low,
        medium=medium,
        high=high
    )
@app.route("/tickets/open")
def open_tickets():
    all_tickets = load_tickets()

    open_list = [
        ticket for ticket in all_tickets
        if ticket["status"] == "open"
    ]

    return render_template(
        "open_tickets.html",
        tickets=open_list
    )
@app.route("/tickets/closed")
def closed_tickets():
    all_tickets = load_tickets()

    closed_list = [
        ticket for ticket in all_tickets
        if ticket["status"] == "closed"
    ]

    return render_template(
        "closed_tickets.html",
        tickets=closed_list
    )
