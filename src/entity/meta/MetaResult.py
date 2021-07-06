class MetaResult:

    def __init__(self):
        self.usedToken = None
        self.metaList = []

    def getMetaList(self):
        return self.metaList

    def setUsedToken(self, ut):
        self.usedToken = ut

    def getUsedToken(self):
        return self.usedToken

    def addMeta(self, meta):
        self.metaList.append(meta)

    def toString(self):
        l = []
        for meta in self.metaList:
            l.append(meta)
            l.append(" ")
        return ''.join(l)
