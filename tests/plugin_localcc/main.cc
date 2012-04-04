#include<libplugin/plugin.h>

#include "ccsd.h" 
#include "../plugin_libcim/cim.h"

INIT_PLUGIN

namespace psi{
  void RunCoupledCluster(Options &options,boost::shared_ptr<psi::CIM> wfn);
};

namespace psi{ namespace plugin_localcc{
extern "C" int 
read_options(std::string name, Options &options)
{
  if (name == "PLUGIN_LOCALCC"|| options.read_globals()) {
     /*- Convergence for the localization procedure-*/
     options.add_double("BOYS_CONVERGENCE", 1.0e-6);
     /*- Maximum number of localization iterations iterations -*/
     options.add_int("BOYS_MAXITER", 100);
     /*- Convergence for the CC amplitudes-*/
     options.add_double("R_CONVERGENCE", 1.0e-7);
     /*- Maximum number of CC iterations -*/
     options.add_int("MAXITER", 50);
     /*- Desired number of DIIS vectors -*/
     options.add_int("DIIS_MAX_VECS", 8);
     /*- For GPU code, cap the amount of memory registerred with the GPU -*/
     options.add_int("MAX_MAPPED_MEMORY", 1000);
     /*- Compute triples contribution? -*/
     options.add_bool("COMPUTE_TRIPLES", true);
     /*- Use MP2 NOs to truncate virtual space for (T)? -*/
     options.add_bool("TRIPLES_USE_NOS", false);
     /*- Cutoff for occupation of MP2 NO orbitals in (T) -*/
     options.add_double("VIRTUAL_CUTOFF", 1.0e-6);
     /*- Desired number of threads. This will override OMP_NUM_THREADS in (T) -*/
     options.add_int("NUM_THREADS", 1);
     /*- Do SCS-MP2? -*/
     options.add_bool("SCS_MP2", false);
     /*- Do SCS-CCSD? -*/
     options.add_bool("SCS_CCSD", false);
     /*- Opposite-spin scaling factor for SCS-MP2 -*/
     options.add_double("MP2_SCALE_OS",1.20);
     /*- Same-spin scaling factor for SCS-MP2 -*/
     options.add_double("MP2_SCALE_SS",1.0/3.0);
     /*- Oppposite-spin scaling factor for SCS-CCSD -*/
     options.add_double("CC_SCALE_OS", 1.27);
     /*- Same-spin scaling factor for SCS-CCSD -*/
     options.add_double("CC_SCALE_SS",1.13);
  }
  return true;
}

extern "C" PsiReturnType
plugin_localcc(Options &options)
{ 
  //boost::shared_ptr<psi::CIM>  wfn =  Process::environment.reference_wavefunction();
  boost::shared_ptr<psi::CIM> wfn(new CIM());
  boost::shared_ptr<psi::Wavefunction> ref = Process::environment.reference_wavefunction();
  wfn->copy(ref);
  RunCoupledCluster(options,wfn);
  return  Success;
} // end plugin_localcc


}} // end namespace psi
