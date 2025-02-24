from typing import TypedDict, Optional, List

class Example(TypedDict):
    content: str
    mean: str
    transcription: str
    furigana_sentence: str # not from API

class Word(TypedDict):
    word: str
    mean: str
    phonetic: str
    am_han_viet_list: Optional[List[str]] # not from API
    examples: List[Example]