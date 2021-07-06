import service.rule.TokenCodeMatcher
import entity.meta.MetaResult


def mapping(rp, token, lookAheadLevel, lookAheadTokens):
    return ruleMapping(rp, token, lookAheadLevel, lookAheadTokens)


def ruleMapping(rp, token, lookAheadLevel, lookAheadTokens):
    dList = rp.getDimensionList()

    for d in dList:
        invertedDimension = rp.getRules(d)

        map = invertedDimension.getInvertedMap()
        tcList = map.get(lookAheadLevel)

        if None == tcList:
            continue

        for tc in tcList:
            if True == service.rule.TokenCodeMatcher.match(tc, token, lookAheadTokens):
                mr = entity.meta.MetaResult.MetaResult()
                usedAhead = lookAheadLevel - 1
                mr.setUsedToken(usedAhead)
                mr.addMeta(tc.getCode())
                return mr

    return None
