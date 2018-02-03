__author__ = 'Chennareddy'


import unittest
import HTMLTestRunner
import os
from getAPI_test import GetAPI_test
from postAPI_test import PostAPI_test

dir = os.getcwd()
tests1 = unittest.TestLoader().loadTestsFromTestCase(GetAPI_test)
tests2 = unittest.TestLoader().loadTestsFromTestCase(PostAPI_test)


all_tests = unittest.TestSuite([tests1,tests2])

outfile = open(dir+"/Reports/API_TestReport.html", "w")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                                       verbosity=1,
                                       title="Handstand API Automation Test Report",
                                       description="Test Automation Report")
runner.run(all_tests)
#unittest.TextTestRunner(verbosity=2).run(all_tests)
