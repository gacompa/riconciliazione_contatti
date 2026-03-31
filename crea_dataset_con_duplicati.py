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
contact_names=["Adele","Alberto","Alessandro","Alessia","Alessio","Alice","Andrea","Angela","Anita","Anna",
"Antonio","Arianna","Aurora","Beatrice","Bianca","Camilla","Caterina","Cesare","Chiara","Christian","Clara",
"Claudia","Claudio","Cristina","Damiano","Daniele","Davide","Diletta","Edoardo","Elena","Eleonora","Elisa","Emanuele","Emma",
"Enrico","Ester","Ettore","Fabio","Federica","Federico","Filippo","Francesca","Francesco","Gabriele","Gaia",
"Giacomo","Ginevra","Giorgia","Giorgio","Giovanni","Giulia","Giuseppe","Greta","Ilaria","Jacopo","Laura",
"Leonardo","Lorenzo","Luca","Lucia","Ludovica","Ludovico","Manuel","Marco","Maria","Marta","Martina","Matilde",
"Matteo","Mattia","Maurizio","Michele","Miriam","Nicola","Noemi","Paola","Paolo","Pietro","Raffaele","Rebecca",
"Riccardo","Roberta","Roberto","Rosa","Salvatore","Samuele","Sara","Sebastiano","Serena","Silvia","Simona",
"Simone","Sofia","Stefano","Tancredi","Tommaso","Valentina","Valerio","Vincenzo","Vittoria"
]
contact_surnames=["Amato","Anderson","Barbera","Barbieri","Barone","Bauer","Becker","Benedetti","Bernardi",
"Bianchi","Brown","Bruno","Caputo","Carbone","Caruso","Cattaneo","Colombo","Conti","Costa","D’Amico","Davis",
"De Luca","De Santis","Donati","Esposito","Farina","Ferrara","Ferrari","Ferri","Fiore","Fischer","Fontana",
"Franceschini","Galli","Gallo","Gatti","Gentile","Giordano","Giuliani","Grassi","Greco","Guerra","Hoffmann",
"Johnson","Jones","Klein","Koch","Leone","Lombardi","Longo","Mancini","Mariani","Marini","Marino","Martini",
"Martino","Mazza","Meyer","Miller","Montanari","Monti","Morelli","Moretti","Moretti","Müller","Negri",
"Pagano","Palmieri","Palumbo","Pellegrini","Pellegrino","Ricci","Richter","Rinaldi","Riva","Rizzi","Rizzo",
"Romano","Rossetti","Rossi","Russo","Sanna","Santoro","Schäfer","Schmidt","Schneider","Schulz","Serra","Silvestri",
"Smith","Taylor","Testa","Tosi","Valentini","Vitale","Vitali","Wagner","Weber","Williams","Wilson"
]
contact_company=["NexaCore Solutions","SkyNetix Systems","ByteFlow Digital","PrismLogic IT","Vertex Innovations","CloudArc Technologies",
"DataPulse Analytics","CyberShield Pro","Quantum Leap Soft","BitStream Global","IronCode Labs","NanoWave Tech","Synapse Robotics",
"Vector Dynamics","AlphaGrid Systems","BlueHorizon Strategy","Zenith Consulting","Peak Performance Partners","Global Bridge Group",
"Meridian Advisory","Sterling Asset Management","Nexus Business Hub","Vantage Point Services","KeyStone Operations","BrightPath Consulting",
"CoreValues Group","Insight Partners","Milestone Management","Catalyst Solutions","Elite Vision Group","SteelForge Industries","TerraMove Logistics",
"AeroStream Manufacturing","PowerGrid Energy","EcoFlow Resources","Titan Heavy Equipment","Global Cargo Express","SolidFoundations Construction",
"Precision Parts Ltd.","OceanBlue Shipping","GreenHarvest Foods","PureNature Organics","UrbanBites Catering","DailyFresh Markets","Velvet Touch Retail",
"Global Gourmet Imports","PrimeSelection Goods","Vitality Health Foods","MountainSpring Beverages","Artisan Heritage Co."
]
data = []

# --- 1. I "GEMELLI CATTIVI" (10 COPPIE / 20 RECORD) ---
# Obiettivo: Testare la sensibilità al Case (Maiuscole) e agli spazi
for i in range(10):
    email_base = f"nomeduplicato_{i}@example.it"
    
    # Record A: Tutto minuscolo e con spazi extra
    row_a = {col: "" for col in columns}
    row_a["First Name"] = "  alessandro  " # Spazi prima e dopo
    row_a["Last Name"] = "ROSSINI"
    row_a["E-mail Address"] = email_base.lower() 
    row_a["Mobile Phone"] = "3471234567" # Senza prefisso
    data.append(row_a)

    # Record B: Mix di maiuscole e spazi diversi
    row_b = {col: "" for col in columns}
    row_b["First Name"] = "Alessandro"
    row_b["Last Name"] = "rossini " # Spazio alla fine
    row_b["E-mail Address"] = f"  {email_base.upper()}  " # Maiuscolo e spazi
    row_b["Company"] = "NexaCore SOLUTIONS"
    row_b["Mobile Phone"] = "+39 347.123.4567" # Formato diverso
    data.append(row_b)

# --- 2. IL RESTO DEL DATASET (80 RECORD) ---
for i in range(80):
    row = {col: "" for col in columns}
    row["First Name"] = random.choice(contact_names)
    row["Last Name"] = random.choice(contact_surnames)
    company_user= random.choice(contact_company)
    row["Company"] = company_user
    row["E-mail Address"] = f"user_{i}@{company_user.replace(' ', '').lower().strip()}.test.com"
    if i < 60:
        row["Mobile Phone"] = f"+39 {random.randint(300, 399)} {random.randint(100000, 999999)}"
    data.append(row)

df = pd.DataFrame(data, columns=columns)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('contatti_originale.csv', index=False, encoding='utf-8')

print("File 'contatti_originale.csv' generato con trappole di formattazione.")
