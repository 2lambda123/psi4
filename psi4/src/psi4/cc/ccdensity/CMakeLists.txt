target_sources(cc
  PRIVATE
    #${CMAKE_CURRENT_SOURCE_DIR}/G_norm.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/add_core_UHF.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/resort_gamma.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/resort_tei.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/G.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gabcd.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gciab.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gibja.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gijab.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gijab_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gijab_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gijab_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gijka.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Gijkl.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Iab.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Iai.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Iia.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/Iij.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/V.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/V_cc2.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/add_core_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/add_ref_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/add_ref_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/add_ref_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_A.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_A_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_A_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_A_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_X.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_Z.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_Z_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_Z_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_Z_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/build_ex_tdensity.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/cache.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ccdensity.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/classify.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/deanti.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/deanti_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/deanti_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/deanti_UHF.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/distribute.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/dump_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/dump_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/dump_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/energy.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/energy_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/energy_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/energy_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_oscillator_strength.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_rotational_strength.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_sort_td_rohf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_sort_td_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_td_cleanup.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_td_print.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_td_setup.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_tdensity.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ex_tdensity_intermediates.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/file_build.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/fold.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/fold_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/fold_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/fold_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/get_frozen.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/get_moinfo.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/get_params.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/get_rho_params.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/get_td_params.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/idx_error.cc
    #${CMAKE_CURRENT_SOURCE_DIR}/idx_permute.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/kinetic.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/lag.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ltdensity.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/ltdensity_intermediates.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/norm.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/onepdm.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/oscillator_strength.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/relax_D.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/relax_I.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/relax_I_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/relax_I_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/relax_I_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/rotational_strength.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/rtdensity.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/setup_LR.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortI.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortI_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortI_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortI_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sort_ltd_rohf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sort_ltd_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sort_rtd_rohf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sort_rtd_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortone.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortone_RHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortone_ROHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/sortone_UHF.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/td_cleanup.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/td_print.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/td_setup.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/tdensity.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/transL.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/transdip.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/transp.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/twopdm.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/wfn_saver.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gabcd.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gciab.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gciab_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gibja.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gibja_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gijab.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gijab_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gijka.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gijka_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_Gijkl.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_V.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_oe_intermediates.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_oe_intermediates_rhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_onepdm.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_onepdm_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_te_intermediates.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_te_intermediates_rhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi1.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi1_connected.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi1_rhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi1_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi2.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi2_rhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi2_uhf.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi_check.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/x_xi_intermediates.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/zero_pdm.cc
  )
