# 🚴 Bike Rental Bot

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![AIogram](https://img.shields.io/badge/AIogram-3.x-green)
![Docker](https://img.shields.io/badge/Docker-✓-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Professional Telegram bot for automating customer bookings in a bike rental service.** Collects applications through an interactive menu and instantly sends them to managers' work chat.

## ✨ Features
- ✅ **Complete application cycle** - from service selection to confirmation
- ✅ **Intuitive interface** - only buttons, minimal text
- ✅ **Telegram integration** - applications go directly to managers' chat
- ✅ **Production ready** - Docker, .env, error handling
- ✅ **Scalable architecture** - easy to add new services

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/SviridovSergey/Bike_Rental_Bot.git
cd Bike_Rental_Bot
pip install -r requirements.txt
```

### 2. Configure
```bash
cp .env.example .env
# Edit .env with your data
```

**`.env` file:**
```env
BOT_TOKEN=your_token_from_BotFather
GROUP_CHAT_ID=-1001234567890  # Group ID with -100 prefix
TOPIC_MESSAGE_ID=8774         # Topic/thread ID in group
MANAGER_PHONE=+79998887766    # Manager contact
```

### 3. Run
```bash
# Local
python bot.py

# With Docker (recommended)
docker-compose up -d
docker-compose logs -f bot
```

## 📁 Project Structure
```
Bike_Rental_Bot/
├── bot.py              # Main entry point
├── config.py           # Configuration
├── keyboards.py        # All bot keyboards
├── handlers/           # Message handlers
│   ├── start.py       # /start, main menu
│   ├── location.py    # Location selection
│   ├── service.py     # Service selection
│   ├── date.py        # Day selection
│   └── contact.py     # Name/phone, sending to group
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🔧 Application Flow
1. `/start` → Main menu
2. "Create application" → Choose location (2 points)
3. Select service (Rent/Repair/Parts/Inspection)
4. Choose day (Monday-Sunday)
5. Enter name (FIO)
6. Share phone via contact button
7. Confirm → Sent to manager's group

## 🐳 Docker Deployment

### Build & Run
```bash
docker-compose build
docker-compose up -d
```

### Useful Commands
```bash
# View logs
docker-compose logs -f bot

# Restart
docker-compose restart bot

# Stop
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

## 🛠️ Tech Stack
- **Python 3.9+** - Main language
- **AIogram 3.x** - Telegram Bot framework
- **Docker** - Containerization
- **Docker Compose** - Orchestration
- **FSM** - Finite State Machine for dialog management

## 📊 Features in Detail

### For Customers
- Simple step-by-step interface
- No registration required
- Instant confirmation
- Manager contact provided

### For Managers
- All applications in one place
- Structured information
- Telegram notifications
- 24/7 availability

## 🔄 Application Example in Group
```
🚴 НОВАЯ ЗАЯВКА 🚴

👤 ФИО: Иванов Иван Иванович
📞 Телефон: +79998887766
📍 Точка: ул. Соколова, 80
🔧 Услуга: Аренда велосипеда 🚲
📅 День: Понедельник
⏰ Создано: 14:30 10.02.2024

📞 Менеджер: +79998887766
```

## ⚙️ Configuration Options

### Locations (in config.py)
```python
LOCATIONS = {
    "west": "ул. Соколова, 80\nВремя работы: 9:00-22:00",
    "center": "ул. Жмайлова, 27в\nВремя работы: 10:00-23:00"
}
```

### Services
```python
SERVICES = {
    "rent": "Аренда велосипеда 🚲",
    "repair": "Ремонт 🔧",
    "parts": "Покупка запчастей ⚙️",
    "inspection": "Техосмотр 📋"
}
```

## 🚨 Troubleshooting

### Common Issues
1. **Bot not sending to group**
   - Check bot is added to group
   - Bot must be admin in group
   - Group must be supergroup (for topics)

2. **Docker errors**
   - Check Docker Desktop is running
   - Verify .env file exists
   - Check port availability

3. **Token errors**
   - Verify BOT_TOKEN in .env
   - Check token with @BotFather

### View Logs
```bash
# Docker
docker-compose logs -f bot

# Local
python bot.py  # View console output
```

## 📈 Business Benefits
- **80% faster** application processing
- **No lost applications**
- **24/7 availability**
- **Professional customer experience**
- **Centralized data management**

## 🔮 Future Plans
- [ ] Web dashboard for managers
- [ ] Statistics and analytics
- [ ] Email/SMS notifications
- [ ] CRM integration
- [ ] Multi-language support

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author
**Sergey Sviridov** 
- GitHub: [@SviridovSergey](https://github.com/SviridovSergey)
- Telegram: For questions about the bot

## ⭐ Support
If you find this project useful, please give it a star on GitHub!

---

**Ready for production use! Deploy and automate your bike rental business today.** 🚀
