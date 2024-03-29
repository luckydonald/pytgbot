#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pytgbot.api_types.sendable.reply_markup import InlineKeyboardMarkup
from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup
from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardRemove
from pytgbot.api_types.sendable.reply_markup import ForceReply
from pytgbot.api_types.sendable.input_media import InputMediaDocument
from pytgbot.api_types.sendable.input_media import InputMediaAudio
from pytgbot.api_types.sendable.input_media import InputMediaPhoto
from pytgbot.api_types.sendable.input_media import InputMediaVideo
from pytgbot.api_types.sendable.input_media import InputMedia
from pytgbot.api_types.receivable.stickers import MaskPosition
from pytgbot.api_types.sendable.passport import PassportElementError
from pytgbot.api_types.sendable.payments import ShippingOption
from pytgbot.api_types.sendable.payments import LabeledPrice
from pytgbot.api_types.receivable.media import MessageEntity
from pytgbot.api_types.sendable.command import BotCommandScope
from pytgbot.api_types.sendable.command import BotCommand
from pytgbot.api_types.receivable.peer import ChatPermissions
from pytgbot.api_types.sendable.inline import InlineQueryResult
from pytgbot.api_types.sendable.files import InputFile
from telethon.tl.functions.messages import SetTypingRequest
from luckydonaldUtils.logger import logging
from telethon.client.chats import _ChatAction
from telethon.tl.types import TypeSendMessageAction
from telethon.errors import BotMethodInvalidError
from fastapi.params import Query
from serializer import to_web_api, get_entity
from telethon import TelegramClient
from fastapi import APIRouter, HTTPException
from typing import Union, List, Optional
from enum import Enum

from .....tools.responses import r_success, JSONableResponse
from .....constants import TOKEN_VALIDATION
from ..generated.models import *

__author__ = 'luckydonald'  # but it's automatically generated.


logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


routes = APIRouter()  # Basically a Blueprint


FAST_API_ISSUE_884_IS_FIXED = False


if FAST_API_ISSUE_884_IS_FIXED:
    from pydantic import Json

    def parse_obj_as(_, obj, *__, **___):
        """
        we don't need any additional parsing as fastapi now does that correctly
        """
        return obj
    # end def
else:
    class __JsonWrapper:
        from pydantic import Json

        def __getitem__(self, item):
            """ Basically throw away `[Type]` when used like `Json[Type]` """
            return self.Json
        # end def
    # end def
    Json = __JsonWrapper()  # so Json[Type] does call Json.__getitem__(self, item=Type)

    from pydantic import parse_obj_as
# end if


