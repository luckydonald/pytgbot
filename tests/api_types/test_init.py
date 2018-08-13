import unittest
from pytgbot.api_types import TgBotApiObject


class TestableTgBotApiObject(TgBotApiObject):
    def __init__(self, foobar, _raw=None):
        super(TestableTgBotApiObject, self).__init__()
        self.foobar = foobar
        self._raw = _raw
    # end def

    @staticmethod
    def from_array(array):
        data = {}
        data['foobar'] = array['foobar']
        data['_raw'] = array
        return TestableTgBotApiObject(**data)
    # end def
# end class


class TgBotApiObjectTestCase(unittest.TestCase):
    def test_deletion_of__raw(self):
        data = {'foobar': 123}
        foo = TestableTgBotApiObject.from_array(data)
        self.assertEqual(foo.foobar, 123, 'constructor. Fail = broken test')
        self.assertIsNotNone(foo._raw, '_raw is the used data.')
        self.assertDictEqual(foo._raw, data, '_raw is the used data.')
        foo.foobar = 456
        self.assertEqual(foo.foobar, 456, 'we just set that. Fail = broken test')
        self.assertEqual(foo._raw, None, '_raw was reset.')
    # end def
# end class
