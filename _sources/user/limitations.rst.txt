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

- AFFDO supports RESP charge fitting for small organic ligands using an
  HF/6-31G* electrostatic-potential workflow, consistent with common
  AMBER/GAFF-style ligand parameterization practice.
- RESP charge fitting may be unreliable for highly charged anions,
  especially molecules with multiple negatively charged groups close in
  space, such as some polycarboxylates. In this regime, AFFDO may be unable
  to generate valid RESP charges.
- Selecting DFT-prepared geometries does not necessarily resolve this
  limitation. For these highly charged systems, the DFT geometry-preparation
  step can encounter similar convergence limits before the RESP calculation
  is reached. In practice, changing the RESP geometry source may change where
  the failure occurs, but it may not make the molecule compatible with the
  current protocol.
- When AFFDO cannot complete RESP for a molecule in this regime, the job
  stops with a diagnostic message in the log and a failure notification is
  sent. The diagnostic identifies the type of failure and suggests possible
  next steps.
- For multi-fragment molecules, AFFDO may still complete the remaining
  fragments when one fragment cannot be reparameterized. In that case, the
  merged topology uses AFFDO-optimized parameters for the successful
  fragments, while the failed fragment region remains at the base GAFF2
  parameterization. The final report identifies any fragments that were not
  reparameterized.
- Alternative charge models such as AM1-BCC and ABCG2 are available when
  RESP cannot be completed, but they are not RESP-equivalent. These methods
  do not require the same HF/6-31G* RESP calculation and may be more robust
  for difficult inputs, but they were developed primarily for typical organic
  molecules. Their reliability for highly charged species may be reduced
  compared with a successful RESP fit.


Scope
-----

- AFFDO parameterizes isolated small molecules. Protein-ligand complex
  preparation is outside the current scope.
- Large molecules are automatically fragmented when beneficial based on
  torsional complexity. Very large molecules may require significant
  computational resources.
