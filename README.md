# python-glosbe
A python client for Glosbe translations

## Current features and examples
#### translate something

```python
from glosbe import Glosbe

g = Glosbe(from_lang='eng', dest_lang='cym')
g.translate('bread')
```

This will return a list of all translations.
Language codes are as specified [here](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes).

## Contributing

Yes please.
