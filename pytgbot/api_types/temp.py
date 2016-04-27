    def send_contact(self, chat_id, phone_number, first_name, last_name=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        https://core.telegram.org/bots/api#sendcontact


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Contact's last name
        :type    last_name:  str

        :keyword disable_notification: Sends the message silently. iOS users will not receive a notification, Android users will receive a notification with no sound.
        :type    disable_notification:  bool

        :keyword reply_to_message_id: If the message is a reply, ID of the original message
        :type    reply_to_message_id:  int

        :keyword reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to hide keyboard or to force a reply from the user.
        :type    reply_markup:  InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardHide | ForceReply


        Returns:

        :return: On success, the sent Message is returned.
        :rtype:  Message
        """
        assert(phone_number is not None)
        assert(isinstance(phone_number, str))
        assert(first_name is not None)
        assert(isinstance(first_name, str))
        assert(last_name is None or isinstance(last_name, str))
        assert(disable_notification is None or isinstance(disable_notification, bool))
        assert(reply_to_message_id is None or isinstance(reply_to_message_id, int))
        return self.do("sendContact", chat_id=chat_id, phone_number=phone_number, first_name=first_name, last_name=last_name, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
    # end def send_contact

    def send_chat_action(self, chat_id, action):
        """
        Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).

        Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of “Retrieving image, please wait…”, the bot may use sendChatAction with action = upload_photo. The user will see a “sending photo” status for the bot.

        We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

        https://core.telegram.org/bots/api#sendchataction


        Parameters:

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type  chat_id:  int | str

        :param action: Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_audio or upload_audio for audio files, upload_document for general files, find_location for location data.
        :type  action:  str


        Returns:

        :return: ???
        :rtype:  ???
        """
        assert(action is not None)
        assert(isinstance(action, str))
        return self.do("sendChatAction", chat_id=chat_id, action=action)
    # end def send_chat_action

    def get_user_profile_photos(self, user_id, offset=None, limit=None):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        https://core.telegram.org/bots/api#getuserprofilephotos


        Parameters:

        :param user_id: Unique identifier of the target user
        :type  user_id:  int


        Optional keyword parameters:

        :keyword offset: Sequential number of the first photo to be returned. By default, all photos are returned.
        :type    offset:  int

        :keyword limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        :type    limit:  int


        Returns:

        :return: Returns a UserProfilePhotos object.
        :rtype:  UserProfilePhotos
        """
        assert(user_id is not None)
        assert(isinstance(user_id, int))
        assert(offset is None or isinstance(offset, int))
        assert(limit is None or isinstance(limit, int))
        return self.do("getUserProfilePhotos", user_id=user_id, offset=offset, limit=limit)
    # end def get_user_profile_photos

    def get_file(self, file_id):
        """
        Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.

        https://core.telegram.org/bots/api#getfile


        Parameters:

        :param file_id: File identifier to get info about
        :type  file_id:  str


        Returns:

        :return: On success, a File object is returned
        :rtype:  File
        """
        assert(file_id is not None)
        assert(isinstance(file_id, str))
        return self.do("getFile", file_id=file_id)
    # end def get_file

    def kick_chat_member(self, chat_id, user_id):
        """
        Use this method to kick a user from a group or a supergroup. In the case of supergroups, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the group for this to work. Returns True on success.

        Note: This will method only work if the ‘All Members Are Admins’ setting is off in the target group. Otherwise members may only be removed by the group's creator or by the member that added them.

        https://core.telegram.org/bots/api#kickchatmember


        Parameters:

        :param chat_id: Unique identifier for the target group or username of the target supergroup (in the format @supergroupusername)
        :type  chat_id:  int | str

        :param user_id: Unique identifier of the target user
        :type  user_id:  int


        Returns:

        :return: True on success
        :rtype:  bool
        """
        assert(user_id is not None)
        assert(isinstance(user_id, int))
        return self.do("kickChatMember", chat_id=chat_id, user_id=user_id)
    # end def kick_chat_member

    def unban_chat_member(self, chat_id, user_id):
        """
        Use this method to unban a previously kicked user in a supergroup. The user will not return to the group automatically, but will be able to join via link, etc. The bot must be an administrator in the group for this to work. Returns True on success.

        https://core.telegram.org/bots/api#unbanchatmember


        Parameters:

        :param chat_id: Unique identifier for the target group or username of the target supergroup (in the format @supergroupusername)
        :type  chat_id:  int | str

        :param user_id: Unique identifier of the target user
        :type  user_id:  int


        Returns:

        :return: Returns True on success.
        :rtype:  bool
        """
        assert(user_id is not None)
        assert(isinstance(user_id, int))
        return self.do("unbanChatMember", chat_id=chat_id, user_id=user_id)
    # end def unban_chat_member

    def answer_callback_query(self, callback_query_id, text=None, show_alert=None):
        """
        Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

        https://core.telegram.org/bots/api#answercallbackquery


        Parameters:

        :param callback_query_id: Unique identifier for the query to be answered
        :type  callback_query_id:  str


        Optional keyword parameters:

        :keyword text: Text of the notification. If not specified, nothing will be shown to the user
        :type    text:  str

        :keyword show_alert: If true, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.
        :type    show_alert:  bool


        Returns:

        :return: Returns True on success.
        :rtype:  bool
        """
        assert(callback_query_id is not None)
        assert(isinstance(callback_query_id, str))
        assert(text is None or isinstance(text, str))
        assert(show_alert is None or isinstance(show_alert, bool))
        return self.do("answerCallbackQuery", callback_query_id=callback_query_id, text=text, show_alert=show_alert)
    # end def answer_callback_query

    def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, disable_web_page_preview=None, reply_markup=None):
        """
        Use this method to edit text messages sent by the bot or via the bot (for inline bots). On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        https://core.telegram.org/bots/api#editmessagetext


        Parameters:

        :param text: New text of the message
        :type  text:  str


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type    chat_id:  int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id:  int

        :keyword inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type    inline_message_id:  str

        :keyword parse_mode: Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str

        :keyword disable_web_page_preview: Disables link previews for links in this message
        :type    disable_web_page_preview:  bool

        :keyword reply_markup: A JSON-serialized object for an inline keyboard.
        :type    reply_markup:  InlineKeyboardMarkup


        Returns:

        :return: On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.
        :rtype:  Message or bool
        """
        assert(message_id is None or isinstance(message_id, int))
        assert(inline_message_id is None or isinstance(inline_message_id, str))
        assert(text is not None)
        assert(isinstance(text, str))
        assert(parse_mode is None or isinstance(parse_mode, str))
        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        return self.do("editMessageText", text=text, chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)
    # end def edit_message_text

    def edit_message_caption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None, reply_markup=None):
        """
        Use this method to edit captions of messages sent by the bot or via the bot (for inline bots). On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        https://core.telegram.org/bots/api#editmessagecaption


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type    chat_id:  int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id:  int

        :keyword inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type    inline_message_id:  str

        :keyword caption: New caption of the message
        :type    caption:  str

        :keyword reply_markup: A JSON-serialized object for an inline keyboard.
        :type    reply_markup:  InlineKeyboardMarkup


        Returns:

        :return: On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.
        :rtype:  Message or bool
        """
        assert(message_id is None or isinstance(message_id, int))
        assert(inline_message_id is None or isinstance(inline_message_id, str))
        assert(caption is None or isinstance(caption, str))
        return self.do("editMessageCaption", chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id, caption=caption, reply_markup=reply_markup)
    # end def edit_message_caption

    def edit_message_reply_markup(self, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
        """
        Use this method to edit only the reply markup of messages sent by the bot or via the bot (for inline bots).  On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.
        The following methods and objects allow your bot to work in inline mode.Please see our Introduction to Inline bots for more details.
        To enable this option, send the /setinline command to @BotFather and provide the placeholder text that the user will see in the input field after typing your bot’s name.

        https://core.telegram.org/bots/api#editmessagereplymarkup


        Optional keyword parameters:

        :keyword chat_id: Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :type    chat_id:  int | str

        :keyword message_id: Required if inline_message_id is not specified. Unique identifier of the sent message
        :type    message_id:  int

        :keyword inline_message_id: Required if chat_id and message_id are not specified. Identifier of the inline message
        :type    inline_message_id:  str

        :keyword reply_markup: A JSON-serialized object for an inline keyboard.
        :type    reply_markup:  InlineKeyboardMarkup


        Returns:

        :return: On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.
        :rtype:  Message or bool
        """
        assert(message_id is None or isinstance(message_id, int))
        assert(inline_message_id is None or isinstance(inline_message_id, str))
        return self.do("editMessageReplyMarkup", chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id, reply_markup=reply_markup)
    # end def edit_message_reply_markup

class InlineQuery (Result):
    """
    This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    https://core.telegram.org/bots/api#inlinequery
    """
    def __init__(self, id, from_peer, query, offset, location = None):
        """
        This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

        https://core.telegram.org/bots/api#inlinequery


        Parameters:

        :param id: Unique identifier for this query
        :type  id:  str

        :param from_peer: Sender
        :type  from_peer:  User

        :param query: Text of the query
        :type  query:  str

        :param offset: Offset of the results to be returned, can be controlled by the bot
        :type  offset:  str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that request user location
        :type    location:  Location
        """
        super(InlineQuery, self).__init__(id)

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        self.from_peer = from_peer

        self.location = location

        assert(query is not None)
        assert(isinstance(query, unicode_type))  # unicode on python 2, str on python 3
        self.query = query

        assert(offset is not None)
        assert(isinstance(offset, unicode_type))  # unicode on python 2, str on python 3
        self.offset = offset
    # end def __init__

    def to_array(self):
        array = super(InlineQuery, self).to_array()
        array["id"] = self.id
        array["from_peer"] = self.from_peer
        array["query"] = self.query
        array["offset"] = self.offset
        if self.location is not None:
            array["location"] = self.location
        return array
    # end def to_array
# end class InlineQuery

    def answer_inline_query(self, inline_query_id, results, cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None, switch_pm_parameter=None):
        """
        Use this method to send answers to an inline query. On success, True is returned.No more than 50 results per query are allowed.

        https://core.telegram.org/bots/api#answerinlinequery


        Parameters:

        :param inline_query_id: Unique identifier for the answered query
        :type  inline_query_id:  str

        :param results: A JSON-serialized array of results for the inline query
        :type  results:  Array of InlineQueryResult


        Optional keyword parameters:

        :keyword cache_time: The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
        :type    cache_time:  int

        :keyword is_personal: Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
        :type    is_personal:  bool

        :keyword next_offset: Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don‘t support pagination. Offset length can’t exceed 64 bytes.
        :type    next_offset:  str

        :keyword switch_pm_text: If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter
        :type    switch_pm_text:  str

        :keyword switch_pm_parameter: Parameter for the start message sent to the bot when user presses the switch buttonExample: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a ‘Connect your YouTube account’ button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an oauth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
        :type    switch_pm_parameter:  str


        Returns:

        :return: On success, True is returned.
        :rtype:  bool
        """
        assert(inline_query_id is not None)
        assert(isinstance(inline_query_id, str))
        assert(results is not None)
        assert(isinstance(results, (list, tuple)))  # Array of InlineQueryResult
        assert(cache_time is None or isinstance(cache_time, int))
        assert(is_personal is None or isinstance(is_personal, bool))
        assert(next_offset is None or isinstance(next_offset, str))
        assert(switch_pm_text is None or isinstance(switch_pm_text, str))
        assert(switch_pm_parameter is None or isinstance(switch_pm_parameter, str))
        return self.do("answerInlineQuery", inline_query_id=inline_query_id, results=results, cache_time=cache_time, is_personal=is_personal, next_offset=next_offset, switch_pm_text=switch_pm_text, switch_pm_parameter=switch_pm_parameter)
    # end def answer_inline_query

class InlineQueryResultArticle (InlineQueryResult):
    """
    Represents a link to an article or web page.

    https://core.telegram.org/bots/api#inlinequeryresultarticle
    """
    def __init__(self, type, id, title, input_message_content, reply_markup = None, url = None, hide_url = None, description = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a link to an article or web page.

        https://core.telegram.org/bots/api#inlinequeryresultarticle


        Parameters:

        :param type: Type of the result, must be article
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param title: Title of the result
        :type  title:  str

        :param input_message_content: Content of the message to be sent
        :type  input_message_content:  InputMessageContent


        Optional keyword parameters:

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword url: Optional. URL of the result
        :type    url:  str

        :keyword hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
        :type    hide_url:  bool

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultArticle, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        self.input_message_content = input_message_content

        self.reply_markup = reply_markup

        assert(url is None or isinstance(url, unicode_type))  # unicode on python 2, str on python 3
        self.url = url

        assert(hide_url is None or isinstance(hide_url, bool))
        self.hide_url = hide_url

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultArticle, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["title"] = self.title
        array["input_message_content"] = self.input_message_content
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.url is not None:
            array["url"] = self.url
        if self.hide_url is not None:
            array["hide_url"] = self.hide_url
        if self.description is not None:
            array["description"] = self.description
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultArticle

class InlineQueryResultPhoto (InlineQueryResult):
    """
    Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultphoto
    """
    def __init__(self, type, id, photo_url, thumb_url, photo_width = None, photo_height = None, title = None, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultphoto


        Parameters:

        :param type: Type of the result, must be photo
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param photo_url: A valid URL of the photo. Photo must be in jpeg format. Photo size must not exceed 5MB
        :type  photo_url:  str

        :param thumb_url: URL of the thumbnail for the photo
        :type  thumb_url:  str


        Optional keyword parameters:

        :keyword photo_width: Optional. Width of the photo
        :type    photo_width:  int

        :keyword photo_height: Optional. Height of the photo
        :type    photo_height:  int

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword caption: Optional. Caption of the photo to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the photo
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultPhoto, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(photo_url is not None)
        assert(isinstance(photo_url, unicode_type))  # unicode on python 2, str on python 3
        self.photo_url = photo_url

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(photo_width is None or isinstance(photo_width, int))
        self.photo_width = photo_width

        assert(photo_height is None or isinstance(photo_height, int))
        self.photo_height = photo_height

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultPhoto, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["photo_url"] = self.photo_url
        array["thumb_url"] = self.thumb_url
        if self.photo_width is not None:
            array["photo_width"] = self.photo_width
        if self.photo_height is not None:
            array["photo_height"] = self.photo_height
        if self.title is not None:
            array["title"] = self.title
        if self.description is not None:
            array["description"] = self.description
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultPhoto

class InlineQueryResultGif (InlineQueryResult):
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultgif
    """
    def __init__(self, type, id, gif_url, thumb_url, gif_width = None, gif_height = None, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultgif


        Parameters:

        :param type: Type of the result, must be gif
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB
        :type  gif_url:  str

        :param thumb_url: URL of the static thumbnail for the result (jpeg or gif)
        :type  thumb_url:  str


        Optional keyword parameters:

        :keyword gif_width: Optional. Width of the GIF
        :type    gif_width:  int

        :keyword gif_height: Optional. Height of the GIF
        :type    gif_height:  int

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword caption: Optional. Caption of the GIF file to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the GIF animation
        :type    input_message_content:  inputMessageContent
        """
        super(InlineQueryResultGif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(gif_url is not None)
        assert(isinstance(gif_url, unicode_type))  # unicode on python 2, str on python 3
        self.gif_url = gif_url

        assert(gif_width is None or isinstance(gif_width, int))
        self.gif_width = gif_width

        assert(gif_height is None or isinstance(gif_height, int))
        self.gif_height = gif_height

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultGif, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["gif_url"] = self.gif_url
        array["thumb_url"] = self.thumb_url
        if self.gif_width is not None:
            array["gif_width"] = self.gif_width
        if self.gif_height is not None:
            array["gif_height"] = self.gif_height
        if self.title is not None:
            array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultGif

class InlineQueryResultMpeg4Gif (InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif
    """
    def __init__(self, type, id, mpeg4_url, thumb_url, mpeg4_width = None, mpeg4_height = None, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif


        Parameters:

        :param type: Type of the result, must be mpeg4_gif
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB
        :type  mpeg4_url:  str

        :param thumb_url: URL of the static thumbnail (jpeg or gif) for the result
        :type  thumb_url:  str


        Optional keyword parameters:

        :keyword mpeg4_width: Optional. Video width
        :type    mpeg4_width:  int

        :keyword mpeg4_height: Optional. Video height
        :type    mpeg4_height:  int

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword caption: Optional. Caption of the MPEG-4 file to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video animation
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultMpeg4Gif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(mpeg4_url is not None)
        assert(isinstance(mpeg4_url, unicode_type))  # unicode on python 2, str on python 3
        self.mpeg4_url = mpeg4_url

        assert(mpeg4_width is None or isinstance(mpeg4_width, int))
        self.mpeg4_width = mpeg4_width

        assert(mpeg4_height is None or isinstance(mpeg4_height, int))
        self.mpeg4_height = mpeg4_height

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultMpeg4Gif, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["mpeg4_url"] = self.mpeg4_url
        array["thumb_url"] = self.thumb_url
        if self.mpeg4_width is not None:
            array["mpeg4_width"] = self.mpeg4_width
        if self.mpeg4_height is not None:
            array["mpeg4_height"] = self.mpeg4_height
        if self.title is not None:
            array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultMpeg4Gif

class InlineQueryResultVideo (InlineQueryResult):
    """
    Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultvideo
    """
    def __init__(self, type, id, video_url, mime_type, thumb_url, title, caption = None, video_width = None, video_height = None, video_duration = None, description = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultvideo


        Parameters:

        :param type: Type of the result, must be video
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param video_url: A valid URL for the embedded video player or video file
        :type  video_url:  str

        :param mime_type: Mime type of the content of video url, “text/html” or “video/mp4”
        :type  mime_type:  str

        :param thumb_url: URL of the thumbnail (jpeg only) for the video
        :type  thumb_url:  str

        :param title: Title for the result
        :type  title:  str


        Optional keyword parameters:

        :keyword caption: Optional. Caption of the video to be sent, 0-200 characters
        :type    caption:  str

        :keyword video_width: Optional. Video width
        :type    video_width:  int

        :keyword video_height: Optional. Video height
        :type    video_height:  int

        :keyword video_duration: Optional. Video duration in seconds
        :type    video_duration:  int

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultVideo, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(video_url is not None)
        assert(isinstance(video_url, unicode_type))  # unicode on python 2, str on python 3
        self.video_url = video_url

        assert(mime_type is not None)
        assert(isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(thumb_url is not None)
        assert(isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        assert(video_width is None or isinstance(video_width, int))
        self.video_width = video_width

        assert(video_height is None or isinstance(video_height, int))
        self.video_height = video_height

        assert(video_duration is None or isinstance(video_duration, int))
        self.video_duration = video_duration

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVideo, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["video_url"] = self.video_url
        array["mime_type"] = self.mime_type
        array["thumb_url"] = self.thumb_url
        array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.video_width is not None:
            array["video_width"] = self.video_width
        if self.video_height is not None:
            array["video_height"] = self.video_height
        if self.video_duration is not None:
            array["video_duration"] = self.video_duration
        if self.description is not None:
            array["description"] = self.description
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultVideo

class InlineQueryResultAudio (InlineQueryResult):
    """
    Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultaudio
    """
    def __init__(self, type, id, audio_url, title, performer = None, audio_duration = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an mp3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultaudio


        Parameters:

        :param type: Type of the result, must be audio
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param audio_url: A valid URL for the audio file
        :type  audio_url:  str

        :param title: Title
        :type  title:  str


        Optional keyword parameters:

        :keyword performer: Optional. Performer
        :type    performer:  str

        :keyword audio_duration: Optional. Audio duration in seconds
        :type    audio_duration:  int

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the audio
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultAudio, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(audio_url is not None)
        assert(isinstance(audio_url, unicode_type))  # unicode on python 2, str on python 3
        self.audio_url = audio_url

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(performer is None or isinstance(performer, unicode_type))  # unicode on python 2, str on python 3
        self.performer = performer

        assert(audio_duration is None or isinstance(audio_duration, int))
        self.audio_duration = audio_duration

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultAudio, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["audio_url"] = self.audio_url
        array["title"] = self.title
        if self.performer is not None:
            array["performer"] = self.performer
        if self.audio_duration is not None:
            array["audio_duration"] = self.audio_duration
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultAudio

class InlineQueryResultVoice (InlineQueryResult):
    """
    Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvoice
    """
    def __init__(self, type, id, voice_url, title, voice_duration = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a voice recording in an .ogg container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvoice


        Parameters:

        :param type: Type of the result, must be voice
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param voice_url: A valid URL for the voice recording
        :type  voice_url:  str

        :param title: Recording title
        :type  title:  str


        Optional keyword parameters:

        :keyword voice_duration: Optional. Recording duration in seconds
        :type    voice_duration:  int

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the voice recording
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultVoice, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(voice_url is not None)
        assert(isinstance(voice_url, unicode_type))  # unicode on python 2, str on python 3
        self.voice_url = voice_url

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(voice_duration is None or isinstance(voice_duration, int))
        self.voice_duration = voice_duration

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVoice, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["voice_url"] = self.voice_url
        array["title"] = self.title
        if self.voice_duration is not None:
            array["voice_duration"] = self.voice_duration
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultVoice

class InlineQueryResultDocument (InlineQueryResult):
    """
    Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultdocument
    """
    def __init__(self, type, id, title, document_url, mime_type, caption = None, description = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only .PDF and .ZIP files can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultdocument


        Parameters:

        :param type: Type of the result, must be document
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param title: Title for the result
        :type  title:  str

        :param document_url: A valid URL for the file
        :type  document_url:  str

        :param mime_type: Mime type of the content of the file, either “application/pdf” or “application/zip”
        :type  mime_type:  str


        Optional keyword parameters:

        :keyword caption: Optional. Caption of the document to be sent, 0-200 characters
        :type    caption:  str

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the file
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. URL of the thumbnail (jpeg only) for the file
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultDocument, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        assert(document_url is not None)
        assert(isinstance(document_url, unicode_type))  # unicode on python 2, str on python 3
        self.document_url = document_url

        assert(mime_type is not None)
        assert(isinstance(mime_type, unicode_type))  # unicode on python 2, str on python 3
        self.mime_type = mime_type

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultDocument, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["title"] = self.title
        array["document_url"] = self.document_url
        array["mime_type"] = self.mime_type
        if self.caption is not None:
            array["caption"] = self.caption
        if self.description is not None:
            array["description"] = self.description
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultDocument

class InlineQueryResultLocation (InlineQueryResult):
    """
    Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultlocation
    """
    def __init__(self, type, id, latitude, longitude, title, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the location.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultlocation


        Parameters:

        :param type: Type of the result, must be location
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param latitude: Location latitude in degrees
        :type  latitude:  Float number

        :param longitude: Location longitude in degrees
        :type  longitude:  Float number

        :param title: Location title
        :type  title:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the location
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultLocation, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        self.latitude = latitude

        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultLocation, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultLocation

class InlineQueryResultVenue (InlineQueryResult):
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultvenue
    """
    def __init__(self, type, id, latitude, longitude, title, address, foursquare_id = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the venue.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultvenue


        Parameters:

        :param type: Type of the result, must be venue
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param latitude: Latitude of the venue location in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the venue location in degrees
        :type  longitude:  Float

        :param title: Title of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue if known
        :type    foursquare_id:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the venue
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultVenue, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        self.latitude = latitude

        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(address is not None)
        assert(isinstance(address, unicode_type))  # unicode on python 2, str on python 3
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, unicode_type))  # unicode on python 2, str on python 3
        self.foursquare_id = foursquare_id

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultVenue, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultVenue

class InlineQueryResultContact (InlineQueryResult):
    """
    Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcontact
    """
    def __init__(self, type, id, phone_number, first_name, last_name = None, reply_markup = None, input_message_content = None, thumb_url = None, thumb_width = None, thumb_height = None):
        """
        Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the contact.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcontact


        Parameters:

        :param type: Type of the result, must be contact
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 Bytes
        :type  id:  str

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the contact
        :type    input_message_content:  InputMessageContent

        :keyword thumb_url: Optional. Url of the thumbnail for the result
        :type    thumb_url:  str

        :keyword thumb_width: Optional. Thumbnail width
        :type    thumb_width:  int

        :keyword thumb_height: Optional. Thumbnail height
        :type    thumb_height:  int
        """
        super(InlineQueryResultContact, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content

        assert(thumb_url is None or isinstance(thumb_url, unicode_type))  # unicode on python 2, str on python 3
        self.thumb_url = thumb_url

        assert(thumb_width is None or isinstance(thumb_width, int))
        self.thumb_width = thumb_width

        assert(thumb_height is None or isinstance(thumb_height, int))
        self.thumb_height = thumb_height
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultContact, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["phone_number"] = self.phone_number
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        if self.thumb_url is not None:
            array["thumb_url"] = self.thumb_url
        if self.thumb_width is not None:
            array["thumb_width"] = self.thumb_width
        if self.thumb_height is not None:
            array["thumb_height"] = self.thumb_height
        return array
    # end def to_array
# end class InlineQueryResultContact

class InlineQueryResultCachedPhoto (InlineQueryResult):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

    https://core.telegram.org/bots/api#inlinequeryresultcachedphoto
    """
    def __init__(self, type, id, photo_file_id, title = None, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a photo stored on the Telegram servers. By default, this photo will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the photo.

        https://core.telegram.org/bots/api#inlinequeryresultcachedphoto


        Parameters:

        :param type: Type of the result, must be photo
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param photo_file_id: A valid file identifier of the photo
        :type  photo_file_id:  str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword caption: Optional. Caption of the photo to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the photo
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedPhoto, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(photo_file_id is not None)
        assert(isinstance(photo_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.photo_file_id = photo_file_id

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedPhoto, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["photo_file_id"] = self.photo_file_id
        if self.title is not None:
            array["title"] = self.title
        if self.description is not None:
            array["description"] = self.description
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedPhoto

class InlineQueryResultCachedGif (InlineQueryResult):
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedgif
    """
    def __init__(self, type, id, gif_file_id, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to an animated GIF file stored on the Telegram servers. By default, this animated GIF file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedgif


        Parameters:

        :param type: Type of the result, must be gif
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param gif_file_id: A valid file identifier for the GIF file
        :type  gif_file_id:  str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword caption: Optional. Caption of the GIF file to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the GIF animation
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedGif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(gif_file_id is not None)
        assert(isinstance(gif_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.gif_file_id = gif_file_id

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedGif, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["gif_file_id"] = self.gif_file_id
        if self.title is not None:
            array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedGif

class InlineQueryResultCachedMpeg4Gif (InlineQueryResult):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

    https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif
    """
    def __init__(self, type, id, mpeg4_file_id, title = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers. By default, this animated MPEG-4 file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the animation.

        https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif


        Parameters:

        :param type: Type of the result, must be mpeg4_gif
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param mpeg4_file_id: A valid file identifier for the MP4 file
        :type  mpeg4_file_id:  str


        Optional keyword parameters:

        :keyword title: Optional. Title for the result
        :type    title:  str

        :keyword caption: Optional. Caption of the MPEG-4 file to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video animation
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedMpeg4Gif, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(mpeg4_file_id is not None)
        assert(isinstance(mpeg4_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.mpeg4_file_id = mpeg4_file_id

        assert(title is None or isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedMpeg4Gif, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["mpeg4_file_id"] = self.mpeg4_file_id
        if self.title is not None:
            array["title"] = self.title
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedMpeg4Gif

class InlineQueryResultCachedSticker (InlineQueryResult):
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedsticker
    """
    def __init__(self, type, id, sticker_file_id, reply_markup = None, input_message_content = None):
        """
        Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the sticker.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedsticker


        Parameters:

        :param type: Type of the result, must be sticker
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param sticker_file_id: A valid file identifier of the sticker
        :type  sticker_file_id:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the sticker
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedSticker, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(sticker_file_id is not None)
        assert(isinstance(sticker_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.sticker_file_id = sticker_file_id

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedSticker, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["sticker_file_id"] = self.sticker_file_id
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedSticker

class InlineQueryResultCachedDocument (InlineQueryResult):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only pdf-files and zip archives can be sent using this method.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcacheddocument
    """
    def __init__(self, type, id, title, document_file_id, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the file. Currently, only pdf-files and zip archives can be sent using this method.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcacheddocument


        Parameters:

        :param type: Type of the result, must be document
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param title: Title for the result
        :type  title:  str

        :param document_file_id: A valid file identifier for the file
        :type  document_file_id:  str


        Optional keyword parameters:

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword caption: Optional. Caption of the document to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the file
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedDocument, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(document_file_id is not None)
        assert(isinstance(document_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.document_file_id = document_file_id

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedDocument, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["title"] = self.title
        array["document_file_id"] = self.document_file_id
        if self.description is not None:
            array["description"] = self.description
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedDocument

class InlineQueryResultCachedVideo (InlineQueryResult):
    """
    Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvideo
    """
    def __init__(self, type, id, video_file_id, title, description = None, caption = None, reply_markup = None, input_message_content = None):
        """
        Represents a link to a video file stored on the Telegram servers. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use input_message_content to send a message with the specified content instead of the video.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvideo


        Parameters:

        :param type: Type of the result, must be video
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param video_file_id: A valid file identifier for the video file
        :type  video_file_id:  str

        :param title: Title for the result
        :type  title:  str


        Optional keyword parameters:

        :keyword description: Optional. Short description of the result
        :type    description:  str

        :keyword caption: Optional. Caption of the video to be sent, 0-200 characters
        :type    caption:  str

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the video
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedVideo, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(video_file_id is not None)
        assert(isinstance(video_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.video_file_id = video_file_id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(description is None or isinstance(description, unicode_type))  # unicode on python 2, str on python 3
        self.description = description

        assert(caption is None or isinstance(caption, unicode_type))  # unicode on python 2, str on python 3
        self.caption = caption

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedVideo, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["video_file_id"] = self.video_file_id
        array["title"] = self.title
        if self.description is not None:
            array["description"] = self.description
        if self.caption is not None:
            array["caption"] = self.caption
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedVideo

class InlineQueryResultCachedVoice (InlineQueryResult):
    """
    Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedvoice
    """
    def __init__(self, type, id, voice_file_id, title, reply_markup = None, input_message_content = None):
        """
        Represents a link to a voice message stored on the Telegram servers. By default, this voice message will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the voice message.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedvoice


        Parameters:

        :param type: Type of the result, must be voice
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param voice_file_id: A valid file identifier for the voice message
        :type  voice_file_id:  str

        :param title: Voice message title
        :type  title:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the voice message
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedVoice, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(voice_file_id is not None)
        assert(isinstance(voice_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.voice_file_id = voice_file_id

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedVoice, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["voice_file_id"] = self.voice_file_id
        array["title"] = self.title
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedVoice

class InlineQueryResultCachedAudio (InlineQueryResult):
    """
    Represents a link to an mp3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inlinequeryresultcachedaudio
    """
    def __init__(self, type, id, audio_file_id, reply_markup = None, input_message_content = None):
        """
        Represents a link to an mp3 audio file stored on the Telegram servers. By default, this audio file will be sent by the user. Alternatively, you can use input_message_content to send a message with the specified content instead of the audio.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inlinequeryresultcachedaudio


        Parameters:

        :param type: Type of the result, must be audio
        :type  type:  str

        :param id: Unique identifier for this result, 1-64 bytes
        :type  id:  str

        :param audio_file_id: A valid file identifier for the audio file
        :type  audio_file_id:  str


        Optional keyword parameters:

        :keyword reply_markup: Optional. An Inline keyboard attached to the message
        :type    reply_markup:  InlineKeyboardMarkup

        :keyword input_message_content: Optional. Content of the message to be sent instead of the audio
        :type    input_message_content:  InputMessageContent
        """
        super(InlineQueryResultCachedAudio, self).__init__(id)

        assert(type is not None)
        assert(isinstance(type, unicode_type))  # unicode on python 2, str on python 3
        self.type = type

        assert(id is not None)
        assert(isinstance(id, unicode_type))  # unicode on python 2, str on python 3
        self.id = id

        assert(audio_file_id is not None)
        assert(isinstance(audio_file_id, unicode_type))  # unicode on python 2, str on python 3
        self.audio_file_id = audio_file_id

        self.reply_markup = reply_markup

        self.input_message_content = input_message_content
    # end def __init__

    def to_array(self):
        array = super(InlineQueryResultCachedAudio, self).to_array()
        array["type"] = self.type
        array["id"] = self.id
        array["audio_file_id"] = self.audio_file_id
        if self.reply_markup is not None:
            array["reply_markup"] = self.reply_markup
        if self.input_message_content is not None:
            array["input_message_content"] = self.input_message_content
        return array
    # end def to_array
# end class InlineQueryResultCachedAudio

class InputTextMessageContent (InputMessageContent):
    """
    Represents the content of a text message to be sent as the result of an inline query.

    https://core.telegram.org/bots/api#inputtextmessagecontent
    """
    def __init__(self, message_text, parse_mode = None, disable_web_page_preview = None):
        """
        Represents the content of a text message to be sent as the result of an inline query.

        https://core.telegram.org/bots/api#inputtextmessagecontent


        Parameters:

        :param message_text: Text of the message to be sent, 1-4096 characters
        :type  message_text:  str


        Optional keyword parameters:

        :keyword parse_mode: Optional. Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :type    parse_mode:  str

        :keyword disable_web_page_preview: Optional. Disables link previews for links in the sent message
        :type    disable_web_page_preview:  bool
        """
        super(InputTextMessageContent, self).__init__(id)

        assert(message_text is not None)
        assert(isinstance(message_text, unicode_type))  # unicode on python 2, str on python 3
        self.message_text = message_text

        assert(parse_mode is None or isinstance(parse_mode, unicode_type))  # unicode on python 2, str on python 3
        self.parse_mode = parse_mode

        assert(disable_web_page_preview is None or isinstance(disable_web_page_preview, bool))
        self.disable_web_page_preview = disable_web_page_preview
    # end def __init__

    def to_array(self):
        array = super(InputTextMessageContent, self).to_array()
        array["message_text"] = self.message_text
        if self.parse_mode is not None:
            array["parse_mode"] = self.parse_mode
        if self.disable_web_page_preview is not None:
            array["disable_web_page_preview"] = self.disable_web_page_preview
        return array
    # end def to_array
# end class InputTextMessageContent

class InputLocationMessageContent (InputMessageContent):
    """
    Represents the content of a location message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputlocationmessagecontent
    """
    def __init__(self, latitude, longitude):
        """
        Represents the content of a location message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputlocationmessagecontent


        Parameters:

        :param latitude: Latitude of the location in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the location in degrees
        :type  longitude:  Float
        """
        super(InputLocationMessageContent, self).__init__(id)

        self.latitude = latitude

        self.longitude = longitude
    # end def __init__

    def to_array(self):
        array = super(InputLocationMessageContent, self).to_array()
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        return array
    # end def to_array
# end class InputLocationMessageContent

class InputVenueMessageContent (InputMessageContent):
    """
    Represents the content of a venue message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputvenuemessagecontent
    """
    def __init__(self, latitude, longitude, title, address, foursquare_id = None):
        """
        Represents the content of a venue message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputvenuemessagecontent


        Parameters:

        :param latitude: Latitude of the venue in degrees
        :type  latitude:  Float

        :param longitude: Longitude of the venue in degrees
        :type  longitude:  Float

        :param title: Name of the venue
        :type  title:  str

        :param address: Address of the venue
        :type  address:  str


        Optional keyword parameters:

        :keyword foursquare_id: Optional. Foursquare identifier of the venue, if known
        :type    foursquare_id:  str
        """
        super(InputVenueMessageContent, self).__init__(id)

        self.latitude = latitude

        self.longitude = longitude

        assert(title is not None)
        assert(isinstance(title, unicode_type))  # unicode on python 2, str on python 3
        self.title = title

        assert(address is not None)
        assert(isinstance(address, unicode_type))  # unicode on python 2, str on python 3
        self.address = address

        assert(foursquare_id is None or isinstance(foursquare_id, unicode_type))  # unicode on python 2, str on python 3
        self.foursquare_id = foursquare_id
    # end def __init__

    def to_array(self):
        array = super(InputVenueMessageContent, self).to_array()
        array["latitude"] = self.latitude
        array["longitude"] = self.longitude
        array["title"] = self.title
        array["address"] = self.address
        if self.foursquare_id is not None:
            array["foursquare_id"] = self.foursquare_id
        return array
    # end def to_array
# end class InputVenueMessageContent

class InputContactMessageContent (InputMessageContent):
    """
    Represents the content of a contact message to be sent as the result of an inline query.
    Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

    https://core.telegram.org/bots/api#inputcontactmessagecontent
    """
    def __init__(self, phone_number, first_name, last_name = None):
        """
        Represents the content of a contact message to be sent as the result of an inline query.
        Note: This will only work in Telegram versions released after 9 April, 2016. Older clients will ignore them.

        https://core.telegram.org/bots/api#inputcontactmessagecontent


        Parameters:

        :param phone_number: Contact's phone number
        :type  phone_number:  str

        :param first_name: Contact's first name
        :type  first_name:  str


        Optional keyword parameters:

        :keyword last_name: Optional. Contact's last name
        :type    last_name:  str
        """
        super(InputContactMessageContent, self).__init__(id)

        assert(phone_number is not None)
        assert(isinstance(phone_number, unicode_type))  # unicode on python 2, str on python 3
        self.phone_number = phone_number

        assert(first_name is not None)
        assert(isinstance(first_name, unicode_type))  # unicode on python 2, str on python 3
        self.first_name = first_name

        assert(last_name is None or isinstance(last_name, unicode_type))  # unicode on python 2, str on python 3
        self.last_name = last_name
    # end def __init__

    def to_array(self):
        array = super(InputContactMessageContent, self).to_array()
        array["phone_number"] = self.phone_number
        array["first_name"] = self.first_name
        if self.last_name is not None:
            array["last_name"] = self.last_name
        return array
    # end def to_array
# end class InputContactMessageContent

class ChosenInlineResult (InlineQueryResult):
    """
    Represents a result of an inline query that was chosen by the user and sent to their chat partner.

    https://core.telegram.org/bots/api#choseninlineresult
    """
    def __init__(self, result_id, from_peer, query, location = None, inline_message_id = None):
        """
        Represents a result of an inline query that was chosen by the user and sent to their chat partner.

        https://core.telegram.org/bots/api#choseninlineresult


        Parameters:

        :param result_id: The unique identifier for the result that was chosen
        :type  result_id:  str

        :param from_peer: The user that chose the result
        :type  from_peer:  User

        :param query: The query that was used to obtain the result
        :type  query:  str


        Optional keyword parameters:

        :keyword location: Optional. Sender location, only for bots that require user location
        :type    location:  Location

        :keyword inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an inline keyboard attached to the message. Will be also received in callback queries and can be used to edit the message.
        :type    inline_message_id:  str
        """
        super(ChosenInlineResult, self).__init__(id)

        assert(result_id is not None)
        assert(isinstance(result_id, unicode_type))  # unicode on python 2, str on python 3
        self.result_id = result_id

        self.from_peer = from_peer

        self.location = location

        assert(inline_message_id is None or isinstance(inline_message_id, unicode_type))  # unicode on python 2, str on python 3
        self.inline_message_id = inline_message_id

        assert(query is not None)
        assert(isinstance(query, unicode_type))  # unicode on python 2, str on python 3
        self.query = query
    # end def __init__

    def to_array(self):
        array = super(ChosenInlineResult, self).to_array()
        array["result_id"] = self.result_id
        array["from_peer"] = self.from_peer
        array["query"] = self.query
        if self.location is not None:
            array["location"] = self.location
        if self.inline_message_id is not None:
            array["inline_message_id"] = self.inline_message_id
        return array
    # end def to_array
# end class ChosenInlineResult

