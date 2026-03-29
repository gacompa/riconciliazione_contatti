import pandas as pd
import random
import numpy as np

# Colonne esatte dalla tua immagine
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

# --- GENERAZIONE DEI PRIMI 80 RECORD (Standard) ---
for i in range(80):
    row = {col: "" for col in columns}
    row["First Name"] = random.choice(["Alessandro", "Sofia", "Leonardo", "Giulia"])
    row["Last Name"] = random.choice(["Rossi", "Ferrari", "Russo", "Smith"])
    
    # 95% hanno la mail (quindi qui quasi tutti)
    row["E-mail Address"] = f"test{i}@progetto-it.com"
    
    # 75% hanno il telefono (60 su 80 qui)
    if i < 60:
        prefisso = "+39" if i > 15 else "+44"
        row["Mobile Phone"] = f"{prefisso} 34{random.randint(10,99)} {random.randint(1000,9999)}"
        
    data.append(row)

# --- GENERAZIONE DEI 10 "GEMELLI" (20 RECORD TOTALI) ---
# Creiamo 10 coppie che condividono la stessa mail ma hanno dati diversi
for i in range(10):
    email_comune = f"duplicato_test_{i}@azienda.it"
    nome = f"UserDupl{i}"
    cognome = f"TestMerge{i}"

    # Versione A: Ha il Telefono ma NON l'indirizzo/azienda
    row_a = {col: "" for col in columns}
    row_a["First Name"], row_a["Last Name"], row_a["E-mail Address"] = nome, cognome, email_comune
    row_a["Mobile Phone"] = "+39 012345678"
    row_a["Notes"] = "Nota presente solo nel record A"
    data.append(row_a)

    # Versione B: Ha Azienda e Job Title ma NON il telefono
    row_b = {col: "" for col in columns}
    row_b["First Name"], row_b["Last Name"], row_b["E-mail Address"] = nome, cognome, email_comune
    row_b["Company"] = "NexaCore Solutions"
    row_b["Job Title"] = "Senior Consultant"
    row_b["Business City"] = "Milano"
    data.append(row_b)

# --- SALVATAGGIO ---
df = pd.DataFrame(data, columns=columns)
# Mescoliamo i record per non averli tutti in fila (test più realistico)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('contatti_duplicati_test.csv', index=False, encoding='utf-8')

print("Dataset generato: 100 righe totali con 10 coppie di duplicati da fondere.")
