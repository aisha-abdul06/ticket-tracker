import sqlite3

DATABASE = "tickets.db"

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection 




def get_all_tickets(status=None, priority=None):
    connection = get_connection()

    sql = """
        SELECT tickets.*, categories.name AS category_name
        FROM tickets
        LEFT JOIN categories ON tickets.category_id = categories.id
    """

    conditions = []
    values = []

    if status:
        conditions.append("tickets.status = ?")
        values.append(status)

    if priority:
        conditions.append("tickets.priority = ?")
        values.append(priority)

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    sql += " ORDER BY tickets.created DESC"

    rows = connection.execute(sql, values).fetchall()

    connection.close()
    return rows




def get_ticket(ticket_id):
    connection = get_connection()
    row = connection.execute(
        "SELECT * FROM tickets WHERE id = ?", (ticket_id,)
    ).fetchone()
    connection.close()
    return row

def get_tickets_by_status(status):
    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM tickets WHERE status = ? ORDER BY created DESC",
        (status,)
    ).fetchall()

    connection.close()
    return rows

    import sqlite3

connection = sqlite3.connect("tickets.db")

title = "O'Brien's laptop"

query = "SELECT * FROM tickets WHERE title = ?"

connection.execute(query, (title,))

print("Query worked!")

connection.close()