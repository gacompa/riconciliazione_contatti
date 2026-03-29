<h1>Riconciliazione Contatti</h1>
<p>La riconciliazione dei contatti mira a raccogliere tutte le informazioni da diversi record di una base dati (file CSV) e integrarle in un unico record completo.</p></br>
Il flusso consiste in
<li>raccogliere utti i record con lo stesso identificatore univoco (per esempio la mail principale)</li>
<li>eleggere il più completo a record finale(master)</li>
<li>leggere successivamente tutti i rimanenti record per estrarre informazioni che non sono presenti nel master ed aggiungerle</li>
<li>marcare con un cambp per indicare che è stata effettuata un'operazione di merge</li>
