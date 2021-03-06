from PublicReference.base import *

class 绯红玫瑰技能0(主动技能):
    名称 = '致命射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1281.30
    成长 = 144.70
    CD = 6.2
    TP成长 = 0.1
    TP上限 = 7

class 绯红玫瑰技能1(被动技能):
    名称 = '左轮奥义'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 绯红玫瑰技能2(被动技能):
    名称 = '花式枪术'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)

class 绯红玫瑰技能3(主动技能):
    名称 = '锁链截击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 27
    基础 = 3907.43
    成长 = 540.57
    CD = 5.0



class 绯红玫瑰技能4(主动技能):
    名称 = '音速劫击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2789.63
    成长 = 315.38
    CD = 4.4
    TP成长 = 0.1
    TP上限 = 7

class 绯红玫瑰技能5(主动技能):
    名称 = '致命回射'
    所在等级 = 30
    等级上限 = 1
    基础等级 = 1
    CD = 12.5

class 绯红玫瑰技能6(主动技能):
    名称 = '枪舞'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 212.00
    成长 = 24.00
    攻击次数 = 20
    基础2 = 377.30
    成长2 = 42.70
    攻击次数2 = 9
    CD = 17.6
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
         self.CD *= 0.9
         self.攻击次数 = 0
         self.攻击次数2 *= (2 * 1.39)

class 绯红玫瑰技能7(主动技能):
    名称 = '移动射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 11618.00
    成长 = 1312.00
    CD = 24.3
    TP成长 = 0.10
    TP上限 = 7

class 绯红玫瑰技能8(主动技能):
    名称 = '多重射击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7723.15
    成长 = 871.85
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
         self.倍率 *= 1.18

class 绯红玫瑰技能9(主动技能):
    名称 = '双鹰回旋'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 464.17
    成长 = 54.83
    基础2 = 474.00
    成长2 = 56.00
    基础3 = 502.58
    成长3 = 59.42
    攻击次数 = 14
    攻击次数2 = 18
    攻击次数3 = 32
    CD = 44.6
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.11 #colg百科
        #self.攻击次数 = 0
        #self.倍率 *= 1.3  不知道手枪静止状态时间占比 持续时间+30% 提升没这么大
        #self.倍率 /= 0.8

class 绯红玫瑰技能10(被动技能):
    名称 = '隐匿切割'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 绯红玫瑰技能11(主动技能):
    名称 = '血腥狂欢'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 38871.42
    成长 = 11779.22
    CD = 145

class 绯红玫瑰技能12(主动技能):
    名称 = '鲜血劫击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 5698.53
    成长 = 643.47
    基础2 = 6385.12
    成长2 = 720.88
    攻击次数 = 1
    攻击次数2 = 1
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.攻击次数 += 1.47
        self.攻击次数2 = 0
        self.倍率 *= 1.25

class 绯红玫瑰技能13(主动技能):
    名称 = '压制射击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 1254.33
    成长 = 141.67
    基础2 = 2789.17
    成长2 = 314.83
    攻击次数 = 20
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.攻击次数 *= 1.37
        self.攻击次数2 *= 1.50

class 绯红玫瑰技能14(被动技能):
    名称 = '枪刃改良'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 绯红玫瑰技能15(主动技能):
    名称 = '死亡锁链'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    基础 = 29878.17
    成长 = 5667.83
    CD = 40.0

class 绯红玫瑰技能16(主动技能):
    名称 = '锁链切割'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 36301.00
    成长 = 4099.00
    CD = 45.0

class 绯红玫瑰技能17(主动技能):
    名称 = '血舞祭'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 82497.00
    成长 = 24905.00
    CD = 180

class 绯红玫瑰技能18(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 绯红玫瑰技能19(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 绯红玫瑰技能20(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

绯红玫瑰技能列表 = []
i = 0
while i >= 0:
    try:
        exec('绯红玫瑰技能列表.append(绯红玫瑰技能'+str(i)+'())')
        i += 1
    except:
        i = -1

绯红玫瑰技能序号 = dict()
for i in range(len(绯红玫瑰技能列表)):
    绯红玫瑰技能序号[绯红玫瑰技能列表[i].名称] = i

绯红玫瑰一觉序号 = 0
绯红玫瑰二觉序号 = 0
绯红玫瑰三觉序号 = 0
for i in 绯红玫瑰技能列表:
    if i.所在等级 == 50:
        绯红玫瑰一觉序号 = 绯红玫瑰技能序号[i.名称]
    if i.所在等级 == 85:
        绯红玫瑰二觉序号 = 绯红玫瑰技能序号[i.名称]
    if i.所在等级 == 100:
        绯红玫瑰三觉序号 = 绯红玫瑰技能序号[i.名称]

绯红玫瑰护石选项 = ['无']
for i in 绯红玫瑰技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        绯红玫瑰护石选项.append(i.名称)

绯红玫瑰符文选项 = ['无']
for i in 绯红玫瑰技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        绯红玫瑰符文选项.append(i.名称)

class 绯红玫瑰角色属性(角色属性):

    职业名称 = '绯红玫瑰'

    武器选项 = ['左轮枪']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['物理百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.25
   
    #基础属性(含唤醒)
    基础力量 = 961.0
    基础智力 = 790.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
  
    def __init__(self):
        self.技能栏= copy.deepcopy(绯红玫瑰技能列表)
        self.技能序号= copy.deepcopy(绯红玫瑰技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['致命回射']].基础 = self.技能栏[self.技能序号['致命射击']].等效百分比(self.武器类型)*1.25
        self.技能栏[self.技能序号['致命回射']].被动倍率 = self.技能栏[self.技能序号['致命射击']].被动倍率

class 绯红玫瑰(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 绯红玫瑰角色属性()
        self.角色属性A = 绯红玫瑰角色属性()
        self.角色属性B = 绯红玫瑰角色属性()
        self.一觉序号 = 绯红玫瑰一觉序号
        self.二觉序号 = 绯红玫瑰二觉序号
        self.三觉序号 = 绯红玫瑰三觉序号
        self.护石选项 = copy.deepcopy(绯红玫瑰护石选项)
        self.符文选项 = copy.deepcopy(绯红玫瑰符文选项)
