if(${ENABLE_gpu_dfcc})
    find_package(gpu_dfcc 0.2 CONFIG QUIET)  # TODO change when final
    if(${gpu_dfcc_FOUND})
        get_property(_loc TARGET gpu_dfcc::gpu_dfcc PROPERTY LOCATION)
        message(STATUS "${Cyan}Found gpu_dfcc${ColourReset}: ${_loc} (found version ${gpu_dfcc_VERSION})")
        add_library(gpu_dfcc_external INTERFACE)  # dummy

    else()
        if(${CMAKE_INSIST_FIND_PACKAGE_gpu_dfcc})
            message(FATAL_ERROR "Suitable gpu_dfcc could not be externally located as user insists")
        endif()

        include(ExternalProject)
        message(STATUS "Suitable gpu_dfcc could not be located, ${Magenta}Building gpu_dfcc${ColourReset} instead.")

        ExternalProject_Add(gpu_dfcc_external
            DEPENDS psi4-core
            GIT_REPOSITORY https://github.com/edeprince3/gpu_dfcc
            GIT_TAG fd1dd94  # v0.2 + 2  # TODO change when final
            UPDATE_COMMAND ""
            CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
                       -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
                       -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
                       -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
                       -DCMAKE_CUDA_COMPILER=${CMAKE_CUDA_COMPILER}
                       -DCUDA_TOOLKIT_ROOT_DIR=${CUDA_TOOLKIT_ROOT_DIR}
                       -DCMAKE_INSTALL_LIBDIR=${CMAKE_INSTALL_LIBDIR}
                       -DPYMOD_INSTALL_LIBDIR=${PYMOD_INSTALL_LIBDIR}
                       -DENABLE_XHOST=${ENABLE_XHOST}
                       -DENABLE_GENERIC=${ENABLE_GENERIC}
                       -Dpsi4_DIR=${STAGED_INSTALL_PREFIX}/share/cmake/psi4
                       -Dpybind11_DIR=${pybind11_DIR}
            CMAKE_CACHE_ARGS -DCMAKE_C_FLAGS:STRING=${CMAKE_C_FLAGS}
                             -DCMAKE_CXX_FLAGS:STRING=${CMAKE_CXX_FLAGS}
                             -DCMAKE_CUDA_FLAGS:STRING=${CMAKE_CUDA_FLAGS}
            INSTALL_COMMAND DESTDIR=${CMAKE_BINARY_DIR}/stage ${CMAKE_MAKE_PROGRAM} install)

        set(gpu_dfcc_DIR ${STAGED_INSTALL_PREFIX}/share/cmake/gpu_dfcc CACHE PATH "path to internally built gpu_dfccConfig.cmake" FORCE)
    endif()
else()
    add_library(gpu_dfcc_external INTERFACE)  # dummy
endif()

