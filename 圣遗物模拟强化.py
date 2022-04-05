import random
from time import sleep

artifact_part = ''
hua = ''
yumao = ''
shalou = ''
beizi = ''
maozi = ''
c = 1

fucitiao1 = ''
fucitiao2 = ''
fucitiao3 = ''
fucitiao4 = ''

fucitiao1_shuzhi = 0
fucitiao2_shuzhi = 0
fucitiao3_shuzhi = 0
fucitiao4_shuzhi = 0

baojilvbaifenbi_jisuan = 0
shengmingbaifenbi_jisuan = 0
gongjilibaifenbi_jisuan = 0
yuanshuchongnengbaifenbi_jisuan = 0
fangyulibaifenbi_jisuan = 0
baojishanghaibaifenbi_jisuan = 0
gongjil_jisuan = 0
fangyuli_jisuan = 0
yuanshujingtong_jisuan = 0
shengmingzhi_jisuan = 0

totalEnhanceTimes = 5


artifact_parts = ['èŠ?','ç¾½æ¯›','æ²™æ¼','æ?å­?','å¸½å­']
hua_main = ['ç”Ÿå‘½å€?']
yumao_main = 'æ”»å‡»åŠ?'
shalou_main = ['æ”»å‡»åŠ›ç™¾åˆ†æ¯”','é˜²å¾¡ç™¾åˆ†æ¯?','ç”Ÿå‘½ç™¾åˆ†æ¯?','å…ƒç´ å……èƒ½æ•ˆçŽ‡','å…ƒç´ ç²¾é€?']
beizi_main = ['æ”»å‡»åŠ›ç™¾åˆ†æ¯”','é˜²å¾¡ç™¾åˆ†æ¯?','ç”Ÿå‘½ç™¾åˆ†æ¯?','å†°å±žæ€§ä¼¤å®?','ç?å±žæ€§ä¼¤å®?','æ°´å±žæ€§ä¼¤å®?','å²©å±žæ€§ä¼¤å®?','é›·å±žæ€§ä¼¤å®?','é£Žå±žæ€§ä¼¤å®?','å…ƒç´ ç²¾é€?']
maozi_main = ['æ”»å‡»åŠ›ç™¾åˆ†æ¯”','é˜²å¾¡ç™¾åˆ†æ¯?','ç”Ÿå‘½ç™¾åˆ†æ¯?','æš´å‡»ä¼¤å??','æš´å‡»çŽ?','å…ƒç´ ç²¾é€?']
fucitiao = ['æš´å‡»çŽ?','ç”Ÿå‘½ç™¾åˆ†æ¯?','æ”»å‡»åŠ›ç™¾åˆ†æ¯”','å…ƒç´ å……èƒ½æ•ˆçŽ‡','é˜²å¾¡ç™¾åˆ†æ¯?','æš´å‡»ä¼¤å??','æ”»å‡»åŠ?','é˜²å¾¡åŠ?','å…ƒç´ ç²¾é€?','ç”Ÿå‘½å€?']
baojilvbaifenbi = [2.7,3.1,3.5,3.9]
shengmingbaifenbi = [4.1,4.7,5.3,5.8]
gongjilibaifenbi = [4.1,4.7,5.3,5.8]
yuanshuchongnengbaifenbi = [4.5,5.2,5.8,6.5]
fangyulibaifenbi = [5.1,5.8,6.6,7.3]
baojishanghaibaifenbi = [5.4,6.2,7.0,7.8]
gongjil = [14,16,18,19]
fangyuli = [16,19,21,23]
yuanshujingtong = [16,19,21,23]
shengmingzhi = [209,239,269,299]

def pick_a_artifact():
	global hua,yumao,shalou,beizi,maozi,artifact_part
	artifact_part = random.choice(artifact_parts)
	hua = random.choice(hua_main)
	yumao = random.choice(yumao_main)
	shalou = random.choice(shalou_main)
	beizi = random.choice(beizi_main)
	maozi = random.choice(maozi_main)

def fucitiao_shuzhi(fucitiao,fucitiao_shuzhi):
	global baojilvbaifenbi_jisuan,shengmingbaifenbi_jisuan,gongjilibaifenbi_jisuan,yuanshuchongnengbaifenbi_jisuan,fangyulibaifenbi_jisuan,baojishanghaibaifenbi_jisuan,gongjil_jisuan,fangyuli_jisuan,yuanshujingtong_jisuan,shengmingzhi_jisuan
	if fucitiao == 'æš´å‡»çŽ?':
		fucitiao_shuzhi += random.choice(baojilvbaifenbi)
	elif fucitiao == 'ç”Ÿå‘½ç™¾åˆ†æ¯?':
		fucitiao_shuzhi += random.choice(shengmingbaifenbi)
	elif fucitiao == 'æ”»å‡»åŠ›ç™¾åˆ†æ¯”':
		fucitiao_shuzhi += random.choice(gongjilibaifenbi)
	elif fucitiao == 'å…ƒç´ å……èƒ½æ•ˆçŽ‡':
		fucitiao_shuzhi += random.choice(yuanshuchongnengbaifenbi)
	elif fucitiao == 'å…ƒç´ ç²¾é€?':
		fucitiao_shuzhi += random.choice(yuanshujingtong)
	elif fucitiao == 'é˜²å¾¡ç™¾åˆ†æ¯?':
		fucitiao_shuzhi += random.choice(fangyulibaifenbi)
	elif fucitiao == 'æš´å‡»ä¼¤å??':
		fucitiao_shuzhi += random.choice(baojishanghaibaifenbi)
	elif fucitiao == 'æ”»å‡»åŠ?':
		fucitiao_shuzhi += random.choice(gongjil)
	elif fucitiao == 'é˜²å¾¡åŠ?':
		fucitiao_shuzhi += random.choice(fangyuli)
	elif fucitiao == 'ç”Ÿå‘½å€?':
		fucitiao_shuzhi += random.choice(shengmingzhi)
	return fucitiao_shuzhi
	
#ç”¨fucitiaoç”Ÿæˆä¸ä¸€æ ·çš„fucitiao1ï¼Œfucitiao2ï¼Œfucitiao3ï¼Œfucitiao4
def makeFucitiao(zhucitiao):
	global fucitiao1,fucitiao2,fucitiao3,fucitiao4,fucitiao1_shuzhi,fucitiao2_shuzhi,fucitiao3_shuzhi,fucitiao4_shuzhi
	temp = fucitiao[:]
	temp.remove(zhucitiao)
	#ç”Ÿæˆfucittiao1
	fucitiao1 = random.choice(temp)
	fucitiao1_shuzhi = fucitiao_shuzhi(fucitiao1,fucitiao1_shuzhi)
	#ç”Ÿæˆfucitiao2
	temp.remove(fucitiao1)
	fucitiao2 = random.choice(temp)
	fucitiao2_shuzhi = fucitiao_shuzhi(fucitiao2,fucitiao2_shuzhi)
	#ç”Ÿæˆfucitiao3
	temp.remove(fucitiao2)
	fucitiao3 = random.choice(temp)
	fucitiao3_shuzhi = fucitiao_shuzhi(fucitiao3,fucitiao3_shuzhi)
	#ç”Ÿæˆfucitiao4
	temp.remove(fucitiao3)
	fucitiao4 = random.choice(temp)
	fucitiao4_shuzhi = fucitiao_shuzhi(fucitiao4,fucitiao4_shuzhi)
	



#èŽ·å¾—ä¸€ä¸?åœ£é—ç‰?
pick_a_artifact()
print("ä½ èŽ·å¾—äº†è¿™ä¸ªåœ£é—ç‰?: ")
print("åœ£é—ç‰©éƒ¨ä½?:" + artifact_part)
if(artifact_part == artifact_parts[0]):
	print("ä¸»è¯æ?: " + hua)
	makeFucitiao(hua)
elif(artifact_part == artifact_parts[1]):
	print("ä¸»è¯æ?: " + yumao)
	makeFucitiao(yumao)
elif(artifact_part == artifact_parts[2]):
	print("ä¸»è¯æ?: " + shalou)
	makeFucitiao(shalou)
elif(artifact_part == artifact_parts[3]):
	print("ä¸»è¯æ?: " + beizi)
	makeFucitiao(beizi)
elif(artifact_part == artifact_parts[4]):
	print("ä¸»è¯æ?: " + maozi)
	makeFucitiao(maozi)

