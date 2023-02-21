from pyrogram import Client, filters
import random

api_id = id
api_hash = "hash"
app=Client("my_account", api_id=api_id, api_hash=api_hash)

list=["Круто!", "Превосходно!","Восхитительно!","Хайпово","Супер!","Прелестно!", "Юрец - молодец!", "Спасибо Юрцу за работу!"]

@app.on_message(filters.text)
async def echo(client, message):
    if "Товар снова в наличии" in message.text:
        await message.reply(('Ого! ' + list[random.randint(0, 7)]))
    elif "Появился новый товар" in message.text:
        await message.reply(('Ого! ' + list[random.randint(0, 7)]))
    elif "Цена на товар снижена" in message.text:
        await message.reply(('Ого! ' + list[random.randint(0, 7)]))


app.run()
