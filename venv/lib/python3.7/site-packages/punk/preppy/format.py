
# Liberally borrowed http://stackoverflow.com/a/21515453/2367526

def split_obj (obj, prefix = None):
    '''
    Split the object, returning a 3-tuple with the flat object, optionally
    followed by the key for the subobjects and a list of those subobjects.
    '''
    # copy the object, optionally add the prefix before each key

    new = obj.copy() if prefix is None else { '{}_{}'.format(prefix, k): v for k, v in obj.items() }

    # try to find the key holding the subobject or a list of subobjects
    for k, v in new.items():
        # list of subobjects
        if isinstance(v, list):
            # this is a list of strings or ints, which is a one-to-many
            # can't deal with that here, but leave the data in case it's 
            # useful downstream
            if not isinstance(v[0], dict):
                new[k] = ','.join(v)
                return new, None, None
            del new[k]
            return new, k, v
        # or just one subobject
        elif isinstance(v, dict):
            del new[k]
            return new, k, [v]
    return new, None, None


def flatten_json(data, prefix = None):
    '''
    Flatten the data, optionally with each key prefixed.
    '''
    # iterate all items
    for item in data:
        # split the object
        flat, key, subs = split_obj(item, prefix)

        # just return fully flat objects
        if key is None:
            yield flat
            continue

        # otherwise recursively flatten the subobjects
        for sub in flatten_json(subs, key):
            sub.update(flat)
            yield sub
