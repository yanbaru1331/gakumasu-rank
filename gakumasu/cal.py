import math

def convTest(convScore: int):
    # ~5000
    score = 0
    temp = convScore - 1500
    if(temp <= 0):
        return int(convScore / 0.3)
    
    score = 5000
    
    # 5000~10000
    temp = temp - 750
    if(temp <= 0):
        return int(((convScore- 1500) / 0.15) + score)
    score += 5000
    
    # 10000~20000
    temp = temp - 800
    if(temp <= 0):
        return int(((convScore - 2250) / 0.08) + score)
    score += 10000
    
    # 20000~30000
    temp = temp - 400
    if(temp <= 0):
        return int(((convScore - 3050) / 0.04) + score)
    score += 10000
    
    # 30000~40000
    temp = temp - 200
    if(temp <= 0):
        return int(((convScore- 3250) / 0.02) + score)
    score += 10000
    
    # 40000~
    return int(((convScore- 3450) / 0.01) + score)

def rankCal(rank: int, vo: int, da: int, vi: int):
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

        case _:
            req = 0

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
# 1位であることを前提として計算
    convScore = req - (1700 + status)
    if(convScore <= 0):
        return 0
    return convTest(convScore)

