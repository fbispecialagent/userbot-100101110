import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd, sudo_cmd

@borg.on(admin_cmd(pattern="twitter ?(.*)",outgoing=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Riswpondi a un messaggio```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Rispondi a un messaggio testuale```")
       return
    chat = "@TwitterStatusBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Rispondi al messaggio di un utente.```")
       return
    await event.edit("```Making a Quote```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1276223938))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Sblocca @TwitterStatusBot negro```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```disabilita le impostazioni di privacy```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

            
@borg.on(sudo_cmd(pattern="twitter ?(.*)",allow_sudo = True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.reply("```Rispondi a un messaggio.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.reply("```Rispondi a un messaggio testuale```")
       return
    chat = "@TwitterStatusBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.reply("```Rispondi al messaggio di un utente.```")
       return
    cat = await event.reply("```Making a Quote```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1276223938))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```sblocca @TwitterStatusBot negro```")
              return
          if response.text.startswith("Hi!"):
             await event.reply("```Disabilita la privacy```")
          else: 
             await cat.delete()
             await event.client.send_message(event.chat_id, response.message)
            
