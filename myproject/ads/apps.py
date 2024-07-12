from django.apps import AppConfig
import threading

class AdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ads'

    def ready(self):
        if not hasattr(self, '_bot_thread_started'):
            self._bot_thread_started = True

            from .BLJADUNUS import bot

            def run_bot():
                # Запускаем бота с флагом 'none_stop=True' для постоянного опроса
                bot.polling(none_stop=True)

            # Запуск бота в отдельном потоке
            threading.Thread(target=run_bot, daemon=True).start()