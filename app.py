from flask import Flask, render_template
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
    heading = "All Support Tickets"
    return render_template("tickets.html",  tickets=all_tickets)

@app.route("/ticket/<int:ticket_id>")
def ticket(ticket_id):
    return f"You asked for ticket number {ticket_id}."

@app.route("/help")
def help():
    return "This is the Ticket Tracker help page."

@app.route("/contact")
def contact():
    return "Contact us at Ticket Tracker Support."