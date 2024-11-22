
# Raccoon Telegram Bot  

Raccoon is a modular Telegram bot designed for easy deployment and customization. This bot allows you to add or remove modules seamlessly and can be run effortlessly using GitHub Actions.  

---

## Features  
- **Modular Structure**: Easily add or remove modules.  
- **GitHub Actions Friendly**: Designed for deployment on GitHub Actions.  
- **Argument-Based Configuration**: Takes the Telegram bot token and chat ID as arguments for flexible setup.  
- **Pre-built Modules**:  
  - **YouTube Module**: Sends notifications when a new video is uploaded.  
  - **Medium Module**: Sends notifications when a new post is published.  

---

## Prerequisites  
1. Python 3.8 or higher.  
2. Required modules in the `module` directory must include a `run` function.  
3. A Telegram bot token and chat ID.  

---

## How to Use  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/Raccoon.git  
   cd Raccoon  
   ```  

2. Install required dependencies:  
   Uncomment the `REQUIREMENTS` section in the script and list your dependencies.  

3. Add or modify modules:  
   - Add new modules in the `module` directory.  
   - Ensure the module has a `run(token, chat_id)` function.  

4. Run the bot:  
   ```bash  
   python bot.py --telegram_token <your-telegram-bot-token> --chat_id <your-chat-id>  
   ```  


## Contribution  
Feel free to fork this repository and add your own modules. Pull requests are welcome!  

