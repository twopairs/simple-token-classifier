import yaml

def openYaml(filepath):
    yamlObject = None
    with open(filepath, "r") as stream:
        try:
            yamlObject = yaml.safe_load(stream)
        except:
            yamlObject = None
        finally:
            return yamlObject
