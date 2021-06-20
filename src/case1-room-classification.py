import constant.Constant
import entity.Context
from module.YamlUtil import openYaml
import service.room.TagGenerator

if __name__ == "__main__":
    # gloval constant
    const = constant.Constant.Constant

    # config
    config = openYaml(const.CONFIG_YAML_PATH)

    # context
    ctx = entity.Context.Ctx(const, config)

    # classify
    c = service.room.TagGenerator.Generator(ctx)
    c.gen()

