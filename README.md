<h1>Riconciliazione Contatti</h1>
<p>La riconciliazione dei contatti mira a raccogliere tutte le informazioni da diversi record di una base dati (file CSV) e integrarle in un unico record completo.</p></br>
Il flusso consiste in
<li>raccogliere utti i record con lo stesso identificatore univoco (per esempio la mail principale)</li>
<li>eleggere il più completo a record finale(master)</li>
<li>leggere successivamente tutti i rimanenti record per estrarre informazioni che non sono presenti nel master ed aggiungerle</li>
<li>marcare con un cambp per indicare che è stata effettuata un'operazione di merge</li>
<p>Questo programma utilizza la libreria <b>pandas</b> per gestire il Merge Selettivo: identifica i duplicati (basandosi sull'email), unisce le informazioni mancanti tra i record simili e contrassegna i nuovi record fusi con lo stato "Da Revisionare".</p>
<p>Per installare la libreria usare</br>pip install pandas</p></br>
<h2>Logica selettiva</h2>
Come funziona la logica "Selettiva"
<li>sort_values + count_nulls: Il programma conta quanti "buchi" (campi vuoti) ha ogni riga. Mette in cima i record più completi.</li>
<li>groupby().first(): Questa è la magia. Per ogni gruppo di email uguali, Python guarda la colonna "Telefono". Se la prima riga è vuota, passa alla seconda, e così via, finché non trova un numero. In questo modo "riempie i buchi" usando i dati dei duplicati meno completi.</li>
<li>Stato Revisione: Se il programma nota che per un'email c'erano originariamente più righe, marchia il risultato come "Da Revisionare". Questo ti protegge dalla Sindrome di Superiorità algoritmica: l'ultima parola resta a te.</li><br></br>
Se il file CSV di Outlook ha le intestazioni diverse (es. in italiano "Indirizzo di posta elettronica"), bisogna cambiare la variabile chiave_duplicati nello script con il nome esatto della colonna.
<h2>Generazione di casi di prova</h2>
Il programma crea_dataset_con_duplicati.py genera un file csv con 100 linee di contatti, di cui 10 sono contatti duplicati.</br>
Ad esempio uno ha l'indirizzo dell'ufficio e l'altro ha il numero di telefono.</br>
Esegui lo script di Merge: Passa questo file contatti_duplicati_test.csv attraverso lo script di pulizia che abbiamo scritto nei messaggi precedenti.</br>
Cosa aspettarsi:</br>
<li>Il file finale deve avere 90 righe (80 originali + 10 fusi).</li>
<li>I 10 record "UserDupl" devono contenere sia il numero di telefono (preso dal record A) sia l'azienda e la città (presi dal record B).</li>
<li>Il campo "Stato Revisione" deve essere valorizzato su "Da Revisionare" solo per questi 10 record.</li>
