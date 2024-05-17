def check_bingo(card, S):
    # 横、縦のラインをチェック
    for i in range(S):
        if all(cell == 0 for cell in card[i]) or all(card[j][i] == 0 for j in range(S)):
            return True
    # 斜めのラインをチェック
    if all(card[i][i] == 0 for i in range(S)) or all(card[i][S-1-i] == 0 for i in range(S)):
        return True
    return False

# ビンゴカードのサイズ
S = int(input())

# ビンゴカードの単語
card = [input().split() for _ in range(S)]

# 選ばれた単語の数
N = int(input())

# 選ばれた単語
bingo = [input() for _ in range(N)]

# ビンゴカードの単語と選択された単語が同じ場合、対応する位置を0にする
for i in range(S):
    for j in range(S):
        if card[i][j] in bingo:
            card[i][j] = 0
        else:
            card[i][j] = 1  # ビンゴに選ばれていない単語を1にする

if check_bingo(card, S):
    print("yes")
else:
    print("no")
