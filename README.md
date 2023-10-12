# Асинхронный VK-бот для игры в "ПолеЧудес"

## Технический стек

![](https://img.shields.io/badge/-Python-386e9d?style=for-the-badge&logo=Python&logoColor=ffd241&) ![](https://img.shields.io/badge/-Aiohttp-DCDCDC?style=for-the-badge&logo=Aiohttp&logoColor=blue) ![](https://img.shields.io/badge/-sqlalchemy-4479A7?style=for-the-badge&amp;&amp;logoColor=ffffff) ![](https://img.shields.io/badge/-Postgresql-%232c3e50?style=for-the-badge&logo=Postgresql)

## Описание

VK-бот для игры в "ПолеЧудес" - выполнен при помощи инструментов асинхронного програмирования asyncio, aiohttp. Ключевая его особенность, возможность обрабатывать события с разных чатов одновременно, при незначительном замедлении производительности.

## Реализовано:
1. Бот с полноценным геймплеем и защитой от спама (троттлингом).
2. Полноценное Long Poll соединение без использования вспомогательных библиотек. 
3. Сервис API для администратора.
4. Gracefull shutdown, возможность пережить restart сервера.

## Архитектура:
В приложение присутствуют следующие основные сущности:
1. VK_API - Poller, Worker, BotManager. Реализована логика соединения и обработка событий.
2. Game, GameScore, Question, User. Реализована Бизнес-логика игры
