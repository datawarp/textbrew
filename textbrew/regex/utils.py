

def extract_args(arg_list, **kwargs):
    return {
        i: kwargs.get(i, None) for i in arg_list
    }


def extract_sub_args(*args, **kwargs):
    arg_list = ["replace", "count", "flags"]
    return extract_args(arg_list, **kwargs)
