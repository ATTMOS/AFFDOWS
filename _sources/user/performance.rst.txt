.. include:: ../affdo_docs_common.rst

Accuracy and Performance
========================

This section presents three chronological benchmarks that document AFFDO's development and validation. Each benchmark phase builds on the previous one, progressively expanding the test set and refining the methodology:

1. **Validation Overview** — Illustrates AFFDO's torsion-fitting approach and its downstream effect on RBFE calculations using representative examples from the Wang et al. [1] dataset.
2. **Manuscript Benchmark** — Expanded evaluation published with |BOLD_AFFDO_VERSION|, optimizing both torsion barrier heights and 1-4 scaling factors simultaneously.
3. **Extended Benchmark** — Comprehensive analysis of current default settings (torsion-only optimization) across 58 systems at three reference levels.

The primary accuracy metric throughout is **torsion-profile agreement** — how well AFFDO-fitted MM energy profiles reproduce quantum-mechanical reference scans. RBFE improvements are reported as complementary downstream validation where available.

**Note**: The code is continuously being improved. Please make sure to use the latest AFFDO version.

Validation Overview
-------------------

AFFDO improves molecular mechanics force fields by fitting torsion parameters to reproduce quantum-mechanical (QM) reference energy profiles. The examples below, drawn from the Wang et al. [1] protein-ligand dataset, illustrate the core approach and its impact.

In **Figure 1**, torsional scan energy profiles are shown for representative torsions of TYK2 ejm42 (**A**) and jmc27 (**B**). The standard GAFF2 profile of the former mostly differs from the reference by barrier height, while the latter differs in both barrier height and phase. Using AFFDO, both the phase and barrier height are fitted, resulting in much tighter agreement with the QM reference profiles (Fitted GAFF). Reparameterization times range from 3 to 48 hours depending on system size, atom types, and hardware.

These torsion-profile improvements also translate to better downstream predictions. As shown in **Figure 2**, RBFE values recomputed with the fitted parameters using the Amber Drug Discovery Boost package [2] (ff14SB for proteins, TIP4P for water) improve for all tested systems, with some pairs (e.g., TYK2 jmc28-jmc30, jmc27-jmc30) showing more prominent improvements than others. The systematic benchmarks that follow quantify these gains across larger datasets.


.. image:: images/validation_figure.png
    :alt: This project was supported by NIH SBIR Seed fund.

Manuscript Benchmark (Torsion + Scaling Factor Optimization)
------------------------------------------------------------

In our manuscript [3], we benchmarked |BOLD_AFFDO_VERSION| against a wider range of drug-like molecules with complex torsions. In this study, both dihedral barrier heights **and** 1-4 scaling factors (scee/scnb) were optimized simultaneously — note that this differs from current default settings, which optimize torsion parameters only (see `Extended Benchmark: Default AFFDO Settings`_ below).

Key findings:

* **Torsion-scan accuracy:** For the TYK2 series, customized GAFF2 reduces MAE/RMSE from 1.56/1.92 kcal/mol to 0.20/0.24 kcal/mol relative to DFT scans; for the MCL1 series, errors drop from 0.81/1.08 to 0.51/0.69 kcal/mol, with Pearson and Spearman correlations ≥0.94 across both sets.
* **RBFE improvements:** As a complementary downstream validation, AFFDO lowers the MAE in roughly 80% of TYK2 and MCL1 transformations; the average drop is ~0.4 kcal/mol for TYK2 and ~0.8 kcal/mol for MCL1, with the largest gain reaching 2.45 kcal/mol.
* **Sampling robustness:** Reparameterized torsions reduce RBFE uncertainty and improve sampling consistency, leading to more stable MD ensembles and more reliable alchemical free-energy calculations.
* **Workflow throughput:** Representative fragments (e.g., TYK2 jmc28_F1, MCL1 L35_F1) complete in roughly 1–7 hours on a 36-core/4×GPU cloud node, with QC centroid optimizations and torsional scans dominating wall time.

Full torsional profiles, benchmarking workflows, and extended RBFE analyses are presented in the manuscript and its supporting information [3].

