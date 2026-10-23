%% CS0019 - Modeling and Simulation
%  Technical Assessment 3: Lucky 9 Monte Carlo Simulation
%  Name    : Dawn Andrei Pamesa
%  Section : TS31
%  Prof    : Sir Abraham Magpantay

clc; clear;
rng(2026);   % fixed seed so the run can be repeated

%% Given data
cardValue = [1 2 3 4 5 6 7 8 9 0 0 0 0];   % Ace, 2 to 9, then 10, J, Q, K
deck      = repmat(cardValue, 1, 4);       % 52 cards, 4 suits
bet       = 10;
N         = 1000;

%% Part A. Play 1000 games
playerTotal = zeros(N, 1);
dealerTotal = zeros(N, 1);

for g = 1:N
    drawn = randperm(52, 4);   % no card is dealt twice in the same game
    playerTotal(g) = mod(sum(deck(drawn(1:2))), 10);
    dealerTotal(g) = mod(sum(deck(drawn(3:4))), 10);
end

playerLucky = playerTotal == 9;
dealerLucky = dealerTotal == 9;
playerWins  = playerTotal > dealerTotal;
dealerWins  = ~playerWins;   % dealer wins ties, so every other game is his

pPlayerLucky = mean(playerLucky);
pDealerLucky = mean(dealerLucky);
pLucky9      = mean(playerLucky | dealerLucky);
pPlayerWin   = mean(playerWins);
pDealerWin   = mean(dealerWins);
expectedValue = (pPlayerWin * bet) - (pDealerWin * bet);

fprintf('Student Name: Dawn Andrei Pamesa\n\n');
fprintf('=== LUCKY 9 SIMULATION (N = %d games, bet = PHP %d) ===\n', N, bet);
fprintf('Probability of Player Lucky 9 : %.4f\n', pPlayerLucky);
fprintf('Probability of Dealer Lucky 9 : %.4f\n', pDealerLucky);
fprintf('Probability of any Lucky 9    : %.4f\n', pLucky9);
fprintf('Probability Player wins       : %.4f\n', pPlayerWin);
fprintf('Probability Dealer wins       : %.4f\n', pDealerWin);
fprintf('Expected value per game       : PHP %.2f\n', expectedValue);
if expectedValue < 0
    fprintf('The game favors the house.\n\n');
else
    fprintf('The game favors the player.\n\n');
end

%% Part B. Effect of the dealer wins ties rule
pTie          = mean(playerTotal == dealerTotal);
pDealerHigher = mean(dealerTotal > playerTotal);
evIfTiePush   = (pPlayerWin * bet) - (pDealerHigher * bet);   % a tie returns the bet

fprintf('=== DEALER WINS TIES RULE ===\n');
fprintf('Probability of a tie                  : %.4f\n', pTie);
fprintf('Dealer wins with a higher total       : %.4f\n', pDealerHigher);
fprintf('Expected value with the rule          : PHP %.2f\n', expectedValue);
fprintf('Expected value if a tie were a push   : PHP %.2f\n\n', evIfTiePush);

%% Part C. Effect of the number of games
sizes = [100 1000 10000 100000 1000000];
fprintf('=== EFFECT OF N ===\n');
fprintf('%-10s %12s %12s %12s %12s\n', 'N', 'P(Player)', 'P(Dealer)', 'P(Lucky 9)', 'EV (PHP)');
for k = 1:numel(sizes)
    n = sizes(k);
    pt = zeros(n, 1);
    dt = zeros(n, 1);
    for g = 1:n
        drawn = randperm(52, 4);
        pt(g) = mod(sum(deck(drawn(1:2))), 10);
        dt(g) = mod(sum(deck(drawn(3:4))), 10);
    end
    pw = mean(pt > dt);
    fprintf('%-10d %12.4f %12.4f %12.4f %12.2f\n', n, pw, 1 - pw, ...
        mean(pt == 9 | dt == 9), (pw - (1 - pw)) * bet);
end
