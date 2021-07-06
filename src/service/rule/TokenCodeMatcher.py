import constant.Constant as const

def match(tc, token, la):
    t = tc.getToken()
    tLen = t.getTokenLength()
    orderType = t.getOrderInfo()

    srcList = t.getTokenList()
    tarList = []

    tarList.append(token)

    for lookAheadToken in la:
        tarList.append(lookAheadToken)

    if tLen > len(tarList):
        return False

    if orderType == const.Constant.ORDER:
        for i in range(0, len(srcList)):
            src = srcList[i]
            tar = tarList[i]

            if eq(src, tar) == False:
                return False

    elif orderType == const.Constant.ANYORDER:
        if tLen != 2:
            raise

        s0 = srcList[0]
        s1 = srcList[1]
        t0 = tarList[0]
        t1 = tarList[1]
        if True == eq(s0, t0) and True == eq(s1, t1):
            return True
        if True == eq(s0, t1) and True == eq(s1, t0):
            return True
        return False
    return True


def eq(src, tar):
    src = src.lower()
    tar = tar.lower()

    if src == tar:
        return True
    return False
