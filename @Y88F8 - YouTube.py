##################### Codded By #####################
##################### ~ Zaid ~ Telegram : @ZDDDU
##################### ~ Source Channel : t.me/Y88F8
##################### © All rights reserved 
##################### 3 Sep 2022 
OWNER = 1918207232 # Owner id ~
TOKEN = "5527189118:AAFEl4YabJD1KADYLwufLnW1A6y0KHj1MIU" # bot token here 
bot = int(TOKEN.split(":")[0])
DT = 7205 # Duration Limit 
############ MODULES
import time
import asyncio
import requests
import os
import wget
import re
import random
import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Message,
)
from typing import Dict, List, Union
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from youtube_search import YoutubeSearch as Y88F8
from yt_dlp import YoutubeDL
############ Client
coddedbyzaid = Client(
   "YouTube Service",
   api_id = 12488427,
   api_hash = "cef695e1719a0f7833574f44c7715482",
   bot_token = TOKEN
)

def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":")))
    )
##################### Codded By #####################
##################### ~ Zaid ~ Telegram : @ZDDDU
##################### ~ Source Channel : t.me/Y88F8
##################### © All rights reserved 
##################### -Start : 3 Sep 2022 
##################### -End : 5 Sep 2022   

##################### DATABASE 
# pip install pymongo[srv]
# pip install motor
from motor.motor_asyncio import AsyncIOMotorClient as mongoclient
MONGO = "mongodb+srv://zaid2:zaid2@cluster0.cvvxkzq.mongodb.net/?retryWrites=true&w=majority" # MONGO URL
mongox = mongoclient(MONGO)
mongodb = mongox.YoutubeBrah
##################### Codded By #####################
##################### ~ Zaid ~ Telegram : @ZDDDU
##################### ~ Source Channel : t.me/Y88F8
##################### © All rights reserved 
##################### -Start : 3 Sep 2022 
##################### -End : 5 Sep 2022   


##################### ENABLE & DISABLE Database 
ytdb = mongodb.youtube

async def is_off(chat: int) -> bool:
    disable = await ytdb.find_one({"chat": chat})
    if not disable:
        return False
    return True

async def add_off(chat: int):
    x = await is_off(chat)
    if x:
        return
    return await ytdb.insert_one({"chat": chat})  
    
async def remove_off(chat: int):
    x = await is_off(chat)
    if not x:
        return
    return await ytdb.delete_one({"chat": chat})  

##################### Codded By #####################
##################### ~ Zaid ~ Telegram : @ZDDDU
##################### ~ Source Channel : t.me/Y88F8
##################### © All rights reserved 
##################### -Start : 3 Sep 2022 
##################### -End : 5 Sep 2022   

##################### ENABLE & DISABLE Commands
DISABLE = filters.regex("^تعطيل اليوتيوب$") & filters.group
@coddedbyzaid.on_message(DISABLE)
@coddedbyzaid.on_edited_message(DISABLE)
async def disable_yt(client, message):
     if message.sender_chat:
       return
     user = message.from_user.id
     chat = message.chat.id
     a = message.from_user.mention
     fd_msg = "**-» عزيزي {}\n- تم تعطيل اليوتيوب مسبقًا**"
     done_msg = "**-» بواسطة {}\n- تم تعطيل اليوتيوب**"
     state = (await client.get_chat_member(chat, user)).status
     x = f"{state}"
     if user == OWNER:
       if await is_off(chat):
         return await message.reply(fd_msg.format(a))
       await add_off(chat)
       return await message.reply(done_msg.format(a))
     if not x == "ChatMemberStatus.MEMBER":
       if await is_off(chat):
         return await message.reply(fd_msg.format(a))
       await add_off(chat)
       return await message.reply(done_msg.format(a))
     else:
        return await message.reply("-» هذا الأمر يخص ( الادمن، المدير، المالك، المطور ) فقط .")

