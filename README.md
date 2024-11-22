
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

---

## Folder Structure  
```  
Raccoon/  
â”‚  
â”œâ”€â”€ bot.py            # Main bot script  
â”œâ”€â”€ module/           # Directory for all modules  
â”‚   â”œâ”€â”€ module_youtube.py  # YouTube module  
â”‚   â”œâ”€â”€ module_medium.py   # Medium module  
â”‚  
```  

---

## Contribution  
Feel free to fork this repository and add your own modules. Pull requests are welcome!  

---

# Ø±Ø¨Ø§Øª ØªÙ„Ú¯Ø±Ø§Ù… Raccoon  

Raccoon ÛŒÚ© Ø±Ø¨Ø§Øª ØªÙ„Ú¯Ø±Ø§Ù… Ù…Ø§Ú˜ÙˆÙ„Ø§Ø± Ø§Ø³Øª Ú©Ù‡ Ø¨Ø±Ø§ÛŒ Ø´Ø®ØµÛŒâ€ŒØ³Ø§Ø²ÛŒ Ùˆ Ø§Ø³ØªÙØ§Ø¯Ù‡ Ø¢Ø³Ø§Ù† Ø·Ø±Ø§Ø­ÛŒ Ø´Ø¯Ù‡ Ø§Ø³Øª. Ø§ÛŒÙ† Ø±Ø¨Ø§Øª Ø¨Ù‡ Ø´Ù…Ø§ Ø§Ø¬Ø§Ø²Ù‡ Ù…ÛŒâ€ŒØ¯Ù‡Ø¯ Ø¨Ù‡ Ø±Ø§Ø­ØªÛŒ Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§ Ø±Ø§ Ø§Ø¶Ø§ÙÙ‡ ÛŒØ§ Ø­Ø°Ù Ú©Ù†ÛŒØ¯ Ùˆ Ø±ÙˆÛŒ GitHub Actions Ø§Ø¬Ø±Ø§ Ú©Ù†ÛŒØ¯.  

---

## ÙˆÛŒÚ˜Ú¯ÛŒâ€ŒÙ‡Ø§  
- **Ø³Ø§Ø®ØªØ§Ø± Ù…Ø§Ú˜ÙˆÙ„Ø§Ø±**: Ø§Ù…Ú©Ø§Ù† Ø§Ø¶Ø§ÙÙ‡ ÛŒØ§ Ø­Ø°Ù Ø¢Ø³Ø§Ù† Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§.  
- **Ø³Ø§Ø²Ú¯Ø§Ø± Ø¨Ø§ GitHub Actions**: Ø·Ø±Ø§Ø­ÛŒ Ø´Ø¯Ù‡ Ø¨Ø±Ø§ÛŒ Ø§Ø³ØªÙ‚Ø±Ø§Ø± Ø±ÙˆÛŒ GitHub Actions.  
- **Ù¾ÛŒÚ©Ø±Ø¨Ù†Ø¯ÛŒ Ø¨Ø± Ø§Ø³Ø§Ø³ Ø¢Ø±Ú¯ÙˆÙ…Ø§Ù†â€ŒÙ‡Ø§**: Ø¯Ø±ÛŒØ§ÙØª ØªÙˆÚ©Ù† ØªÙ„Ú¯Ø±Ø§Ù… Ùˆ Ø´Ù†Ø§Ø³Ù‡ Ú†Øª Ø¨Ù‡ Ø¹Ù†ÙˆØ§Ù† ÙˆØ±ÙˆØ¯ÛŒ.  
- **Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§ÛŒ Ø¢Ù…Ø§Ø¯Ù‡**:  
  - **Ù…Ø§Ú˜ÙˆÙ„ YouTube**: Ø§Ø±Ø³Ø§Ù„ Ø§Ø¹Ù„Ø§Ù† Ù‡Ù†Ú¯Ø§Ù… Ø§Ù†ØªØ´Ø§Ø± ÙˆÛŒØ¯ÛŒÙˆÛŒ Ø¬Ø¯ÛŒØ¯.  
  - **Ù…Ø§Ú˜ÙˆÙ„ Medium**: Ø§Ø±Ø³Ø§Ù„ Ø§Ø¹Ù„Ø§Ù† Ù‡Ù†Ú¯Ø§Ù… Ø§Ù†ØªØ´Ø§Ø± Ù¾Ø³Øª Ø¬Ø¯ÛŒØ¯.  

---

