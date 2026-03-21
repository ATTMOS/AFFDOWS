.. include:: ../affdo_docs_common.rst

Accuracy and Performance
========================

The data presented in this section were initially obtained using a previous version of AFFDO and have been further extended using the latest version, |BOLD_AFFDO_VERSION|. See the details below.

**Note**: The code is continuously being improved. Please make sure to use the latest AFFDO version.

Validation Study
----------------

We have validated the accuracy of AFFDO using a protein-ligand dataset reported by Wang et al. [1]. In this dataset, the authors
report the experimental relative binding free energies (RBFE) values for a series of protein-ligand systems. For the validation
study, a subset of these systems was selected, and RBFE simulations were carried out using the Amber Drug Discovery Boost package [2].
The standard GAFF (GAFF 2.11) force field was used for ligands, the ff14SB parameter set was used for proteins, and the TIP4P model was used for water.
The computed RBFE values using GAFF were compared against the experimental values; protein-ligand systems that displayed >1.0 kcal/mol error
(the chemical accuracy threshold) were identified to test and validate AFFDO. Each ligand was used as input to the workflow, and force fields with optimized
dihedral parameters were obtained for each ligand. The time taken for the full reparameterization process varied from 3 to 48 hours, depending
on the system size, atom types, and hardware being used.

In **Figure 1**, we present the torsional scan energy profiles for the most significant torsions
of TYK2 ejm42 (**A**) and jmc27 (**B**). The GAFF2 energy profile (Standard GAFF) of the former mostly differs from the reference profile by barrier height.
In contrast, the latter not only differs in barrier height, but also in phase. Using the AFFDO platform, both the phase and barrier height can be fitted,
resulting in much tighter fits to the reference profiles (Fitted GAFF). After reparameterization, fitted force field parameters were used to recompute RBFE
values for protein-ligand pairs. As depicted in **Figure 2**, the reparameterized GAFF force field improves the computed RBFE for all systems. For certain systems
(e.g., TYK2 jmc28-jmc30, jmc27-jmc30), this improvement is more prominent than in others.


.. image:: images/validation_figure.png
    :alt: This project was supported by NIH SBIR Seed fund.

We have extended these validations using our latest version |BOLD_AFFDO_VERSION| in our manuscript [3], where we benchmark AFFDO against a wider range of drug-like molecules with complex torsions. In this study, both dihedral barrier heights and 1-4 scaling factors were optimized simultaneously. The results further demonstrate that AFFDO can significantly improve GAFF torsion parameters, leading to more accurate free energy predictions across different chemical environments.

Highlights from this new study include:

* **Torsion-scan accuracy:** For the TYK2 series, customized GAFF2 reduces MAE/RMSE from 1.56/1.92 kcal/mol to 0.20/0.24 kcal/mol relative to DFT scans; for the MCL1 series, errors drop from 0.81/1.08 to 0.51/0.69 kcal/mol, with Pearson and Spearman correlations ≥0.94 across both sets.
* **RBFE improvements:** AFFDO lowers the MAE in roughly 80% of the TYK2 and MCL1 transformations; inside this positively impacted subset the average drop is ~0.4 kcal/mol for TYK2 and ~0.8 kcal/mol for MCL1, with the largest gain reaching 2.45 kcal/mol. When considering all transformations, the net MAE reduction drops to half.
* **Sampling robustness:** Sampling robustness: Reparameterized torsions reduce RBFE uncertainty and improve sampling consistency, leading to more stable MD ensembles and more reliable alchemical free-energy calculations.
* **Workflow throughput:** Representative fragments (e.g., TYK2 jmc28_F1, MCL1 L35_F1) complete in roughly 1–7 hours on a 36-core/4×GPU cloud node, with QC centroid optimizations and torsional scans dominating wall time.

These findings, along with full torsional profiles, benchmarking workflows, and extended RBFE analyses, are presented comprehensively in our manuscript and its accompanying supporting information [3].

Extended Benchmark: Default AFFDO Settings
-------------------------------------------

In addition to the manuscript results above, we have benchmarked the current default AFFDO configuration on an extended subset of the Wang et al. [1] dataset. In this benchmark, only dihedral barrier heights are optimized (without scaling factor adjustments). This represents the out-of-the-box AFFDO experience for users running with default settings.

The benchmark covers 58 systems from two protein families: **TYK2** (16 systems, neutral ligands) and **MCL1** (42 systems, charged ligands q = −1). Each system was evaluated at three reference levels to assess the impact of reference quality on fitting accuracy.

Aggregate Metrics
^^^^^^^^^^^^^^^^^^

