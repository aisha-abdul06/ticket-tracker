import sqlite3

DATABASE = "tickets.db"

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection 

def get_all_tickets():
    connection = get_connection()
    rows = connection.execute(
        "SELECT * FROM tickets ORDER BY created DESC"
    ).fetchall()
    connection.close()
    return rows

def get_ticket(ticket_id):
    connection = get_connection()
    row = connection.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()
    connection.close()
    return row

    