from .counting_sort import CountingSortByKey


class RadixSort(object):
    """基数排序的实现
    """

    def __init__(self, list_):
        self._list = [{'number': x} for x in list_]

    def sort(self, d):
        """按每个元素是 d 位的进行排序

        :param d: 十进制的最大位数
        :return: 排好序的列表
        """
        ret_list = self._list
        for i in range(1, d + 1):
            tmp_list = [
                {
                    'number': m['number'],
                    'key': self.__get_index_number(m['number'], i)
                }
                for m in ret_list
            ]
            cs = CountingSortByKey(tmp_list, 'key')
            ret_list = cs.sort()

        return [m['number'] for m in ret_list]

    @staticmethod
    def __get_index_number(n, i):
        """获得一个十进制数的第 i 位的数字，从个位开始，没有这一位则返回 0"""
        s = str(n)
        return int(s[-i]) if len(s) >= i else 0
