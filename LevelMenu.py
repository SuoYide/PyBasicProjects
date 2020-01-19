menu = {
    '北京': {
        '朝阳': {
            '国贸': {},
            'CICC': {},
            'HP': {},
            'ATCC': {},
            'CCTV': {},
        },
        '望京': {
            '陌陌': {},
            '奔驰': {},
            '360': {},
        },
        '三里屯': {
            '优衣库': {},
            'apple': {},
        },
        '昌平': {
            '沙河': {
                '佰盛': {},
                '华润医药': {},
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {},
            },
            '回龙观': {},
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                'sohu': {},
                '快手': {},
            },
            '中关村': {
                'youku': {},
                'Iqiyi': {},
                '汽车之家': {},
                '新东方': {},
                'QQ': {},
            },

        },
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                'CICC': {},
                '高盛': {},
                '摩根': {},
            },
        },
        '闵行': {},
        '静安': {},
    },
    '山东': {
        '济南': {},
        '德州': {
            '乐陵': {
                '丁务镇': {},
                '城区': {},
            },
            '平原': {},
        },
        '青岛': {},
    },
}

back_flag = False
exit_flag = Flase
# 循环第一层
while not back_flag and not exit_flag:
    for k in menu:
        print(k)
    choice = input("1>>>:").strip()
    if choice in menu:
        # 停留第二层
        while not back_flag and not exit_flag:
            for k2 in menu[choice]:
                print(k2)
            choice2 = input("2>>:").strip()
            if choice2 in menu[choice]:
                # 停留第三层
                while not back_flag and not exit_falg:
                    for k3 in menu[choice][choice2]:
                        print(k3)
                    choice3 = input("3>>:").strip()
                    if choice3 in menu[choice][choice2]:
                        while not back_flag and not exit_falg:
                            for k4 in menu[choice][choice2][choice3]:
                                print(k4)
                            choice4 = input("这是最后一层，输入(B/b)返回上一级:")
                            if choice4 == 'B' or choice4 == 'b':
                                back_falg = True
                            elif choice4 == q:
                                exit_falg = True
                        else:
                            back_flag = True
                    if choice3 == 'B' or choice3 == 'b':
                        back_flag = True
                    elif choice3 == 'q':
                        exit_flag = True
                else:
                    back_flag = False
            if choice2 == 'B' or choice2 == 'b':
                back_flag = True
            elif choice2 == 'q':
                exit_flag = True
        else:
            back_flag = False
    if choice == 'b' == choice == 'B':
        back_flag = True
    elif choice == 'q':
        exit_flag = True
                                 
                                
                        
                    
