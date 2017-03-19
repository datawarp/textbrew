def extract_args(arg_list , **kwargs):
	return dict((i, kwargs.get(i , None)) for i in arg_list)
def extract_sub_args( *args ,**kwargs):
	arg_list = [u"replace" , u"count" , u"flags"]
	return extract_args(arg_list , **kwargs)