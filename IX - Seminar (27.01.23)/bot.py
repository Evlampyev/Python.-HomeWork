from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q')
updater = Updater(token='5916882745:AAHDomrnWWXirqjByn6-XiztHz9nDXolK1Q')
dispatcher = updater.dispatcher

A = 0


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\n Введите фразу для удаления - абв?')
    return A


def delete(update, context):
    text = update.message.text
    lst_text = text.split()
    for i in lst_text:
        if 'абв' in i:
            lst_text.remove(i)
    text = "Ответ: " + ' '.join(lst_text)
    context.bot.send_message(update.effective_chat.id, text)
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!!!')


start_handler = CommandHandler('start', start)
delete_handler = MessageHandler(Filters.text, delete)
cancel_handler = MessageHandler(Filters.text, cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={A: [delete_handler]},
                                   fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
