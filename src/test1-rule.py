import constant.Constant
import entity.Context
from module.YamlUtil import openYaml
import service.room.TagGenerator

import factory.rule.RuleProvider


if __name__ == "__main__":
    # global constant
    const = constant.Constant.Constant

    # config
    config = openYaml(const.CONFIG_YAML_PATH)

    # context
    ctx = entity.Context.Ctx(const, config)

    # rule provider
    rp = factory.rule.RuleProvider.Provider(ctx)
    rp.buildDimensionMap()

    for n, v in rp.getRuleMap().items():
        print(n)
        print(v.toString())