@routes.api_route('/{token}/getUpdates', methods=['GET', 'POST'], tags=['official'])
async def get_updates(
    token: str = TOKEN_VALIDATION,
    offset: Optional[int] = Query(None, description='Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will forgotten.'),
    limit: Optional[int] = Query(None, description='Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.'),
    timeout: Optional[int] = Query(None, description='Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.'),
    allowed_updates: Optional[List[str]] = Query(None, description='A JSON-serialized list of the update types you want your bot to receive. For example, specify ["message", "edited_channel_post", "callback_query"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used.Please note that this parameter doesn\'t affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.'),
) -> JSONableResponse:
    """
    Use this method to receive incoming updates using long polling (wiki). An Array of Update objects is returned.

    Notes1. This method will not work if an outgoing webhook is set up.2. In order to avoid getting duplicate updates, recalculate offset after each server response.


    https://core.telegram.org/bots/api#getupdates
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_updates(
        offset=offset,
        limit=limit,
        timeout=timeout,
        allowed_updates=allowed_updates,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setWebhook', methods=['GET', 'POST'], tags=['official'])
async def set_webhook(
    token: str = TOKEN_VALIDATION,
    url: str = Query(..., description='HTTPS url to send updates to. Use an empty string to remove webhook integration'),
    certificate: Optional[Json['InputFileModel']] = Query(None, description='Upload your public key certificate so that the root certificate in use can be checked. See our self-signed guide for details.'),
    ip_address: Optional[str] = Query(None, description='The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS'),
    max_connections: Optional[int] = Query(None, description="Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to 40. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput."),
    allowed_updates: Optional[List[str]] = Query(None, description='A JSON-serialized list of the update types you want your bot to receive. For example, specify ["message", "edited_channel_post", "callback_query"] to only receive updates of these types. See Update for a complete list of available update types. Specify an empty list to receive all update types except chat_member (default). If not specified, the previous setting will be used.Please note that this parameter doesn\'t affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.'),
    drop_pending_updates: Optional[bool] = Query(None, description='Pass True to drop all pending updates'),
) -> JSONableResponse:
    """
    Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns True on success.
    If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. https://www.example.com/<token>. Since nobody else knows your bot's token, you can be pretty sure it's us.

    Notes1. You will not be able to receive updates using getUpdates for as long as an outgoing webhook is set up.2. To use a self-signed certificate, you need to upload your public key certificate using certificate parameter. Please upload as InputFile, sending a String will not work.3. Ports currently supported for Webhooks: 443, 80, 88, 8443.
    NEW! If you're having any trouble setting up webhooks, please check out this amazing guide to Webhooks.


    https://core.telegram.org/bots/api#setwebhook
    """
    certificate: Optional[InputFileModel] = parse_obj_as(
        Optional[InputFileModel],
        obj=certificate,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.set_webhook(
        url=url,
        certificate=certificate,
        ip_address=ip_address,
        max_connections=max_connections,
        allowed_updates=allowed_updates,
        drop_pending_updates=drop_pending_updates,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/deleteWebhook', methods=['GET', 'POST'], tags=['official'])
async def delete_webhook(
    token: str = TOKEN_VALIDATION,
    drop_pending_updates: Optional[bool] = Query(None, description='Pass True to drop all pending updates'),
) -> JSONableResponse:
    """
    Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.

    https://core.telegram.org/bots/api#deletewebhook
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.delete_webhook(
        drop_pending_updates=drop_pending_updates,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getWebhookInfo', methods=['GET', 'POST'], tags=['official'])
async def get_webhook_info(
    token: str = TOKEN_VALIDATION,
) -> JSONableResponse:
    """
    Use this method to get current webhook status. Requires no parameters. On success, returns a WebhookInfo object. If the bot is using getUpdates, will return an object with the url field empty.

    https://core.telegram.org/bots/api#getwebhookinfo
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_webhook_info(
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getMe', methods=['GET', 'POST'], tags=['official'])
async def get_me(
    token: str = TOKEN_VALIDATION,
) -> JSONableResponse:
    """
    A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a User object.

    https://core.telegram.org/bots/api#getme
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_me(
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/logOut', methods=['GET', 'POST'], tags=['official'])
async def log_out(
    token: str = TOKEN_VALIDATION,
) -> JSONableResponse:
    """
    Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters.

    https://core.telegram.org/bots/api#logout
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.log_out(
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendMessage', methods=['GET', 'POST'], tags=['official'])
async def send_message(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    text: str = Query(..., description='Text of the message to be sent, 1-4096 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the message text. See formatting options for more details.'),
    entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode'),
    disable_web_page_preview: Optional[bool] = Query(None, description='Disables link previews for links in this message'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send text messages. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendmessage
    """
    entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_message(
        entity=entity,
        text=text,
        parse_mode=parse_mode,
        entities=entities,
        disable_web_page_preview=disable_web_page_preview,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/forwardMessage', methods=['GET', 'POST'], tags=['official'])
async def forward_message(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    from_chat_id: Union[int, str] = Query(..., description='Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)'),
    message_id: int = Query(..., description='Message identifier in the chat specified in from_chat_id'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the forwarded message from forwarding and saving'),
) -> JSONableResponse:
    """
    Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#forwardmessage
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.forward_message(
        entity=entity,
        from_chat_id=from_chat_id,
        message_id=message_id,
        disable_notification=disable_notification,
        protect_content=protect_content,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/copyMessage', methods=['GET', 'POST'], tags=['official'])
async def copy_message(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    from_chat_id: Union[int, str] = Query(..., description='Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername)'),
    message_id: int = Query(..., description='Message identifier in the chat specified in from_chat_id'),
    caption: Optional[str] = Query(None, description='New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the new caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to copy messages of any kind. Service messages and invoice messages can't be copied. The method is analogous to the method forwardMessage, but the copied message doesn't have a link to the original message. Returns the MessageId of the sent message on success.

    https://core.telegram.org/bots/api#copymessage
    """
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.copy_message(
        entity=entity,
        from_chat_id=from_chat_id,
        message_id=message_id,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendPhoto', methods=['GET', 'POST'], tags=['official'])
async def send_photo(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    photo: Json[Union['InputFileModel', str]] = Query(..., description="Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20. More info on Sending Files »"),
    caption: Optional[str] = Query(None, description='Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the photo caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send photos. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendphoto
    """
    photo: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=photo,
    )
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_photo(
        entity=entity,
        photo=photo,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendAudio', methods=['GET', 'POST'], tags=['official'])
async def send_audio(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    audio: Json[Union['InputFileModel', str]] = Query(..., description='Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'),
    caption: Optional[str] = Query(None, description='Audio caption, 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the audio caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    duration: Optional[int] = Query(None, description='Duration of the audio in seconds'),
    performer: Optional[str] = Query(None, description='Performer'),
    title: Optional[str] = Query(None, description='Track name'),
    thumb: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail\'s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can\'t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent Message is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.
    For sending voice messages, use the sendVoice method instead.

    https://core.telegram.org/bots/api#sendaudio
    """
    audio: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=audio,
    )
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    thumb: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=thumb,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_audio(
        entity=entity,
        audio=audio,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        duration=duration,
        performer=performer,
        title=title,
        thumb=thumb,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendDocument', methods=['GET', 'POST'], tags=['official'])
async def send_document(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    document: Json[Union['InputFileModel', str]] = Query(..., description='File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'),
    thumb: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail\'s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can\'t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'),
    caption: Optional[str] = Query(None, description='Document caption (may also be used when resending documents by file_id), 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the document caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    disable_content_type_detection: Optional[bool] = Query(None, description='Disables automatic server-side content type detection for files uploaded using multipart/form-data'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send general files. On success, the sent Message is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#senddocument
    """
    document: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=document,
    )
    thumb: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=thumb,
    )
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_document(
        entity=entity,
        document=document,
        thumb=thumb,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        disable_content_type_detection=disable_content_type_detection,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendVideo', methods=['GET', 'POST'], tags=['official'])
async def send_video(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    video: Json[Union['InputFileModel', str]] = Query(..., description='Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. More info on Sending Files »'),
    duration: Optional[int] = Query(None, description='Duration of sent video in seconds'),
    width: Optional[int] = Query(None, description='Video width'),
    height: Optional[int] = Query(None, description='Video height'),
    thumb: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail\'s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can\'t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'),
    caption: Optional[str] = Query(None, description='Video caption (may also be used when resending videos by file_id), 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the video caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    supports_streaming: Optional[bool] = Query(None, description='Pass True, if the uploaded video is suitable for streaming'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document). On success, the sent Message is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#sendvideo
    """
    video: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=video,
    )
    thumb: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=thumb,
    )
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_video(
        entity=entity,
        video=video,
        duration=duration,
        width=width,
        height=height,
        thumb=thumb,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        supports_streaming=supports_streaming,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendAnimation', methods=['GET', 'POST'], tags=['official'])
async def send_animation(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    animation: Json[Union['InputFileModel', str]] = Query(..., description='Animation to send. Pass a file_id as String to send an animation that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an animation from the Internet, or upload a new animation using multipart/form-data. More info on Sending Files »'),
    duration: Optional[int] = Query(None, description='Duration of sent animation in seconds'),
    width: Optional[int] = Query(None, description='Animation width'),
    height: Optional[int] = Query(None, description='Animation height'),
    thumb: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail\'s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can\'t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'),
    caption: Optional[str] = Query(None, description='Animation caption (may also be used when resending animation by file_id), 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the animation caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send animation files (GIF or H.264/MPEG-4 AVC video without sound). On success, the sent Message is returned. Bots can currently send animation files of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#sendanimation
    """
    animation: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=animation,
    )
    thumb: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=thumb,
    )
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_animation(
        entity=entity,
        animation=animation,
        duration=duration,
        width=width,
        height=height,
        thumb=thumb,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendVoice', methods=['GET', 'POST'], tags=['official'])
async def send_voice(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    voice: Json[Union['InputFileModel', str]] = Query(..., description='Audio file to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'),
    caption: Optional[str] = Query(None, description='Voice message caption, 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the voice message caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    duration: Optional[int] = Query(None, description='Duration of the voice message in seconds'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message. For this to work, your audio must be in an .OGG file encoded with OPUS (other formats may be sent as Audio or Document). On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

    https://core.telegram.org/bots/api#sendvoice
    """
    voice: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=voice,
    )
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_voice(
        entity=entity,
        voice=voice,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        duration=duration,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendVideoNote', methods=['GET', 'POST'], tags=['official'])
async def send_video_note(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    video_note: Json[Union['InputFileModel', str]] = Query(..., description='Video note to send. Pass a file_id as String to send a video note that exists on the Telegram servers (recommended) or upload a new video using multipart/form-data. More info on Sending Files ». Sending video notes by a URL is currently unsupported'),
    duration: Optional[int] = Query(None, description='Duration of sent video in seconds'),
    length: Optional[int] = Query(None, description='Video width and height, i.e. diameter of the video message'),
    thumb: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail\'s width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can\'t be reused and can be only uploaded as a new file, so you can pass "attach://<file_attach_name>" if the thumbnail was uploaded using multipart/form-data under <file_attach_name>. More info on Sending Files »'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    As of v.4.0, Telegram clients support rounded square mp4 videos of up to 1 minute long. Use this method to send video messages. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendvideonote
    """
    video_note: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=video_note,
    )
    thumb: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=thumb,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_video_note(
        entity=entity,
        video_note=video_note,
        duration=duration,
        length=length,
        thumb=thumb,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendMediaGroup', methods=['GET', 'POST'], tags=['official'])
async def send_media_group(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    media: Json[Union[List['InputMediaAudioModel'], List['InputMediaDocumentModel'], List['InputMediaPhotoModel'], List['InputMediaVideoModel']]] = Query(..., description='A JSON-serialized array describing messages to be sent, must include 2-10 items'),
    disable_notification: Optional[bool] = Query(None, description='Sends messages silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent messages from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the messages are a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
) -> JSONableResponse:
    """
    Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of Messages that were sent is returned.

    https://core.telegram.org/bots/api#sendmediagroup
    """
    media: Union[List[InputMediaAudioModel], List[InputMediaDocumentModel], List[InputMediaPhotoModel], List[InputMediaVideoModel]] = parse_obj_as(
        Union[List[InputMediaAudioModel], List[InputMediaDocumentModel], List[InputMediaPhotoModel], List[InputMediaVideoModel]],
        obj=media,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_media_group(
        entity=entity,
        media=media,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendLocation', methods=['GET', 'POST'], tags=['official'])
async def send_location(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    latitude: float = Query(..., description='Latitude of the location'),
    longitude: float = Query(..., description='Longitude of the location'),
    horizontal_accuracy: Optional[float] = Query(None, description='The radius of uncertainty for the location, measured in meters; 0-1500'),
    live_period: Optional[int] = Query(None, description='Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.'),
    heading: Optional[int] = Query(None, description='For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.'),
    proximity_alert_radius: Optional[int] = Query(None, description='For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send point on the map. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendlocation
    """
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_location(
        entity=entity,
        latitude=latitude,
        longitude=longitude,
        horizontal_accuracy=horizontal_accuracy,
        live_period=live_period,
        heading=heading,
        proximity_alert_radius=proximity_alert_radius,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/editMessageLiveLocation', methods=['GET', 'POST'], tags=['official'])
async def edit_message_live_location(
    token: str = TOKEN_VALIDATION,
    latitude: float = Query(..., description='Latitude of new location'),
    longitude: float = Query(..., description='Longitude of new location'),
    chat_id: Optional[Union[int, str]] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the message to edit'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
    horizontal_accuracy: Optional[float] = Query(None, description='The radius of uncertainty for the location, measured in meters; 0-1500'),
    heading: Optional[int] = Query(None, description='Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.'),
    proximity_alert_radius: Optional[int] = Query(None, description='Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for a new inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to edit live location messages. A location can be edited until its live_period expires or editing is explicitly disabled by a call to stopMessageLiveLocation. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    https://core.telegram.org/bots/api#editmessagelivelocation
    """
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.edit_message_live_location(
        latitude=latitude,
        longitude=longitude,
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
        horizontal_accuracy=horizontal_accuracy,
        heading=heading,
        proximity_alert_radius=proximity_alert_radius,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/stopMessageLiveLocation', methods=['GET', 'POST'], tags=['official'])
async def stop_message_live_location(
    token: str = TOKEN_VALIDATION,
    chat_id: Optional[Union[int, str]] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the message with live location to stop'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for a new inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to stop updating a live location message before live_period expires. On success, if the message is not an inline message, the edited Message is returned, otherwise True is returned.

    https://core.telegram.org/bots/api#stopmessagelivelocation
    """
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.stop_message_live_location(
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendVenue', methods=['GET', 'POST'], tags=['official'])
async def send_venue(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    latitude: float = Query(..., description='Latitude of the venue'),
    longitude: float = Query(..., description='Longitude of the venue'),
    title: str = Query(..., description='Name of the venue'),
    address: str = Query(..., description='Address of the venue'),
    foursquare_id: Optional[str] = Query(None, description='Foursquare identifier of the venue'),
    foursquare_type: Optional[str] = Query(None, description='Foursquare type of the venue, if known. (For example, "arts_entertainment/default", "arts_entertainment/aquarium" or "food/icecream".)'),
    google_place_id: Optional[str] = Query(None, description='Google Places identifier of the venue'),
    google_place_type: Optional[str] = Query(None, description='Google Places type of the venue. (See supported types.)'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send information about a venue. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendvenue
    """
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_venue(
        entity=entity,
        latitude=latitude,
        longitude=longitude,
        title=title,
        address=address,
        foursquare_id=foursquare_id,
        foursquare_type=foursquare_type,
        google_place_id=google_place_id,
        google_place_type=google_place_type,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendContact', methods=['GET', 'POST'], tags=['official'])
async def send_contact(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    phone_number: str = Query(..., description="Contact's phone number"),
    first_name: str = Query(..., description="Contact's first name"),
    last_name: Optional[str] = Query(None, description="Contact's last name"),
    vcard: Optional[str] = Query(None, description='Additional data about the contact in the form of a vCard, 0-2048 bytes'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send phone contacts. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendcontact
    """
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_contact(
        entity=entity,
        phone_number=phone_number,
        first_name=first_name,
        last_name=last_name,
        vcard=vcard,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendPoll', methods=['GET', 'POST'], tags=['official'])
async def send_poll(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    question: str = Query(..., description='Poll question, 1-300 characters'),
    options: List[str] = Query(..., description='A JSON-serialized list of answer options, 2-10 strings 1-100 characters each'),
    is_anonymous: Optional[bool] = Query(None, description='True, if the poll needs to be anonymous, defaults to True'),
    type: Optional[str] = Query(None, description='Poll type, "quiz" or "regular", defaults to "regular"'),
    allows_multiple_answers: Optional[bool] = Query(None, description='True, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to False'),
    correct_option_id: Optional[int] = Query(None, description='0-based identifier of the correct answer option, required for polls in quiz mode'),
    explanation: Optional[str] = Query(None, description='Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing'),
    explanation_parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the explanation. See formatting options for more details.'),
    explanation_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of parse_mode'),
    open_period: Optional[int] = Query(None, description="Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with close_date."),
    close_date: Optional[int] = Query(None, description="Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with open_period."),
    is_closed: Optional[bool] = Query(None, description='Pass True, if the poll needs to be immediately closed. This can be useful for poll preview.'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send a native poll. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendpoll
    """
    explanation_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=explanation_entities,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_poll(
        entity=entity,
        question=question,
        options=options,
        is_anonymous=is_anonymous,
        type=type,
        allows_multiple_answers=allows_multiple_answers,
        correct_option_id=correct_option_id,
        explanation=explanation,
        explanation_parse_mode=explanation_parse_mode,
        explanation_entities=explanation_entities,
        open_period=open_period,
        close_date=close_date,
        is_closed=is_closed,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendDice', methods=['GET', 'POST'], tags=['official'])
async def send_dice(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    emoji: Optional[str] = Query(None, description='Emoji on which the dice throw animation is based. Currently, must be one of "🎲", "🎯", "🏀", "⚽", "🎳", or "🎰". Dice can have values 1-6 for "🎲", "🎯" and "🎳", values 1-5 for "🏀" and "⚽", and values 1-64 for "🎰". Defaults to "🎲"'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send an animated emoji that will display a random value. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#senddice
    """
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_dice(
        entity=entity,
        emoji=emoji,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendChatAction', methods=['GET', 'POST'], tags=['official'])
async def send_chat_action(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    action: str = Query(..., description='Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes.'),
) -> JSONableResponse:
    """
    Use this method when you need to tell the user that something is happening on the bot's side. The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status). Returns True on success.

    Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message along the lines of "Retrieving image, please wait…", the bot may use sendChatAction with action = upload_photo. The user will see a "sending photo" status for the bot.

    We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

    https://core.telegram.org/bots/api#sendchataction
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_chat_action(
        entity=entity,
        action=action,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getUserProfilePhotos', methods=['GET', 'POST'], tags=['official'])
async def get_user_profile_photos(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='Unique identifier of the target user'),
    offset: Optional[int] = Query(None, description='Sequential number of the first photo to be returned. By default, all photos are returned.'),
    limit: Optional[int] = Query(None, description='Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.'),
) -> JSONableResponse:
    """
    Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

    https://core.telegram.org/bots/api#getuserprofilephotos
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_user_profile_photos(
        user_id=user_id,
        offset=offset,
        limit=limit,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getFile', methods=['GET', 'POST'], tags=['official'])
async def get_file(
    token: str = TOKEN_VALIDATION,
    file_id: str = Query(..., description='File identifier to get info about'),
) -> JSONableResponse:
    """
    Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a File object is returned. The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.
    Note: This function may not preserve the original file name and MIME type. You should save the file's MIME type and name (if available) when the File object is received.

    https://core.telegram.org/bots/api#getfile
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_file(
        file_id=file_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/banChatMember', methods=['GET', 'POST'], tags=['official'])
async def ban_chat_member(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
    until_date: Optional[int] = Query(None, description='Date when the user will be unbanned, unix time. If user is banned for more than 366 days or less than 30 seconds from the current time they are considered to be banned forever. Applied for supergroups and channels only.'),
    revoke_messages: Optional[bool] = Query(None, description='Pass True to delete all messages from the chat for the user that is being removed. If False, the user will be able to see messages in the group that were sent before the user was removed. Always True for supergroups and channels.'),
) -> JSONableResponse:
    """
    Use this method to ban a user in a group, a supergroup or a channel. In the case of supergroups and channels, the user will not be able to return to the chat on their own using invite links, etc., unless unbanned first. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#banchatmember
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.ban_chat_member(
        entity=entity,
        user_id=user_id,
        until_date=until_date,
        revoke_messages=revoke_messages,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/unbanChatMember', methods=['GET', 'POST'], tags=['official'])
async def unban_chat_member(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target group or username of the target supergroup or channel (in the format @channelusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
    only_if_banned: Optional[bool] = Query(None, description='Do nothing if the user is not banned'),
) -> JSONableResponse:
    """
    Use this method to unban a previously banned user in a supergroup or channel. The user will not return to the group or channel automatically, but will be able to join via link, etc. The bot must be an administrator for this to work. By default, this method guarantees that after the call the user is not a member of the chat, but will be able to join it. So if the user is a member of the chat they will also be removed from the chat. If you don't want this, use the parameter only_if_banned. Returns True on success.

    https://core.telegram.org/bots/api#unbanchatmember
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.unban_chat_member(
        entity=entity,
        user_id=user_id,
        only_if_banned=only_if_banned,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/restrictChatMember', methods=['GET', 'POST'], tags=['official'])
async def restrict_chat_member(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
    permissions: Json['ChatPermissionsModel'] = Query(..., description='A JSON-serialized object for new user permissions'),
    until_date: Optional[int] = Query(None, description='Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever'),
) -> JSONableResponse:
    """
    Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass True for all permissions to lift restrictions from a user. Returns True on success.

    https://core.telegram.org/bots/api#restrictchatmember
    """
    permissions: ChatPermissionsModel = parse_obj_as(
        ChatPermissionsModel,
        obj=permissions,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.restrict_chat_member(
        entity=entity,
        user_id=user_id,
        permissions=permissions,
        until_date=until_date,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/promoteChatMember', methods=['GET', 'POST'], tags=['official'])
async def promote_chat_member(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
    is_anonymous: Optional[bool] = Query(None, description="Pass True, if the administrator's presence in the chat is hidden"),
    can_manage_chat: Optional[bool] = Query(None, description='Pass True, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege'),
    can_post_messages: Optional[bool] = Query(None, description='Pass True, if the administrator can create channel posts, channels only'),
    can_edit_messages: Optional[bool] = Query(None, description='Pass True, if the administrator can edit messages of other users and can pin messages, channels only'),
    can_delete_messages: Optional[bool] = Query(None, description='Pass True, if the administrator can delete messages of other users'),
    can_manage_voice_chats: Optional[bool] = Query(None, description='Pass True, if the administrator can manage voice chats'),
    can_restrict_members: Optional[bool] = Query(None, description='Pass True, if the administrator can restrict, ban or unban chat members'),
    can_promote_members: Optional[bool] = Query(None, description='Pass True, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)'),
    can_change_info: Optional[bool] = Query(None, description='Pass True, if the administrator can change chat title, photo and other settings'),
    can_invite_users: Optional[bool] = Query(None, description='Pass True, if the administrator can invite new users to the chat'),
    can_pin_messages: Optional[bool] = Query(None, description='Pass True, if the administrator can pin messages, supergroups only'),
) -> JSONableResponse:
    """
    Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass False for all boolean parameters to demote a user. Returns True on success.

    https://core.telegram.org/bots/api#promotechatmember
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.promote_chat_member(
        entity=entity,
        user_id=user_id,
        is_anonymous=is_anonymous,
        can_manage_chat=can_manage_chat,
        can_post_messages=can_post_messages,
        can_edit_messages=can_edit_messages,
        can_delete_messages=can_delete_messages,
        can_manage_voice_chats=can_manage_voice_chats,
        can_restrict_members=can_restrict_members,
        can_promote_members=can_promote_members,
        can_change_info=can_change_info,
        can_invite_users=can_invite_users,
        can_pin_messages=can_pin_messages,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setChatAdministratorCustomTitle', methods=['GET', 'POST'], tags=['official'])
async def set_chat_administrator_custom_title(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
    custom_title: str = Query(..., description='New custom title for the administrator; 0-16 characters, emoji are not allowed'),
) -> JSONableResponse:
    """
    Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns True on success.

    https://core.telegram.org/bots/api#setchatadministratorcustomtitle
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_chat_administrator_custom_title(
        entity=entity,
        user_id=user_id,
        custom_title=custom_title,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/banChatSenderChat', methods=['GET', 'POST'], tags=['official'])
async def ban_chat_sender_chat(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    sender_chat_id: int = Query(..., description='Unique identifier of the target sender chat'),
) -> JSONableResponse:
    """
    Use this method to ban a channel chat in a supergroup or a channel. Until the chat is unbanned, the owner of the banned chat won't be able to send messages on behalf of any of their channels. The bot must be an administrator in the supergroup or channel for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#banchatsenderchat
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.ban_chat_sender_chat(
        entity=entity,
        sender_chat_id=sender_chat_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/unbanChatSenderChat', methods=['GET', 'POST'], tags=['official'])
async def unban_chat_sender_chat(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    sender_chat_id: int = Query(..., description='Unique identifier of the target sender chat'),
) -> JSONableResponse:
    """
    Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#unbanchatsenderchat
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.unban_chat_sender_chat(
        entity=entity,
        sender_chat_id=sender_chat_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setChatPermissions', methods=['GET', 'POST'], tags=['official'])
async def set_chat_permissions(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)'),
    permissions: Json['ChatPermissionsModel'] = Query(..., description='A JSON-serialized object for new default chat permissions'),
) -> JSONableResponse:
    """
    Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the can_restrict_members administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#setchatpermissions
    """
    permissions: ChatPermissionsModel = parse_obj_as(
        ChatPermissionsModel,
        obj=permissions,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_chat_permissions(
        entity=entity,
        permissions=permissions,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/exportChatInviteLink', methods=['GET', 'POST'], tags=['official'])
async def export_chat_invite_link(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method to generate a new primary invite link for a chat; any previously generated primary link is revoked. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the new invite link as String on success.

    Note: Each administrator in a chat generates their own invite links. Bots can't use invite links generated by other administrators. If you want your bot to work with invite links, it will need to generate its own link using exportChatInviteLink or by calling the getChat method. If your bot needs to generate a new primary invite link replacing its previous one, use exportChatInviteLink again.


    https://core.telegram.org/bots/api#exportchatinvitelink
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.export_chat_invite_link(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/createChatInviteLink', methods=['GET', 'POST'], tags=['official'])
async def create_chat_invite_link(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    name: Optional[str] = Query(None, description='Invite link name; 0-32 characters'),
    expire_date: Optional[int] = Query(None, description='Point in time (Unix timestamp) when the link will expire'),
    member_limit: Optional[int] = Query(None, description='Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999'),
    creates_join_request: Optional[bool] = Query(None, description="True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified"),
) -> JSONableResponse:
    """
    Use this method to create an additional invite link for a chat. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. The link can be revoked using the method revokeChatInviteLink. Returns the new invite link as ChatInviteLink object.

    https://core.telegram.org/bots/api#createchatinvitelink
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.create_chat_invite_link(
        entity=entity,
        name=name,
        expire_date=expire_date,
        member_limit=member_limit,
        creates_join_request=creates_join_request,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/editChatInviteLink', methods=['GET', 'POST'], tags=['official'])
async def edit_chat_invite_link(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    invite_link: str = Query(..., description='The invite link to edit'),
    name: Optional[str] = Query(None, description='Invite link name; 0-32 characters'),
    expire_date: Optional[int] = Query(None, description='Point in time (Unix timestamp) when the link will expire'),
    member_limit: Optional[int] = Query(None, description='Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999'),
    creates_join_request: Optional[bool] = Query(None, description="True, if users joining the chat via the link need to be approved by chat administrators. If True, member_limit can't be specified"),
) -> JSONableResponse:
    """
    Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a ChatInviteLink object.

    https://core.telegram.org/bots/api#editchatinvitelink
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.edit_chat_invite_link(
        entity=entity,
        invite_link=invite_link,
        name=name,
        expire_date=expire_date,
        member_limit=member_limit,
        creates_join_request=creates_join_request,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/revokeChatInviteLink', methods=['GET', 'POST'], tags=['official'])
async def revoke_chat_invite_link(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier of the target chat or username of the target channel (in the format @channelusername)'),
    invite_link: str = Query(..., description='The invite link to revoke'),
) -> JSONableResponse:
    """
    Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as ChatInviteLink object.

    https://core.telegram.org/bots/api#revokechatinvitelink
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.revoke_chat_invite_link(
        entity=entity,
        invite_link=invite_link,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/approveChatJoinRequest', methods=['GET', 'POST'], tags=['official'])
async def approve_chat_join_request(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
) -> JSONableResponse:
    """
    Use this method to approve a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.

    https://core.telegram.org/bots/api#approvechatjoinrequest
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.approve_chat_join_request(
        entity=entity,
        user_id=user_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/declineChatJoinRequest', methods=['GET', 'POST'], tags=['official'])
async def decline_chat_join_request(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
) -> JSONableResponse:
    """
    Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the can_invite_users administrator right. Returns True on success.

    https://core.telegram.org/bots/api#declinechatjoinrequest
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.decline_chat_join_request(
        entity=entity,
        user_id=user_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setChatPhoto', methods=['GET', 'POST'], tags=['official'])
async def set_chat_photo(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    photo: Json['InputFileModel'] = Query(..., description='New chat photo, uploaded using multipart/form-data'),
) -> JSONableResponse:
    """
    Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#setchatphoto
    """
    photo: InputFileModel = parse_obj_as(
        InputFileModel,
        obj=photo,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_chat_photo(
        entity=entity,
        photo=photo,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/deleteChatPhoto', methods=['GET', 'POST'], tags=['official'])
async def delete_chat_photo(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method to delete a chat photo. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#deletechatphoto
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.delete_chat_photo(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setChatTitle', methods=['GET', 'POST'], tags=['official'])
async def set_chat_title(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    title: str = Query(..., description='New chat title, 1-255 characters'),
) -> JSONableResponse:
    """
    Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#setchattitle
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_chat_title(
        entity=entity,
        title=title,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setChatDescription', methods=['GET', 'POST'], tags=['official'])
async def set_chat_description(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    description: Optional[str] = Query(None, description='New chat description, 0-255 characters'),
) -> JSONableResponse:
    """
    Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns True on success.

    https://core.telegram.org/bots/api#setchatdescription
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_chat_description(
        entity=entity,
        description=description,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/pinChatMessage', methods=['GET', 'POST'], tags=['official'])
async def pin_chat_message(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: int = Query(..., description='Identifier of a message to pin'),
    disable_notification: Optional[bool] = Query(None, description='Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels and private chats.'),
) -> JSONableResponse:
    """
    Use this method to add a message to the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

    https://core.telegram.org/bots/api#pinchatmessage
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.pin_chat_message(
        entity=entity,
        message_id=message_id,
        disable_notification=disable_notification,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/unpinChatMessage', methods=['GET', 'POST'], tags=['official'])
async def unpin_chat_message(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned.'),
) -> JSONableResponse:
    """
    Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

    https://core.telegram.org/bots/api#unpinchatmessage
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.unpin_chat_message(
        entity=entity,
        message_id=message_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/unpinAllChatMessages', methods=['GET', 'POST'], tags=['official'])
async def unpin_all_chat_messages(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method to clear the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can_pin_messages' administrator right in a supergroup or 'can_edit_messages' administrator right in a channel. Returns True on success.

    https://core.telegram.org/bots/api#unpinallchatmessages
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.unpin_all_chat_messages(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/leaveChat', methods=['GET', 'POST'], tags=['official'])
async def leave_chat(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method for your bot to leave a group, supergroup or channel. Returns True on success.

    https://core.telegram.org/bots/api#leavechat
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.leave_chat(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getChat', methods=['GET', 'POST'], tags=['official'])
async def get_chat(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method to get up to date information about the chat (current name of the user for one-on-one conversations, current username of a user, group or channel, etc.). Returns a Chat object on success.

    https://core.telegram.org/bots/api#getchat
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.get_chat(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getChatAdministrators', methods=['GET', 'POST'], tags=['official'])
async def get_chat_administrators(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method to get a list of administrators in a chat. On success, returns an Array of ChatMember objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.

    https://core.telegram.org/bots/api#getchatadministrators
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.get_chat_administrators(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getChatMemberCount', methods=['GET', 'POST'], tags=['official'])
async def get_chat_member_count(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)'),
) -> JSONableResponse:
    """
    Use this method to get the number of members in a chat. Returns Int on success.

    https://core.telegram.org/bots/api#getchatmembercount
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.get_chat_member_count(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getChatMember', methods=['GET', 'POST'], tags=['official'])
async def get_chat_member(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)'),
    user_id: int = Query(..., description='Unique identifier of the target user'),
) -> JSONableResponse:
    """
    Use this method to get information about a member of a chat. Returns a ChatMember object on success.

    https://core.telegram.org/bots/api#getchatmember
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.get_chat_member(
        entity=entity,
        user_id=user_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setChatStickerSet', methods=['GET', 'POST'], tags=['official'])
async def set_chat_sticker_set(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)'),
    sticker_set_name: str = Query(..., description='Name of the sticker set to be set as the group sticker set'),
) -> JSONableResponse:
    """
    Use this method to set a new group sticker set for a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

    https://core.telegram.org/bots/api#setchatstickerset
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_chat_sticker_set(
        entity=entity,
        sticker_set_name=sticker_set_name,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/deleteChatStickerSet', methods=['GET', 'POST'], tags=['official'])
async def delete_chat_sticker_set(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target supergroup (in the format @supergroupusername)'),
) -> JSONableResponse:
    """
    Use this method to delete a group sticker set from a supergroup. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Use the field can_set_sticker_set optionally returned in getChat requests to check if the bot can use this method. Returns True on success.

    https://core.telegram.org/bots/api#deletechatstickerset
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.delete_chat_sticker_set(
        entity=entity,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/answerCallbackQuery', methods=['GET', 'POST'], tags=['official'])
async def answer_callback_query(
    token: str = TOKEN_VALIDATION,
    callback_query_id: str = Query(..., description='Unique identifier for the query to be answered'),
    text: Optional[str] = Query(None, description='Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters'),
    show_alert: Optional[bool] = Query(None, description='If True, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to false.'),
    url: Optional[str] = Query(None, description="URL that will be opened by the user's client. If you have created a Game and accepted the conditions via @Botfather, specify the URL that opens your game — note that this will only work if the query comes from a callback_game button.Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter."),
    cache_time: Optional[int] = Query(None, description='The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.'),
) -> JSONableResponse:
    """
    Use this method to send answers to callback queries sent from inline keyboards. The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

    Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via @Botfather and accept the terms. Otherwise, you may use links like t.me/your_bot?start=XXXX that open your bot with a parameter.


    https://core.telegram.org/bots/api#answercallbackquery
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.answer_callback_query(
        callback_query_id=callback_query_id,
        text=text,
        show_alert=show_alert,
        url=url,
        cache_time=cache_time,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setMyCommands', methods=['GET', 'POST'], tags=['official'])
async def set_my_commands(
    token: str = TOKEN_VALIDATION,
    commands: Json[List['BotCommandModel']] = Query(..., description="A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified."),
    scope: Optional[Json['BotCommandScopeModel']] = Query(None, description='A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.'),
    language_code: Optional[str] = Query(None, description='A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands'),
) -> JSONableResponse:
    """
    Use this method to change the list of the bot's commands. See https://core.telegram.org/bots#commands for more details about bot commands. Returns True on success.

    https://core.telegram.org/bots/api#setmycommands
    """
    commands: List[BotCommandModel] = parse_obj_as(
        List[BotCommandModel],
        obj=commands,
    )
    scope: Optional[BotCommandScopeModel] = parse_obj_as(
        Optional[BotCommandScopeModel],
        obj=scope,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.set_my_commands(
        commands=commands,
        scope=scope,
        language_code=language_code,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/deleteMyCommands', methods=['GET', 'POST'], tags=['official'])
async def delete_my_commands(
    token: str = TOKEN_VALIDATION,
    scope: Optional[Json['BotCommandScopeModel']] = Query(None, description='A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to BotCommandScopeDefault.'),
    language_code: Optional[str] = Query(None, description='A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands'),
) -> JSONableResponse:
    """
    Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, higher level commands will be shown to affected users. Returns True on success.

    https://core.telegram.org/bots/api#deletemycommands
    """
    scope: Optional[BotCommandScopeModel] = parse_obj_as(
        Optional[BotCommandScopeModel],
        obj=scope,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.delete_my_commands(
        scope=scope,
        language_code=language_code,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getMyCommands', methods=['GET', 'POST'], tags=['official'])
async def get_my_commands(
    token: str = TOKEN_VALIDATION,
    scope: Optional[Json['BotCommandScopeModel']] = Query(None, description='A JSON-serialized object, describing scope of users. Defaults to BotCommandScopeDefault.'),
    language_code: Optional[str] = Query(None, description='A two-letter ISO 639-1 language code or an empty string'),
) -> JSONableResponse:
    """
    Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of BotCommand on success. If commands aren't set, an empty list is returned.

    https://core.telegram.org/bots/api#getmycommands
    """
    scope: Optional[BotCommandScopeModel] = parse_obj_as(
        Optional[BotCommandScopeModel],
        obj=scope,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_my_commands(
        scope=scope,
        language_code=language_code,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/editMessageText', methods=['GET', 'POST'], tags=['official'])
async def edit_message_text(
    token: str = TOKEN_VALIDATION,
    text: str = Query(..., description='New text of the message, 1-4096 characters after entities parsing'),
    chat_id: Optional[Union[int, str]] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the message to edit'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the message text. See formatting options for more details.'),
    entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode'),
    disable_web_page_preview: Optional[bool] = Query(None, description='Disables link previews for links in this message'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for an inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to edit text and game messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    https://core.telegram.org/bots/api#editmessagetext
    """
    entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=entities,
    )
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.edit_message_text(
        text=text,
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
        parse_mode=parse_mode,
        entities=entities,
        disable_web_page_preview=disable_web_page_preview,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/editMessageCaption', methods=['GET', 'POST'], tags=['official'])
async def edit_message_caption(
    token: str = TOKEN_VALIDATION,
    chat_id: Optional[Union[int, str]] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the message to edit'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
    caption: Optional[str] = Query(None, description='New caption of the message, 0-1024 characters after entities parsing'),
    parse_mode: Optional[str] = Query(None, description='Mode for parsing entities in the message caption. See formatting options for more details.'),
    caption_entities: Optional[Json[List['MessageEntityModel']]] = Query(None, description='A JSON-serialized list of special entities that appear in the caption, which can be specified instead of parse_mode'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for an inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    https://core.telegram.org/bots/api#editmessagecaption
    """
    caption_entities: Optional[List[MessageEntityModel]] = parse_obj_as(
        Optional[List[MessageEntityModel]],
        obj=caption_entities,
    )
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.edit_message_caption(
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
        caption=caption,
        parse_mode=parse_mode,
        caption_entities=caption_entities,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/editMessageMedia', methods=['GET', 'POST'], tags=['official'])
async def edit_message_media(
    token: str = TOKEN_VALIDATION,
    media: Json['InputMediaModel'] = Query(..., description='A JSON-serialized object for a new media content of the message'),
    chat_id: Optional[Union[int, str]] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the message to edit'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for a new inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to edit animation, audio, document, photo, or video messages. If a message is part of a message album, then it can be edited only to an audio for audio albums, only to a document for document albums and to a photo or a video otherwise. When an inline message is edited, a new file can't be uploaded; use a previously uploaded file via its file_id or specify a URL. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    https://core.telegram.org/bots/api#editmessagemedia
    """
    media: InputMediaModel = parse_obj_as(
        InputMediaModel,
        obj=media,
    )
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.edit_message_media(
        media=media,
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/editMessageReplyMarkup', methods=['GET', 'POST'], tags=['official'])
async def edit_message_reply_markup(
    token: str = TOKEN_VALIDATION,
    chat_id: Optional[Union[int, str]] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the message to edit'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for an inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to edit only the reply markup of messages. On success, if the edited message is not an inline message, the edited Message is returned, otherwise True is returned.

    https://core.telegram.org/bots/api#editmessagereplymarkup
    """
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.edit_message_reply_markup(
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/stopPoll', methods=['GET', 'POST'], tags=['official'])
async def stop_poll(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: int = Query(..., description='Identifier of the original message with the poll'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description='A JSON-serialized object for a new message inline keyboard.'),
) -> JSONableResponse:
    """
    Use this method to stop a poll which was sent by the bot. On success, the stopped Poll is returned.

    https://core.telegram.org/bots/api#stoppoll
    """
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.stop_poll(
        entity=entity,
        message_id=message_id,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/deleteMessage', methods=['GET', 'POST'], tags=['official'])
async def delete_message(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    message_id: int = Query(..., description='Identifier of the message to delete'),
) -> JSONableResponse:
    """
    Use this method to delete a message, including service messages, with the following limitations:- A message can only be deleted if it was sent less than 48 hours ago.- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.- Bots can delete outgoing messages in private chats, groups, and supergroups.- Bots can delete incoming messages in private chats.- Bots granted can_post_messages permissions can delete outgoing messages in channels.- If the bot is an administrator of a group, it can delete any message there.- If the bot has can_delete_messages permission in a supergroup or a channel, it can delete any message there.Returns True on success.

    https://core.telegram.org/bots/api#deletemessage
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.delete_message(
        entity=entity,
        message_id=message_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendSticker', methods=['GET', 'POST'], tags=['official'])
async def send_sticker(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    sticker: Json[Union['InputFileModel', str]] = Query(..., description='Sticker to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a .WEBP file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json[Union['InlineKeyboardMarkupModel', 'ReplyKeyboardMarkupModel', 'ReplyKeyboardRemoveModel', 'ForceReplyModel']]] = Query(None, description='Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'),
) -> JSONableResponse:
    """
    Use this method to send static .WEBP, animated .TGS, or video .WEBM stickers. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendsticker
    """
    sticker: Union[InputFileModel, str] = parse_obj_as(
        Union[InputFileModel, str],
        obj=sticker,
    )
    reply_markup: Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]] = parse_obj_as(
        Optional[Union[InlineKeyboardMarkupModel, ReplyKeyboardMarkupModel, ReplyKeyboardRemoveModel, ForceReplyModel]],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_sticker(
        entity=entity,
        sticker=sticker,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getStickerSet', methods=['GET', 'POST'], tags=['official'])
async def get_sticker_set(
    token: str = TOKEN_VALIDATION,
    name: str = Query(..., description='Name of the sticker set'),
) -> JSONableResponse:
    """
    Use this method to get a sticker set. On success, a StickerSet object is returned.

    https://core.telegram.org/bots/api#getstickerset
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.get_sticker_set(
        name=name,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/uploadStickerFile', methods=['GET', 'POST'], tags=['official'])
async def upload_sticker_file(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='User identifier of sticker file owner'),
    png_sticker: Json['InputFileModel'] = Query(..., description='PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. More info on Sending Files »'),
) -> JSONableResponse:
    """
    Use this method to upload a .PNG file with a sticker for later use in createNewStickerSet and addStickerToSet methods (can be used multiple times). Returns the uploaded File on success.

    https://core.telegram.org/bots/api#uploadstickerfile
    """
    png_sticker: InputFileModel = parse_obj_as(
        InputFileModel,
        obj=png_sticker,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.upload_sticker_file(
        user_id=user_id,
        png_sticker=png_sticker,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/createNewStickerSet', methods=['GET', 'POST'], tags=['official'])
async def create_new_sticker_set(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='User identifier of created sticker set owner'),
    name: str = Query(..., description='Short name of sticker set, to be used in t.me/addstickers/ URLs (e.g., animals). Can contain only english letters, digits and underscores. Must begin with a letter, can\'t contain consecutive underscores and must end in "_by_<bot username>". <bot_username> is case insensitive. 1-64 characters.'),
    title: str = Query(..., description='Sticker set title, 1-64 characters'),
    emojis: str = Query(..., description='One or more emoji corresponding to the sticker'),
    png_sticker: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'),
    tgs_sticker: Optional[Json['InputFileModel']] = Query(None, description='TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#animated-sticker-requirements for technical requirements'),
    webm_sticker: Optional[Json['InputFileModel']] = Query(None, description='WEBM video with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#video-sticker-requirements for technical requirements'),
    contains_masks: Optional[bool] = Query(None, description='Pass True, if a set of mask stickers should be created'),
    mask_position: Optional[Json['MaskPositionModel']] = Query(None, description='A JSON-serialized object for position where the mask should be placed on faces'),
) -> JSONableResponse:
    """
    Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Returns True on success.

    https://core.telegram.org/bots/api#createnewstickerset
    """
    png_sticker: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=png_sticker,
    )
    tgs_sticker: Optional[InputFileModel] = parse_obj_as(
        Optional[InputFileModel],
        obj=tgs_sticker,
    )
    webm_sticker: Optional[InputFileModel] = parse_obj_as(
        Optional[InputFileModel],
        obj=webm_sticker,
    )
    mask_position: Optional[MaskPositionModel] = parse_obj_as(
        Optional[MaskPositionModel],
        obj=mask_position,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.create_new_sticker_set(
        user_id=user_id,
        name=name,
        title=title,
        emojis=emojis,
        png_sticker=png_sticker,
        tgs_sticker=tgs_sticker,
        webm_sticker=webm_sticker,
        contains_masks=contains_masks,
        mask_position=mask_position,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/addStickerToSet', methods=['GET', 'POST'], tags=['official'])
async def add_sticker_to_set(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='User identifier of sticker set owner'),
    name: str = Query(..., description='Sticker set name'),
    emojis: str = Query(..., description='One or more emoji corresponding to the sticker'),
    png_sticker: Optional[Json[Union['InputFileModel', str]]] = Query(None, description='PNG image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files »'),
    tgs_sticker: Optional[Json['InputFileModel']] = Query(None, description='TGS animation with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#animated-sticker-requirements for technical requirements'),
    webm_sticker: Optional[Json['InputFileModel']] = Query(None, description='WEBM video with the sticker, uploaded using multipart/form-data. See https://core.telegram.org/stickers#video-sticker-requirements for technical requirements'),
    mask_position: Optional[Json['MaskPositionModel']] = Query(None, description='A JSON-serialized object for position where the mask should be placed on faces'),
) -> JSONableResponse:
    """
    Use this method to add a new sticker to a set created by the bot. You must use exactly one of the fields png_sticker, tgs_sticker, or webm_sticker. Animated stickers can be added to animated sticker sets and only to them. Animated sticker sets can have up to 50 stickers. Static sticker sets can have up to 120 stickers. Returns True on success.

    https://core.telegram.org/bots/api#addstickertoset
    """
    png_sticker: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=png_sticker,
    )
    tgs_sticker: Optional[InputFileModel] = parse_obj_as(
        Optional[InputFileModel],
        obj=tgs_sticker,
    )
    webm_sticker: Optional[InputFileModel] = parse_obj_as(
        Optional[InputFileModel],
        obj=webm_sticker,
    )
    mask_position: Optional[MaskPositionModel] = parse_obj_as(
        Optional[MaskPositionModel],
        obj=mask_position,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.add_sticker_to_set(
        user_id=user_id,
        name=name,
        emojis=emojis,
        png_sticker=png_sticker,
        tgs_sticker=tgs_sticker,
        webm_sticker=webm_sticker,
        mask_position=mask_position,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setStickerPositionInSet', methods=['GET', 'POST'], tags=['official'])
async def set_sticker_position_in_set(
    token: str = TOKEN_VALIDATION,
    sticker: str = Query(..., description='File identifier of the sticker'),
    position: int = Query(..., description='New sticker position in the set, zero-based'),
) -> JSONableResponse:
    """
    Use this method to move a sticker in a set created by the bot to a specific position. Returns True on success.

    https://core.telegram.org/bots/api#setstickerpositioninset
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.set_sticker_position_in_set(
        sticker=sticker,
        position=position,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/deleteStickerFromSet', methods=['GET', 'POST'], tags=['official'])
async def delete_sticker_from_set(
    token: str = TOKEN_VALIDATION,
    sticker: str = Query(..., description='File identifier of the sticker'),
) -> JSONableResponse:
    """
    Use this method to delete a sticker from a set created by the bot. Returns True on success.

    https://core.telegram.org/bots/api#deletestickerfromset
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.delete_sticker_from_set(
        sticker=sticker,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setStickerSetThumb', methods=['GET', 'POST'], tags=['official'])
async def set_sticker_set_thumb(
    token: str = TOKEN_VALIDATION,
    name: str = Query(..., description='Sticker set name'),
    user_id: int = Query(..., description='User identifier of the sticker set owner'),
    thumb: Optional[Json[Union['InputFileModel', str]]] = Query(None, description="A PNG image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a TGS animation with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#animated-sticker-requirements for animated sticker technical requirements, or a WEBM video with the thumbnail up to 32 kilobytes in size; see https://core.telegram.org/stickers#video-sticker-requirements for video sticker technical requirements. Pass a file_id as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. More info on Sending Files ». Animated sticker set thumbnails can't be uploaded via HTTP URL."),
) -> JSONableResponse:
    """
    Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns True on success.

    https://core.telegram.org/bots/api#setstickersetthumb
    """
    thumb: Optional[Union[InputFileModel, str]] = parse_obj_as(
        Optional[Union[InputFileModel, str]],
        obj=thumb,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.set_sticker_set_thumb(
        name=name,
        user_id=user_id,
        thumb=thumb,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/answerInlineQuery', methods=['GET', 'POST'], tags=['official'])
async def answer_inline_query(
    token: str = TOKEN_VALIDATION,
    inline_query_id: str = Query(..., description='Unique identifier for the answered query'),
    results: Json[List['InlineQueryResultModel']] = Query(..., description='A JSON-serialized array of results for the inline query'),
    cache_time: Optional[int] = Query(None, description='The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.'),
    is_personal: Optional[bool] = Query(None, description='Pass True, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query'),
    next_offset: Optional[str] = Query(None, description="Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes."),
    switch_pm_text: Optional[str] = Query(None, description='If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter switch_pm_parameter'),
    switch_pm_parameter: Optional[str] = Query(None, description="Deep-linking parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only A-Z, a-z, 0-9, _ and - are allowed.Example: An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a switch_inline button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities."),
) -> JSONableResponse:
    """
    Use this method to send answers to an inline query. On success, True is returned.No more than 50 results per query are allowed.

    https://core.telegram.org/bots/api#answerinlinequery
    """
    results: List[InlineQueryResultModel] = parse_obj_as(
        List[InlineQueryResultModel],
        obj=results,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.answer_inline_query(
        inline_query_id=inline_query_id,
        results=results,
        cache_time=cache_time,
        is_personal=is_personal,
        next_offset=next_offset,
        switch_pm_text=switch_pm_text,
        switch_pm_parameter=switch_pm_parameter,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendInvoice', methods=['GET', 'POST'], tags=['official'])
async def send_invoice(
    token: str = TOKEN_VALIDATION,
    chat_id: Union[int, str] = Query(..., description='Unique identifier for the target chat or username of the target channel (in the format @channelusername)'),
    title: str = Query(..., description='Product name, 1-32 characters'),
    description: str = Query(..., description='Product description, 1-255 characters'),
    payload: str = Query(..., description='Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.'),
    provider_token: str = Query(..., description='Payments provider token, obtained via Botfather'),
    currency: str = Query(..., description='Three-letter ISO 4217 currency code, see more on currencies'),
    prices: Json[List['LabeledPriceModel']] = Query(..., description='Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)'),
    max_tip_amount: Optional[int] = Query(None, description='The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0'),
    suggested_tip_amounts: Optional[List[int]] = Query(None, description='A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount.'),
    start_parameter: Optional[str] = Query(None, description='Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter'),
    provider_data: Optional[str] = Query(None, description='A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.'),
    photo_url: Optional[str] = Query(None, description='URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.'),
    photo_size: Optional[int] = Query(None, description='Photo size'),
    photo_width: Optional[int] = Query(None, description='Photo width'),
    photo_height: Optional[int] = Query(None, description='Photo height'),
    need_name: Optional[bool] = Query(None, description="Pass True, if you require the user's full name to complete the order"),
    need_phone_number: Optional[bool] = Query(None, description="Pass True, if you require the user's phone number to complete the order"),
    need_email: Optional[bool] = Query(None, description="Pass True, if you require the user's email address to complete the order"),
    need_shipping_address: Optional[bool] = Query(None, description="Pass True, if you require the user's shipping address to complete the order"),
    send_phone_number_to_provider: Optional[bool] = Query(None, description="Pass True, if user's phone number should be sent to provider"),
    send_email_to_provider: Optional[bool] = Query(None, description="Pass True, if user's email address should be sent to provider"),
    is_flexible: Optional[bool] = Query(None, description='Pass True, if the final price depends on the shipping method'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description="A JSON-serialized object for an inline keyboard. If empty, one 'Pay total price' button will be shown. If not empty, the first button must be a Pay button."),
) -> JSONableResponse:
    """
    Use this method to send invoices. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendinvoice
    """
    prices: List[LabeledPriceModel] = parse_obj_as(
        List[LabeledPriceModel],
        obj=prices,
    )
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_invoice(
        entity=entity,
        title=title,
        description=description,
        payload=payload,
        provider_token=provider_token,
        currency=currency,
        prices=prices,
        max_tip_amount=max_tip_amount,
        suggested_tip_amounts=suggested_tip_amounts,
        start_parameter=start_parameter,
        provider_data=provider_data,
        photo_url=photo_url,
        photo_size=photo_size,
        photo_width=photo_width,
        photo_height=photo_height,
        need_name=need_name,
        need_phone_number=need_phone_number,
        need_email=need_email,
        need_shipping_address=need_shipping_address,
        send_phone_number_to_provider=send_phone_number_to_provider,
        send_email_to_provider=send_email_to_provider,
        is_flexible=is_flexible,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/answerShippingQuery', methods=['GET', 'POST'], tags=['official'])
async def answer_shipping_query(
    token: str = TOKEN_VALIDATION,
    shipping_query_id: str = Query(..., description='Unique identifier for the query to be answered'),
    ok: bool = Query(..., description='Specify True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)'),
    shipping_options: Optional[Json[List['ShippingOptionModel']]] = Query(None, description='Required if ok is True. A JSON-serialized array of available shipping options.'),
    error_message: Optional[str] = Query(None, description='Required if ok is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable\'). Telegram will display this message to the user.'),
) -> JSONableResponse:
    """
    If you sent an invoice requesting a shipping address and the parameter is_flexible was specified, the Bot API will send an Update with a shipping_query field to the bot. Use this method to reply to shipping queries. On success, True is returned.

    https://core.telegram.org/bots/api#answershippingquery
    """
    shipping_options: Optional[List[ShippingOptionModel]] = parse_obj_as(
        Optional[List[ShippingOptionModel]],
        obj=shipping_options,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.answer_shipping_query(
        shipping_query_id=shipping_query_id,
        ok=ok,
        shipping_options=shipping_options,
        error_message=error_message,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/answerPreCheckoutQuery', methods=['GET', 'POST'], tags=['official'])
async def answer_pre_checkout_query(
    token: str = TOKEN_VALIDATION,
    pre_checkout_query_id: str = Query(..., description='Unique identifier for the query to be answered'),
    ok: bool = Query(..., description='Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.'),
    error_message: Optional[str] = Query(None, description='Required if ok is False. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.'),
) -> JSONableResponse:
    """
    Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an Update with the field pre_checkout_query. Use this method to respond to such pre-checkout queries. On success, True is returned. Note: The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.

    https://core.telegram.org/bots/api#answerprecheckoutquery
    """

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre_checkout_query_id,
        ok=ok,
        error_message=error_message,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setPassportDataErrors', methods=['GET', 'POST'], tags=['official'])
async def set_passport_data_errors(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='User identifier'),
    errors: Json[List['PassportElementErrorModel']] = Query(..., description='A JSON-serialized array describing the errors'),
) -> JSONableResponse:
    """
    Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns True on success.
    Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.

    https://core.telegram.org/bots/api#setpassportdataerrors
    """
    errors: List[PassportElementErrorModel] = parse_obj_as(
        List[PassportElementErrorModel],
        obj=errors,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)



    result = await bot.set_passport_data_errors(
        user_id=user_id,
        errors=errors,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/sendGame', methods=['GET', 'POST'], tags=['official'])
async def send_game(
    token: str = TOKEN_VALIDATION,
    chat_id: int = Query(..., description='Unique identifier for the target chat'),
    game_short_name: str = Query(..., description='Short name of the game, serves as the unique identifier for the game. Set up your games via Botfather.'),
    disable_notification: Optional[bool] = Query(None, description='Sends the message silently. Users will receive a notification with no sound.'),
    protect_content: Optional[bool] = Query(None, description='Protects the contents of the sent message from forwarding and saving'),
    reply_to_message_id: Optional[int] = Query(None, description='If the message is a reply, ID of the original message'),
    allow_sending_without_reply: Optional[bool] = Query(None, description='Pass True, if the message should be sent even if the specified replied-to message is not found'),
    reply_markup: Optional[Json['InlineKeyboardMarkupModel']] = Query(None, description="A JSON-serialized object for an inline keyboard. If empty, one 'Play game_title' button will be shown. If not empty, the first button must launch the game."),
) -> JSONableResponse:
    """
    Use this method to send a game. On success, the sent Message is returned.

    https://core.telegram.org/bots/api#sendgame
    """
    reply_markup: Optional[InlineKeyboardMarkupModel] = parse_obj_as(
        Optional[InlineKeyboardMarkupModel],
        obj=reply_markup,
    )

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.send_game(
        entity=entity,
        game_short_name=game_short_name,
        disable_notification=disable_notification,
        protect_content=protect_content,
        reply_to_message_id=reply_to_message_id,
        allow_sending_without_reply=allow_sending_without_reply,
        reply_markup=reply_markup,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/setGameScore', methods=['GET', 'POST'], tags=['official'])
async def set_game_score(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='User identifier'),
    score: int = Query(..., description='New score, must be non-negative'),
    force: Optional[bool] = Query(None, description='Pass True, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters'),
    disable_edit_message: Optional[bool] = Query(None, description='Pass True, if the game message should not be automatically edited to include the current scoreboard'),
    chat_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the sent message'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
) -> JSONableResponse:
    """
    Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the Message is returned, otherwise True is returned. Returns an error, if the new score is not greater than the user's current score in the chat and force is False.

    https://core.telegram.org/bots/api#setgamescore
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.set_game_score(
        user_id=user_id,
        score=score,
        force=force,
        disable_edit_message=disable_edit_message,
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def


@routes.api_route('/{token}/getGameHighScores', methods=['GET', 'POST'], tags=['official'])
async def get_game_high_scores(
    token: str = TOKEN_VALIDATION,
    user_id: int = Query(..., description='Target user id'),
    chat_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Unique identifier for the target chat'),
    message_id: Optional[int] = Query(None, description='Required if inline_message_id is not specified. Identifier of the sent message'),
    inline_message_id: Optional[str] = Query(None, description='Required if chat_id and message_id are not specified. Identifier of the inline message'),
) -> JSONableResponse:
    """
    Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an Array of GameHighScore objects.

    This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.


    https://core.telegram.org/bots/api#getgamehighscores
    """

    from .....main import _get_bot
    bot = await _get_bot(token)

    try:
        entity = await get_entity(bot, chat_id)
    except BotMethodInvalidError:
        assert isinstance(chat_id, int) or (isinstance(chat_id, str) and len(chat_id) > 0 and chat_id[0] == '@')
        entity = chat_id
    except ValueError:
        raise HTTPException(404, detail="chat not found?")
    # end try

    result = await bot.get_game_high_scores(
        user_id=user_id,
        entity=entity,
        message_id=message_id,
        inline_message_id=inline_message_id,
    )
    data = await to_web_api(result, bot)
    return r_success(data.to_array())
# end def

