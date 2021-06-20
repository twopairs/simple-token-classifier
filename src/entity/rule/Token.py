class Token:

    def __init__(self, ctx, raw, type):
        self.ctx = ctx
        if raw == None or raw == "":
            print(" token is null or empty")
            exit(-1)

        self.type = type
        self.token = raw

        self.list = []
        st = self.token.split(" ")
        for t in st:
            if t.strip() == "":
                continue
            self.list.append(t)

    def getTokenLength(self):
        return len(self.list)

    def getTokenList(self):
        return self.list

    def getOrderInfo(self):
        return self.type

    def toString(self, prefix = ""):
        return prefix + "[" + self.token + "] len=(" + str(len(self.list)) + ") " + self.type








