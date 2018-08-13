import unittest
from pytgbot.api_types import TgBotApiObject


class TestableTgBotApiObjectRawViaConstructor(TgBotApiObject):
    def __init__(self, foobar, _raw=None):
        super(TestableTgBotApiObjectRawViaConstructor, self).__init__()
        self.foobar = foobar
        self._raw = _raw
    # end def

    @staticmethod
    def from_array(array):
        data = {}
        data['foobar'] = array['foobar']
        data['_raw'] = array
        return TestableTgBotApiObjectRawViaConstructor(**data)
    # end def
# end class

class TestableTgBotApiObjectRawViaAssignLater(TgBotApiObject):
    def __init__(self, foobar):
        super(TestableTgBotApiObjectRawViaAssignLater, self).__init__()
        self.foobar = foobar
    # end def

    @staticmethod
    def from_array(array):
        data = {}
        data['foobar'] = array['foobar']
        new = TestableTgBotApiObjectRawViaAssignLater(**data)
        new._raw = array
        return new
    # end def
# end class


class TgBotApiObjectTestCase(unittest.TestCase):
    def test_deletion_of__raw_via_constructor(self):
        # Like class Update
        data = {'foobar': 123}
        foo = TestableTgBotApiObjectRawViaConstructor.from_array(data)
        self.assertEqual(foo.foobar, 123, 'constructor. Fail = broken test')
        self.assertIsNotNone(foo._raw, '_raw is the used data.')
        self.assertDictEqual(foo._raw, data, '_raw is the used data.')
        foo.foobar = 456
        self.assertEqual(foo.foobar, 456, 'we just set that. Fail = broken test')
        self.assertEqual(foo._raw, None, '_raw was reset.')
    # end def

    def test_deletion_of__raw_via_assign_later(self):
        # Like class InputMedia
        data = {'foobar': 123}
        foo = TestableTgBotApiObjectRawViaAssignLater.from_array(data)
        self.assertEqual(foo.foobar, 123, 'constructor. Fail = broken test')
        self.assertIsNotNone(foo._raw, '_raw is the used data.')
        self.assertDictEqual(foo._raw, data, '_raw is the used data.')
        foo.foobar = 456
        self.assertEqual(foo.foobar, 456, 'we just set that. Fail = broken test')
        self.assertEqual(foo._raw, None, '_raw was reset.')
    # end def
# end class
