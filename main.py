from fsm import Rekrutmen

bot=Rekrutmen()
while True:
    user=input("you:")
    bot.proses(user)
    print("Bot:",bot.respon)