from textnode import *


def main():
    obj1 = TextNode("This is some text", "plain", "https://www.boot.dev")
    obj2 = TextNode("This is some tet", "plain", "https://www.boot.dev")
    print(obj1 == obj2)

main()