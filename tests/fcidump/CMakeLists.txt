include(TestingMacros)

file(COPY Ne.6311G.INTDUMP.ref DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY Ne.C1.6311G.INTDUMP.ref DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY Ne.cc-pVDZ.UHF.INTDUMP.ref DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY Ne.C1.cc-pVDZ.UHF.INTDUMP.ref DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY Ne.6311G.frozen.INTDUMP.ref DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
add_regression_test(fcidump "psi;quicktests;smoketests;fcidump;noc1")
