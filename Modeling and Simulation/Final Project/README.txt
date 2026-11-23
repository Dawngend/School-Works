CS0019 Final Project: Threshold Bunching Monte Carlo Simulation
Members: John Ashley Alba, Dawn Andrei Pamesa, Rogelio Porras

What it does
Simulates one agency over two years. In Year 2 a share of the awards just above
PHP 1,000,000 is moved just below it. A one-sided two-proportion z test (alpha 0.05)
compares the Year 2 below-threshold share with Year 1 and flags a run when it is
significantly higher. The detection rate is the share of 5,000 runs flagged. The
0 percent moved scenario gives the false alarm rate.

Files
threshold_bunching_simulation.m   the whole project, one script
fig_overview.png                  overview figure (4 panels)
fig_scenario1.png                 baseline, 0 percent moved
fig_scenario2.png                 scenario 2, 20 percent moved
fig_scenario3.png                 scenario 3, 50 percent moved

How to run
1. Open threshold_bunching_simulation.m in MATLAB (R2019b or later, no toolbox needed).
2. Press Run. It takes about 30 seconds.
3. The results table prints in the Command Window and four figures open.
   The same figures are saved as the fig_*.png files in the current folder.

Inputs (Given data section at the top of the script)
threshold 1,000,000 | nearBandPercent 2 | lognormalMedian 1,150,000 | lognormalSigma 0.28
simulationRuns 5000 | alpha 0.05 | agencySizes 100, 300, 1000 | movedShares 0, 20, 50
rng(42) is fixed, so every run gives the same numbers.

Expected output at 300 awards per year
Baseline (0 percent moved):     5.24 percent detected (false alarm rate)
Scenario 2 (20 percent moved):  9.68 percent detected
Scenario 3 (50 percent moved): 21.70 percent detected
