import cards_tools
#无线循环，由用户主动决定什么售后退出循环
while True:

    #显示功能菜单
    cards_tools.show_menu()


    action_str=input("请选择希望之星的操作：")
    print("您选择的操作是【%s】" % action_str)

    #1,2,3针对名片的操作
    if action_str in ["1","2","3"]:#使用in针对列表判断，避免使用or拼接复杂的逻辑条件
        #新增名片
        if action_str=="1":
            cards_tools.new_card()
        #显示全部
        elif action_str == "2":
            cards_tools.show_all()
        #查询名片
        elif action_str == "3":
            cards_tools.search_card()

    #0 退出系统
    elif action_str=="0":
        print("欢迎再次使用【名片管理系统】")
        break


#其他内容贴输入错误，需要提示用户
else:
    print("您输入的不正确，情重新选择")