import pandas as pd
import random

# Colonne basate sulla tua immagine
columns = [
    "First Name", "Middle Name", "Last Name", "Title", "Suffix", "Nickname",
    "Given Yomi", "Surname Yomi", "E-mail Address", "E-mail 2 Address",
    "E-mail 3 Address", "Home Phone", "Home Phone 2", "Business Phone",
    "Business Phone 2", "Mobile Phone", "Car Phone", "Other Phone",
    "Primary Phone", "Pager", "Business Fax", "Home Fax", "Other Fax",
    "Company Main", "Callback", "Radio Phone", "Telex", "TTY/TDD Phone",
    "IMAddress", "Job Title", "Department", "Company", "Office Location",
    "Manager's Name", "Assistant's Name", "Assistant's Phone", "Company Yomi",
    "Business Street", "Business City", "Business State", "Business Postal Code",
    "Business Country", "Home Street", "Home City", "Home State",
    "Home Postal Code", "Home Country", "Other Street", "Other City",
    "Other State", "Other Postal Code", "Other Country", "Personal Web Page",
    "Spouse", "Schools", "Hobby", "Location", "Web Page", "Birthday",
    "Anniversary", "Notes"
]

data = []

# --- 1. I "GEMELLI CATTIVI" (10 COPPIE / 20 RECORD) ---
# Obiettivo: Testare la sensibilità al Case (Maiuscole) e agli spazi
for i in range(10):
    email_base = f"Cattivo_{i}@SindromeFortino.it"
    
    # Record A: Tutto minuscolo e con spazi extra
    row_a = {col: "" for col in columns}
    row_a["First Name"] = "  alessandro  " # Spazi prima e dopo
    row_a["Last Name"] = "ROSSI"
    row_a["E-mail Address"] = email_base.lower() 
    row_a["Mobile Phone"] = "3471234567" # Senza prefisso
    data.append(row_a)

    # Record B: Mix di maiuscole e spazi diversi
    row_b = {col: "" for col in columns}
    row_b["First Name"] = "Alessandro"
    row_b["Last Name"] = "rossi " # Spazio alla fine
    row_b["E-mail Address"] = f"  {email_base.upper()}  " # Maiuscolo e spazi
    row_b["Company"] = "NexaCore SOLUTIONS"
    row_b["Mobile Phone"] = "+39 347.123.4567" # Formato diverso
    data.append(row_b)

# --- 2. IL RESTO DEL DATASET (80 RECORD) ---
for i in range(80):
    row = {col: "" for col in columns}
    row["First Name"] = random.choice(["Marco", "Elena", "Klaus", "John"])
    row["Last Name"] = random.choice(["Bianchi", "Müller", "Smith", "Ferrari"])
    row["E-mail Address"] = f"user_{i}@test.com"
    if i < 60:
        row["Mobile Phone"] = f"+39 {random.randint(300, 399)} {random.randint(100000, 999999)}"
    data.append(row)

df = pd.DataFrame(data, columns=columns)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('contatti_variante_cattiva.csv', index=False, encoding='utf-8')

print("File 'contatti_variante_cattiva.csv' generato con trappole di formattazione.")
