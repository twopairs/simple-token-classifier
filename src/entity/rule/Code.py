import entity.rule.Token

class Code:
    def __init__(self, c):
        self.code = c
        self.tokens = []

    def addToken(self, t):
        if not isinstance(t, entity.rule.Token.Token):
            print("not token Type")
            exit(-1)

        self.tokens.append(t)

    def getTokens(self):
        return self.tokens

    def getCode(self):
        return  self.code

    def toString(self, prefix = ""):
        sb = []
        sb.append(prefix + self.code + "\n")
        for t in self.tokens:
            sb.append(t.toString(prefix + "  ") + "\n")

        return ''.join(sb)
