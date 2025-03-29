from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_props_link(self):
        node = HTMLNode("a", "This is a link", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')
    def test_props_image(self):
        node = HTMLNode("img", props={"src": "https://www.boot.dev/image.png"})
        self.assertEqual(node.props_to_html(), ' src="https://www.boot.dev/image.png"')
    def test_props_no_props(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")
    def test_repr(self):
        node = HTMLNode("a", "This is a link", props={"href": "https://www.boot.dev"})
        self.assertEqual(repr(node), "HTMLNode(a, This is a link, None, {'href': 'https://www.boot.dev'})")  

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "This is a link", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev">This is a link</a>')
    def test_to_html_no_tag(self):
        node = LeafNode(None, value="This is a link", props={"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), 'This is a link')
    def test_repr(self):
        node = LeafNode("a", "This is a link", props={"href": "https://www.boot.dev"})
        self.assertEqual(repr(node), "HTMLNode(a, This is a link, None, {'href': 'https://www.boot.dev'})")   

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )