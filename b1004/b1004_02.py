import random

# 10번도전에서
# 입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다.
# 10번 도전에서 맞추지 못하면 , 10번도전에 실패했습니다. 랜덤숫자 : 10
# 도전에 성공했습니다. 랜덤숫자 : 10

def number_guessing_game():
    # 랜덤 숫자 생성 (1-100)
    random_number = random.randint(1, 100)

    # 10번 도전
    for attempt in range(1, 11):
        guess = int(input(f"도전 {attempt}: 숫자를 입력하세요 (1-100): "))

        if guess > random_number:
            print(f"작은 수를 입력하셔야 합니다.")
        elif guess < random_number:
            print(f"큰 수를 입력하셔야 합니다.")
        else:
            print(f"도전에 성공했습니다! 랜덤 숫자: {random_number}")
            break
    else:
        print(f"10번 도전에 실패했습니다. 랜덤 숫자: {random_number}")

# 게임 실행
number_guessing_game()


