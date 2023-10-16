import pandas as pd
import numpy as np


#creo nuovo dataframe con arrivi e partenze per gli agriturismi
df_arrivi_agriturismo = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/dati_turismo/Arrivi-negli-agriturismi-in-Italia-per-regione.csv', sep=';', encoding='latin1')
df_presenze_agriturismo = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/dati_turismo/Presenze-negli-agriturismi-in-Italia-per-regione.csv', sep=';', encoding='latin1')
colonna_arrivi_agriturismo = df_arrivi_agriturismo['Arrivi'].to_numpy()
df_presenze_agriturismo.insert(3, "arrivi", colonna_arrivi_agriturismo)
df_presenze_agriturismo.insert(4, "structure", 0)
#print(df_presenze_agriturismo)

#creo nuovo dataframe con arrivi e partenze per gli campeggi
df_arrivi_campeggio = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/dati_turismo/Arrivi-nei-campeggi-e-villaggi-turistici-in-italia-per-regione.csv', sep=';', encoding='latin1')
df_presenze_campeggio = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/dati_turismo/Presenze-nei-campeggi-e-villaggi-turistici-in-italia-per-regione.csv', sep=';', encoding='latin1')
colonna_arrivi_campeggio=df_arrivi_campeggio['Arrivi'].to_numpy()
df_presenze_campeggio.insert(3, "arrivi", colonna_arrivi_campeggio)
df_presenze_campeggio.insert(4, "structure", 2)
#print(df_presenze_campeggio)

#creo nuovo dataframe per alberghi
df_arrivi_albergo = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/dati_turismo/Arrivi-negli-esercizi-alberghieri-in-Italia-per-regione.csv', sep=';', encoding='latin1')
df_arrivi_albergo= df_arrivi_albergo.drop(df_arrivi_albergo[df_arrivi_albergo['Anno']== 2012].index)
df_presenze_albergo = pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/dati_turismo/Presenze-negli-agriturismi-in-Italia-per-regione.csv', sep=';', encoding='latin1')
colonna_arrivi_albergo = df_arrivi_albergo['Arrivi'].to_numpy()
df_presenze_albergo.insert(3, "arrivi", colonna_arrivi_albergo)
df_presenze_albergo.insert(4, "structure", 1)

#print(df_presenze_albergo)


#creo databse finale concatenando i dataset delle 3 strutture. Aggiungo una colonna con id crescente. Modifico nome colonne. 
final=[df_presenze_agriturismo, df_presenze_campeggio, df_presenze_albergo]
df=pd.concat(final)
df.insert(0, "id", range(0, 0+len(df)))
df.rename(columns = {'Regione':'region', 'Anno':'year', 'Presenze': 'presenze'}, inplace = True)
#print(df)

