logging
=======
因为logging是分级别的，上面5个级别的信息从上到下依次递增，可以通过设置logging的level，使其只打印某个级别以上的信息。因为默认等级是 WARNING，所以只有 WARNING 以上级别的日志被打印出来。

设置级别
-------
可以使用 basicConfig 对其进行配置(放在最上面一行)

记录器
-----
getLogger 获取了一个记录器。

输出格式
-------
可以通过basicConfig进行配置
``` py
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
```