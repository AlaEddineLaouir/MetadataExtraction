import xml.etree.ElementTree as ET

class licenceclass :
    def __init__(self, licence, lang ):
        self.licence=licence
        self.lang=lang


tree = ET.parse('Horacio_Quiroga_Cuentos.xml')
root = tree.getroot()


titleStmt = root.find('.//{http://www.tei-c.org/ns/1.0}titleStmt')
editionStmt = root.find('.//{http://www.tei-c.org/ns/1.0}editionStmt')
publicationStmt = root.find('.//{http://www.tei-c.org/ns/1.0}publicationStmt')
sourceDesc = root.find('.//{http://www.tei-c.org/ns/1.0}sourceDesc')


title = titleStmt.find('{http://www.tei-c.org/ns/1.0}title').text


author= titleStmt.find('{http://www.tei-c.org/ns/1.0}author')
authorSurName = author.find('{http://www.tei-c.org/ns/1.0}surname').text
authorGivenName = author.find('{http://www.tei-c.org/ns/1.0}forename').text



publisher = publicationStmt.find('{http://www.tei-c.org/ns/1.0}publisher').text

dateSubmitted = publicationStmt.find('{http://www.tei-c.org/ns/1.0}date').text

availability = publicationStmt.find('{http://www.tei-c.org/ns/1.0}availability')
licences =[]
for licence in availability.findall('{http://www.tei-c.org/ns/1.0}licence'):
    licenceText = ""
    licenceLang = ""
    licenceLang=licence.attrib['{http://www.w3.org/XML/1998/namespace}lang']
    for p in licence.findall('{http://www.tei-c.org/ns/1.0}p'):
        licenceText = licenceText + str.rstrip(p.text,"\n")
    licenceText=licenceText.rstrip("\n")
    licences.append(licenceclass(licenceText,licenceLang))





#################### Metadata API expression #############
#   "value": "string",
#   "lang": "string",
#   "typeUri": "string",
#   "propertyUri": "string"
##########################################################
metas = []

titleMeta = '{ "value": "'+title+'",\n "typeUri":"http://www.w3.org/2001/XMLSchema#xsd:string",\n"propertyUri": "http://purl.org/dc/terms/title" }'

metas.append(titleMeta)

authorMeta = '{ "value": { "givenname": "'+authorGivenName+'", "surname": "'+authorSurName+'" },\n"propertyUri": "http://purl.org/dc/terms/creator" }'

metas.append(authorMeta)

publisherMeta= '{ "value": "'+publisher+'",\n"propertyUri": "http://purl.org/dc/terms/publisher" }'

metas.append(publisherMeta)

dateSubmitted= '{ "value": "'+dateSubmitted+'",\n "typeUri":"http://www.w3.org/2001/XMLSchema#xsd:date",\n"propertyUri": "http://purl.org/dc/terms/dateSubmited" }'

metas.append(dateSubmitted)

for licenceData in licences :
    licenceMeta = '{ "value": "'+licenceData.licence+'",\n "typeUri":"http://www.w3.org/2001/XMLSchema#xsd:string",\n"propertyUri": "http://purl.org/dc/terms/dateSubmited",\n "lang": "'+licenceData.lang+'" }'
    metas.append(licenceMeta)

### enregistrement des metas dans fichier
metadataFile = open("metadate.txt","+w")
metadataFile.write('{"metas" :[')

for i, meta in enumerate(metas) :
    if i == len(metas) :
        metadataFile.write(meta+'\n')
    metadataFile.write(meta+',\n')


metadataFile.write(']}')
metadataFile.close()



