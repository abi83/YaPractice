import csv

count = 0
robots_file_template = 'User-agent: *\n' \
                       'Disallow: /search/\n' \
                       'Disallow: /profile/\n' \
                       'Disallow: /lostpass/*\n' \
                       'Disallow: /activate/*\n' \
                       'Sitemap: https://{city}.mediaohvat.ru/sitemap.xml'
output_file_name_template = './robots/{}.robots.txt'

with open('cities.csv', 'r', encoding='utf8') as csv_file, open(
        './robots/0_list.txt', 'w', encoding='utf8') as list_file:

    cities = csv.DictReader(csv_file)
    for city in cities:
        if (city['subdomen'] == '0'
                and city['is_capital'] == '1'
                and int(city['population']) > 400000)\
                and '_' not in city['code']:
            count += 1
            with open(
                    output_file_name_template.format(city['code']),
                    'x',
                    encoding='utf8') as output_file:
                output_file.write(
                    robots_file_template.format(city=city['code']))
            list_file.write(f'{city["code"]}.mediaohvat.ru\n')

print(count)
