import os
import module.YamlUtil
import entity.rule.InvertedDimension
import entity.rule.Code


class Provider:

    def __init__(self, ctx):
        self.dimensionList = []
        self.ruleMap = {}
        self.ctx = ctx

    def getRuleMap(self):
        return self.ruleMap

    def getDimensionList(self):
        return self.dimensionList

    def getRules(self, ruleName):
        if ruleName in self.ruleMap.keys():
            return self.ruleMap.get(ruleName)
        raise

    def buildDimensionMap(self):
        # dir
        dirPath = self.ctx.conf['resource']['path']

        # file list to load
        listNode = self.ctx.conf['resource']['dimension']
        for nvMap in listNode:
            if len(nvMap) != 1:
                raise

            for n, v in nvMap.items():
                if v == None:
                    raise

                dimensionRoot = module.YamlUtil.openYaml(os.path.join(dirPath, v))
                codeMap = self.buildCodeMap(dimensionRoot)
                inverted = entity.rule.InvertedDimension.InvertedDimension(self.ctx, codeMap)
                self.ruleMap[n] = inverted

                self.dimensionList.append(n)

    def buildCodeMap(self, root):
        codeList = []

        for c in root.keys():
            code = entity.rule.Code.Code(c)
            tokenList = root.get(c)

            for list in tokenList:
                nvMap = list

                value = None
                type = None

                if len(nvMap) != 1:
                    raise

                # always len == 1
                for n, v in nvMap.items():
                    if n in [self.ctx.const.ORDER, self.ctx.const.ANYORDER, self.ctx.const.COMBINATION]:
                        value = v
                        type = n

                if value == None:
                    raise

                token = entity.rule.Token.Token(self.ctx, value, type)
                code.addToken(token)

            codeList.append(code)

        return codeList
