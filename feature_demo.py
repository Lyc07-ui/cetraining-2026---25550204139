def calculate_average(numbers):
    """通过循环计算列表的平均值"""
    if not numbers:  # 处理空列表的情况
        return 0
    
    total = 0
    for num in numbers:
        total += num  # 累加列表中的每个数字
        
    return total / len(numbers)

# 测试代码
my_list = [15, 25, 35]
print(f"平均值是: {calculate_average(my_list)}")  # 输出: 平均值是: 25.0