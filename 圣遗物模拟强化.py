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


artifact_parts = ['�?','羽毛','沙漏','�?�?','帽子']
hua_main = ['生命�?']
yumao_main = '攻击�?'
shalou_main = ['攻击力百分比','防御百分�?','生命百分�?','元素充能效率','元素精�?']
beizi_main = ['攻击力百分比','防御百分�?','生命百分�?','冰属性伤�?','�?属性伤�?','水属性伤�?','岩属性伤�?','雷属性伤�?','风属性伤�?','元素精�?']
maozi_main = ['攻击力百分比','防御百分�?','生命百分�?','暴击伤�??','暴击�?','元素精�?']
fucitiao = ['暴击�?','生命百分�?','攻击力百分比','元素充能效率','防御百分�?','暴击伤�??','攻击�?','防御�?','元素精�?','生命�?']
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
	if fucitiao == '暴击�?':
		fucitiao_shuzhi += random.choice(baojilvbaifenbi)
	elif fucitiao == '生命百分�?':
		fucitiao_shuzhi += random.choice(shengmingbaifenbi)
	elif fucitiao == '攻击力百分比':
		fucitiao_shuzhi += random.choice(gongjilibaifenbi)
	elif fucitiao == '元素充能效率':
		fucitiao_shuzhi += random.choice(yuanshuchongnengbaifenbi)
	elif fucitiao == '元素精�?':
		fucitiao_shuzhi += random.choice(yuanshujingtong)
	elif fucitiao == '防御百分�?':
		fucitiao_shuzhi += random.choice(fangyulibaifenbi)
	elif fucitiao == '暴击伤�??':
		fucitiao_shuzhi += random.choice(baojishanghaibaifenbi)
	elif fucitiao == '攻击�?':
		fucitiao_shuzhi += random.choice(gongjil)
	elif fucitiao == '防御�?':
		fucitiao_shuzhi += random.choice(fangyuli)
	elif fucitiao == '生命�?':
		fucitiao_shuzhi += random.choice(shengmingzhi)
	return fucitiao_shuzhi
	
#用fucitiao生成不一样的fucitiao1，fucitiao2，fucitiao3，fucitiao4
def makeFucitiao(zhucitiao):
	global fucitiao1,fucitiao2,fucitiao3,fucitiao4,fucitiao1_shuzhi,fucitiao2_shuzhi,fucitiao3_shuzhi,fucitiao4_shuzhi
	temp = fucitiao[:]
	temp.remove(zhucitiao)
	#生成fucittiao1
	fucitiao1 = random.choice(temp)
	fucitiao1_shuzhi = fucitiao_shuzhi(fucitiao1,fucitiao1_shuzhi)
	#生成fucitiao2
	temp.remove(fucitiao1)
	fucitiao2 = random.choice(temp)
	fucitiao2_shuzhi = fucitiao_shuzhi(fucitiao2,fucitiao2_shuzhi)
	#生成fucitiao3
	temp.remove(fucitiao2)
	fucitiao3 = random.choice(temp)
	fucitiao3_shuzhi = fucitiao_shuzhi(fucitiao3,fucitiao3_shuzhi)
	#生成fucitiao4
	temp.remove(fucitiao3)
	fucitiao4 = random.choice(temp)
	fucitiao4_shuzhi = fucitiao_shuzhi(fucitiao4,fucitiao4_shuzhi)
	



#获得一�?圣遗�?
pick_a_artifact()
print("你获得了这个圣遗�?: ")
print("圣遗物部�?:" + artifact_part)
if(artifact_part == artifact_parts[0]):
	print("主词�?: " + hua)
	makeFucitiao(hua)
elif(artifact_part == artifact_parts[1]):
	print("主词�?: " + yumao)
	makeFucitiao(yumao)
elif(artifact_part == artifact_parts[2]):
	print("主词�?: " + shalou)
	makeFucitiao(shalou)
elif(artifact_part == artifact_parts[3]):
	print("主词�?: " + beizi)
	makeFucitiao(beizi)
elif(artifact_part == artifact_parts[4]):
	print("主词�?: " + maozi)
	makeFucitiao(maozi)

#开始生成副词条
print("�?词条: ")
#输出fucitiao1，fucitiao2，fucitiao3，fucitiao4
print('1. '+ str(fucitiao1) + ' ' + str(fucitiao1_shuzhi))
print('2. '+ str(fucitiao2) + ' ' + str(fucitiao2_shuzhi))
print('3. '+ str(fucitiao3) + ' ' + str(fucitiao3_shuzhi))
print('4. '+ str(fucitiao4) + ' ' + str(fucitiao4_shuzhi))



a = int(input("你�?�继�?强化完的圣遗物的�?: "))
if a == 1:
	while c <= 5:
		temp = random.choice([1,2,3,4])
		if temp == 1:
			fucitiao1_shuzhi = fucitiao_shuzhi(fucitiao1,fucitiao1_shuzhi)
			print("圣遗物副词条****************" + str(fucitiao1))
		elif temp == 2:
			fucitiao2_shuzhi = fucitiao_shuzhi(fucitiao2,fucitiao2_shuzhi)
			print("圣遗物副词条****************" + str(fucitiao2))
		elif temp == 3:
			fucitiao3_shuzhi = fucitiao_shuzhi(fucitiao3,fucitiao3_shuzhi)
			print("圣遗物副词条****************" + str(fucitiao3))
		elif temp == 4:
			fucitiao4_shuzhi = fucitiao_shuzhi(fucitiao4,fucitiao4_shuzhi)
			print("圣遗物副词条****************" + str(fucitiao4))
		print('1. '+ str(fucitiao1) + ' ' + str("%.1f" %fucitiao1_shuzhi))
		print('2. '+ str(fucitiao2) + ' ' + str("%.1f" %fucitiao2_shuzhi))
		print('3. '+ str(fucitiao3) + ' ' + str("%.1f" %fucitiao3_shuzhi))
		print('4. '+ str(fucitiao4) + ' ' + str("%.1f" %fucitiao4_shuzhi))
		sleep(1)
		c += 1
"""
���������ʥ����: 
ʥ���ﲿλ:��
������: ����ֵ
������:
1. �����˺� 7.0
2. ������ 18
3. ������ 2.7
4. �������ٷֱ� 5.3
��Ҫ����ǿ�����ʥ�������: 1
ʥ���︱����****************�����˺�
1. �����˺� 12.4
2. ������ 18.0
3. ������ 2.7
4. �������ٷֱ� 5.3
ʥ���︱����****************������
1. �����˺� 12.4
2. ������ 32.0
3. ������ 2.7
4. �������ٷֱ� 5.3
ʥ���︱����****************������
1. �����˺� 12.4
2. ������ 50.0
3. ������ 2.7
4. �������ٷֱ� 5.3
ʥ���︱����****************������
1. �����˺� 12.4
2. ������ 64.0
3. ������ 2.7
4. �������ٷֱ� 5.3
ʥ���︱����****************�������ٷֱ�
1. �����˺� 12.4
2. ������ 64.0
3. ������ 2.7
4. �������ٷֱ� 11.1
"""