ENABLE = filters.regex("^تفعيل اليوتيوب$") & filters.group
@coddedbyzaid.on_message(ENABLE)
@coddedbyzaid.on_edited_message(ENABLE)
async def enable_yt(client, message):
      if message.sender_chat:
        return
      user = message.from_user.id
      chat = message.chat.id
      a = message.from_user.mention
      fd_msg = "**-» عزيزي {}\n- تم تفعيل اليوتيوب مسبقًا**"
      done_msg = "**-» بواسطة {}\n- تم تفعيل اليوتيوب**"
      state = (await client.get_chat_member(chat, user)).status
      x = f"{state}"
      if user == OWNER:
        if not await is_off(chat):
          return await message.reply(fd_msg.format(a))
        await remove_off(chat)
        return await message.reply(done_msg.format(a))
      if not x == "ChatMemberStatus.MEMBER":
        if not await is_off(chat):
          return await message.reply(fd_msg.format(a))
        await remove_off(chat)
        return await message.reply(done_msg.format(a))
      else:
        return await message.reply("-» هذا الأمر يخص ( الادمن، المدير، المالك، المطور ) فقط .")
       
   
SEARCH = filters.command("بحث", ["&", ""]) & filters.group
@coddedbyzaid.on_message(SEARCH)
async def resaults(_, message):
    chat = message.chat.id
    if await is_off(chat):
      return 
    m = message.chat.id
    usr = message.from_user.id
    q = message.text.split(None, 1)[1]
    m = await message.reply("**~ جاري البحث عن : {} **".format(q))
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = Y88F8(q, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:70]
        title1 = results[1]["title"][:70]
        title2 = results[2]["title"][:70]
        title3 = results[3]["title"][:70]
        title4 = results[4]["title"][:70]
        duration = results[0]["duration"]
        REPLY_MESSAGE = f"**- نتائج بحثك عن : {q}**"
        REPLY_MESSAGE_BUTTONS = [
          [
             (f"» ⬇️ «")
          ],
          [
             (f"- {title}")
          ],
          [
             (f"- {title1}")
          ],
          [
             (f"- {title2}")
          ],
          [
             (f"- {title3}")
          ],
          [
             (f"- {title4}")
          ]
    ]
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True, one_time_keyboard=True)
        await message.reply(
            text=text,
            reply_markup=reply_markup
        )
        await m.delete()

    except Exception as e:
        await m.edit("**~ لم يتم العثور على نتائج ، حدث خطأ اثناء البحث ، او لم تكتب المطلوب بشكل صحيح**")
        print(str(e))
        return

@coddedbyzaid.on_message(filters.command("-", ["&", ""]) & filters.group)
async def mdry(client, message):
    chat = message.chat.id
    if await is_off(chat):
      return 
    if not 'بحثك' in message.reply_to_message.text:
      return
    q = " ".join(message.command[1:])
    r = await message.reply("**~ انتظر جاري جمع البيانات ...**")
    await coddedbyzaid.delete_messages(message.chat.id, message.reply_to_message.id)
    try:
        results = Y88F8(q, max_results=1).to_dict()
        thumbnail = results[0]["thumbnails"][0]
        title = results[0]["title"]
        thumb = requests.get(thumbnail, allow_redirects=True)
        dd = results[0]["duration"]
        views = (results[0]["views"]).replace("views", "")
        preview = wget.download(thumbnail)
    except Exception as e:
        print(e)
    try:
        BTNS = [
          [
             ("» ⬇️ «")
          ],
          [
             ("🎙️ صوت"),
             ("🎞 فيديو️")
          ],
          [
             ("• معلومات الفيديو •")
          ],
          [
             (f"• المشاهدات : {views}"),
             (f"• المدة : {dd}"),
          ]
    ]
        x = ReplyKeyboardMarkup(BTNS, selective=True, resize_keyboard=True, one_time_keyboard=True)
        await r.delete()
        await message.reply_photo(
           preview,
           caption=title,
           reply_markup=x
        )
        await message.delete()
    except:
         pass


