import unittest

from pytgbot.api_types.receivable.peer import ChatMember, ChatMemberOwner
from pytgbot.bot.synchronous import Bot


class MyTestCase(unittest.TestCase):
    def test_s(self):
        bot = Bot('not-a-real-api-key')
        result = bot._get_chat_member__process_result(
            {
                 'user': {
                     'id': 10717954, 'is_bot': False, 'first_name': 'Lucky',
                     'last_name': 'Donald :\uf803', 'username': 'luckydonald',
                     'language_code': 'en'
                 }, 'status': 'creator', 'is_anonymous': False
             }
        )
        self.assertIsInstance(result, ChatMember)
        self.assertIsInstance(result, ChatMemberOwner)
    # end def
# end class

if __name__ == '__main__':
    unittest.main()
