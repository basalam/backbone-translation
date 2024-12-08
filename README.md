#### Requirements

- Python 3.6+

#### Installation & Upgrade

```shell
pip install basalam.backbone-translation
```

#### Usage

```python
from backbone_translation.translator import Translator

translator = Translator({
    "messages.greeting" : "Bonjour {name}"
})

# OR translator = Translator.from_json_file("path_to_json_file")

translator.translate("messages.greeting", name="Mojtabaa")
# Bonjour Mojtabaa
```

#### Testing

```bash
# install pytest
pip install pytest

# run tests
python -m pytest
```

#### Changelog
- 0.0.2 added from_json_file method
- 0.0.3 Now build and push are done using gitlab-ci
- 0.0.4 new `exists(phrase: str) -> bool` method
- 0.1.0 added utf-8 encoding thanks to alimohammayali@gmail.com
