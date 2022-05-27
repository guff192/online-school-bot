# online-school-bot

## Run the bot

 1. Export environment variables for your bot token and your public url:
```bash
export API_TOKEN="<YOUR-BOT-API-TOKEN>"
export WEBHOOK_HOST="<YOUR-PUBLIC-URL>"
```
 2. Also change url field in data.json file:
```json
{
  "url": "<YOUR-PUBLIC-URL>/webhook",
  "drop_pending_updates": true
}
```
 3. Create virtualenv and install requirements:
```bash
python3 -m venv env
source ./env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
 ```
 4. Run the bot:
```bash
python bot.py
```
5. Set the webhook (change <YOUR-BOT-API-TOKEN> to your bot token):
```bash
curl -X POST -d @data.json -H "Content-Type: application/json" "https://api.telegram.org/bot<YOUR-BOT-API-TOKEN>/setWebhook
```
