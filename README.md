# Chervi это черви бро

___
## Установка на Андроид

По этой ссылке скачиваем приложение [Termux](https://github.com/termux/termux-app/releases/download/v0.118.0/termux-app_v0.118.0+github-debug_arm64-v8a.apk) с Гитхаба<br>
Открываем и пишем команды поочерёдно<br>

***Для копирования команды нажмите справа от неё***

*Обновляем*

 	apt update
	apt upgrade
*Ставим git и python*

	apt install git python
Если спросит `Do you want to continue? [Y/n]` отвечаем `Y` и продолжаем<br>
*Устанавливаем pyrogram*

	pip install pyrogram
*Клонируем репозиторий*

	git clone https://github.com/FLARMIX/chervi_broo.git

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
*Введите* и ждите пока скрипт запросит номер телефона, привязанный к **ВАШЕМУ** телеграму

 	cd telepython
	python main.py
	
В **ТЕЛЕГРАМ** придёт код, введите его и скрипт заработает

![Запуск](https://github.com/FLARMIX/chervi_broo/blob/main/Screenshots/start.png)<br>

Если у вас стоит *двухфакторная аутентификация*, то скрипт запросит пароль<br>

**После запуска скрипт даст тебе знать, *последующие запуски выполняются без каких-либо установок***<br>

___
## Обновление
*Заходим в папочку со скриптом*

	cd telepython
	
*Обновляем*	

	git pull
	
*Выходим из папки, для удобного последующего запуска*

	cd ../
