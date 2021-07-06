import entity.meta.MetaResult

class ClassificationResult:

    def __init__(self):
        self.metaResultList = []
        self.unusedTokenList = []

    def putMetaResult(self, mr):
        if not isinstance(mr, entity.meta.MetaResult.MetaResult):
            print("should be MetaResult Type")
            raise

        self.metaResultList.append(mr)

    def putUnusedToken(self, t):
        self.unusedTokenList.append(t)

    def getMetaResultList(self):
        return self.metaResultList

    def getUnusedTokenList(self):
        return self.unusedTokenList