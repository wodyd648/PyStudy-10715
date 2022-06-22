flavor = float(input("이 음식의 맛 점수는?"))
price = float(input("이 음식의 가격은? (단위 : 만원)"))
score = flavor/price


if score >= 30:
    print("5 스타")
elif score >= 10:
    print("4 스타")
elif score >= 6:
    print("3 스타")
elif score >= 2:
    print("2 스타")
elif score < 2:
    print("1 스타")

