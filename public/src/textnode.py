from enum import Enum

class TextType(Enum):
    TEXT = None
    BOLD = None
    ITALIC = None
    CODE = None
    LINK = None
    IMAGE = None

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        self.other = other
        if self.text == self.other.text and self.text_type == self.other.text_type and self.url == self.other.url:
            return True
        
    def __repr__(self):
         return f"TextNode({self.text}, {self.text_type}, {self.url})"
