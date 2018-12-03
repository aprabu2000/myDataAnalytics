from .clean_values import string_cleaner

def concat_columns(*args, sep=','):
    args = [[string_cleaner(v) for v in values] for arg in args]
    return [sep.join(group) for group in zip(*args)]    