The table below summarizes the overall GAFF2 vs AFFDO performance across 58 systems (305 torsions) from the Wang et al. [1] dataset, using DFT constrained-optimization (PBE0-D3BJ/6-31G*) as the reference level. Metrics quantify agreement with QC torsional potential energy surfaces obtained from constrained dihedral scans evaluated on a 20° angular grid (i.e., scan-point energies) and should not be interpreted as RBFE predictive accuracy.

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th style="text-align: left; padding: 8px;"><b>Metric</b></th>
     <th style="padding: 8px;"><b>GAFF2</b></th>
     <th style="padding: 8px;"><b>AFFDO</b></th>
   </tr>
   </thead>
   <tbody>
   <tr><td style="text-align: left; padding: 6px;">MAE<sup>a</sup> (kcal/mol)</td><td>1.12 ± 0.10</td><td>0.41 ± 0.04</td></tr>
   <tr><td style="text-align: left; padding: 6px;">RMSE<sup>a</sup> (kcal/mol)</td><td>1.39 ± 0.12</td><td>0.55 ± 0.05</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Pearson (<i>r</i>)</td><td>0.87</td><td>0.96</td></tr>
   <tr style="border-bottom: 2px solid #333;"><td style="text-align: left; padding: 6px;">Spearman (<i>ρ</i>)</td><td>0.85</td><td>0.94</td></tr>
   </tbody>
   <tfoot>
   <tr><td colspan="3" style="text-align: left; padding: 6px; font-size: 0.9em;"><sup>a</sup> Uncertainties are reported as 95% CI calculated analytically.</td></tr>
   </tfoot>
   </table>

Across 58 systems and 305 torsions, AFFDO reduces the overall RMSE by 60% (from 1.39 to 0.55 kcal/mol) and the MAE by 63% (from 1.12 to 0.41 kcal/mol), while improving the Pearson correlation from 0.87 to 0.96. These improvements are consistent across both the MCL1 (42 systems, charged) and TYK2 (16 systems, neutral) protein families.

Fitting Accuracy by Reference Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AFFDO supports multiple reference levels for torsion energy profiles. To guide users in selecting the appropriate reference level, we benchmarked the same 58 systems (16 TYK2, 42 MCL1) at three theory levels:

* **XTB**: GFN2-XTB torsional scan (fast, semi-empirical)
* **DFT-SP**: DFT single-point on XTB geometries (PBE0-D3BJ/6-31G*)
* **DFT**: Full DFT constrained optimization (PBE0-D3BJ/6-31G*)

.. note::

   Each reference level uses a different energy surface. The metrics below assess how well AFFDO fits each level's own profile. Because the reference profiles differ, RMSE/MAE values **cannot be directly compared across levels** — a lower RMSE at XTB reflects the smoothness of XTB profiles, not necessarily better parameter quality. For a direct comparison of reference levels against DFT ground truth, see the `Cross-Reference Analysis`_ below.

