import factory.rule.RuleProvider
import entity.meta.ClassificationResult
import service.rule.MappingRules

class MetaClassifier:

    def __init__(self, ctx, rp):
        self.ctx = ctx
        self.rp = rp

    def classify(self, operand):

        if operand == None or operand == '':
            return entity.meta.ClassificationResult.ClassificationResult()


        input = operand.strip()
        splited = input.split(" ")
        tokens = []
        for s in splited:
            if s.strip() == "":
                continue
            tokens.append(s)

        cr = entity.meta.ClassificationResult.ClassificationResult()

        # do mapping
        idx = -1
        usedToken = 0

        for t in tokens:
            idx = idx + 1
            if usedToken != 0:
                usedToken = usedToken -1
                continue

            lookAhead = self.getLookAhead(idx, tokens)

            mr = None
            for i in range(self.ctx.const.MAX_LOOKAHEAD, 0, -1):
                mr = service.rule.MappingRules.mapping(self.rp, t, i, lookAhead)
                if mr != None:
                    usedToken = mr.getUsedToken()
                    cr.putMetaResult(mr)
                    break

            if mr == None:
                cr.putUnusedToken(t)

        return cr



    def getLookAhead(self, idx, tokens):
        MAX = idx + self.ctx.const.MAX_LOOKAHEAD
        l = len(tokens)
        end = MAX
        if l > MAX:
            end = MAX

        la = []

        i = 0
        for t in tokens:
            if i > idx:
                la.append(t)
            i += 1

        return la