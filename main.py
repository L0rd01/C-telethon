from telethon import TelegramClient, events

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage())
async def handler(event):
    # сохраняем сообщение в файл
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f'{event.message}\n')

await client.start()
await client.run_until_disconnected()
