# whatsapp-messages

Simple Django app that can receive and handle WhatsApp messages.


## Setup
NB: Please ensure you have Python3.6+ installed on your local dev machine.

Clone repo locally and change directory into it:
```bash
git clone https://github.com/nickmwangemi/whatsapp-messages.git
cd whatsapp-messages
```

Setup virtual environment and activate.
```bash
virtualenv env
source env/bin/activate
```

Install project dependencies.
```bash
pip install -r requirements.txt
```

Run migrations and start server
```bash
python manage.py migrate
python manage.py runserver
```

Open a second terminal window, and on it,
- activate the virtual environment and then run the following command:
```bash
ngrok http 8000
```
This will expose your local development server to the internet as required for you to send messages to your WhatsApp contact.


