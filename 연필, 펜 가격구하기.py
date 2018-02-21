num_pencil = int(input("구입하려는 연필의 개수를 적어주세요 :"))
num_pen = int(input("구입하려는 펜의 개수를 적어주세요 :"))
total_price = 3000*num_pencil + 4000*num_pen
discount_price = 0.7*total_price
print("총 가격은 %s 입니다." %(discount_price))
