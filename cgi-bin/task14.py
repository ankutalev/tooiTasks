#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import html
import http.cookies
import os

from _wall import Wall
wall = Wall()

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
session = cookie.get("session")
if session is not None:
    session = session.value
user = wall.find_cookie(session)

form = cgi.FieldStorage()
action = form.getfirst("action", "")

if action == "publish":
    text = form.getfirst("text", "")
    text = html.escape(text)
    if text and user is not None:
        wall.publish(user, text)
elif action == "login":
    login = form.getfirst("login", "")
    login = html.escape(login)
    password = form.getfirst("password", "")
    password = html.escape(password)
    if wall.find(login, password):
        cookie = wall.set_cookie(login)
        print('Set-cookie: session={}'.format(cookie))
    elif wall.find(login):
        pass
    else:
        wall.register(login, password)
        cookie = wall.set_cookie(login)
        print('Set-cookie: session={}'.format(cookie))

pattern = '''
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>ТВИТТОР</title>
</head>
<body>
    ЗАЛОГИНЬТЕСЬ В ЧАТИК
    <form action="/cgi-bin/wall.py">
        ВАШЕ ИМЯ: <input type="text" name="login">
        СУПЕР СЕКРЕТНЫЙ ПАРОЛЬ: <input type="password" name="password">
        <input type="hidden" name="action" value="login">
        <input type="submit">
    </form>

    {posts}

    {publish}
</body>
</html>
'''

if user is not None:
    pub = '''
    <form action="/cgi-bin/wall.py">
        <textarea name="text"></textarea>
        <input type="hidden" name="action" value="publish">
        <input type="submit">
    </form>
    '''
else:
    pub = ''

print('Content-type: text/html\n')

print(pattern.format(posts=wall.html_list(), publish=pub))
