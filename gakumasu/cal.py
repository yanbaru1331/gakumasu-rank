import math

def convTest(convScore: int):
    # ~5000
    score = 0
    temp = convScore - 1500
    if(temp <= 0):
        return math.ceil(convScore / 0.3)
    
    score = 5000
    
    # 5000~10000
    temp = temp - 750
    if(temp <= 0):
        return math.ceil(((convScore- 1500) / 0.15) + score)
    score += 5000
    
    # 10000~20000
    temp = temp - 800
    if(temp <= 0):
        return math.ceil(((convScore - 2250) / 0.08) + score)
    score += 10000
    
    # 20000~30000
    temp = temp - 400
    if(temp <= 0):
        return math.ceil(((convScore - 3050) / 0.04) + score)
    score += 10000
    
    # 30000~40000
    temp = temp - 200
    if(temp <= 0):
        return math.ceil(((convScore- 3450) / 0.02) + score)
    score += 10000
    
    # 40000~
    return math.ceil(((convScore- 3650) / 0.01) + score)

 
def rankCal(vo: int, da: int, vi: int, rank: int, precedence: int):
# ランク区分認識処理
    match rank:
        case 1:
            # S
            req = 13000
        case 2:
            # A+
            req = 11500
        case 3:
            # A
            req = 10000
        case 4:
            # B+
            req = 8000
        case 5:
            # B
            req = 6000
        case 6:
            req = 14500

        case _:
            req = 0
    
    match  precedence:
        case 1:
            basepoint = 1700
        case 2:
            basepoint = 900
        case 3:
            basepoint = 500
        case _:
            basepoint = 0
            
# 育成終了後VoDaVi合計*2.3
    vo += 30
    da += 30
    vi += 30
    if(vo > 1500):
        vo = 1500
    if(da > 1500):
        da = 1500
    if(vi > 1500):
        vi = 1500
    status = math.ceil((vo + da + vi) * 2.3)

    convScore = req - (basepoint + status)
    if(convScore <= 0):
        return 0
    return convTest(convScore)


def reverseCal(vo: int ,da: int,vi: int, score: int):
    vo -= 30
    da -= 30
    vi -= 30
    status = math.ceil((vo + da + vi) * 2.3)
    # 突貫で作るけど、多分ここに1500のときの処理が必要
    temp  = []
    for i in (1700, 900, 500, 0):
        
        temp.append(convTest(score - (i+status)))

    
    return temp
print(rankCal(1111,1111,1111, 6, 1))
