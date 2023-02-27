JWT
===
具有加密签名，无状态，存在客户端。 能够通过多个节点进行用户认证，也就是跨域认证。从客户端发送到服务器端，服务器认证后生成一个JSON对象

组成
----
Header.Payload.Signature

Header
======
标头：令牌+签名算法

Payload
=======
载荷：有关实体（通常是用户）和其他数据的声明：registered, public 和 private 声明

Signature
=========
签名

Flask-RESTful
=============
创建API端点

Flask-JWT-Extended
==================
生成和校验JWT

passlib
=======
生成密码的摘要值

Flask-SQLAlchemy
================
数据库对象的ORM映射

postcode插件
============
测试post方法

token
=====
当用户成功注册或登录，会受到两个token: access token和 refresh token