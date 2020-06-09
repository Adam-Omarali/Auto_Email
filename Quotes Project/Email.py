import smtplib, ssl
import bs4 as bs
import urllib.request
import random
import datetime as dt
import time

website = urllib.request.urlopen('https://blog.hubspot.com/sales/famous-quotes').read()

soup = bs.BeautifulSoup(website, 'lxml')

for paragraph in soup.find_all('ol'):
        quotes = []
        quotes.append(paragraph.text)
        quotes = " ".join(quotes)
        quotes = quotes.split('\n')

for sentence in enumerate(quotes):
    if len(sentence[1]) < 2:
        quotes.pop(sentence[0])



num = random.randint(1, len(quotes))
daily_quote = quotes[num - 1]



def read_creds():
    user = passw = ""
    with open("credentials.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


port = 465

sender, password = read_creds()


recieve = sender

message = """\
Subject: Your daily motivational quote!!!

Remember to do a reflection on it.\
\n
"""\
          + daily_quote


context = ssl.create_default_context()

print("Starting to send")

scheduled_time = dt.time(18, 22, 0, 0)

while True:
    if dt.datetime.now().time() > scheduled_time > (dt.datetime.now() - dt.timedelta(seconds=59)).time():
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, recieve, message)

        print("sent email!")
        time.sleep(59)