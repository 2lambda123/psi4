if(${ENABLE_dkh})
    find_package(dkh 1.2 CONFIG QUIET)

    if(${dkh_FOUND})
        get_property(_loc TARGET dkh::dkh PROPERTY LOCATION)
        message(STATUS "${Cyan}Found dkh${ColourReset}: ${_loc} (found version ${dkh_VERSION})")
        add_library(dkh_external INTERFACE)  # dummy
    else()
        if(${CMAKE_INSIST_FIND_PACKAGE_dkh})
            message(FATAL_ERROR "Suitable dkh could not be externally located as user insists")
        endif()

        include(ExternalProject)
        message(STATUS "Suitable dkh could not be located, ${Magenta}Building dkh${ColourReset} instead.")
        ExternalProject_Add(dkh_external
            URL https://github.com/psi4/dkh/archive/v1.2.tar.gz
            UPDATE_COMMAND ""
            CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${STAGED_INSTALL_PREFIX}
                       -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
                       -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
                       -DCMAKE_Fortran_COMPILER=${CMAKE_Fortran_COMPILER}
                       -DCMAKE_INSTALL_LIBDIR=${CMAKE_INSTALL_LIBDIR}
                       -DCMAKE_INSTALL_INCLUDEDIR=${CMAKE_INSTALL_INCLUDEDIR}
                       -DBUILD_SHARED_LIBS=${BUILD_SHARED_LIBS}
                       -DENABLE_OPENMP=${ENABLE_OPENMP}  # relevant for thread safety
                       -DENABLE_XHOST=${ENABLE_XHOST}
                       -DBUILD_FPIC=${BUILD_FPIC}
                       -DENABLE_GENERIC=${ENABLE_GENERIC}
                       -DLIBC_INTERJECT=${LIBC_INTERJECT}
                       -DCMAKE_OSX_DEPLOYMENT_TARGET=${CMAKE_OSX_DEPLOYMENT_TARGET}
                       -DCMAKE_OSX_SYSROOT=${CMAKE_OSX_SYSROOT}
            CMAKE_CACHE_ARGS -DCMAKE_Fortran_FLAGS:STRING=${CMAKE_Fortran_FLAGS}
                             -DCMAKE_C_FLAGS:STRING=${CMAKE_C_FLAGS})

        set(dkh_DIR ${STAGED_INSTALL_PREFIX}/share/cmake/dkh CACHE PATH "path to internally built dkhConfig.cmake" FORCE)
    endif()
else()
    add_library(dkh_external INTERFACE)  # dummy
endif()

