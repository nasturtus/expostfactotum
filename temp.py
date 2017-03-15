# Printing dictionaries using format fields {..}
# https://en.wikipedia.org/wiki/List_of_oldest_companies

import pprint
oldest_companies = {
    'Kongo Gumi': {
        'year': 578,
        'location': 'Japan',
        'industry': 'Construction'
    },
    'Koman': {
        'year': 717,
        'location': 'Japan',
        'industry': 'Hotel',
    },
    'The Bingley Arms': {
        'year': 717,
        'location': 'Japan',
        'industry': 'Hotel',
    }
}

# Determine maximum length of key string to use for width while printing
w = 0
for key in oldest_companies.keys():
    if len(key) > w:
        w = len(key) + 1  # add 1 for some padding

print("{0}{1}{2}{3}".format('NAME'.ljust(w), 'YEAR'.ljust(w),
                            'LOCATION'.ljust(w), 'INDUSTRY'.ljust(w)))
print('-' * 79)
for key in oldest_companies.keys():
    print("{0}{1}{2}{3}".format(key.ljust(w),
                                str(oldest_companies[key]['year']).ljust(w),
                                oldest_companies[key]['location'].ljust(w),
                                oldest_companies[key]['industry'].ljust(w)))
