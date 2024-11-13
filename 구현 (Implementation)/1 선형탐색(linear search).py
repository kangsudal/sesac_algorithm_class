gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

#   1등급 광물 찾기 : 리스에서 데이터가 존재하는지 여부를 확인하는 로직
# for gem in gems:
#     if gem == 1:
#         print("찾았다!")
#         break
# else:
#     print("없다") #for 반복문이 제대로 완주되면 보상으로 이 구문이 실행됨

for idx in range(len(gems)):
    if gems[idx] == 1:
        print('찾았다!')
        break
else:
    print('없다!')


