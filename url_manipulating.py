import re


def update_query_string(url, key, new_value):
	base_query, query_string = url.split('?')
	#query_dict = dict(i.split('=') for i in query_string.split('&'))
	query_dict = {}
	for query in query_string.split('&'):
		qs = query.split("=")
		query_dict[qs[0]] = qs[1]
	print query_dict
	if query_dict.get(key):
		query_dict[key] = new_value
	updated_url = base_query
	return append_query_string(updated_url, **query_dict)



def append_query_string(url, **kwrgs):
	# Check if url already contains query params
	if url.find('?'):
		if url[-1] != '&':
			url += '&'
	else:
		url += '?'
	query_params_str = []
	for key, val in kwrgs.items():
		query_params_str.append(key + "=" + str(val))
	url += "&".join(query_params_str)
	return url

def get_scheme_from_url(url):
	regex = r'((?P<scheme>http[s]?|ftp):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'
	regex_compiled = re.compile(regex)
	scheme = re.match(regex_compiled, url).group('scheme')
	return scheme


def get_domain_from_url(url):
	regex = r'((?P<scheme>http[s]?|ftp):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'
	regex_compiled = re.compile(regex)
	domain = re.match(regex_compiled, url).group('domain')
	return domain


if __name__ == '__main__':
	print get_domain_from_url('http://google.com')
	print append_query_string('http://google.com', foo="foo", name="test")
	print append_query_string('http://google.com?bar=bar', foo="foo", name="test")
	print update_query_string('http://google.com?bar=bar&foo=foo&name=test', 'foo', 'india')
	print get_scheme_from_url('ftp://google.com?bar=bar')
