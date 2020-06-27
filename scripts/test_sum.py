import pytest
from Base.get_yaml import GetData


def sum_data():
    # 空列表 存储测试数据
    sum_list = []
    # 引用GetData类
    data = GetData.get_yaml_data("data.yml")
    print("data:", data)
    # print("values:",data.values()) # 返回列表 存储所有value
    for i in data.values():
        # print("tup:", (i.get("a"), i.get("b"), i.get("c")))
        # 添加元组数据到列表
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
    return sum_list


class TestSum:
    @pytest.mark.parametrize("a,b,c", sum_data())
    def test_sum(self, a, b, c):
        """判断两个数之和 等于 第三个数"""
        print("\n{}+{}={}".format(a, b, c))
        assert a + b == c
