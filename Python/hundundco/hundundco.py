import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime


#########################################Funktionen#########################################

#Diese Funktion holt mir die offenen Rechnungen ab
def get_open_invoices():
    try:
        query = """
        SELECT clients.vorname, clients.nachname, DATE_FORMAT(rechnungen.rechnungsdatum, '%d.%m.%Y')
        FROM clients
        JOIN rechnungen ON clients.client_id = rechnungen.client_id
        WHERE rechnungen.rechnung_bezahlt = FALSE;
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Clear previous results
        canvas_query.delete("text")  
        
        # Überschrift über den Headern des Canvas anzeigen
        text_x = 100
        text_y = 50
        canvas_query.create_text(text_x, text_y, text="Offene Rechnungen", font=("Arial", 14, "bold"), anchor="w", tags="text")
        
        # Display rows
        y_position = 100  # Startposition für Datenzeilen
        for row in result:
            # Datenzeilen anzeigen
            for i, item in enumerate(row):
                canvas_query.create_text(text_x + i * 200, y_position, text=item, anchor="w", tags="text")
            y_position += 20  # Abstand zwischen den Zeilen
    except Exception as e:
        messagebox.showerror("Query Error", str(e))

#Diese Funktion erstellt das Formular
def submit_form():
    try:
        # Verbindung zur Datenbank herstellen
        db_connection = mysql.connector.connect(
            host='172.19.158.26',
            database='hundundco',
            user='admin',
            password='Cr3ative'
        )
        cursor = db_connection.cursor()

        # SQL-Statement zum Einfügen der Daten
        query = "INSERT INTO deine_tabelle (spalte1, spalte2) VALUES (%s, %s)"
        # Hier müssen die Eingabewerte aus deinen Formularfeldern kommen
        data = (entry1.get(), entry2.get())

        # Daten in die Datenbank einfügen
        cursor.execute(query, data)
        db_connection.commit()

        # Erfolgsmeldung anzeigen
        messagebox.showinfo("Success", "Data inserted successfully.")

        # Verbindung schließen
        cursor.close()
        db_connection.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))

def clear_canvas():
    canvas_query.delete("text")


#########################################Code-Teil#########################################

# Database connection
try:
    db_connection = mysql.connector.connect(
        host='172.19.158.26',
        database='hundundco',
        user='admin',
        password='Cr3ative'
    )
    cursor = db_connection.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Database Connection Error", str(err))
    exit(1)

# Hier wird die Grösse und der Titel des Hauptfensters definiert
root = tk.Tk()
root.title("HundundCo")
root.geometry("800x600")

# Hier wird das Ausgabefenster definiert
result_label = tk.Label(root, text="Query Results:")
result_label.pack(pady=5)

# Hier wird das Canvas Widget für die Abfrageergebnisse definiert
canvas_query = tk.Canvas(root, width=400, height=200, bg="white")
canvas_query.pack(side="right", padx=10, pady=10, fill="both", expand=True)

# Hier wird das Canvas Widget für das Formular definiert
canvas_form = tk.Canvas(root, width=400, height=200, bg="lightgray")
canvas_form.pack(side="left", padx=10, pady=10, fill="both", expand=True)

# Formularfelder im Formular-Canvas erstellen
label1 = tk.Label(root, text="Feld 1:")
label1_window = canvas_form.create_window(50, 50, window=label1)

entry1 = tk.Entry(root)
entry1_window = canvas_form.create_window(150, 50, window=entry1)

label2 = tk.Label(root, text="Feld 2:")
label2_window = canvas_form.create_window(50, 100, window=label2)

entry2 = tk.Entry(root)
entry2_window = canvas_form.create_window(150, 100, window=entry2)

# Button zum Absenden des Formulars im Formular-Canvas erstellen
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button_window = canvas_form.create_window(150, 150, window=submit_button)

# Button zum Löschen der Abfrageergebnisse im Abfrageergebnis-Canvas erstellen
clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack(side="top", padx=10, pady=5)

# Diese Funktion wird als erstes gestartet, wenn das Programm startet
get_open_invoices()

# Dieser Prozess startet das GUI
root.mainloop()

# Am Ende wird die DB Verbindung geschlossen
cursor.close()
db_connection.close()
