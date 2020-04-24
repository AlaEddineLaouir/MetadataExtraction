import pandas as pd

#####   the csv file is renamed to DonneesJC
myFile = pd.read_csv("DonneesJC.csv", header=None )

### Map column name to corresponding http://purl.org/dc/terms term ##########
dictionary = {
    "Type": "type", "DataType":"type", "Dates":"date", "Titre":"title", "Auteur":"creator", "Sujet":"subject",
    "Description":"description", "Résumé":"abstract",  "Droits":"rights","Ayants-droit":"rightsHolder",
    "Format" : "format", "Langue" :"language","Représentation":"description","Contexte géographique":"Location",
    "Périodicité":"accrualPeriodicity"
}
myFile.columns = myFile.iloc[0]

metadataFile = open("metadate2.txt", "+w")

for index, row in myFile.iterrows() :
    if index == 1 : ## to make sur the first row only is processed
        rowMetaArray = []
        for term in dictionary.keys() :
            info = row[term]
            if str(info) != "" and str(info) != 'nan':
                meta = '{ "value": "'+str(info)+'",\n"propertyUri": "http://purl.org/dc/terms/'+dictionary.get(term)+'" }'
                rowMetaArray.append(meta)
        ### enregistrement des metas dans fichier
        metadataFile.write('{ "metas":[ \n')
        for i, meta in enumerate(rowMetaArray):
            if i == len(rowMetaArray):
                metadataFile.write(meta + '\n')
            metadataFile.write(meta + ',\n')
        break

metadataFile.write(']}')
metadataFile.close()



