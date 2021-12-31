def sort_me(courses): 
    # for i in courses:
    #     print(sorted(i.split('-'), key=lambda x:x[1]))

    return sorted(courses, key=lambda x:(x.split('-')[1]))

print(sort_me(['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']))
# Output: ['play-1215', 'web-1304', 'site-1304', 'aeb-1305', 'site-1305', 'beb-1305']
# Answer: ["play-1215", "site-1304", "web-1304", "aeb-1305", "beb-1305", "site-1305"]