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

- DFT calculations use PBE0-D3BJ with Pople-family basis sets (``6-31G*``
  for neutral and cationic species; ``6-31+G*`` with diffuse functions for
  anionic species).
- AFFDO relies on third-party tools (Amber, QUICK, XTB, RDKit) whose
  own limitations may impose additional constraints. Refer to the respective
  documentation for details.

Element coverage at the DFT level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two element/charge combinations are outside the current DFT scope because
of basis-set limitations. When detected, AFFDO does **not** start the
workflow; the submission is rejected up front with a clear message in the
log and an explanatory email, and no compute time is consumed.

- **Iodine (I).** Iodine requires effective core potentials (ECPs) at any
  charge state. The DFT engine used by AFFDO does not currently provide
  ECPs, so I-containing ligands cannot be run at any DFT reference level.

  *Workaround:* Use the ``XTB`` reference level (``-l xtb``) for
  I-containing molecules. XTB is parameterized for the full periodic table
  up to Rn and handles iodine natively.

- **Bromine (Br) on anions.** Bromine is fully supported on neutral and
  cationic species at the standard ``6-31G*`` basis. For anionic species
  AFFDO uses the diffuse-augmented ``6-31+G*`` basis, which does not cover
  bromine in the current DFT engine. AFFDO therefore rejects Br-containing
  anions at the DFT reference level.

  *Workaround:* If the chemistry permits, submit a neutral or cationic
  protonation state — Br is then fully supported at DFT. Otherwise, switch
  to the ``XTB`` reference level.

These two combinations are detected at the file-upload stage in the web
app and at project initialization in the CLI. The submission is blocked
before any DFT calculation begins; you receive an explanatory email
instead of a workflow-failure notification.


RESP Charge Fitting
-------------------

- AFFDO supports RESP charge fitting for small organic ligands using an
  HF/6-31G* electrostatic-potential workflow, consistent with common
  AMBER/GAFF-style ligand parameterization practice.
- RESP charge fitting may be unreliable in some cases, most commonly (but
  not limited to) highly charged anions — especially molecules with
  multiple negatively charged groups close in space, such as some
  polycarboxylates. Neutral molecules with challenging electronic
  structures can occasionally fall into the same regime. In such cases,
  AFFDO may be unable to generate valid RESP charges.
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
  for difficult inputs, but they were developed primarily for neutral
  organic molecules. Their reliability for highly charged species may be
  reduced compared with a successful RESP fit.


Scope
-----

- AFFDO parameterizes isolated small molecules. Protein-ligand complex
  preparation is outside the current scope.
- Large molecules are automatically fragmented when beneficial based on
  torsional complexity. Very large molecules may require significant
  computational resources.
