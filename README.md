# gfunction-telegram-bot

1. Code to deploy the function telegram_bot from main.py to production with variables needed:

```gcloud functions deploy telegram_bot --set-env-vars "TELEGRAM_TOKEN=<YOUR_TELEGRAM_TOKEN>,CLIENT_ID=<YOUR_CLIENT_ID>,CLIENT_SECRET=<YOUR_CLIENT_SECRET>,REFRESH_TOKEN=<YOUR_REFRESH_TOKEN>" --runtime python38 --trigger-http --project=<YOUR_PROJECT_ID>```

With the log you can find the URL to the next code.

2. Code to set the api:

```curl "https://api.telegram.org/bot<TELEGRAM_TOKEN>/setWebhook?url=<URL>"```
