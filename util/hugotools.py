import toml
import yaml
import re
import collections

class Error(Exception):
    pass


def SplitToml(content):
    return re.split('\+\+\+\n', content, 3, flags=re.M)


def GetTomlFromFile(content):
    parts = SplitToml(content)
    if len(parts) < 3:
        raise Error('Content did not have 3 parts')
    return toml.loads(parts[1], _dict=collections.OrderedDict)


def ExtractYaml(content):
    parts = re.split('---\n', content, 3, flags=re.M)
    if len(parts) < 3:
        raise Error('Content did not have 3 parts')
    return yaml.load(parts[1])


def ContentToMetadata(content):
    if content.startswith('---'):
        front_matter = ExtractYaml(content)
    elif content.startswith('+++'):
        front_matter = GetTomlFromFile(content)
    else:
        raise Error("This content doesn't seem to have a separator for front matter.")
    return {
            'front_matter': front_matter,
            'content': content,
    }


def GetPageData(filename):
    try:
        with open(filename, 'r') as fd:
            content = fd.read()
    except UnicodeDecodeError as e:
        logging.error("{} {}".format(p, e))
        raise
    return ContentToMetadata(content)


def ReplaceFrontMatter(content, new_front_matter):
    parts = SplitToml(content)
    parts[1] = toml.dumps(new_front_matter) + '\n'
    return '+++\n'.join(parts)


def GetBody(content):
    parts = SplitToml(content)
    if len(parts) != 3:
        raise Error("Content %r doesn't have 3 parts." %  content)
    return parts[2]


def ReplaceBody(content, new_body):
    parts = SplitToml(content)
    parts[2] = new_body
    return '+++\n'.join(parts)
