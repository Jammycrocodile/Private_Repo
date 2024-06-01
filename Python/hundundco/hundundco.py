import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HundundCo")
        self.geometry("800x600")
        self.locpull = ['ZH', 'AG']
        self.kurspull = ['Gruppenkurs','Privatkurs','Rückruftraining','Verhaltenstherapie', 'Hausbesuch', 'Online Kurs']
        self.form_filled = False
        self.db_connection = None
        self.cursor = None
        try:
            # Verbindung zur Datenbank herstellen
            self.db_connection = mysql.connector.connect(
                host='172.19.158.26',
                database='hundundco',
                user='admin',
                password='Cr3ative'
            )
            self.cursor = self.db_connection.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Connection Error", str(err))
            exit(1)
        self.create_widgets()

    def create_widgets(self):
        # Query Results Canvas
        self.canvas_query = tk.Canvas(self, width=400, height=200, bg="white")
        self.canvas_query.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        # New Client Button
        self.new_client = tk.Button(self, text="Neuer Kunde", command=self.create_client_form)
        self.new_client.pack(side="top", padx=10, pady=5)

        # New Course Visit Button
        self.new_course_visit = tk.Button(self, text="Neuer Kursbesuch", command=self.create_course_visit_form)
        self.new_course_visit.pack(side="top", padx=10, pady=5)

    def submit_course_visit(self):
    # Deine bestehenden Codezeilen hier...

    # Wenn das neue Abo weniger als oder gleich 2 ist, erstelle eine E-Mail
    if abo_state == 2:
        self.send_email_alert(givenname, surname, abo_state)

    def clear_canvas_form(self):
        if hasattr(self, 'canvas_form'):
            self.canvas_form.destroy()

    def create_client_form(self):
        self.clear_canvas_form()
        self.form_filled = True
        # Canvas Widget for the formula
        self.canvas_form = tk.Canvas(self, width=400, height=200, bg="lightgray")
        self.canvas_form.pack(side="left", padx=10, pady=10, fill="both", expand=True)

        # All Form fields 
        self.givenname_label = tk.Label(self, text="Vorname:")
        self.givenname_label_window = self.canvas_form.create_window(50, 50, window=self.givenname_label)

        self.givenname_sql = tk.Entry(self)
        self.givenname_sql_window = self.canvas_form.create_window(150, 50, window=self.givenname_sql)

        self.surname_label = tk.Label(self, text="Nachname:")
        self.surname_label_window = self.canvas_form.create_window(50, 100, window=self.surname_label)

        self.surname_sql = tk.Entry(self)
        self.surname_sql_window = self.canvas_form.create_window(150, 100, window=self.surname_sql)

        self.location_label = tk.Label(self, text="Ort:")
        self.location_label_window = self.canvas_form.create_window(50, 150, window=self.location_label)

        #Location is as Pulldown to minimizes errors
        self.location_sql = ttk.Combobox(self, values=self.locpull)
        self.location_sql.current(0)  # Setze den Standardwert auf das erste Element der Liste
        self.location_sql_window = self.canvas_form.create_window(150, 150, window=self.location_sql)

        self.dog_label = tk.Label(self, text="Hundename:")
        self.dog_label_window = self.canvas_form.create_window(50, 200, window=self.dog_label)

        self.dog_sql = tk.Entry(self)
        self.dog_sql_window = self.canvas_form.create_window(150, 200, window=self.dog_sql)

        self.mail_label = tk.Label(self, text="E-Mail:")
        self.mail_label_window = self.canvas_form.create_window(50, 250, window=self.mail_label)

        self.mail_sql = tk.Entry(self)
        self.mail_sql_window = self.canvas_form.create_window(150, 250, window=self.mail_sql)

        self.phone_label = tk.Label(self, text="Telefon:")
        self.phone_label_window = self.canvas_form.create_window(50, 300, window=self.phone_label)

        self.phone_sql = tk.Entry(self)
        self.phone_sql.insert(0, '+41')
        self.phone_sql_window = self.canvas_form.create_window(150, 300, window=self.phone_sql)

        # Button for adding the values to the db
        self.submit_button = tk.Button(self, text="Submit", command=self.submit_new_client)
        self.submit_button_window = self.canvas_form.create_window(100, 350, window=self.submit_button)

    def create_course_visit_form(self):
        self.clear_canvas_form()
        # Canvas Widget for the course visit form
        self.canvas_form = tk.Canvas(self, width=400, height=200, bg="lightgray")
        self.canvas_form.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    
        # Labels and Entry fields for the form
        self.givenname_label = tk.Label(self, text="Vorname:")  # ÄNDERUNG: Vorname-Feld hinzugefügt
        self.givenname_label_window = self.canvas_form.create_window(50, 50, anchor='w', window=self.givenname_label)

        self.givenname_sql = tk.Entry(self)  # ÄNDERUNG: Vorname-Feld hinzugefügt
        self.givenname_sql_window = self.canvas_form.create_window(150, 50, anchor='w', window=self.givenname_sql)

        self.surname_label = tk.Label(self, text="Nachname:")  # ÄNDERUNG: Nachname-Feld hinzugefügt
        self.surname_label_window = self.canvas_form.create_window(50, 80, anchor='w', window=self.surname_label)

        self.surname_sql = tk.Entry(self)  # ÄNDERUNG: Nachname-Feld hinzugefügt
        self.surname_sql_window = self.canvas_form.create_window(150, 80, anchor='w', window=self.surname_sql)

        self.kurs_label = tk.Label(self, text="Kurs:")
        self.kurs_label_window = self.canvas_form.create_window(50, 110, anchor='w', window=self.kurs_label)

        self.kurs_sql = ttk.Combobox(self, values=self.kurspull)
        self.kurs_sql.current(0)  
        self.kurs_sql_window = self.canvas_form.create_window(210, 110, window=self.kurs_sql)

        self.duration_label = tk.Label(self, text="Dauer:")
        self.duration_label_window = self.canvas_form.create_window(50, 140, anchor='w', window=self.duration_label)

        self.duration_sql = tk.Entry(self)
        self.duration_sql.insert(0,60)
        self.duration_sql_window = self.canvas_form.create_window(150, 140, anchor='w', window=self.duration_sql)
        
        self.kursdatum_label = tk.Label(self, text="Kursdatum:")
        self.kursdatum_label_window = self.canvas_form.create_window(50, 170, anchor='w', window=self.kursdatum_label)
    
        self.current_date = datetime.now().strftime("%d.%m.%Y")
        self.kursdatum_entry = tk.Entry(self)
        self.kursdatum_entry.insert(0, self.current_date)
        self.kursdatum_entry_window = self.canvas_form.create_window(150, 170, anchor='w', window=self.kursdatum_entry)
    
        self.submit_course_visit_button = tk.Button(self, text="Submit", command=self.submit_course_visit)
        self.submit_course_visit_button_window = self.canvas_form.create_window(80, 220, anchor='w', window=self.submit_course_visit_button)

    def submit_new_client(self):
        #Mache gewisse Felder pflichtfelder
        if not self.givenname_sql.get() or not self.surname_sql.get() or not self.mail_sql.get():
            messagebox.showerror("Error", "Vorname, Nachname und Mail sind Pflichtfelder")
            return
        
        try:
            # SQL-Statement zum Einfügen der Daten
            query = "INSERT INTO clients (vorname, nachname, ort, hundename, mail, telefonnummer) VALUES (%s, %s, %s, %s, %s, %s)"
            # Hier müssen die Eingabewerte aus deinen Formularfeldern kommen
            data = (
                self.givenname_sql.get(), 
                self.surname_sql.get(), 
                self.location_sql.get(), 
                self.dog_sql.get(), 
                self.mail_sql.get(), 
                self.phone_sql.get()
            )

            # Daten in die Datenbank einfügen
            self.cursor.execute(query, data)
            self.db_connection.commit()

            # Erfolgsmeldung anzeigen
            messagebox.showinfo("Success", "Kunde wurde erfolgreich in die DB gesichert.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Etwas ist schief gelaufen: {err}")

    def submit_course_visit(self):
        givenname = self.givenname_sql.get()
        surname = self.surname_sql.get()
        kurs = self.kurs_sql.get()
        kursdatum = self.kursdatum_entry.get()
        dauer = self.duration_sql.get()

        #Mache gewisse Felder pflichtfelder
        if not self.givenname_sql.get() or not self.surname_sql.get() or not self.kurs_sql.get() or not self.kursdatum_entry.get():
            messagebox.showerror("Error", "Vorname, Nachname, Kurs und Kursdatum sind Pflichtfelder")
            return

        try:
            # SQL-Statement zum Abrufen der client_id basierend auf Vorname und Nachname
            query_client = "SELECT client_id FROM clients WHERE vorname = %s AND nachname = %s"  # ÄNDERUNG: client_id durch Vorname und Nachname abfragen
            self.cursor.execute(query_client, (givenname, surname))
            client_result = self.cursor.fetchone()

            try:
                kursdatum = datetime.strptime(kursdatum, "%d.%m.%Y").strftime("%Y-%m-%d")  # ÄNDERUNG: Datumskonvertierung
            except ValueError:
                messagebox.showerror("Error", "Bitte das Kursdatum im Format dd.mm.YYYY eingeben.")
                return
        
            if client_result:
                client_id = client_result[0]

                # SQL-Statement zum Einfügen der Kursbesuchsdaten
                insert = "INSERT INTO kursbesuch (client_id, kurs_id, kursdatum, kursdauer_in_min) VALUES (%s, %s, %s, %s)"
                # Hier müssen die Eingabewerte aus deinem Formularfeld kommen
                kurs_id = self.get_kurs_id(kurs)  # ÄNDERUNG: Kurs ID abrufen
                data = (client_id, kurs_id, kursdatum, dauer)

                # Daten in die Datenbank einfügen
                self.cursor.execute(insert, data)
                self.db_connection.commit()

                query_abo = "SELECT aboanzahl FROM clients WHERE client_id = %s"
                self.cursor.execute(query_abo, (client_id,))
                abo_result = self.cursor.fetchone()
                

                #Bei vorhandenen Abo und Gruppenkurse, wird das Abo nach einem Kursbesuch direkt vom Kunden abgezogen    
                if abo_result is not None and abo_result[0] is not None:
                    aboanzahl = abo_result[0]
                else:
                    aboanzahl = 0

                if kurs == "Gruppenkurs" and aboanzahl > 0:
                    current_abo = abo_result[0]
                    abo_state = current_abo - 1
                    messagebox.showinfo(f"{givenname} {surname} hat noch {abo_state} Abos übrig")
                    update_query = "UPDATE clients SET aboanzahl = %s WHERE client_id = %s"
                    self.cursor.execute(update_query, (abo_state, client_id))
                    self.db_connection.commit()
                else:
                    messagebox.showerror("Error", "kein abo übrig")

                # Erfolgsmeldung anzeigen
                messagebox.showinfo("Success", f"Kursbesuch für {givenname} {surname} wurde erfolgreich gesichert.")
            else:
                messagebox.showerror("Error", f"Kunde {givenname} {surname} wurde nicht gefunden. Bitte Kunde zuerst anlegen.")  # ÄNDERUNG: Fehlermeldung bei nicht gefundenem Kunden

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Etwas ist schief gelaufen: {err}")
    
    def get_kurs_id(self, kursname):
        kursname = self.kurs_sql.get()
        try:
            query = "SELECT kurs_id FROM kurse WHERE kurse = %s"  # ÄNDERUNG: Kurs ID abfragen
            self.cursor.execute(query, (kursname,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            else:
                messagebox.showerror("Error", f"Kurs '{kursname}' nicht in der DB gefunden.")
                return None
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Etwas ist schief gelaufen: {err}")
            return None

    def get_open_invoice(self):
        try:
            # Hier den Code für die Abfrage der offenen Rechnungen einfügen
            # Beispiel:
            query = """
            SELECT clients.vorname, clients.nachname, DATE_FORMAT(rechnungen.rechnungsdatum, '%d.%m.%Y')
            FROM clients
            JOIN rechnungen ON clients.client_id = rechnungen.client_id
            WHERE rechnungen.rechnung_bezahlt = FALSE;
            """
            self.cursor.execute(query)
            result = self.cursor.fetchall()

            # Clear previous results
            self.canvas_query.delete("text")

            # Überschrift über den Headern des Canvas anzeigen
            text_x = 50
            text_y = 50
            self.canvas_query.create_text(text_x, text_y, text="Offene Rechnungen", font=("Arial", 14, "bold"), anchor="w", tags="text")

            # Display rows
            x_start = 50  # Startposition für Datenzeilen
            y_start = 100
            row_height = 30  # Höhe jeder Datenzeile
            column_width = 100  # Breite jeder Spalte
            for row in result:
                x_position = x_start
                for item in row:
                    self.canvas_query.create_text(x_position, y_start, text=item, anchor="w", tags="text")
                    x_position += column_width  # Spaltenabstand
                y_start += row_height  # Zeilenabstand
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Query Fehler: {err}")

app = Application()
app.mainloop()
