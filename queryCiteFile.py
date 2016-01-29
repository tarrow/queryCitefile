import csv,io

class CiteFile():
    global csvfileinmem
    csvfileinmem = None

    def __init__(self):
        self.filename = "C:\git\wikieupmcanalytics\citations-enwiki-20151002.csv"
        self.csvfile = open(self.filename, "r", encoding='utf-8', newline='\r\n')
        global csvfileinmem
        if csvfileinmem == None:
            csvfileinmem = self.csvfile.read()
        self.csvreader = csv.reader(csvfileinmem.splitlines(), delimiter='\t')

    def findPagesIDAppears(self, id ):
        """Given an ID return list of articles which cite it

        :param id: string of id to search for
        :return: list of articles
        """
        if id[:3] == 'PMC':
            id = id[3:]
        articles = list()
        for row in self.csvreader:
            if row[5] == id and row[4] == 'pmc':
                articles.append(row[1])
        return articles

    def findRowsWithIDType(self ,type, inlist = None):
        if inlist == None: inlist = self.csvreader
        outlist = list()
        for row in inlist:

            if row[4] == type:
                outlist.append(row)
        return outlist

    def findRowsWithID(self, id, inlist = None):
        if inlist == None: inlist = self.csvreader
        outlist = list()
        for row in inlist:
            if row[5] == id:
                outlist.append(row)
        return outlist

    def findRowsWithArticle(self, article, inlist = None):
        if inlist == None: inlist = self.csvreader
        for row in inlist:
            outlist = list()
            if row[2] == article:
                outlist.append(row)
        return outlist