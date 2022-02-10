# Телеграм PDF бот
  Бот для заполнения и отправки PDF документа в телеграме

# Настройки бота
 <b>Создаем файл env.sh</b>

 <code>touch env.sh</code>

 В этом файле будут храниться настройки бота. Телеграм токен, токен яндекс кассы, промокод

 <b>Дать права исполнения файлу</b>

 <code>chmod +x env.sh</code>

 Это bash скрипт. При запуске, он активирует переменые и бот сможет их читать

 <b>Структура файла</b>

 <code>#! /bin/bash

export TG_TOKEN='токен от @botFather'

export PROMO_CODE='уникальный промокод'

export YTOKEN='токен от яндекс кассы'

echo 'Activated'
</code>

 <b>Теперь нужно запустить файл, чтобы активировать переменные</b>

 <code>. ./env.sh</code>

# Запуск бота

 <b>Создать виртуальное окружение</b>

 <code>python3.10 -m venv venv</code>

 <b>Активировать виртуальное окружение</b>

 <code>. venv/bin/activate</code>

 <b>Обновить пакетный менеджер</b>

 <code>pip install -U pip</code>

 <b>Скачать зависимости</b>

 <code>pip install -r requirements.txt</code>

 <b>Запуск бота</b>

 <code>python -m src</code>

 При повтором запуске вам нужно будет только запустить env.sh <code>. ./env.sh</code>, активировать виртуальное окружение <code>. venv/bin/activate</code> и запустить бота <code>python -m src</code>
