from addons import *


@ctest_labeler("quick;casscf;noc1")
def test_dfcasscf_sp():
    ctest_runner(__file__)
