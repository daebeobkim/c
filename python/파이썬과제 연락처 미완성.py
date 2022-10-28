a = []


count=0

while True:
    per = input('메뉴를 입력하시오')
    if per == 'quit':
            break
    while True:
        if per == 'add':
            count += 1
            a.append([input(str('이름을 입력하시오')),input('전화번호를 입력하시오'),input('메일을 입력하시오'),input('주소를 입력하시오')])
            break
        if per == 'all':
            a.sort()
            break
        if per == 'search':
            name = input('이름입력시 정보 출력')
            for i in range(count):
                if name == a[i][0]:
                    print('%s' %(a[i]))
            break
        if per == 'change':
            name = input('정보를 수정하고싶은 사용자의 이름을 입력하시오')
            for i in range(count):
                if name == a[i][0]:
                    del a[i]
                    a.append([input('이름을 입력하시오'),input('전화번호를 입력하시오'),input('메일을 입력하시오'),input('주소를 입력하시오')])
            break
        if per == 'delete':
            name = input('전화번호를 삭제 할 사용자의 이름을 입력하시오')
            for i in range(count):
                if name == a[i][0]:
                    a[i][1] = ("삭제된 전화번호")
            if name != a[i][0]:
                    print('해당 이름이 없습니다')
            break
        if per == 'a':
            for i in range(1):
                print('%s' %a)
            break
        if per == 'quit':
            break
        else:
            print("메뉴를 다시 선택하시오")
            break
        break
           

