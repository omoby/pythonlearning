from fontTools.ttLib import TTFont

font = TTFont('D:\MyFile\工作记录文件\python3开发网络爬虫\python3爬虫原理与绕过实战\movie.woff')
font.saveXML('./movie.xml')