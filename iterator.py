import json


class Countries:
    def __init__(self, file):
        with open(file, 'r') as read_file:
            self.countries = json.load(read_file)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        country_name = self.countries.pop().get('name').get('common')
        country_link = 'https://en.wikipedia.org/wiki/' + country_name.replace(' ', '_')
        return f'{country_name} - {country_link}'



