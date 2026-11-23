%% THRESHOLD BUNCHING MONTE CARLO SIMULATION
% CS0019 Final Project: Alba, Pamesa, Porras
% Monte Carlo simulation of procurement awards near the PHP 1,000,000 threshold.
% A self-baseline test (one-sided two-proportion z test) compares the share of
% awards just below the threshold in Year 2 against Year 1 of the same agency.

clear; clc; close all;
rng(42);

%% Given data
threshold        = 1000000;   % PHP 1,000,000 procurement threshold
nearBandPercent  = 2;         % width of the band just below and above the threshold
simulationRuns   = 5000;      % Monte Carlo runs per condition
lognormalMedian  = 1150000;   % median award amount
lognormalSigma   = 0.28;      % spread of the award amounts
alpha            = 0.05;      % one-sided significance level

agencySizes  = [100 300 1000];   % awards per year
movedShares  = [0 20 50];        % percent of near-threshold awards moved below
scenarioName = {'Baseline (0% moved)', 'Scenario 2 (20% moved)', 'Scenario 3 (50% moved)'};
reportSize   = 300;              % agency size used for the three scenario figures

%% Part A. Run every agency size and moved share
results = cell(numel(agencySizes), numel(movedShares));
for a = 1:numel(agencySizes)
    for m = 1:numel(movedShares)
        results{a, m} = simulateScenario(agencySizes(a), movedShares(m), ...
            nearBandPercent, simulationRuns, threshold, ...
            lognormalMedian, lognormalSigma, alpha);
    end
end

detectionRates = zeros(numel(agencySizes), numel(movedShares));
for a = 1:numel(agencySizes)
    for m = 1:numel(movedShares)
        detectionRates(a, m) = results{a, m}.detectionRate;
    end
end

%% Part B. Print the three scenarios at the report size
row = find(agencySizes == reportSize);

fprintf('\nTHRESHOLD BUNCHING MONTE CARLO SIMULATION\n');
fprintf('------------------------------------------\n');
fprintf('Awards per year:      %d\n', reportSize);
fprintf('Near-threshold band:  %.0f%%\n', nearBandPercent);
fprintf('Simulation runs:      %d\n', simulationRuns);
fprintf('Significance level:   %.2f (one-sided)\n\n', alpha);

scenarioTable = table(scenarioName', movedShares', ...
    100 * detectionRates(row, :)', ...
    100 * arrayfun(@(m) results{row, m}.averageYear1, 1:3)', ...
    100 * arrayfun(@(m) results{row, m}.averageYear2, 1:3)', ...
    'VariableNames', {'Scenario', 'MovedPercent', 'DetectionRatePercent', ...
    'AverageYear1Percent', 'AverageYear2Percent'});
disp(scenarioTable);

fprintf('False alarm rate (0%% moved): %.2f%%\n', 100 * detectionRates(row, 1));

fprintf('\nDetection rate (%%) by agency size and moved share\n');
disp(array2table(100 * detectionRates, ...
    'VariableNames', {'Moved0', 'Moved20', 'Moved50'}, ...
    'RowNames', {'N100', 'N300', 'N1000'}));

%% Part C. Overview figure
overview = figure('Name', 'Overview', 'Color', 'w', 'Position', [100 100 1250 760]);
tiledlayout(2, 2, 'TileSpacing', 'compact', 'Padding', 'compact');

nexttile;
histogram(100 * results{row, 2}.year2Shares, (-0.5:1:30.5) * 100 / reportSize, ...
    'FaceColor', [0.20 0.55 0.85], 'EdgeColor', 'w', 'DisplayName', 'Year 2 shares');
hold on;
xline(100 * results{row, 2}.averageYear1, '--', 'Color', [0.95 0.55 0.05], ...
    'LineWidth', 1.5, 'DisplayName', 'Year 1 average');
xline(100 * results{row, 2}.averageYear2, '--', 'Color', [0.05 0.60 0.50], ...
    'LineWidth', 1.5, 'DisplayName', 'Year 2 average');
legend('Location', 'northeast');
hold off; grid on;
xlabel('Year 2 below-threshold share (%)');
ylabel('Number of simulation runs');
title(sprintf('Distribution: %d awards/year, 20%% moved', reportSize));