#å¼€å§‹ç”Ÿæˆå‰¯è¯æ¡
print("å‰?è¯æ¡: ")
#è¾“å‡ºfucitiao1ï¼Œfucitiao2ï¼Œfucitiao3ï¼Œfucitiao4
print('1. '+ str(fucitiao1) + ' ' + str(fucitiao1_shuzhi))
print('2. '+ str(fucitiao2) + ' ' + str(fucitiao2_shuzhi))
print('3. '+ str(fucitiao3) + ' ' + str(fucitiao3_shuzhi))
print('4. '+ str(fucitiao4) + ' ' + str(fucitiao4_shuzhi))



a = int(input("ä½ è?ç»§ç»?å¼ºåŒ–å®Œçš„åœ£é—ç‰©çš„å?: "))
if a == 1:
	while c <= 5:
		temp = random.choice([1,2,3,4])
		if temp == 1:
			fucitiao1_shuzhi = fucitiao_shuzhi(fucitiao1,fucitiao1_shuzhi)
			print("åœ£é—ç‰©å‰¯è¯æ¡****************" + str(fucitiao1))
		elif temp == 2:
			fucitiao2_shuzhi = fucitiao_shuzhi(fucitiao2,fucitiao2_shuzhi)
			print("åœ£é—ç‰©å‰¯è¯æ¡****************" + str(fucitiao2))
		elif temp == 3:
			fucitiao3_shuzhi = fucitiao_shuzhi(fucitiao3,fucitiao3_shuzhi)
			print("åœ£é—ç‰©å‰¯è¯æ¡****************" + str(fucitiao3))
		elif temp == 4:
			fucitiao4_shuzhi = fucitiao_shuzhi(fucitiao4,fucitiao4_shuzhi)
			print("åœ£é—ç‰©å‰¯è¯æ¡****************" + str(fucitiao4))
		print('1. '+ str(fucitiao1) + ' ' + str("%.1f" %fucitiao1_shuzhi))
		print('2. '+ str(fucitiao2) + ' ' + str("%.1f" %fucitiao2_shuzhi))
		print('3. '+ str(fucitiao3) + ' ' + str("%.1f" %fucitiao3_shuzhi))
		print('4. '+ str(fucitiao4) + ' ' + str("%.1f" %fucitiao4_shuzhi))
		sleep(1)
		c += 1
"""
Äã»ñµÃÁËÕâ¸öÊ¥ÒÅÎï: 
Ê¥ÒÅÎï²¿Î»:»¨
Ö÷´ÊÌõ: ÉúÃüÖµ
¸±´ÊÌõ:
1. ±©»÷ÉËº¦ 7.0
2. ¹¥»÷Á¦ 18
3. ±©»÷ÂÊ 2.7
4. ¹¥»÷Á¦°Ù·Ö±È 5.3
ÄãÒª¼ÌÐøÇ¿»¯ÍêµÄÊ¥ÒÅÎïµÄÂð: 1
Ê¥ÒÅÎï¸±´ÊÌõ****************±©»÷ÉËº¦
1. ±©»÷ÉËº¦ 12.4
2. ¹¥»÷Á¦ 18.0
3. ±©»÷ÂÊ 2.7
4. ¹¥»÷Á¦°Ù·Ö±È 5.3
Ê¥ÒÅÎï¸±´ÊÌõ****************¹¥»÷Á¦
1. ±©»÷ÉËº¦ 12.4
2. ¹¥»÷Á¦ 32.0
3. ±©»÷ÂÊ 2.7
4. ¹¥»÷Á¦°Ù·Ö±È 5.3
Ê¥ÒÅÎï¸±´ÊÌõ****************¹¥»÷Á¦
1. ±©»÷ÉËº¦ 12.4
2. ¹¥»÷Á¦ 50.0
3. ±©»÷ÂÊ 2.7
4. ¹¥»÷Á¦°Ù·Ö±È 5.3
Ê¥ÒÅÎï¸±´ÊÌõ****************¹¥»÷Á¦
1. ±©»÷ÉËº¦ 12.4
2. ¹¥»÷Á¦ 64.0
3. ±©»÷ÂÊ 2.7
4. ¹¥»÷Á¦°Ù·Ö±È 5.3
Ê¥ÒÅÎï¸±´ÊÌõ****************¹¥»÷Á¦°Ù·Ö±È
1. ±©»÷ÉËº¦ 12.4
2. ¹¥»÷Á¦ 64.0
3. ±©»÷ÂÊ 2.7
4. ¹¥»÷Á¦°Ù·Ö±È 11.1
"""