import logging


logger = logging.getLogger('test')
logger.setLevel(level=logging.DEBUG)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
logger.info('info级别，一般用来打印一些正常的操作信息')
logger.warning('waring级别，一般用来打印警告信息')
logger.error('error级别，一般用来打印一些错误信息')
logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')

