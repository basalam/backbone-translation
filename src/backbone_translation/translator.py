import json
from pathlib import Path
from typing import Dict


class Translator:

    def __init__(self, dictionary: Dict) -> None:
        self.__dictionary: Dict = dictionary

    @classmethod
    def from_json_file(cls, path: str):
        return cls(json.loads(Path(path).read_text()))

    def set_dictionary(self, dictionary: Dict):
        self.__dictionary = dictionary

    def translate(self, phrase: str, **kwargs):
        translation: str = self.__dictionary.get(phrase) if phrase in self.__dictionary else phrase
        return translation if len(kwargs) == 0 else translation.format(**kwargs)
