
def flatten(d, result, parent = ""):
    # print(d, result)
    for key, value in d.items():
        if len(parent) != 0:
            name = parent + "." + key
        else: name = key
            
        if not isinstance(value, dict):
            result[name] = value
        else:
            flatten(value, result, name)
    return result

    
def unflatten(d):
    result = {}
    for key, value in d.items():
        names = key.split('.')
        index = 0
        current_dict = result
        while index < len(names) - 1:
            if names[index] not in current_dict:
                current_dict[names[index]] = {}
            current_dict = current_dict[names[index]]
            index += 1
        current_dict[names[index]] = value
    return result
            
            
    
test1 = dict()

test2 = {
    "a": "foo",
    "b": "bar",
}
test3 ={
    "a" : {
        "b" : {
            "c": "cat"
        }
    }
}
test4 = {
    "a": "foo", 
    "b" :{
        "c": "bar",
        "d": {
            "e": "baz"
        }
    }
}

print(flatten(test1, {}))
print(flatten(test2, {}))
print(flatten(test3, {}))
print(flatten(test4, {}))


test5 = {}
test6 = {'a': 'foo', 'b': 'bar'}
test7 = {'a.b.c': 'cat'}
test8 = {'a': 'foo', 'b.c': 'bar', 'b.d.e': 'baz'}

print(unflatten(test5))
print(unflatten(test6))
print(unflatten(test7))
print(unflatten(test8))
