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
                '老男孩': {},
                '阿泰包子': {},
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

# 记录当前层，实现动态循环
current_layer = menu
# 定义一个用来记录父级的列表，最后一个元素永远都是父级
parent_layers = []
while True:
	for k in parent_layer:
		print(k)
	choice = input(">>>:").strip()
	if len(choice) == 0:
		continue
	if choice in current_layer:
		# 在进入下一层之前，将此层记录为父级
		parent_layers.append(current_layer)
		# 将当前层改为子集
		current_layer = current_layer[choice]
	# 当用户选择b时就可以直接取列表的最后一个值就ok了
	elif choice == 'b':
		if parent_layers:
			# 取出列表的最后一个值，因为他就是当前层的父级
			current_layer = parent_layers.pop()
	else:
		print("无此项！")
