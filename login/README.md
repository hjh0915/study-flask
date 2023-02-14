开启一个 交互 Python shell
=========================
会导入实例
---------
> $ flask --app serve.py shell

> $ dir()
['User', '__builtins__', 'app', 'db', 'g']
>>> u = User()
>>> u.username = 'admin'
>>> u.password = '123'
>>> db.session.commit()
>>> db.session.add(u)
>>> db.session.commit()
>>> u.verify_password('123')
True

slqite3
========
>>> select * from users;

HTTP
=====
*flask里面的session默认是cookies*
http协议是一种无状态协议，无法根据之前的状态进行本次的请求处理，即不记录已登录状态（服务器不知道客户端的历史请求）

session
-------
客户端请求服务器端，保存在服务器端
如果服务器启用Session，服务器就要为该用户创建一个SESSION，服务器首先检查这个用户发来的请求里是否包含了一个SESSION ID，如果包含了一个SESSION ID则说明之前该用户已经登陆过并为此用户创建过SESSION，那服务器就按照这个SESSION ID把这个SESSION在服务器的内存中查找出来（如果查找不到，就有可能为他新创建一个），如果客户端请求里不包含有SESSION ID，则为该客户端创建一个SESSION并生成一个与此SESSION相关的SESSION ID。

cookies
-------
服务器发送到客户端，保存在客户端。
cookie的内容主要包括：名字，值，过期时间，路径和域。

GET
---
在Flask对象的route方法中指定HTTP方法，如果不写的话，默认的就是GET。
GET产生一个TCP数据包
对于GET方式的请求，浏览器会把http header和data一并发送出去，服务器响应200

POST
----
POST产生两个TCP数据包，在网络环境差的情况下，两次包的TCP在验证数据包完整性上，有非常大的优点。
对于POST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200