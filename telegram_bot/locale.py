from aiogram.utils.i18n import I18nMiddleware

class MyI18n(I18nMiddleware):
    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        return user.language_code

i18n = MyI18n('bot', default='en')
_ = i18n.gettext

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(_('Hello! This is your ToDo list bot.'))