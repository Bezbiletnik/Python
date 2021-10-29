'''My solution'''
# import re
# def domain_name(url):
#     return re.sub(r'(http(s)?://|www.)|\.\w+|/(\w+)?/?(\w+)?', '', url)


#refactoring
import re
def domain_name(url):
    return re.sub(r'(https?://|www.)|\..+', '', url)


import re
def domain_name(url):
    return re.search(r'(https?://)?(www.)?(?P<name>[\w-]+)\.', url).group('name')


'''Best Practices'''
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
