Known Limitations
=================

The following limitations define the current scope of the AFFDO platform.

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
- AFFDO relies on third-party tools (Amber, QUICK, XTB, RDKit) whose
  own limitations may impose additional constraints. Refer to the respective
  documentation for details.


RESP Charge Fitting
-------------------

- AFFDO performs RESP charge fitting at HF/6-31+G* in the gas phase.
  The SCF step at this theory level does not converge reliably for
  highly charged anions with multiple negatively-charged groups close
  in space (formal charge ≤ −2; e.g., polycarboxylates), and
  submissions in this regime will likely fail at the charge-fitting
  step.
- For these molecules, use the AM1-BCC or ABCG2 charge model instead.
  Both are well-defined at any charge state and bypass the HF SCF
  requirement. The submission form surfaces this recommendation
  automatically when RESP is selected for highly anionic species.


Scope
-----

- AFFDO parameterizes isolated small molecules. Protein-ligand complex
  preparation is outside the current scope.
- Large molecules are automatically fragmented when beneficial based on
  torsional complexity. Very large molecules may require significant
  computational resources.
