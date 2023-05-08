# from django.test import TestCase
# from unittest.mock import patch
#
# class MyTestCase(TestCase):
#     @classmethod # remove this to make before each method
#     def setUpClass(cls):
#         # Code to be run once before all test methods
#         cls.my_class_object = MyClass()
#
#     @classmethod
#     def tearDownClass(cls):
#         # Code to be run once after all test methods
#         cls.my_class_object.cleanup()
#
#     def test_my_function(self):
#         # test code here
#         return
#
#     # this is how to mock objects
#     @patch('myapp.mymodule.MyClass')
#     def test_my_function(MockClass):
#         MockClass.return_value.my_method.return_value = 'mocked result'
#         instance = MockClass()
#         assert instance.my_method() == 'mocked result'
