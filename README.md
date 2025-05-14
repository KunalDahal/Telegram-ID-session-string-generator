# 🔐 Telethon Session String Generator

A minimal and secure Python script to generate session strings for [Telethon](https://github.com/LonamiWebs/Telethon), allowing you to authenticate your Telegram account and use it in your Telegram bot or userbot.

---

## 🚀 Features

- Supports both bot and user sessions
- Secure login using phone number and 2FA if enabled
- Generates `.session` files and printable session strings
- Works with Telethon's `StringSession`
- Easy to use and lightweight

---

## 🧰 Requirements

- Python 3.7+
- Telethon

Install requirements using pip:

```bash
pip install telethon
```

---

## ⚙️ Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telethon-session-generator.git
cd telethon-session-generator
```

### 2. Run the Script

```bash
python generate.py
```

### 3. Follow the Prompts

- Enter your **API ID** and **API Hash** (Get it from [my.telegram.org](https://my.telegram.org/apps))
- Choose whether you want a **user session** or **bot session**
- For users: Enter phone number, and login confirmation code
- For bots: Enter bot token

---

## 📝 Example Output

```bash
Your Telethon session string:

1AABp8Ics8a3...<trimmed>...ks9p93K94aB

✅ Save this securely and use it in your project.
```

---

## 🔐 Security Warning

- **Never share your session string.**
- It grants full access to your Telegram account or bot.
- Store it securely and avoid uploading it to public repositories.

---

## 📄 License

MIT License

---

## 🌐 Connect

For support or contributions, feel free to open an issue or pull request.
