
string='Ãâ·Ñ'
result = string.encode("windows-1252").decode("gbk")
print(result)

string2 = "ºÓÄÏ×¨Éý±¾2016Ó¢Óï½²×ù"
result2 = string2.encode("windows-1252").decode("gbk")
print(result2)

string3 = "CDRÊÓÆµ½Ì³ÌCorelDRAWÆ½Ãæ¹ã¸æX7ÅÅ°æÉè¼ÆÁã»ù´¡ÈëÃÅÈ«Ì××ÔÑ§¿Î³Ì"
result3 = string3.encode("windows-1252").decode("gbk")
print(result3)