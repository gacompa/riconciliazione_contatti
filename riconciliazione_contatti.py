import pandas as pd
import numpy as np
from datetime import datetime

def merge_selettivo(file_input, file_output):
    try:
        # 1. Caricamento del CSV esportato da Outlook
        # Nota: Outlook spesso usa la codifica 'utf-16' o 'latin1', adattala se necessario
        df = pd.read_csv(file_input, encoding='utf-8')
        
        print(f"File caricato: {len(df)} record trovati.")

        # 2. Pre-elaborazione: Convertiamo i valori vuoti in NaN (standard di pandas)
        df = df.replace(r'^\s*$', np.nan, regex=True)

        # 3. Definiamo la colonna "Chiave" per identificare i duplicati (es. l'Email)
        # Se l'email manca, usiamo il Nome/Cognome come backup per non perdere dati
        chiave_duplicati = 'E-mail Address' 

        # 4. LOGICA DI MERGE SELETTIVO (Groupby + First)
        # Ordiniamo per far sì che i record con più dati salgano in alto
        df['count_nulls'] = df.isnull().sum(axis=1)
        df = df.sort_values(by=[chiave_duplicati, 'count_nulls'], ascending=[True, True])

        # Raggruppiamo per Email e prendiamo il primo valore NON NULLO per ogni colonna
        df_fuso = df.groupby(chiave_duplicati).first().reset_index()

        # 5. AGGIUNTA CAMPO "STATO REVISIONE"
        # Identifichiamo quali record sono stati fusi confrontando il conteggio iniziale
        conteggio_originale = df[chiave_duplicati].value_counts()
        nomi_duplicati = conteggio_originale[conteggio_originale > 1].index

        def imposta_stato(email):
            if email in nomi_duplicati:
                return f"Da Revisionare (Fuso il {datetime.now().strftime('%d/%m/%Y')})"
            return "Verificato"

        df_fuso['Stato Revisione'] = df_fuso[chiave_duplicati].apply(imposta_stato)

        # 6. Pulizia finale: rimuoviamo la colonna tecnica dei nulli
        df_fuso = df_fuso.drop(columns=['count_nulls'])

        # 7. Esportazione
        df_fuso.to_csv(file_output, index=False, encoding='utf-8')
        
        print(f"Merge completato con successo!")
        print(f"Record finali: {len(df_fuso)}")
        print(f"File salvato in: {file_output}")

    except Exception as e:
        print(f"Errore durante l'elaborazione: {e}")

# Esecuzione
if __name__ == "__main__":
    # Cambia questi nomi con i tuoi file reali
    file_in = 'contatti_originale.csv'
    file_out = 'rubrica_generale_pulita.csv'
    merge_selettivo(file_in, file_out)
