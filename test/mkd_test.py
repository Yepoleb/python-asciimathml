import unittest
import xml.dom.minidom as md
from xml.etree.ElementTree import tostring

from asciimathml import element_factory
import markdown

def pretty_print(s):
    return md.parseString(s).toprettyxml(indent='  ')

class MkdTestCase(unittest.TestCase):
    def testTwoLines(self):
        self.maxDiff = None

        output = markdown.markdown(
            (
                'First line containing the formula $$f(x)=x^2$$.\n'
                'The second line should be here.'
            ),
            ["asciimathml"]
        )

        formula = element_factory('math',
            element_factory('mstyle',
                element_factory('mi', text='f'),
                element_factory('mrow',
                    element_factory('mo', text='('),
                    element_factory('mi', text='x'),
                    element_factory('mo', text=')')
                ),
                element_factory('mo', text='='),
                element_factory('msup',
                    element_factory('mi', text='x'),
                    element_factory('mn', text='2')
                )
            )
        )
        formula.set('xmlns', 'http://www.w3.org/1998/Math/MathML')

        expected = (
            '<p>First line containing the formula {0}.\n'
            'The second line should be here.</p>'
        ).format(tostring(formula, encoding='unicode').strip())

        self.assertEquals(
            output,
            expected
        )
