
class Ctx:
    conf = ""
    const = ""

    def __init__(self, const, config):
        self.const = const
        self.conf = config

    def getConf(self):
        return self.conf
