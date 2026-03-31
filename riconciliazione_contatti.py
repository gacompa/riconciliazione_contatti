import pandas as pd
import pandas as pd
import numpy as np
import re
from datetime import datetime

def clean_phone(phone):
    """Rimuove caratteri non numerici per facilitare il confronto dei telefoni."""
    if pd.isna(phone) or str(phone).strip() == "":
        return ""
    return re.sub(r'\D', '', str(phone))

def merge_contatti(file_input, file_output):
    try:
        # 1. Caricamento del file CSV
        df = pd.read_csv(file_input, encoding='utf-8')
        print(f"--- Inizio Elaborazione: {len(df)} record caricati ---")

        # 2. NORMALIZZAZIONE (Sconfiggiamo la 'Variante Cattiva')
        # Trasformiamo stringhe vuote o spazi in NaN reali per usare la funzione combine_first
        df = df.replace(r'^\s*$', np.nan, regex=True)

        # Pulizia Email: tutto minuscolo e senza spazi ai lati
        df['E-mail Address'] = df['E-mail Address'].astype(str).str.lower().str.strip()
        
        # Pulizia Nomi e Cognomi: Capitalize e Trim
        df['First Name'] = df['First Name'].astype(str).str.strip().str.capitalize()
        df['Last Name'] = df['Last Name'].astype(str).str.strip().str.capitalize()

        # 3. IDENTIFICAZIONE DUPLICATI
        # Contiamo quante volte appare ogni email per impostare lo Stato Revisione dopo
        counts = df['E-mail Address'].value_counts()
        emails_duplicate = counts[counts > 1].index.tolist()

        # 4. LOGICA DI MERGE SELETTIVO
        # Ordiniamo i record: quelli con più dati (meno NaN) vanno in alto
        df['null_count'] = df.isnull().sum(axis=1)
        df = df.sort_values(by=['E-mail Address', 'null_count'], ascending=[True, True])

        # Raggruppiamo per Email e usiamo 'first' per prendere il primo valore non nullo disponibile
        # Questo "riempie i buchi" dei record principali usando i dati dei duplicati
        df_merged = df.groupby('E-mail Address', as_index=False).first()

        # 5. AGGIUNTA CAMPO "STATO REVISIONE"
        def definisci_stato(row):
            email = row['E-mail Address']
            if email in emails_duplicate:
                return f"DA REVISIONARE: Fuso il {datetime.now().strftime('%d/%m/%Y')}"
            return "Verificato"

        df_merged['Stato Revisione'] = df_merged.apply(definisci_stato, axis=1)

        # 6. PULIZIA FINALE
        # Rimuoviamo colonne tecniche e ripristiniamo i valori "nan" come stringhe vuote per Outlook
        df_merged = df_merged.drop(columns=['null_count'])
        df_merged = df_merged.fillna("")

        # 7. SALVATAGGIO
        df_merged.to_csv(file_output, index=False, encoding='utf-8')
        
        print(f"--- Elaborazione Completata ---")
        print(f"Record originali: {len(df)}")
        print(f"Record dopo il merge: {len(df_merged)}")
        print(f"File salvato: {file_output}")

    except Exception as e:
        print(f"Errore critico: {e}")

if __name__ == "__main__":
    file_in = 'contatti_originale.csv' # Il file generato prima
    file_out = 'rubrica_generale_pulita.csv'
    merge_contatti(file_in, file_out)