nexttile;
plot(movedShares, 100 * detectionRates', '-o', 'LineWidth', 2, 'MarkerSize', 7);
grid on; ylim([0 100]);
xlabel('Share of near-threshold awards moved (%)');
ylabel('Detection rate (%)');
title('Detection rate by agency size');
legend('100 awards', '300 awards', '1,000 awards', 'Location', 'northwest');

nexttile;
bar(1:3, 100 * detectionRates(row, :), 0.55, 'FaceColor', [0.10 0.45 0.75]);
grid on; ylim([0 100]);
set(gca, 'XTick', 1:3, 'XTickLabel', {'0%', '20%', '50%'});
xlabel('Scenario: moved share');
ylabel('Detection rate (%)');
title(sprintf('Scenario comparison (%d awards/year)', reportSize));
text(1:3, 100 * detectionRates(row, :) + 3, ...
    compose('%.1f%%', 100 * detectionRates(row, :)), 'HorizontalAlignment', 'center');

nexttile;
imagesc(100 * detectionRates);
colormap(parula); colorbar;
set(gca, 'XTick', 1:3, 'XTickLabel', {'0%', '20%', '50%'}, ...
    'YTick', 1:3, 'YTickLabel', {'100', '300', '1,000'});
xlabel('Share moved below threshold');
ylabel('Awards per year');
title('Detection-rate heatmap');
for r = 1:3
    for c = 1:3
        textColor = 'w';
        if detectionRates(r, c) > 0.30
            textColor = 'k';
        end
        text(c, r, sprintf('%.1f%%', 100 * detectionRates(r, c)), ...
            'HorizontalAlignment', 'center', 'FontWeight', 'bold', 'Color', textColor);
    end
end

sgtitle('Monte Carlo Simulation of Threshold Bunching in Procurement Awards', ...
    'FontWeight', 'bold');

%% Part D. One figure per scenario
scenarioFigures = gobjects(1, 3);
for m = 1:3
    r = results{row, m};
    scenarioFigures(m) = figure('Name', scenarioName{m}, 'Color', 'w', ...
        'Position', [100 100 1100 450]);
    tiledlayout(1, 2, 'TileSpacing', 'compact', 'Padding', 'compact');

    nexttile;
    shareEdges = (-0.5:1:30.5) * 100 / reportSize;   % one bin per whole award count
    histogram(100 * r.year1Shares, shareEdges, 'FaceColor', [0.95 0.55 0.05], ...
        'FaceAlpha', 0.6, 'EdgeColor', 'w'); hold on;
    histogram(100 * r.year2Shares, shareEdges, 'FaceColor', [0.10 0.45 0.75], ...
        'FaceAlpha', 0.6, 'EdgeColor', 'w'); hold off;
    grid on;
    xlabel('Below-threshold share (%)');
    ylabel('Number of simulation runs');
    legend('Year 1', 'Year 2');
    title('Year 1 and Year 2 shares');

    nexttile;
    histogram(r.zScores, 'BinWidth', 0.25, 'FaceColor', [0.20 0.55 0.85], 'EdgeColor', 'w'); hold on;
    criticalZ = sqrt(2) * erfinv(1 - 2 * alpha);
    xline(criticalZ, '--r', sprintf('Critical z = %.3f', criticalZ), 'LineWidth', 1.5, ...
        'LabelVerticalAlignment', 'bottom');
    hold off; grid on;
    xlabel('z statistic');
    ylabel('Number of simulation runs');
    title(sprintf('Detection rate: %.2f%%', 100 * r.detectionRate));

    sgtitle(sprintf('%s, %d awards per year', scenarioName{m}, reportSize), ...
        'FontWeight', 'bold');
end

%% Part E. Save the figures
if exist('theme', 'file') || exist('theme', 'builtin')
    theme(overview, 'light');
    for m = 1:3
        theme(scenarioFigures(m), 'light');
    end
end
exportgraphics(overview, 'fig_overview.png', 'Resolution', 150);
for m = 1:3
    exportgraphics(scenarioFigures(m), sprintf('fig_scenario%d.png', m), 'Resolution', 150);
end

function result = simulateScenario(awardsPerYear, shareMoved, nearBandPercent, ...
    simulationRuns, threshold, lognormalMedian, lognormalSigma, alpha)

    lowerBand = threshold * (1 - nearBandPercent / 100);
    upperBand = threshold * (1 + nearBandPercent / 100);

    probabilityBelow = lognormalCDF(threshold, lognormalMedian, lognormalSigma) ...
        - lognormalCDF(lowerBand, lognormalMedian, lognormalSigma);
    probabilityNear = lognormalCDF(upperBand, lognormalMedian, lognormalSigma) ...
        - lognormalCDF(threshold, lognormalMedian, lognormalSigma);

    year1BelowCounts = sum(rand(simulationRuns, awardsPerYear) < probabilityBelow, 2);
    year2BelowCounts = sum(rand(simulationRuns, awardsPerYear) < probabilityBelow, 2);

    % Moved awards come from the band just above the threshold, so they are extra
    % below-threshold awards in Year 2 only.
    movementProbability = probabilityNear * shareMoved / 100;
    movedCounts = sum(rand(simulationRuns, awardsPerYear) < movementProbability, 2);

    x1 = year1BelowCounts;
    x2 = year2BelowCounts + movedCounts;
    p1 = x1 / awardsPerYear;
    p2 = x2 / awardsPerYear;

    % One-sided two-proportion z test: H0 p2 <= p1, H1 p2 > p1
    pooledShare   = (x1 + x2) / (2 * awardsPerYear);
    standardError = sqrt(pooledShare .* (1 - pooledShare) * (2 / awardsPerYear));

    zScores = zeros(size(standardError));
    valid = standardError > 0;
    zScores(valid) = (p2(valid) - p1(valid)) ./ standardError(valid);

    pValues  = 0.5 * erfc(zScores / sqrt(2));
    detected = pValues < alpha;

    result.detectionRate = mean(detected);
    result.averageYear1  = mean(p1);
    result.averageYear2  = mean(p2);
    result.year1Shares   = p1;
    result.year2Shares   = p2;
    result.zScores       = zScores;
end

function probability = lognormalCDF(x, medianValue, sigma)
    z = log(x / medianValue) / sigma;
    probability = 0.5 * (1 + erf(z / sqrt(2)));
end
