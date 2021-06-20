import entity.rule.TokenCodePair

class InvertedDimension:

    def __init__(self, ctx, list):
        self.ctx = ctx
        self.invertedMap = {}
        for i in range(1, self.ctx.const.MAX_LOOKAHEAD+1):
            pairList = []
            self.invertedMap[i] = pairList
        self.invert(list)

    def getInvertedMap(self):
        return self.invertedMap


    def invert(self, list):
        for c in list:
            for t in c.getTokens():
                len = t.getTokenLength()
                tc = entity.rule.TokenCodePair.TokenCodePair(t, c.getCode())
                p = self.invertedMap.get(len)
                p.append(tc)

    def toString(self):
        sb = []

        for i in range (self.ctx.const.MAX_LOOKAHEAD+1, 1, -1):
            p = self.invertedMap.get(i)

            if p == None:
                continue

            sb.append("map " + str(i) + "\n")
            for tc in p:
                sb.append(tc.toString() + "\n")

        return ''.join(sb)
