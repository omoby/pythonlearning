# -*- coding: utf-8 -*-

import os
import logging


class Logger(object):
    __path = None
    __level = logging.DEBUG
    __dict = {
        "info": logging.INFO,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "debug": logging.DEBUG
    }

    @classmethod
    def set_target(cls, path):
        """
        设置日志打印的目标位置,如果该路径不存在则创建.
        :param path:    str     日志打印的目标文件的路径
        :return:
        """
        # 从路径中提取目录路径
        directory = path[:-len(path.split("\\")[-1].split("/")[-1]) - 1]

        # 如果目录不存在则创建
        if not os.path.exists(directory):
            os.makedirs(directory)

        cls.__path = path

    @classmethod
    def get_target(cls):
        """
        返回日志打印的目标位置.
        :return:
        """
        return cls.__path

    @classmethod
    def set_level(cls, level):
        """
        设置日志文件和Console窗口中记录的日志级别.
        :param level:   str     可选"info"、"error"、"warning"和"debug"不区分大小写
        :return:
        """
        # 检查输入的日志级别是否合法
        if level.lower() not in ["info", "error", "warning", "debug"]:
            raise ValueError("Only info|error|warning|debug is available.")

        cls.__level = cls.__dict[level.lower()]

    @classmethod
    def get_level(cls):
        """
        获取打印的日志级别.
        :return:
        """
        return cls.__level

    def log(self, msg, level="info"):
        """
        将日志输出到屏幕.
        :param msg:     str     要打印的日志信息
        :param level:   str     可选"info"、"error"、"warning"和"debug"不区分大小写
        :return:
        """
        # 检查输入的日志级别是否合法
        if level.lower() not in ["info", "error", "warning", "debug"]:
            raise ValueError("Only info|error|warning|debug is available.")

        # 设置日志打印格式
        # [2020-09-08 14:08:29,860][LogTool.py:94][INFO] 1
        format_ = "[%(asctime)s][%(threadName)s][%(levelname)s] %(message)s"

        # 2020-09-08 14:07:58,443 - D:/pycharmproject/py-spider/util/LogTool.py[line:93] - INFO: 1
        # format_ = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'

        # 开启输出到日志文件的打印器
        logging.basicConfig(
            filename=self.get_target(),
            filemode="a",
            format=format_,
            level=self.get_level()
        )

        # 开启输出到Console的打印器
        console = logging.StreamHandler()
        console.setLevel(self.get_level())
        formatter = logging.Formatter(format_)
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

        # 将日志打印到日志文件和Console页面
        logging.log(self.__dict[level.lower()], msg)

        # 关闭Console打印器否则会重复打印
        logging.getLogger('').removeHandler(console)


if __name__ == "__main__":
    Logger.set_target("D:/test/test.log")
    logger2 = Logger()
    logger2.log("1", "info")
