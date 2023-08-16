# a = ('a') # type str
# a = ('a',) # type tuple


# d = {'dict': 1, 'dict_2': 2}
# b = dict(dict = 1, dict_2 =  2)
#
# key = d.keys()
# val = d.values()
# itm = d.items()
# gt = d.get('dict')
# gt_2 = d.get('test', 'Ключа нет')
# pp = d.pop('dict')
# cl = d.clear()
# print(key, val, itm, gt, gt_2, pp, cl, sep='\n')
# print(d)


# dict_button = {
#     'Ожидаемый результат': 'blue'
# }
# dict_input = {
#     'Ожидаемый результат': 'active'
# }
# dict_find = {
#     'Ожидаемый результат': 'placeholder'
# }
# res = 'Ожидаемый результат'
#
# print(dict_button.get(res))
# print(dict_input[res])
# print(dict_find[res])


# dict_href = {
#     'sv-se': 'https://www.slotozilla.com/sv',
#     'da-dk': 'https://www.slotozilla.com/dk',
#     'fi-fi': 'https://www.slotozilla.com/fi',
#     'en-ca': 'https://www.slotozilla.com/ca',
#     'en-au': 'https://www.slotozilla.com/au',
#     'en-gb': 'https://www.slotozilla.com/uk',
#     'pt-pt': 'https://www.slotozilla.com/pt',
#     'de': 'https://www.slotozilla.com/de',
#     'fr': 'https://www.slotozilla.com/fr',
#     'pl': 'https://www.slotozilla-poland.com/pl/',
#     'es': 'https://www.slotozilla.com/es/',
#     'en': 'https://www.slotozilla.com/'
# }
#
# for key, value in dict_href.items():
#     first_char = key[:2]
#     last_char = value[-2:]
#     first_char_slash = key[:2] + '/'
#     last_char_slash = value[-3:]
#     duble_href = key[3:5]
#
#     if first_char == last_char:
#         print(f"[PASSED] Hreflang: '{key}' ends with '{last_char}' in {value}")
#     elif last_char_slash == first_char_slash:
#         print(f"[PASSED] Hreflang: '{key}' ends with '/' and = '{last_char_slash}' in {value}")
#     elif duble_href == last_char or duble_href == last_char_slash:
#         print(f"[PASSED] Hreflang: '{key}' ends with '{duble_href}' in {value}")
#     else:
#         print(f"[WARNING] Failed: '{value}'")
