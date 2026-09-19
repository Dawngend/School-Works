%% CS0019 - Modeling and Simulation
%  Technical Assessment 1: Introduction to MATLAB
%  Name    : Dawn Andrei Pamesa
%  Section : TS31
%  Prof    : Sir Abraham Magpantay

clc; clear;

%% Given data
production = [
    120  95  80;
    135 100  76;
    128 110  85;
    140 105  90;
    150 115  88
];

sellingPrice     = [50 65 80];
productionCost   = [30 40 55];
adjustmentFactor = [1.10 1.05 0.97];

productNames = ["Product A", "Product B", "Product C"];

%% 1. Size and number of elements of the production matrix
[numDays, numProducts] = size(production);
totalElements = numel(production);

% Input validation, adopted from the AI review. Each per-product vector must
% hold exactly one value per column of the production matrix.
assert(numel(sellingPrice)     == numProducts, 'sellingPrice must contain one value per product.');
assert(numel(productionCost)   == numProducts, 'productionCost must contain one value per product.');
assert(numel(adjustmentFactor) == numProducts, 'There must be exactly one adjustment factor per product.');
assert(numel(productNames)     == numProducts, 'productNames must contain one name per product.');

fprintf('=== 1. MATRIX PROPERTIES ===\n');
fprintf('Size of production matrix : %d rows x %d columns\n', numDays, numProducts);
fprintf('Number of working days    : %d\n', numDays);
fprintf('Number of products        : %d\n', numProducts);
fprintf('Total number of elements  : %d\n\n', totalElements);

%% 2. Daily and weekly production totals
dailyTotals   = sum(production, 2);   % sum across the columns, one total per day
productTotals = sum(production, 1);   % sum down the rows, one total per product
weeklyTotal   = sum(production, 'all');

fprintf('=== 2. PRODUCTION TOTALS ===\n');
for d = 1:numDays
    fprintf('Day %d total production   : %d units\n', d, dailyTotals(d));
end
fprintf('\n');
for p = 1:numProducts
    fprintf('%s weekly production: %d units\n', productNames(p), productTotals(p));
end
fprintf('Total weekly production   : %d units\n\n', weeklyTotal);

%% 3. Weekly revenue, cost, and profit
revenuePerProduct = productTotals .* sellingPrice;   % element-wise, per product
costPerProduct    = productTotals .* productionCost;
profitPerProduct  = revenuePerProduct - costPerProduct;

weeklyRevenue = sum(revenuePerProduct);
weeklyCost    = sum(costPerProduct);
weeklyProfit  = weeklyRevenue - weeklyCost;

fprintf('=== 3. ORIGINAL WEEKLY FINANCIALS ===\n');
fprintf('%-12s %12s %12s %12s\n', 'Product', 'Revenue', 'Cost', 'Profit');
for p = 1:numProducts
    fprintf('%-12s %12.2f %12.2f %12.2f\n', productNames(p), ...
        revenuePerProduct(p), costPerProduct(p), profitPerProduct(p));
end
fprintf('%-12s %12.2f %12.2f %12.2f\n\n', 'TOTAL', ...
    weeklyRevenue, weeklyCost, weeklyProfit);

%% 4. Apply the adjustment factors to simulate a new production plan
simProduction = round(production .* adjustmentFactor);

simProductTotals = sum(simProduction, 1);
simDailyTotals   = sum(simProduction, 2);
simWeeklyTotal   = sum(simProduction, 'all');

simRevenuePerProduct = simProductTotals .* sellingPrice;
simCostPerProduct    = simProductTotals .* productionCost;
simProfitPerProduct  = simRevenuePerProduct - simCostPerProduct;

simWeeklyRevenue = sum(simRevenuePerProduct);
simWeeklyCost    = sum(simCostPerProduct);
simWeeklyProfit  = simWeeklyRevenue - simWeeklyCost;

fprintf('=== 4. SIMULATED PRODUCTION PLAN ===\n');
fprintf('Adjustment factors applied: A = %.2f, B = %.2f, C = %.2f\n\n', ...
    adjustmentFactor(1), adjustmentFactor(2), adjustmentFactor(3));
fprintf('%-8s %12s %12s %12s %12s\n', 'Day', 'Product A', 'Product B', 'Product C', 'Day Total');
for d = 1:numDays
    fprintf('Day %-4d %12d %12d %12d %12d\n', d, ...
        simProduction(d,1), simProduction(d,2), simProduction(d,3), simDailyTotals(d));
end
fprintf('%-8s %12d %12d %12d %12d\n\n', 'TOTAL', ...
    simProductTotals(1), simProductTotals(2), simProductTotals(3), simWeeklyTotal);

fprintf('=== SIMULATED WEEKLY FINANCIALS ===\n');
fprintf('%-12s %12s %12s %12s\n', 'Product', 'Revenue', 'Cost', 'Profit');
for p = 1:numProducts
    fprintf('%-12s %12.2f %12.2f %12.2f\n', productNames(p), ...
        simRevenuePerProduct(p), simCostPerProduct(p), simProfitPerProduct(p));
end
fprintf('%-12s %12.2f %12.2f %12.2f\n\n', 'TOTAL', ...
    simWeeklyRevenue, simWeeklyCost, simWeeklyProfit);

%% 5. Compare the original and simulated weekly profits
profitDifference = simWeeklyProfit - weeklyProfit;
percentChange    = (profitDifference / weeklyProfit) * 100;

fprintf('=== 5. PROFIT COMPARISON ===\n');
fprintf('Original weekly profit    : %.2f\n', weeklyProfit);
fprintf('Simulated weekly profit   : %.2f\n', simWeeklyProfit);
fprintf('Difference                : %.2f\n', profitDifference);
fprintf('Percent change            : %.2f%%\n\n', percentChange);

%% 6. Recommendation based on the results
fprintf('=== 6. RECOMMENDATION ===\n');
if profitDifference > 0
    fprintf(['ADOPT the proposed production adjustment.\n' ...
             'It increases weekly profit by %.2f (%.2f%%).\n'], ...
             profitDifference, percentChange);
elseif profitDifference < 0
    fprintf(['REJECT the proposed production adjustment.\n' ...
             'It decreases weekly profit by %.2f (%.2f%%).\n'], ...
             abs(profitDifference), abs(percentChange));
else
    fprintf(['The adjustment is FINANCIALLY NEUTRAL.\n' ...
             'Weekly profit is unchanged, so the decision should rest on\n' ...
             'other factors such as demand, storage, or material supply.\n']);
end

[bestProfit, bestIdx] = max(simProfitPerProduct);
fprintf('Highest contributor under the new plan: %s (%.2f profit).\n', ...
    productNames(bestIdx), bestProfit);
