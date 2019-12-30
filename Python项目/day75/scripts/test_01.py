# import pytest
#
# @pytest.mark.skip()
# def test_func():
#     assert 0
# def test_func1():
#     assert 0
#
# @pytest.mark.skipif(condition=0,reason='666')
# class TestCase:
#
#     def test_1(self):
#         assert 1
#
#     def test_2(self):
#         assert 0
#
#     def test3(self):
#         assert 0
# # if __name__ == '__main__':
# #     pytest.main(['-s','py_test.py'])
#
import pytest


class TestCase(object):

    @pytest.mark.xfail(1 < 2, reason='预期失败， 执行失败')
    def test_case_01(self):
        """ 预期失败， 执行也是失败的 """
        print('预期失败， 执行失败')
        assert 0

    @pytest.mark.xfail(1 < 2, reason='预期失败， 执行成功')
    def test_case_02(self):
        """ 预期失败， 但实际执行结果却成功了 """
        print('预期失败， 执行成功')
        assert 1