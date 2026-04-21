from textnode import TextType, TextNode

node = TextNode("This is a text node", TextType.Link.value)

print(repr(node))