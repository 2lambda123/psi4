from addons import *


@ctest_labeler("quick;smoke")
def test_psi4numpy_rhf_hessian():
    ctest_runner(__file__)
