from addons import *


@ctest_labeler("dft;scf")
def test_dft_grad_lr1():
    ctest_runner(__file__)
