"""
1. 딜러가 카드를 한 장 뽑아 플레이어에게 준다.
2. 딜러가 카드를 한 장 뽑아 딜러 앞에 뒤집어 놓는다.
3. 딜러가 카드를 한 장 뽑아 플레이어에게 준다.
4. 딜러가 카드를 한 장 뽑아 딜러 앞에 보이도록 놓는다.
5. 플레이어에게 카드를 더 받을지 말지 물어본다.
    5.1 플레이어가 최초로 받은 카드 두 장의 합이 21인 경우에는 더 이상 카드를 받지 않고,
        딜러의 카드를 확인하여 승패를 결정한다.
    5.2 플레이어가 받은 모든 카드의 합이 21보다 작으면 계속해서 한 장씩 더 받을 수 있다.
    5.3 플레이어가 받은 모든 카드의 합이 21을 넘어가면 플레이어가 즉시 게임에서 진다.
6. 플레이어가 더이상 카드를 받지 않으면 딜러 앞의 뒤집어놓은 카드를 공개한 후,
   딜러의 카드 합이 17 이상이 될 때까지 계속해서 딜러가 카드를 한 장씩 받는다.
    6.1 딜러가 받은 모든 카드의 합이 21을 넘으면 딜러가 즉시 게임에서 진다.
    6.2 이때 딜러는 플레이어가 가진 카드의 합을 고려하지 않으며, 딜러가 가진 카드의 합이 17 이상이 되면 받기를 중단한다.
7. 승패를 가린다. 카드 합이 21에 더 가까운 사람이 이기며, 카드 합이 서로 같으면 비긴다.

플레이어의 전략
1. 딜러의 보이는 카드가 1이거나 7 이상인 경우, 플레이어는 카드 합이 17 이상이 될 때까지 받는다.
2. 딜러의 보이는 카드가 4, 5, 6인 경우, 플레이어는 카드를 받지 않는다.
3. 딜러의 보이는 카드가 2, 3인 경우, 플레이어는 카드 합이 12 이상이 될 때까지 받는다.

블랙잭 (10, 1) -> 3원
비김 : 잃지 않음
패배 : -2원
승리 : 2원
0에서 시작, 음수가 될 수 있다.
카드를 뽑을 수 없는 경우: 무효하고 종료
"""


def solution(cards):
    answer = -1

    for c in cards:
        if c > 10:
            c = 10

    player = [cards[0], cards[2]]
    dealer = [cards[1], cards[3]]
    cards = cards[:4]

    flag = 0
    dealer_front = dealer[-1]
    player_get_or_not = True
    if dealer_front == 1 or dealer_front > 6:
        flag = 1
        # 1. 딜러의 보이는 카드가 1이거나 7 이상인 경우, 플레이어는 카드 합이 17 이상이 될 때까지 받는다.
    elif dealer_front in (4, 5, 6):
        flag = 2
        player_get_or_not = False
        # 2. 딜러의 보이는 카드가 4, 5, 6인 경우, 플레이어는 카드를 받지 않는다.
    elif dealer_front in (2, 3):
        flag = 3
        # 3. 딜러의 보이는 카드가 2, 3인 경우, 플레이어는 카드 합이 12 이상이 될 때까지 받는다.

    a, b = player
    if a == 1 or b == 1 and a + b == 11:
        return

    if flag == 3:
        if a == 1 and b == 1:
            player_get_or_not = False
        elif a + b > 11:
            player_get_or_not = False
        elif a == 1 or b == 1:
            if a + b + 9 > 11:
                player_get_or_not = False


    while cards:
        if player_get_or_not:
            player.append(cards.pop(0))



    return answer



cards = [12, 7, 11, 6, 2, 12]
# cards = [1, 4, 10, 6, 9, 1, 8, 13]
# cards = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
# cards = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
solution(cards)