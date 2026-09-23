from flask import Flask, render_template, abort
from ticket_cli import load_tickets
app = Flask(__name__)
@app.route("/")
def home():
    return "My ticket is working!"
@app.route("/about")
def about():
    return "An IT support ticket tracker for the IT Department."

@app.route("/tickets")
def tickets():
    all_tickets = load_tickets()
    ticket_count = len(all_tickets)
    return render_template("tickets.html", tickets=all_tickets, ticket_count=ticket_count)

@app.route("/tickets/<int:ticket_id>")
def ticket_detail():
    all_tickets = load_tickets()

    if ticket_id < 1 or ticket_id > len(all_tickets):
        abort(404)
    
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