All energies are in kcal/mol. Uncertainties are 95% confidence intervals. When AFFDO does not improve a torsion, GAFF2 parameters are retained.

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th rowspan="2" style="text-align: left; padding: 8px; border-bottom: 2px solid #333;"><b>Metric</b></th>
     <th colspan="2" style="padding: 8px; border-bottom: 1px solid #999;"><b>TYK2</b> (16 sys, neutral)</th>
     <th colspan="2" style="padding: 8px; border-bottom: 1px solid #999;"><b>MCL1</b> (42 sys, q = −1)</th>
   </tr>
   <tr style="border-bottom: 2px solid #333;">
     <th style="padding: 6px;">GAFF2</th><th style="padding: 6px;">AFFDO</th>
     <th style="padding: 6px;">GAFF2</th><th style="padding: 6px;">AFFDO</th>
   </tr>
   </thead>
   <tbody>
   <tr style="background: #f0f0f0;"><td colspan="5" style="text-align: left; padding: 6px;"><b>XTB reference</b></td></tr>
   <tr><td style="text-align: left; padding: 6px;">MAE (kcal/mol)</td><td>1.61 ± 0.27</td><td>0.15 ± 0.04</td><td>1.37 ± 0.10</td><td>0.30 ± 0.03</td></tr>
   <tr><td style="text-align: left; padding: 6px;">RMSE (kcal/mol)</td><td>2.00 ± 0.31</td><td>0.21 ± 0.07</td><td>1.76 ± 0.13</td><td>0.40 ± 0.04</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Pearson (<i>r</i>)</td><td>0.79</td><td>0.99</td><td>0.86</td><td>0.96</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Spearman (<i>ρ</i>)</td><td>0.75</td><td>0.98</td><td>0.86</td><td>0.95</td></tr>

   <tr style="background: #f0f0f0;"><td colspan="5" style="text-align: left; padding: 6px;"><b>DFT-SP reference</b></td></tr>
   <tr><td style="text-align: left; padding: 6px;">MAE (kcal/mol)</td><td>1.68 ± 0.22</td><td>0.28 ± 0.06</td><td>1.05 ± 0.08</td><td>0.34 ± 0.03</td></tr>
   <tr><td style="text-align: left; padding: 6px;">RMSE (kcal/mol)</td><td>2.09 ± 0.26</td><td>0.39 ± 0.09</td><td>1.32 ± 0.09</td><td>0.47 ± 0.05</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Pearson (<i>r</i>)</td><td>0.82</td><td>0.99</td><td>0.88</td><td>0.97</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Spearman (<i>ρ</i>)</td><td>0.77</td><td>0.98</td><td>0.88</td><td>0.95</td></tr>

   <tr style="background: #f0f0f0;"><td colspan="5" style="text-align: left; padding: 6px;"><b>DFT reference</b></td></tr>
   <tr><td style="text-align: left; padding: 6px;">MAE (kcal/mol)</td><td>1.66 ± 0.24</td><td>0.45 ± 0.09</td><td>0.89 ± 0.09</td><td>0.39 ± 0.04</td></tr>
   <tr><td style="text-align: left; padding: 6px;">RMSE (kcal/mol)</td><td>2.04 ± 0.27</td><td>0.62 ± 0.12</td><td>1.12 ± 0.11</td><td>0.52 ± 0.06</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Pearson (<i>r</i>)</td><td>0.81</td><td>0.98</td><td>0.90</td><td>0.96</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Spearman (<i>ρ</i>)</td><td>0.75</td><td>0.95</td><td>0.89</td><td>0.94</td></tr>
   </tbody>
   </table>

All three reference levels produce significant improvements over standard GAFF2, with RMSE reductions of 60–90% and Pearson correlations reaching 0.95–0.99. In terms of torsion improvement rates, XTB improves 82% of TYK2 and 95% of MCL1 torsions; DFT-SP achieves the highest rates at 83% (TYK2) and 98% (MCL1); DFT constrained-optimization improves 81% of TYK2 and 79% of MCL1 torsions.

DFT-SP combines DFT-quality energies with XTB geometries at single-point cost, producing smooth energy profiles that the optimizer fits reliably. XTB is competitive for both neutral and charged molecules, achieving the lowest absolute RMSE values. DFT constrained-optimization produces the most physically accurate profiles but is the hardest to fit — full geometry relaxation introduces complex energy landscape features that single-barrier fitting cannot fully capture.

Geometry Fidelity
^^^^^^^^^^^^^^^^^^

AFFDO uses a two-level optimization strategy to balance energy accuracy with geometric fidelity. In the inner loop, torsion parameters are refined using single-point (SP) energy evaluations on fixed geometries — this is fast and allows efficient gradient-based exploration of parameter space. Periodically, outer geometry-refresh cycles re-minimize MM geometries with the updated parameters and recompute energy profiles, ensuring that the torsion parameters remain consistent with relaxed molecular structures.

This approach yields substantial energy improvements (60–90% RMSE reduction) with only a modest increase in structural deviation from the reference geometries. Across the 58 benchmarked systems, the mean Max RMSD between reference and MM-optimized geometries increases by approximately 0.09 A after fitting — roughly 6–7% of a typical C–C bond length and well within general force field accuracy expectations.

To further control this trade-off, AFFDO employs a composite scoring function during outer-cycle selection:

.. math::

   S = \text{RMSD}_{\text{energy}} + \lambda \cdot \overline{\text{RMSD}}_{\text{geom}}

where :math:`\lambda` (default 0.5) weights geometric fidelity against energy accuracy. This provides a light geometry bias when selecting among candidate parameter sets from different optimization cycles, without significantly affecting energy quality. The net result is a fitting procedure that converges faster than full geometry optimization at every iteration, produces better energy fits, and maintains acceptable structural accuracy.

.. _Cross-Reference Analysis:

Cross-Reference Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^

