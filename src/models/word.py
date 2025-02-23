from typing import TypedDict, Optional, List

class Example(TypedDict):
    content: str
    mean: str
    transcription: str

class Word(TypedDict):
    word: str
    mean: str
    phonetic: str
    am_han_viet_list: Optional[List[str]]
    examples: List[Example]