from DPCrawler.oracle_util import OracleUtil

oracle_util = OracleUtil()
data = oracle_util.get_main_category()

for sub in data:
    id = sub[0]
    # name = eval('u"'+sub[1]+'"')
    name = sub[1].encode('utf-8')
    print(name)