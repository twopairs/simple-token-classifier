import constant.Constant
import entity.Context
from module.YamlUtil import openYaml
import factory.rule.RuleProvider
import service.rule.MetaClassifier
import entity.meta.ClassificationResult

if __name__ == "__main__":
    # gloval constant
    const = constant.Constant.Constant

    # config
    config = openYaml(const.CONFIG_YAML_PATH)

    # context
    ctx = entity.Context.Ctx(const, config)

    # rule provider
    rp = factory.rule.RuleProvider.Provider(ctx)
    rp.buildDimensionMap()

    # meta classifier
    mc = service.rule.MetaClassifier.MetaClassifier(ctx, rp)

    input = "deluxe twin room with ocean view"

    # classify
    classified = mc.classify(input)

    # indentified
    metaResultList = classified.getMetaResultList()
    for r in metaResultList:
        print(r.toString())

    # unused
    unusedList = classified.getUnusedTokenList()
    for u in unusedList:
        print(u)

    # TODO implement combination type





