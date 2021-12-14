from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text



bot = Bot(token="9497cbbce145bdb6bd636befd3468aa46cca373e4868a2957ef9f7aa3f79837433c49cb6df6a713afdd08")

dialogs = {}
wait = []


start_keyboard = Keyboard(one_time=False)
start_keyboard.row()
start_keyboard.add(Text(label="Поиск собеседника"), color="negative")

wait_keyboard = Keyboard(one_time=True)
wait_keyboard.row()
wait_keyboard.add(Text(label="Отменить поиск"), color="positive")

stop_keyboard = Keyboard(one_time=False)
stop_keyboard.row()
stop_keyboard.add(Text(label="Отключиться от диалога"), color="primary")


@bot.on.message(text='Поиск собеседника')
async def start(message: Message):
    if message.from_id not in wait and message.from_id not in dialogs:
        if len(wait) == 0:
            await message('Вы добавлены в очередь поиска собеседника.', keyboard=wait_keyboard)
            wait.append(message.from_id)
            await bot.add(message.peer_id, "wait")
        else:
            dialogs[message.from_id] = wait[0]
            dialogs[wait[0]] = message.from_id
            await bot.api.messages.send(peer_id=message.from_id, random_id=0, message='Мы нашли вам собеседника!', keyboard=stop_keyboard)
            await bot.api.messages.send(peer_id=wait[0], random_id=0, message=' Мы нашли вам собеседника!', keyboard=stop_keyboard)
            await bot.add(message.from_id, "dialog")
            await bot.add(wait[0], "dialog")
            del wait[0]

@bot.on.message("Отменить поиск")
async def branch(message: Message):
    if message.text == "Отменить поиск":
        await message("Поиск собеседника остановлен.", keyboard=start_keyboard)
        await bot.exit(message.peer_id)
        del wait[0]
    else:
        await message('Вы находитесь в поиске собеседника.', keyboard=wait_keyboard)

@bot.on.message("dialog")
async def branch(message: Message):
    if message.text == "Отключиться от диалога":
        await bot.api.messages.send(peer_id=message.from_id, random_id=0, message='Диалог был остановлен.', keyboard=start_keyboard)
        await bot.api.messages.send(peer_id=dialogs[message.from_id], random_id=0, message='Собеседник остановил диалог.', keyboard=start_keyboard)
        await bot.exit(dialogs[message.from_id])
        await bot.exit(message.from_id)
        del dialogs[dialogs[message.from_id]]
        del dialogs[message.from_id]
    else:
        await bot.api.messages.send(peer_id=dialogs[message.from_id], random_id=0, message='Собеседник: ' + ans.text)

@bot.on.message()
async def all(message: Message):
    await message('Привет! Я анонимный чат-бот. Чтобы начать поиск собеседника, воспользуйтесь кнопками.', keyboard=start_keyboard)

bot.run_forever()