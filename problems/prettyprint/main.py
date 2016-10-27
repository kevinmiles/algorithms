
def prettyprint(root, level=0, key=None, indent_string='  '):
    result = ''
    result += indent_string * level
    if key:
        result += '"' + key + '": '
    if isinstance(root, dict):
        result += '{\n'
        i = 0
        for key in root:
            value = root[key]
            result += prettyprint(value, level + 1, key)
            if i != len(root) - 1:
                result += ','
            result += '\n'
            i += 1
        result += indent_string * level + '}'
    elif isinstance(root, list):
        result += '[\n'
        for i in xrange(len(root)):
            value = root[i]
            result += prettyprint(value, level + 1)
            if i != len(root) - 1:
                result += ','
            result += '\n'
        result += indent_string * level + ']'
    elif isinstance(root, basestring):
        result += '"' + str(root) + '"'
    elif isinstance(root, int):
        result += str(root)
    elif isinstance(root, float):
        result += str(root)
    elif isinstance(root, bool):
        result += str(root)
    elif root == None:
        result += 'null'
    else:
        raise Exception('bad type in object')
    return result

print prettyprint({'a':['b','c'], 'd': [1,2,False]})

