# Django Telegram Bot with Channels

This project is a simple Telegram bot implemented using Django and Channels library. It allows users to interact with the bot through Telegram and displays the chat history and chat counts on the home page.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/diptampaul/Impress-Telegram-Chat-Bot
   ```

2. Change to the project directory:

   ```bash
   cd impressai
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - On Linux or macOS:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the main folder with the following content:

   ```plaintext
   SECRET_KEY=django-insecure-4@&qd#r#r4-#am!o!@3*-a(gic7!4hyh$5m26u$xybs&^64laz
   CHATBOT_NAME=ImpressAI
   CHATBOT_USERNAME=impress_aibot
   CHATBOT_LINK=t.me/impress_aibot
   CHATBOT_TOEKN=YOUR_TELEGRAM_TOKEN
   OPENAI_KEY=YOUR_OPENAI_API_KEY
   ```

   Replace `YOUR_TELEGRAM_TOKEN` with your Telegram bot token and `YOUR_OPENAI_API_KEY` with your OpenAI API key. Make sure to keep these values secure and private.

## Usage

To start the Django development server, run the following command:

```bash
python manage.py runserver
```

The Telegram bot is now running and listening for incoming messages. You can access the home page at `http://localhost:8000/` to view the chat history and chat counts.

**Note:** Make sure to replace the placeholder values in the `.env` file with your actual tokens and keys. The `.env` file should not be committed to version control to keep sensitive information secure.