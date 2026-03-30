Known Limitations
=================

AFFDO is designed for automated reparameterization of small organic
drug-like molecules. The following limitations define the current scope
of the platform.

Supported Molecules
-------------------

- Only organic drug-like molecules are supported (C, H, N, O, S, P, F, Cl,
  Br, I). Molecules containing other elements are rejected at submission.
- Metal atoms, coordination compounds, and inorganic species are outside
  AFFDO's scope.
- Molecular charge must be an integer. All calculations assume a closed-shell
  (singlet) electronic state.

Force Field and Parameterization
--------------------------------

- Only GAFF and GAFF2 force fields are supported.
- Only torsion and charge parameters are optimized. Lennard-Jones and
  bond/angle parameters retain their default GAFF values.
- In-ring torsions are not reparameterized, including in macrocycles and
  medium-sized rings. Only exocyclic rotatable bonds are fitted.
- Terminal group torsions (e.g., methyl rotations) and aromatic dihedral
  angles are excluded from fitting.
- Output uses AMBER topology format. Direct export to other MD engines
  (e.g., GROMACS) is not currently supported.

Reference Level Constraints
---------------------------

- DFT calculations use PBE0-D3BJ with Pople-family basis sets (via QUICK).
  Basis set coverage may be limited for certain element and charge
  combinations depending on the underlying QC engine.
- AFFDO relies on third-party tools (QUICK, XTB, RDKit, AmberTools) whose
  own limitations may impose additional constraints. Refer to the respective
  documentation for details.


Scope
-----

- AFFDO parameterizes isolated small molecules. Protein-ligand complex
  preparation is outside the current scope.
- Large molecules are automatically fragmented when beneficial based on
  torsional complexity. Very large molecules may require significant
  computational resources.
