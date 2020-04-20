def parse_para(data, para):
    ret = {}
    for k, v in para.items():
        if v:
            for vl in v:
                print(ret.get(k))
                x = ret[k].get(vl) if ret.get(k) else data.get(vl)
                if not x:
                    ret[k] = ''
                    break
                elif isinstance(x, list):
                    ret[k] = x[0]
                else:
                    ret[k] = x
        else:
            ret[k] = ''
    return ret


_data = {
    'name': 'hehao',
    'age': [26, 18],
    'marjor': {'one': 'java', 'two': ['python', 'other']},
    'time': None,
    'marjor2': {'one': 'java', 'two': None},
    'marjor3': {'one': 'java', 'two': ''}
}
_para = {'name': ['name'], 'age': ['age'], 'marjor': ['marjor', 'two'], 'time': [], 'marjor2': ['marjor2', 'two'], 'marjor3': ['marjor3', 'two']}
print(parse_para(_data, _para))