Extended Benchmark: Default AFFDO Settings
-------------------------------------------

In addition to the manuscript results above, we have benchmarked the current default AFFDO configuration on an extended subset of the Wang et al. [1] dataset. In this benchmark, only dihedral barrier heights are optimized (without scaling factor adjustments). This represents the out-of-the-box AFFDO experience for users running with default settings.

The benchmark covers 58 systems from two protein families: **TYK2** (16 systems, neutral ligands) and **MCL1** (42 systems, charged ligands q = −1). Each system was evaluated at three reference levels to assess the impact of reference quality on fitting accuracy.

Aggregate Metrics
^^^^^^^^^^^^^^^^^^

The table below summarizes the overall GAFF2 vs AFFDO performance across 58 systems (305 torsions) from the Wang et al. [1] dataset, using DFT constrained-optimization (PBE0-D3BJ/6-31G*, with 6-31+G* for anionic species) as the reference level. Metrics quantify agreement with QC torsional potential energy surfaces obtained from constrained dihedral scans evaluated on a 20° angular grid (i.e., scan-point energies) and should not be interpreted as RBFE predictive accuracy.

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th style="text-align: left; padding: 8px;"><b>Metric</b></th>
     <th style="padding: 8px;"><b>GAFF2</b></th>
     <th style="padding: 8px;"><b>AFFDO</b></th>
     <th style="padding: 8px;"><b>Change</b></th>
   </tr>
   </thead>
   <tbody>
   <tr><td style="text-align: left; padding: 6px;">MAE<sup>a</sup> (kcal/mol)</td><td>1.12 ± 0.10</td><td>0.41 ± 0.04</td><td>−63%</td></tr>
   <tr><td style="text-align: left; padding: 6px;">RMSE<sup>a</sup> (kcal/mol)</td><td>1.39 ± 0.12</td><td>0.55 ± 0.05</td><td>−60%</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Pearson (<i>r</i>)</td><td>0.87</td><td>0.96</td><td>+10%</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Spearman (<i>ρ</i>)</td><td>0.85</td><td>0.94</td><td>+11%</td></tr>
   <tr style="border-bottom: 2px solid #333;"><td style="text-align: left; padding: 6px;">Max RMSD<sup>b</sup> (&#8491;)</td><td>0.68 ± 0.06</td><td>0.65 ± 0.06</td><td>&#8722;4%</td></tr>
   </tbody>
   <tfoot>
   <tr><td colspan="4" style="text-align: left; padding: 6px; font-size: 0.9em;"><sup>a</sup> Uncertainties are reported as 95% CI calculated analytically.<br><sup>b</sup> Maximum RMSD between reference (DFT) and MM-optimized geometries across scan points per torsion; see <a href="#geometry-fidelity">Geometry Fidelity</a>.</td></tr>
   </tfoot>
   </table>

Across 58 systems and 305 torsions, AFFDO reduces the overall RMSE by 60% (from 1.39 to 0.55 kcal/mol) and the MAE by 63% (from 1.12 to 0.41 kcal/mol), while improving the Pearson correlation from 0.87 to 0.96. Geometry fidelity is preserved: the per-torsion Max RMSD between reference and MM-optimized geometries is essentially unchanged (0.68 → 0.65 Å, −4%) thanks to AFFDO's geometry-aware regularization (see `Geometry Fidelity`_). These improvements are consistent across both the MCL1 (42 systems, charged) and TYK2 (16 systems, neutral) protein families.

Fitting Accuracy by Reference Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AFFDO supports multiple reference levels for torsion energy profiles. To guide users in selecting the appropriate reference level, we benchmarked the same 58 systems (16 TYK2, 42 MCL1) at three theory levels:

* **XTB**: GFN2-XTB torsional scan (fast, semi-empirical)
* **DFT-SP**: DFT single-point on XTB geometries (PBE0-D3BJ/6-31G*, with 6-31+G* for anionic species)
* **DFT**: Full DFT constrained optimization (PBE0-D3BJ/6-31G*, with 6-31+G* for anionic species)

.. note::

   Each reference level uses a different energy surface. The metrics below assess how well AFFDO fits each level's own profile. Because the reference profiles differ, RMSE/MAE values **cannot be directly compared across levels** — a lower RMSE at XTB reflects the smoothness of XTB profiles, not necessarily better parameter quality. For a direct comparison of reference levels against DFT ground truth, see the `Cross-Reference Analysis`_ below.

All energies are in kcal/mol. Uncertainties are 95% confidence intervals. When AFFDO does not improve a torsion, GAFF2 parameters are retained.

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0; border-spacing: 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th rowspan="2" style="text-align: left; padding: 10px 14px; border-bottom: 2px solid #333;"><b>Metric</b></th>
     <th colspan="3" style="padding: 10px 12px; border-bottom: 1px solid #999; border-left: 2px solid #ccc;"><b>TYK2</b> (16 sys, neutral)</th>
     <th colspan="3" style="padding: 10px 12px; border-bottom: 1px solid #999; border-left: 2px solid #ccc;"><b>MCL1</b> (42 sys, q = −1)</th>
   </tr>
   <tr style="border-bottom: 2px solid #333;">
     <th style="padding: 8px 12px; border-left: 2px solid #ccc;">GAFF2</th><th style="padding: 8px 12px;">AFFDO</th><th style="padding: 8px 10px;">Δ</th>
     <th style="padding: 8px 12px; border-left: 2px solid #ccc;">GAFF2</th><th style="padding: 8px 12px;">AFFDO</th><th style="padding: 8px 10px;">Δ</th>
   </tr>
   </thead>
   <tbody>
   <tr style="background: #f0f0f0;"><td colspan="7" style="text-align: left; padding: 8px 14px;"><b>XTB reference</b></td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">MAE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.61 ± 0.27</td><td style="padding: 8px 12px;">0.15 ± 0.04</td><td style="padding: 8px 10px;">−91%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.37 ± 0.10</td><td style="padding: 8px 12px;">0.30 ± 0.03</td><td style="padding: 8px 10px;">−78%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">RMSE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">2.00 ± 0.31</td><td style="padding: 8px 12px;">0.21 ± 0.07</td><td style="padding: 8px 10px;">−90%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.76 ± 0.13</td><td style="padding: 8px 12px;">0.40 ± 0.04</td><td style="padding: 8px 10px;">−77%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Pearson (<i>r</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.79</td><td style="padding: 8px 12px;">0.99</td><td style="padding: 8px 10px;">+25%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.86</td><td style="padding: 8px 12px;">0.96</td><td style="padding: 8px 10px;">+12%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Spearman (<i>ρ</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.75</td><td style="padding: 8px 12px;">0.98</td><td style="padding: 8px 10px;">+31%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.86</td><td style="padding: 8px 12px;">0.95</td><td style="padding: 8px 10px;">+10%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Max RMSD (&#8491;)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.85 ± 0.11</td><td style="padding: 8px 12px;">0.92 ± 0.11</td><td style="padding: 8px 10px;">+8%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.79 ± 0.08</td><td style="padding: 8px 12px;">0.77 ± 0.08</td><td style="padding: 8px 10px;">&#8722;3%</td></tr>

   <tr style="background: #f0f0f0;"><td colspan="7" style="text-align: left; padding: 8px 14px;"><b>DFT-SP reference</b></td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">MAE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.68 ± 0.22</td><td style="padding: 8px 12px;">0.28 ± 0.06</td><td style="padding: 8px 10px;">−83%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.05 ± 0.08</td><td style="padding: 8px 12px;">0.34 ± 0.03</td><td style="padding: 8px 10px;">−68%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">RMSE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">2.09 ± 0.26</td><td style="padding: 8px 12px;">0.39 ± 0.09</td><td style="padding: 8px 10px;">−81%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.32 ± 0.09</td><td style="padding: 8px 12px;">0.47 ± 0.05</td><td style="padding: 8px 10px;">−64%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Pearson (<i>r</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.82</td><td style="padding: 8px 12px;">0.99</td><td style="padding: 8px 10px;">+21%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.88</td><td style="padding: 8px 12px;">0.97</td><td style="padding: 8px 10px;">+10%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Spearman (<i>ρ</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.77</td><td style="padding: 8px 12px;">0.98</td><td style="padding: 8px 10px;">+27%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.88</td><td style="padding: 8px 12px;">0.95</td><td style="padding: 8px 10px;">+8%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Max RMSD (&#8491;)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.82 ± 0.11</td><td style="padding: 8px 12px;">0.93 ± 0.12</td><td style="padding: 8px 10px;">+13%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.79 ± 0.08</td><td style="padding: 8px 12px;">0.84 ± 0.07</td><td style="padding: 8px 10px;">+6%</td></tr>

   <tr style="background: #f0f0f0;"><td colspan="7" style="text-align: left; padding: 8px 14px;"><b>DFT reference</b></td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">MAE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.66 ± 0.24</td><td style="padding: 8px 12px;">0.46 ± 0.09</td><td style="padding: 8px 10px;">−72%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.90 ± 0.09</td><td style="padding: 8px 12px;">0.39 ± 0.04</td><td style="padding: 8px 10px;">−57%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">RMSE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">2.04 ± 0.27</td><td style="padding: 8px 12px;">0.63 ± 0.13</td><td style="padding: 8px 10px;">−69%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.12 ± 0.11</td><td style="padding: 8px 12px;">0.52 ± 0.05</td><td style="padding: 8px 10px;">−54%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Pearson (<i>r</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.81</td><td style="padding: 8px 12px;">0.98</td><td style="padding: 8px 10px;">+21%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.90</td><td style="padding: 8px 12px;">0.96</td><td style="padding: 8px 10px;">+7%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Spearman (<i>ρ</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.75</td><td style="padding: 8px 12px;">0.95</td><td style="padding: 8px 10px;">+27%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.89</td><td style="padding: 8px 12px;">0.94</td><td style="padding: 8px 10px;">+6%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Max RMSD (&#8491;)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.89 ± 0.11</td><td style="padding: 8px 12px;">0.90 ± 0.12</td><td style="padding: 8px 10px;">+1%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.58 ± 0.07</td><td style="padding: 8px 12px;">0.53 ± 0.06</td><td style="padding: 8px 10px;">&#8722;9%</td></tr>
   </tbody>
   </table>

All three reference levels produce significant improvements over standard GAFF2, with RMSE reductions of 60–90% and Pearson correlations reaching 0.95–0.99. Geometry fidelity is preserved across all three: Max RMSD stays within roughly ±0.1 Å of the GAFF2 baseline post-fit, with DFT MCL1 actually improving slightly (0.58 → 0.53 Å). In terms of torsion improvement rates, XTB improves 82% of TYK2 and 95% of MCL1 torsions; DFT-SP achieves the highest rates at 83% (TYK2) and 98% (MCL1); DFT constrained-optimization improves 81% of TYK2 and 79% of MCL1 torsions.

DFT-SP combines DFT-quality energies with XTB geometries at single-point cost, producing smooth energy profiles that the optimizer fits reliably. XTB is competitive for both neutral and charged molecules, achieving the lowest absolute RMSE values. DFT constrained-optimization produces the most physically accurate profiles but is the hardest to fit — full geometry relaxation introduces complex energy landscape features that single-barrier fitting cannot fully capture.

Geometry Fidelity
^^^^^^^^^^^^^^^^^^

AFFDO uses a two-level optimization strategy to balance energy accuracy with geometric fidelity. In the inner loop, torsion parameters are refined using single-point (SP) energy evaluations on fixed geometries — this is fast and allows efficient gradient-based exploration of parameter space. Periodically, outer geometry-refresh cycles re-minimize MM geometries with the updated parameters and recompute energy profiles, ensuring that the torsion parameters remain consistent with relaxed molecular structures.

This approach yields substantial energy improvements (60–90% RMSE reduction) without compromising geometric fidelity. The Max RMSD between reference and MM-optimized geometries (see per-reference-level tables above) stays within ±0.1 Å of the GAFF2 baseline after fitting — and decreases for the largest, charged-ligand subset (DFT MCL1).

To further control this trade-off, AFFDO employs a composite scoring function during outer-cycle selection:

.. math::

   S = \text{RMSD}_{\text{energy}} + \lambda \cdot \overline{\text{RMSD}}_{\text{geom}}

where :math:`\lambda` (default 0.5) weights geometric fidelity against energy accuracy. This provides a light geometry bias when selecting among candidate parameter sets from different optimization cycles, without significantly affecting energy quality.

Benchmarking on the 16 TYK2 ligands (73 torsions) at the XTB reference level illustrates the effect of geometry regularization:

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th style="text-align: left; padding: 8px;"><b>Metric</b></th>
     <th style="padding: 8px;"><b>&lambda; = 0</b></th>
     <th style="padding: 8px;"><b>&lambda; = 0.5</b> (default)</th>
   </tr>
   </thead>
   <tbody>
   <tr><td style="text-align: left; padding: 6px;">Mean energy RMSD (kcal/mol)</td><td><b>0.129</b></td><td>0.132</td></tr>
   <tr><td style="text-align: left; padding: 6px;">Mean geom RMSD (&#8491;)</td><td>0.418</td><td><b>0.375</b></td></tr>
   <tr style="border-bottom: 2px solid #333;"><td style="text-align: left; padding: 6px;">Mean norm_RMSE</td><td><b>0.045</b></td><td>0.046</td></tr>
   </tbody>
   </table>

With no regularization (:math:`\lambda = 0`), the optimizer achieves the lowest energy RMSD but the mean geometry RMSD rises to 0.418 A. Enabling the default regularization (:math:`\lambda = 0.5`) brings geometry RMSD down to 0.375 A — a 10% improvement — at a negligible energy cost. The net result is a fitting procedure that converges faster than full geometry optimization at every iteration, produces better energy fits, and maintains acceptable structural accuracy.

.. note::

   Two geometry RMSD metrics appear in the AFFDO results:

   - **Max RMSD** (per-reference-level tables above): the maximum RMSD between reference and MM-optimized geometries across all scan points for a given torsion, evaluated once with the final fitted parameters. This is a post-hoc quality metric.
   - **Mean geom RMSD** (lambda comparison table): the mean RMSD across all scan points, computed *during* fitting at each outer geometry-refresh cycle. This is the metric used by the composite score to select among candidate parameter sets from different optimization cycles.

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
~~~~~~~~~~~~~~~~~~~~~~~

Torsion parameters and partial charges are deeply coupled in molecular mechanics force fields.
The torsion Fourier series must compensate for errors in 1-4 electrostatic interactions, so the
quality of partial charges directly affects torsion fitting accuracy. GAFF2's generic torsion
parameters were derived assuming RESP-quality electrostatics; pairing them with approximate charges
therefore introduces a coupling error that the fitted torsions must absorb alongside genuine
torsional effects.

We benchmarked three charge models on all 58 DFT reference systems using identical optimizer settings:

- **AM1-BCC**: semi-empirical AM1 charges with Bond Charge Corrections — fast, default in AmberTools
- **ABCG2**: BCC parameters re-fitted for GAFF2 against neutral solvation free energies — fast, improved solvation accuracy on neutral organic solutes
- **RESP**: charges fitted to the QM electrostatic potential (HF/6-31G*, with HF/6-31+G* for anions) — requires a DFT-level QM calculation

All metrics below are averaged only over torsions where AFFDO improved on the
GAFF2 baseline (the per-section "torsions fitted" counts). This differs from
the production-behavior RMSE in the per-reference-level table above, which
retains GAFF2 for unfitted torsions.

.. raw:: html

   <table style="border-collapse: collapse; text-align: center; margin: 20px 0; border-spacing: 0;">
   <thead>
   <tr style="border-bottom: 2px solid #333;">
     <th rowspan="2" style="text-align: left; padding: 10px 14px; border-bottom: 2px solid #333;"><b>Metric</b></th>
     <th colspan="3" style="padding: 10px 12px; border-bottom: 1px solid #999; border-left: 2px solid #ccc;"><b>TYK2</b> (16 sys, neutral)</th>
     <th colspan="3" style="padding: 10px 12px; border-bottom: 1px solid #999; border-left: 2px solid #ccc;"><b>MCL1</b> (42 sys, q = &minus;1)</th>
   </tr>
   <tr style="border-bottom: 2px solid #333;">
     <th style="padding: 8px 12px; border-left: 2px solid #ccc;">GAFF2</th><th style="padding: 8px 12px;">AFFDO</th><th style="padding: 8px 10px;">&Delta;</th>
     <th style="padding: 8px 12px; border-left: 2px solid #ccc;">GAFF2</th><th style="padding: 8px 12px;">AFFDO</th><th style="padding: 8px 10px;">&Delta;</th>
   </tr>
   </thead>
   <tbody>
   <tr style="background: #f0f0f0;"><td colspan="7" style="text-align: left; padding: 8px 14px;"><b>AM1-BCC charges</b> &mdash; torsions fitted: TYK2 73/90 (81%), MCL1 169/215 (79%)</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">MAE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.66 ± 0.24</td><td style="padding: 8px 12px;">0.34 ± 0.08</td><td style="padding: 8px 10px;">&minus;80%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.89 ± 0.09</td><td style="padding: 8px 12px;">0.43 ± 0.05</td><td style="padding: 8px 10px;">&minus;52%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">RMSE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">2.04 ± 0.27</td><td style="padding: 8px 12px;">0.47 ± 0.11</td><td style="padding: 8px 10px;">&minus;77%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.12 ± 0.11</td><td style="padding: 8px 12px;">0.56 ± 0.07</td><td style="padding: 8px 10px;">&minus;50%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Pearson (<i>r</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.81</td><td style="padding: 8px 12px;">0.98</td><td style="padding: 8px 10px;">+21%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.90</td><td style="padding: 8px 12px;">0.96</td><td style="padding: 8px 10px;">+7%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Spearman (<i>ρ</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.75</td><td style="padding: 8px 12px;">0.95</td><td style="padding: 8px 10px;">+27%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.89</td><td style="padding: 8px 12px;">0.94</td><td style="padding: 8px 10px;">+6%</td></tr>

   <tr style="background: #f0f0f0;"><td colspan="7" style="text-align: left; padding: 8px 14px;"><b>ABCG2 charges</b> &mdash; torsions fitted: TYK2 90/90 (100%), MCL1 173/215 (80%)</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">MAE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.80 ± 0.27</td><td style="padding: 8px 12px;">0.14 ± 0.04</td><td style="padding: 8px 10px;">&minus;92%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.92 ± 0.09</td><td style="padding: 8px 12px;">0.31 ± 0.03</td><td style="padding: 8px 10px;">&minus;66%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">RMSE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">2.24 ± 0.32</td><td style="padding: 8px 12px;">0.21 ± 0.08</td><td style="padding: 8px 10px;">&minus;91%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.15 ± 0.11</td><td style="padding: 8px 12px;">0.43 ± 0.04</td><td style="padding: 8px 10px;">&minus;63%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Pearson (<i>r</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.81</td><td style="padding: 8px 12px;">0.99</td><td style="padding: 8px 10px;">+22%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.90</td><td style="padding: 8px 12px;">0.97</td><td style="padding: 8px 10px;">+8%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Spearman (<i>ρ</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.75</td><td style="padding: 8px 12px;">0.98</td><td style="padding: 8px 10px;">+31%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.89</td><td style="padding: 8px 12px;">0.95</td><td style="padding: 8px 10px;">+7%</td></tr>

   <tr style="background: #f0f0f0;"><td colspan="7" style="text-align: left; padding: 8px 14px;"><b>RESP charges</b> &mdash; torsions fitted: TYK2 90/90 (100%), MCL1 202/215 (94%)</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">MAE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.95 ± 0.23</td><td style="padding: 8px 12px;">0.17 ± 0.04</td><td style="padding: 8px 10px;">&minus;91%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.03 ± 0.10</td><td style="padding: 8px 12px;">0.26 ± 0.02</td><td style="padding: 8px 10px;">&minus;75%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">RMSE (kcal/mol)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">2.38 ± 0.26</td><td style="padding: 8px 12px;">0.24 ± 0.07</td><td style="padding: 8px 10px;">&minus;90%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">1.31 ± 0.13</td><td style="padding: 8px 12px;">0.35 ± 0.04</td><td style="padding: 8px 10px;">&minus;73%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Pearson (<i>r</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.83</td><td style="padding: 8px 12px;">0.99</td><td style="padding: 8px 10px;">+19%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.86</td><td style="padding: 8px 12px;">0.98</td><td style="padding: 8px 10px;">+14%</td></tr>
   <tr><td style="text-align: left; padding: 8px 14px;">Spearman (<i>ρ</i>)</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.75</td><td style="padding: 8px 12px;">0.97</td><td style="padding: 8px 10px;">+29%</td><td style="padding: 8px 12px; border-left: 2px solid #ccc;">0.87</td><td style="padding: 8px 12px;">0.96</td><td style="padding: 8px 10px;">+10%</td></tr>
   </tbody>
   </table>

Aggregating across both families: AM1-BCC fits 242/305 torsions (79%) with mean
post-fit RMSE 0.531 kcal/mol; ABCG2 fits 263/305 (86%) with 0.354; RESP fits
292/305 (96%) with **0.313**. The RMSE reduction over GAFF2 is 62%, 76%, and
**81%** respectively.

To make the comparison robust to the choice of GAFF2 baseline, we also report a
direct head-to-head on the absolute AFFDO RMSE — i.e., the per-torsion RMSE
after fitting, ignoring the starting point — on the 226 torsions fitted by all
three charge models. The table also includes per-system wins on the full
58-system set (mean improvement delta > 1%).

.. list-table:: Head-to-Head: per-torsion (226 common) and per-system (58 total)
   :header-rows: 1
   :widths: 22 26 26 26

   * - Matchup
     - Per-torsion winner
     - Per-system winner
     - Tie
   * - AM1-BCC vs ABCG2
     - **ABCG2 73%** (BCC 25%)
     - **ABCG2 45/58** (BCC 11)
     - 2% / 2 sys
   * - AM1-BCC vs RESP
     - **RESP 81%** (BCC 15%)
     - **RESP 51/58** (BCC 4)
     - 3% / 3 sys
   * - ABCG2 vs RESP
     - **RESP 40%** (ABCG2 35%)
     - **RESP 34/58** (ABCG2 18)
     - 24% / 6 sys

To translate these RMSE values into something more interpretable, the
distribution table below shows the fraction of fitted torsions that fall
below common quality thresholds:

.. list-table:: AFFDO RMSE Quality Distribution
   :header-rows: 1
   :widths: 25 18 18 18 21

   * - Charge Model
     - Torsions Fitted
     - < 0.25 kcal/mol
     - < 0.50 kcal/mol
     - < 1.00 kcal/mol
   * - AM1-BCC
     - 242
     - 26%
     - 65%
     - 84%
   * - ABCG2
     - 263
     - 48%
     - 80%
     - 95%
   * - **RESP**
     - **292**
     - **64%**
     - **82%**
     - **96%**

RESP also has the highest "torsion rescue rate": switching from AM1-BCC to RESP
moves 50 additional torsions across the fitting threshold (242 → 292), and
ABCG2 moves 21 (242 → 263). Many of these rescued torsions are in charged MCL1
systems where AM1-BCC's electrostatic errors mask the true torsional error,
making the GAFF2 baseline appear acceptable when it is not.

**Key findings:**

- **RESP is the overall best charge model for torsion fitting**: lowest post-fit RMSE (0.313 kcal/mol),
  highest fit rate (96%), and largest RMSE reduction (81%). RESP wins 51/58 systems head-to-head
  against AM1-BCC.

- **ABCG2 excels for neutral molecules**: For TYK2 (neutral), ABCG2 slightly outperforms RESP
  (90.4% vs 89.0% improvement) with the lowest AFFDO RMSE (0.21 kcal/mol). Both achieve 100%
  fit rate vs 81% for AM1-BCC.

- **RESP dominates for charged systems**: For MCL1 (q = -1), RESP fits 94% of torsions vs 79-80% for
  BCC/ABCG2. Both AM1-BCC and ABCG2 were parameterized primarily on neutral organic molecules, while
  RESP fits charges directly to the QM electrostatic potential of the actual (anionic) state — which
  is reflected in the data here, where bespoke torsion fitting cannot fully compensate for the
  electrostatic errors of the BCC-family models on charged ligands.

- **GAFF2 baseline inversion**: RESP shows the highest GAFF2 baseline RMSE because its more accurate
  charges expose larger discrepancies with generic torsion parameters. After bespoke fitting, RESP
  achieves the best result — confirming that generic GAFF2 torsions absorb electrostatic errors when
  paired with approximate charges.

- **Quality distribution**: 64% of RESP-fitted torsions achieve sub-0.25 kcal/mol RMSE, compared to
  48% for ABCG2 and 26% for AM1-BCC.

RESP Geometry Source — XTB vs DFT-Opt Centroids
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AFFDO 25.11 introduces the ``resp_geometry_source`` setting, which controls
how centroid geometries feed the RESP HF/6-31G\* ESP single-point. The new
default ``xtb`` uses post-clustering XTB centroids directly and skips the
upstream PBE0/6-31G\* centroid optimization; the legacy ``dft`` path is
preserved for reproducibility and edge cases. ESP and the RESP fit itself
are unchanged in both modes (HF/6-31G\*, 6-31+G\* for anions). Validated on
the Wang benchmark (58 systems, 291 fitted torsions): aggregate post-fit
AFFDO RMSE differs by 0.003 kcal/mol — statistically equivalent at the MM
noise floor. A DFT geometry optimization is therefore not a strict
prerequisite for a RESP charge fit; an ensemble of reasonable
XTB-optimized structures is sufficient when XTB minima are close to DFT
minima, which holds across the entire Wang benchmark.

.. list-table:: RESP geometry source comparison (mean AFFDO RMSE, kcal/mol)
   :header-rows: 1

   * - Family
     - Fitted torsions
     - dft (PBE0-opt geom)
     - xtb (XTB centroid)
     - Δ %
   * - TYK2 (neutral, 16 sys)
     - 90
     - 0.241
     - 0.227
     - −5.6%
   * - MCL1 (q = −1, 42 sys)
     - 202
     - 0.345
     - 0.347
     - +0.6%
   * - **TOTAL (58 sys)**
     - **291**
     - **0.313**
     - **0.310**
     - **−0.9%**

Median identical (0.230 kcal/mol both modes); 31/58 systems are slightly
better under ``xtb``, 27/58 slightly worse — symmetric, no systematic bias.
Validation covers neutral (TYK2) and anionic (MCL1, q = −1) ligands. For
cationic, zwitterionic, or unusual ligand classes a head-to-head check on a
representative molecule is recommended. To revert to the classical
PBE0-opt pipeline use ``--resp-geometry-source dft`` on the CLI, or pick
"DFT (advanced — slowest)" in the AFFDOWS RESP geometry source selector.

**References**

[1] Wang, L., Wu, Y., Deng, Y., et al. (2015). Accurate and reliable prediction of relative ligand binding
potency in prospective drug discovery by way of a modern free-energy calculation protocol and force
field. Journal of the American Chemical Society, 137(7), 2695-2703.

[2] Ganguly, A., Tsai, H. C., Fernández-Pendás, M., Lee, T. S., Giese, T. J., & York, D. M. (2022). AMBER
Drug Discovery Boost Tools: Automated Workflow for Production Free-Energy Simulation Setup and Analysis (ProFESSA).
Journal of Chemical Information and Modeling, 62(23), 6069-6083.

[3] Blanco-Gonzalez, A.; Betancourt, W.; Snyder, R. M.; Zhang, S.; Giese, T. J.; Piskulich, Z. A.; Götz, A. W.; Merz, K. M., Jr.; York, D. M.; Aktulga, H. M.; Manathunga, M. Automated Force Field Developer and Optimizer Platform: Torsion Reparameterization. J. Chem. Inf. Model. 2026, 66 (6), 3206–3219. DOI: 10.1021/acs.jcim.6c00528

*Last updated on* |UPDATE_DATE|.
