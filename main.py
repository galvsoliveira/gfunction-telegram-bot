import os
import telegram
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def telegram_bot(request):
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        message_text = update.message.text
        
        if not message_text.startswith('/add'):
            bot.sendMessage(chat_id=chat_id, text='Comando inválido. Tente novamente.')
            return 'okay'
            
        if ' ' not in message_text or len(message_text.split(' ')) != 4:
            bot.sendMessage(chat_id=chat_id, text='Adicione todos os valores, por favor. Exemplo: /add 01/01/2023 1000,00 Categoria.')
            return 'okay'
            
        startcommand, date, value, description = message_text.split(' ')

        description = description[0].upper() + description[1:]
        value = float(value.replace(',', '.'))
        date = f'=DATEVALUE("{date}")'
        
        creds = Credentials.from_authorized_user_info(info={
            'client_id': os.environ["CLIENT_ID"],
            'client_secret': os.environ["CLIENT_SECRET"],
            'refresh_token': os.environ["REFRESH_TOKEN"],
        })

        service = build('sheets', 'v4', credentials=creds)

        spreadsheet_id = '1rVk5js9CPKOz0KygTJMQUV5-HbFcFu5IXPYqEND95Jk'
        mes = 'Março'
        range_ = f'{mes}!I1:J1'
        values = [[date, value, description]]

        body = {
            'values': values
        }

        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS',
            body=body).execute()

        bot.sendMessage(chat_id=chat_id, text=f'{result.get("updates").get("updatedCells")} células adicionadas.')
    return 'okay'