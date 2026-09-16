from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "My ticket is working!"
@app.route("/about")
def about():
    return "An IT support ticket tracker for the IT Department."

@app.route("/tickets")
def tickets():
    return "<h1>All Tickets</h1><p>Nothing here yet.</p>"

@app.route("/ticket/<int:ticket_id>")
def ticket(ticket_id):
    return f"You asked for ticket number {ticket_id}."