## Ù¾ÛŒØ´â€ŒÙ†ÛŒØ§Ø²Ù‡Ø§  
1. Ù¾Ø§ÛŒØªÙˆÙ† Ù†Ø³Ø®Ù‡ 3.8 ÛŒØ§ Ø¨Ø§Ù„Ø§ØªØ±.  
2. Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§ÛŒ Ù…ÙˆØ¬ÙˆØ¯ Ø¯Ø± Ù¾ÙˆØ´Ù‡ `module` Ø¨Ø§ÛŒØ¯ Ø¯Ø§Ø±Ø§ÛŒ ØªØ§Ø¨Ø¹ `run` Ø¨Ø§Ø´Ù†Ø¯.  
3. ÛŒÚ© ØªÙˆÚ©Ù† Ø±Ø¨Ø§Øª ØªÙ„Ú¯Ø±Ø§Ù… Ùˆ ÛŒÚ© Ø´Ù†Ø§Ø³Ù‡ Ú†Øª.  

---

## Ù†Ø­ÙˆÙ‡ Ø§Ø³ØªÙØ§Ø¯Ù‡  
1. Ú©Ù„ÙˆÙ† Ú©Ø±Ø¯Ù† Ù…Ø®Ø²Ù†:  
   ```bash  
   git clone https://github.com/your-username/Raccoon.git  
   cd Raccoon  
   ```  

2. Ù†ØµØ¨ ÙˆØ§Ø¨Ø³ØªÚ¯ÛŒâ€ŒÙ‡Ø§:  
   Ø¨Ø®Ø´ `REQUIREMENTS` Ø±Ø§ Ø¯Ø± Ø§Ø³Ú©Ø±ÛŒÙ¾Øª Ø§ØµÙ„ÛŒ ÙØ¹Ø§Ù„ Ú©Ù†ÛŒØ¯ Ùˆ ÙˆØ§Ø¨Ø³ØªÚ¯ÛŒâ€ŒÙ‡Ø§ÛŒ Ù…ÙˆØ±Ø¯ Ù†ÛŒØ§Ø² Ø±Ø§ Ù„ÛŒØ³Øª Ú©Ù†ÛŒØ¯.  

3. Ø§ÙØ²ÙˆØ¯Ù† ÛŒØ§ ÙˆÛŒØ±Ø§ÛŒØ´ Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§:  
   - Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§ÛŒ Ø¬Ø¯ÛŒØ¯ Ø±Ø§ Ø¯Ø± Ù¾ÙˆØ´Ù‡ `module` Ø§Ø¶Ø§ÙÙ‡ Ú©Ù†ÛŒØ¯.  
   - Ø§Ø·Ù…ÛŒÙ†Ø§Ù† Ø­Ø§ØµÙ„ Ú©Ù†ÛŒØ¯ Ú©Ù‡ Ù…Ø§Ú˜ÙˆÙ„ Ø´Ø§Ù…Ù„ ØªØ§Ø¨Ø¹ `run(token, chat_id)` Ø¨Ø§Ø´Ø¯.  

4. Ø§Ø¬Ø±Ø§ÛŒ Ø±Ø¨Ø§Øª:  
   ```bash  
   python bot.py --telegram_token <ØªÙˆÚ©Ù†-Ø±Ø¨Ø§Øª-ØªÙ„Ú¯Ø±Ø§Ù…-Ø´Ù…Ø§> --chat_id <Ø´Ù†Ø§Ø³Ù‡-Ú†Øª-Ø´Ù…Ø§>  
   ```  

---

## Ø³Ø§Ø®ØªØ§Ø± Ù¾ÙˆØ´Ù‡â€ŒÙ‡Ø§  
```  
Raccoon/  
â”‚  
â”œâ”€â”€ bot.py            # Ø§Ø³Ú©Ø±ÛŒÙ¾Øª Ø§ØµÙ„ÛŒ Ø±Ø¨Ø§Øª  
â”œâ”€â”€ module/           # Ù¾ÙˆØ´Ù‡ Ù…Ø±Ø¨ÙˆØ· Ø¨Ù‡ Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§  
â”‚   â”œâ”€â”€ module_youtube.py  # Ù…Ø§Ú˜ÙˆÙ„ ÛŒÙˆØªÛŒÙˆØ¨  
â”‚   â”œâ”€â”€ module_medium.py   # Ù…Ø§Ú˜ÙˆÙ„ Ù…Ø¯ÛŒÙˆÙ…  
â”‚  
```  

---

## Ù…Ø´Ø§Ø±Ú©Øª  
Ù…ÛŒâ€ŒØªÙˆØ§Ù†ÛŒØ¯ Ø§ÛŒÙ† Ù…Ø®Ø²Ù† Ø±Ø§ ÙÙˆØ±Ú© Ú©Ø±Ø¯Ù‡ Ùˆ Ù…Ø§Ú˜ÙˆÙ„â€ŒÙ‡Ø§ÛŒ Ø®ÙˆØ¯ Ø±Ø§ Ø§Ø¶Ø§ÙÙ‡ Ú©Ù†ÛŒØ¯. Ø¯Ø±Ø®ÙˆØ§Ø³Øªâ€ŒÙ‡Ø§ÛŒ pull Ø§Ø³ØªÙ‚Ø¨Ø§Ù„ Ù…ÛŒâ€ŒØ´ÙˆÙ†Ø¯!  
 
