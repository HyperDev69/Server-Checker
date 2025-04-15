import socket
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 'TOKEH' # Replace with your bot's token 

# Function that checks if a service is running on a given IP and port
def check_status(ip, port, timeout=3):
    try:
        # Tries to send a connection to given IP and port 
        with socket.create_connection((ip, port), timeout=timeout):
            return True  # If successful, return True
    except Exception:
        return False  # If it fails, return False

# This function handles the /status command
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args

        # Check that exactly two arguments were provided
        if len(args) != 2:
            await update.message.reply_text("To use the bot, write: /status 0.0.0.0 9339 (example usage)" )
            return

        # Extract and prepare IP and port
        ip = args[0]
        port = int(args[1])
        isOnline = check_status(ip, port) # Check if server is online using check_status function
        status_message = "online" if isOnline else "offline"
        await update.message.reply_text(f"{ip}:{port} is {status_message}.") # Sends response
    except Exception:
        await update.message.reply_text("Unkown error")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("status", status))
    print("Welcome to Server Status bot (by https://github.com/hyperdev69)")
    app.run_polling()