The fitting accuracy table above shows how well AFFDO reproduces each reference level's own energy surface — but it does not tell us how close the resulting parameters are to DFT ground truth. To answer that question, we evaluated XTB and DFT-SP torsion profiles directly against DFT constrained-optimization profiles for the same 305 torsions.

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th style="text-align: left; padding: 8px;"><b>Metric</b></th>
     <th style="padding: 8px;"><b>XTB vs DFT</b></th>
     <th style="padding: 8px;"><b>DFT-SP vs DFT</b></th>
   </tr>
   </thead>
   <tbody>
   <tr><td style="text-align: left; padding: 6px;">RMSE (kcal/mol)</td><td>1.39 ± 0.09</td><td>0.97 ± 0.13</td></tr>
   <tr><td style="text-align: left; padding: 6px;">MAE (kcal/mol)</td><td>1.14 ± 0.08</td><td>0.74 ± 0.10</td></tr>
   <tr style="border-bottom: 2px solid #333;"><td style="text-align: left; padding: 6px;">Pearson (<i>r</i>)</td><td>0.84</td><td>0.85</td></tr>
   </tbody>
   </table>

DFT-SP profiles are 30% closer to DFT ground truth than XTB profiles (RMSE 0.97 vs 1.39 kcal/mol). This gap propagates through fitting: even though XTB fitting achieves a lower self-referential RMSE (0.21 vs 0.39), the XTB reference surface itself is further from DFT, so the final fitted parameters end up less accurate.

The table below combines fitting quality, reference quality, and net accuracy to show the full picture:

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th style="text-align: left; padding: 8px;"><b>Reference</b></th>
     <th style="padding: 8px;"><b>Fitting quality</b><br><span style="font-size: 0.85em;">(self-ref RMSE)</span></th>
     <th style="padding: 8px;"><b>Reference quality</b><br><span style="font-size: 0.85em;">(vs DFT RMSE)</span></th>
     <th style="padding: 8px;"><b>Net accuracy</b><br><span style="font-size: 0.85em;">(fitted vs DFT RMSE)</span></th>
   </tr>
   </thead>
   <tbody>
   <tr><td style="text-align: left; padding: 6px;">XTB</td><td>0.21</td><td>1.39</td><td>1.40</td></tr>
   <tr><td style="text-align: left; padding: 6px;">DFT-SP</td><td>0.39</td><td>0.97</td><td>1.07</td></tr>
   <tr style="border-bottom: 2px solid #333;"><td style="text-align: left; padding: 6px;">DFT</td><td>0.55</td><td>0.00</td><td>0.41</td></tr>
   </tbody>
   <tfoot>
   <tr><td colspan="4" style="text-align: left; padding: 6px; font-size: 0.9em;">All RMSE values in kcal/mol. 305 torsions from 58 Wang et al. systems.</td></tr>
   </tfoot>
   </table>

DFT constrained-optimization yields the highest accuracy (net RMSE 0.41 kcal/mol) but requires the longest computation time. DFT-SP is a cost-effective alternative, achieving 24% lower net error than XTB (1.07 vs 1.40 kcal/mol) at a fraction of the cost of full DFT. XTB provides rapid turnaround but its reference surface is further from DFT ground truth, which limits the final parameter quality regardless of fitting accuracy.

.. list-table:: Reference Level Summary
   :header-rows: 1
   :widths: 20 15 15 50

   * - Reference Level
     - Speed
     - Net RMSE
     - Notes
   * - **DFT**
     - Slow
     - 0.41
     - Highest accuracy; longest computation time
   * - **DFT-SP**
     - Medium
     - 1.07
     - Good alternative; best improvement rate (83–98%)
   * - **XTB**
     - Fast
     - 1.40
     - Rapid screening; limited by reference quality

Charge Model Comparison
^^^^^^^^^^^^^^^^^^^^^^^^

*This section will be updated with charge model benchmarks (AM1-BCC vs ABCG2 vs RESP) as results become available.*

This benchmark is being extended to additional Wang et al. [1] systems and will be updated as new results become available.

**References**

[1] Wang, L., Wu, Y., Deng, Y., et al. (2015). Accurate and reliable prediction of relative ligand binding
potency in prospective drug discovery by way of a modern free-energy calculation protocol and force
field. Journal of the American Chemical Society, 137(7), 2695-2703.

[2] Ganguly, A., Tsai, H. C., Fernández-Pendás, M., Lee, T. S., Giese, T. J., & York, D. M. (2022). AMBER
Drug Discovery Boost Tools: Automated Workflow for Production Free-Energy Simulation Setup and Analysis (ProFESSA).
Journal of Chemical Information and Modeling, 62(23), 6069-6083.

[3] Blanco-Gonzalez, A., Betancourt, W., Snyder, R., Zhang, S., Giese, T. J., Piskulich, Z. A., Goetz, A. W., Merz, K. M. Jr., York, D. M., Aktulga, H. M., Manathunga, M. (2024).
Automated Force Field Developer and Optimizer Platform: Torsion Reparameterization. ChemRxiv. doi:10.26434/chemrxiv-2024-lcnx1.

*Last updated on* |UPDATE_DATE|.
