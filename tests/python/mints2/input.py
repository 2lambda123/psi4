#! A test of the basis specification.  A benzene atom is defined using a ZMatrix containing dummy atoms
#! and various basis sets are assigned to different atoms.  The symmetry of the molecule is automatically
#! lowered to account for the different basis sets.
import psi4

psi4.set_output_file("output.dat", False)

refnuc = 204.01995818061  #TEST
refscf = -228.95763005900784  #TEST

bz = psi4.geometry("""
    X
    X   1  RXX
    X   2  RXX  1  90.0
    C   3  RCC  2  90.0  1   0.0
    C   3  RCC  2  90.0  1  60.0
    C1  3  RCC  2  90.0  1 120.0
    C   3  RCC  2  90.0  1 180.0
    C1  3  RCC  2  90.0  1 240.0
    C   3  RCC  2  90.0  1 300.0  # unnecessary comment
    H1  3  RCH  2  90.0  1   0.0
    H   3  RCH  2  90.0  1  60.0
    H   3  RCH  2  90.0  1 120.0
    H1  3  RCH  2  90.0  1 180.0
    H   3  RCH  2  90.0  1 240.0
    H   3  RCH  2  90.0  1 300.0

    RCC  = 1.3915
    RCH  = 2.4715
    RXX  = 1.00
""")

# Here we specify some of the basis sets manually.  They could be written to one or more external
# files and included by adding the directory to environment variable PSIPATH
#
# The format of these external files follows the same format as those below, where there's a [name]
# tag before the standard G94 basis set specification:

# [DZ]
# spherical
# ****
# H     0
# S   3   1.00
#      19.2406000              0.0328280
#       2.8992000              0.2312080
#       0.6534000              0.8172380
# S   1   1.00
#       0.1776000              1.0000000
# ****
# C     0
# definition of carbon atom DZ basis...
# ****
# Any more atoms needed...
# ****

# The keywords cartesian or spherical are optional and provide default behavior if the
# puream keyword is not set. In basis strings, like below, multiple basis sets can appear, as long
# as there is a [name] tag above the definition of each basis set. The basis sets specified
# using either basis <opt_name> {...} are utilized first (in the order specified
# in the input file). Any remaining basis sets required are extracted from the built-in library,
# if they exist, or an error message is printed.
psi4.basis_helper("""
#
# We start by assigning basis sets to atoms.  These commands can go anywhere in the basis block
#
   # First, assign DZ to all atoms
   assign DZ
   # Now, assign 3-21G to all carbon atoms
   assign C my3-21G
   # The two atoms labelled H1 get a STO-3G basis two
   assign H1 sto-3g
   # Carbons 3 and 5 get a STO-3G basis, too
   assign C1 sto-3g
   # With all these in place, the symmetry is lowered to C2v automatically
   # The commands are applied in order i.e., adding a line like
   # assign cc-pvtz
   # here would override all of the above and assign cc-pvtz to all atoms

#
# Now we define the basis sets.  N.B. Indentation does not matter; it just looks prettier.
#
    [my3-21G] #This is really the standard 3-21G basis, but with a different name
    cartesian
    ****
    H     0
    S   2   1.00
          5.4471780              0.1562850
          0.8245470              0.9046910
    S   1   1.00
          0.1831920              1.0000000
    ****
    C     0
    S   3   1.00
        172.2560000              0.0617669
         25.9109000              0.3587940
          5.5333500              0.7007130
    SP   2   1.00
          3.6649800             -0.3958970              0.2364600
          0.7705450              1.2158400              0.8606190
    SP   1   1.00
          0.1958570              1.0000000              1.0000000
    ****
    [DZ]
    spherical
    ****
    H     0 
    S   3   1.00
         19.2406000              0.0328280        
          2.8992000              0.2312080        
          0.6534000              0.8172380        
    S   1   1.00
          0.1776000              1.0000000        
    ****
""")

psi4.set_options({'d_convergence': 11, 'e_convergence': 11, 'scf_type': 'pk'})

scfenergy = psi4.energy('scf')

psi4.compare_strings("c2v", bz.schoenflies_symbol(), "Point group")  #TEST
psi4.compare_values(refnuc, bz.nuclear_repulsion_energy(), 10, "Nuclear repulsion energy")  #TEST
psi4.compare_values(refscf, scfenergy, 9, "SCF Energy")  #TEST
