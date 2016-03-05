import requests


API_ROOT = 'https://glosbe.com/gapi_v0_1'


class GlosbeException(Exception):
    pass


class Glosbe(object):

    def __init__(self, from_lang, dest_lang):
        self.from_lang = from_lang
        self.dest_lang = dest_lang

    def _translate(self, phrase, tm=False):
        params = dict({
            'from': self.from_lang,
            'dest': self.dest_lang,
            'phrase': phrase,
            'format': 'json',
        })
        if tm:
            params['tm'] = 'true'

        url = '%s/%s' % (API_ROOT, 'translate')
        resp = requests.get(url, params=params)

        if resp.status_code != 200:
            raise GlosbeException

        return resp.json()

    def translate(self, phrase):
        json = self._translate(phrase)
        if not json['result'] == 'ok':
            raise GlosbeException

        results = list()
        for translation in json['tuc']:
            if 'phrase' in translation:
                results.append(translation['phrase']['text'])

        return results
