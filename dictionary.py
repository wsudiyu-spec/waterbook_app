# 定义水族水书符号字典
symbol_dict = { 
    "01":"引贯", "02":"空蒙", "03":"大腻", "04":"尖辛", "05":"各木", 
    "06":"代哇", "07":"大更", "08":"计饿", "09":"半用", "10":"代排", 
    "11":"九火", "12":"休四", "13":"沙朋", "14":"八平", "15":"十平", 
    "16":"杀师铜", "17":"杀伤", "18":"地转", "19":"姑秀", "20":"忌方宿", 
    "21":"九星", "22":"壬辰", "23":"公溶", "24":"吉方", "25":"大旺方", 
    "26":"大利方", "27":"吉立", "28":"抽条", "29":"设金堂", "30":"富癸"
}

def main():
    print("=== 水族水书符号检索系统 ===")
    print("使用说明：")
    print("1. 输入编号(01-30)可查询对应符号名称")
    print("2. 输入单个汉字可搜索包含该字的所有符号")
    print("3. 输入 q 可退出程序\n")
    
    while True:
        # 接收用户输入并去除首尾空格
        user_input = input("请输入检索内容（编号/关键词/q退出):").strip()
        
        # 安全退出逻辑：输入q（不区分大小写）则退出
        if user_input.lower() == 'q':
            print("程序已退出，感谢使用！")
            break
        
        # 空输入处理（去空格后为空）
        if not user_input:
            print("输入不能为空，请重新输入！")
            continue
        
        # 编号检索逻辑：判断输入是否为有效编号
        if user_input in symbol_dict:
            print(f"编号 {user_input} 对应的符号：{symbol_dict[user_input]}")
        else:
            # 关键词搜索逻辑：输入不是编号则按单个汉字搜索
            # 先判断是否为单个汉字（避免多字输入干扰）
            if len(user_input) == 1 and user_input.isalpha() and '\u4e00' <= user_input <= '\u9fff':
                # 遍历字典，收集包含该汉字的符号
                matched = []
                for num, name in symbol_dict.items():
                    if user_input in name:
                        matched.append(f"编号 {num}:{name}")
                
                if matched:
                    print("搜索结果（包含该字的符号）：")
                    for item in matched:
                        print(f"  {item}")
                else:
                    print("未找到包含该字的符号！")
            else:
                # 既不是编号、也不是单个汉字、也不是q，提示查无此号
                print("查无此号！")

if __name__ == "__main__":
    main()
