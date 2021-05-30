import pywhatkit
import requests
import json
import time
import datetime
import schedule

print("Bot is starting...")

def job():
    url = f'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr'
    res = requests.get(url)
    print(res)
    data = json.loads(res.text)
    output_string = "1 bitcoin will cost you "+str(data["bitcoin"]["inr"])+ " Indian Rupees!!"
    print(output_string)
    now = datetime.datetime.now()
    print("preparing to send message")
    pywhatkit.sendwhatmsg("+917760788835",output_string,now.hour,now.minute+2)

job()
#schedule.every(1).minutes.do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