@coddedbyzaid.on_message(filters.regex("^🎞 فيديو️$") & filters.group)
async def vdownloader(client, message):
    if await is_off(message.chat.id):
      return
    if not message.reply_to_message:
      return
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    q = message.reply_to_message.caption
    await coddedbyzaid.delete_messages(message.chat.id, message.reply_to_message.id)
    c = ReplyKeyboardRemove(selective=True)
    v = await message.reply("~ جاري تجهيز الفيديو ...", reply_markup=c)
    try:
        results = Y88F8(q, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        dx = results[0]["duration"]
    except Exception as e:
        print(e)
    try:
        await v.delete()
        zaid = int(time_to_seconds(dx))
        if zaid > DT:
          return await message.reply("~ حد التحميل المسموح ساعتين فقط")
        x = await message.reply("**🎞️ جار تحميل الفيديو ...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        await v.delete()
        return await message.reply(f"- **حدث خطأ :** {e}")
    preview = wget.download(thumbnail)
    await x.edit("**🎞️ جار ارسال الفيديو ...**")
    user = message.from_user.first_name
    userid = message.from_user.id
    buttons = [[InlineKeyboardButton(user, user_id=userid)]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
        reply_markup=reply_markup,
    )
    await message.delete()
    try:
        os.remove(file_name)
        await x.delete()
    except Exception as e:
        print(e)    

ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}        
@coddedbyzaid.on_message(filters.command("🎙️ صوت", ["&", ""]) & filters.group)
async def songdownloader(_, message):
    m = message.chat.id
    if await is_off(m):
      return
    if not message.reply_to_message.caption:
      return
    query = message.reply_to_message.caption
    await coddedbyzaid.delete_messages(m, message.reply_to_message.id)
    n = ReplyKeyboardRemove(selective=True)
    dd = [[InlineKeyboardButton("🎶", callback_data='none')]]
    d = InlineKeyboardMarkup(dd)
    uu = [[InlineKeyboardButton("🎙️", callback_data='none')]]
    u = InlineKeyboardMarkup(uu)
    usr = message.from_user.id
    m = await message.reply("**• جار جمع المعلومات **", reply_markup=n)
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = Y88F8(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
    except Exception as e:
        await m.delete()
        await message.reply("**~ حدث خطأ تأكد من المطلوب بشكل صحيح**")
        print(str(e))
        return
    zaid = int(time_to_seconds(duration))
    if zaid > DT:
      return await message.reply("~ حد التحميل المسموح ساعتين فقط")
    await m.delete()
    m2 = await message.reply("**• جار التحميل ..**", reply_markup=d)
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m2.edit("**• جار الإرسال ..**", reply_markup=u)
        a = message.from_user.first_name
        b = message.from_user.id
        buttons = [[InlineKeyboardButton(a, user_id=b)]]
        reply_markup = InlineKeyboardMarkup(buttons)

        await message.reply_audio(
            audio_file,
            reply_markup=reply_markup,
            thumb=thumb_name,
            title=title,
            duration=dur,
            performer="- @Y88F8"
        )
        await m2.delete()
        await message.delete()
    except Exception as e:
        await m2.delete()
        await message.reply(" - حدث خطأ تواصل مع المطور")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)            

one = filters.regex("^• معلومات الفيديو •$") & filters.group
two = filters.regex("• المشاهدات") & filters.group
three = filters.regex("• المدة") & filters.group
@coddedbyzaid.on_message(one)
@coddedbyzaid.on_message(two)
@coddedbyzaid.on_message(three)
def nospam(client, message):
     message.delete()
     
@coddedbyzaid.on_message(filters.regex("^» ⬇️ «$") & filters.group)
def nothing(client, message):
    c = ReplyKeyboardRemove(selective=True)
    x = message.reply("✅", reply_markup=c)
    x.delete()
    message.delete()

coddedbyzaid.run()

##################### Codded By #####################
##################### ~ Zaid ~ Telegram : @ZDDDU
##################### ~ Source Channel : t.me/Y88F8
##################### © All rights reserved 
##################### -Start : 3 Sep 2022 
##################### -End : 5 Sep 2022   
     