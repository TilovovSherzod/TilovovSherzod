from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config import TOKEN
from ism_manosi import find_name

token = TOKEN



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        text=f"👋 Assalom aleykum <b>{update.effective_user.full_name}</b>.\n"
             f"Ismlar Ma'nosini aniqlab beruvchi botimizga hush kelibsiz!\n"
             f"Sizni qaysi isimning manosi qiziqtiradi? shu isimni kiriting:"

    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        text=(
            "🤖 <b>Bot haqida to'liq ma'lumot:</b>\n\n"
            "Bu bot orqali siz o'zbek ismlarining ma'nosini bilib olishingiz mumkin.\n"
            "Quyidagi buyruqlar mavjud:\n"
            "/start - Botni boshlash\n"
            "/help - Bot haqida ma'lumot\n"
            "/dasturchi_haqida_malumot - Dasturchi haqida ma'lumot\n\n"
            "Ismni yozib yuboring va bot sizga ismning ma'nosini, tilini va jinsini aytib beradi."
        )
    )

async def developer_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        text=(
            "👨‍💻 <b>Dasturchi haqida ma'lumot:</b>\n\n"
            "Ism: Tilovov Sherzod Davron o'g'li\n"
            "Email: shrzdtilovov@gmail.com\n"
            "GitHub: TilovovSherzod\n"
            "Men dasturchiman va bu botni sizning ismlaringizning ma'nosini bilib olishingizga yordam berish uchun yaratdim."
        )
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if len(text.split()) > 1:
        await update.message.reply_html(
            text="<b>🫸 Ismni bitta so'z orqali kiriting yoki qo'shib yozing!</b>"
        )
    else:
        ism_data = find_name(text)
        if ism_data:
            gender_text = "Erkak" if ism_data['properties']['gender'] == "M" else "Ayol"
            await update.message.reply_html(
                text=f"🙂 <b>Ism: </b>{ism_data['properties']['name']}\n\n"
                     f"🇺🇿 <b>Til: </b> {ism_data['properties']['origin']}\n"
                     f"🐼 <b>Jins:</b> {gender_text}\n"
                     f"🔖 <b>Ma'nosi: </b> {ism_data['properties']['meaning']}."
            )
        else:
            await update.message.reply_html(
                text="<b>❌ Afsuski siz kiritgan ism bo'yicha ma'lumot topilmadi!</b>"
            )

def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("dasturchi_haqida_malumot", developer_info))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()

if __name__ == '__main__':
    main()
