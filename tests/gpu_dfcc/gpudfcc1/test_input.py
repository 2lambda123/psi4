from addons import *


@uusing("gpu_dfcc")
@ctest_labeler("")
def test_gpu_dfcc_gpudfcc1():
    ctest_runner(__file__)
