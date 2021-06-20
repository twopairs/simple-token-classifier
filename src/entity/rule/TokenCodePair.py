import entity.rule.Token

class TokenCodePair:

    def __init__(self, token, code):
        if not isinstance(token, entity.rule.Token.Token):
            print("not token Type")
            exit(-1)

        self.token = token
        self.code = code

    def getToken(self):
        return self.token

    def getCode(self):
        return self.code

    def toString(self):
        return self.code + " : " + self.token.toString()