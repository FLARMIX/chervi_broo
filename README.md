# Калькулятор прямо в телеграм?

![Работа бота](https://github.com/FLARMIX/telepython/blob/main/Screenshots/-2147483648_-217065.jpg)
![Работа бота](https://github.com/FLARMIX/telepython/blob/main/Screenshots/-2147483648_-217067.jpg)
![Работа бота](https://github.com/FLARMIX/telepython/blob/main/Screenshots/-2147483648_-217069.jpg)

___
## Установка на Андроид

Скачиваем приложение [Termux](https://play.google.com/store/apps/details?id=com.termux) в Play Market<br>
Открываем и пишем команды поочерёдно<br>

***Для копирования команды нажмите справа от неё***

*Обновляем*

	apt-get update
*Ставим git и python*

	apt-get install git python
Если спросит `Do you want to continue? [Y/n]` отвечаем `Y` и продолжаем<br>
*Устанавливаем pyrogram*

	pip install pyrogram
*Клонируем репозиторий*

	https://github.com/FLARMIX/telepython.git

___
## Команды в Телеграме
`help` - небольшой гайд<br>
`send` - выполнить код/команду<br>
`calc` - посчитать<br>


___
## Помощь
При возникновении ошибок проверьте правильность написания/копирования команд<br>
Попробуйте еще раз и только потом пишите мне в [**Личные Сообщения**](https://t.me/FLARMIX) вместе со скриншотом!
Так же по поводу установки на ПК писать мне в ЛС.

__
## Запуск
*Введите* и ждите пока бот запросит номер телефона, привязанный к **ВАШЕМУ** телеграму

	python teleghoul/index.py
	
В **ТЕЛЕГРАМ** придёт код, введите его и бот заработает

![Запуск](https://github.com/error1001es/teleghoul/blob/main/screenshots/start.png)<br>

Если у вас стоит *двухфакторная аутентификация*, то бот запросит пароль<br>

**После запуска бот даст тебе знать, *последующие запуски выполняются без каких-либо установок***<br>

___
## Обновление
*Заходим в папочку со скриптом*

	cd telepython
	
*Обновляем*	

	git pull
	
*Выходим из папки, для удобного последующего запуска*

	cd ../
