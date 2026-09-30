%% CS0019 - Modeling and Simulation
%  Technical Assessment 2: Network Packet Queue Simulation
%  Names   : John Kizon Guo, Dawn Andrei Pamesa
%  Section : TS31
%  Prof    : Sir Abraham Magpantay

clc; clear;

studentName = "John Kizon Guo, Dawn Andrei Pamesa";

%% Given data
packet           = ["A"; "B"; "C"];
arrivalTime      = [0; 1; 3];
transmissionTime = [4; 2; 1];

fprintf('Student Name: %s\n\n', studentName);

%% Part B. Original arrivals
fprintf('=== ORIGINAL PACKET QUEUE SIMULATION ===\n\n');
simulateQueue(packet, arrivalTime, transmissionTime);

%% Part C. Packet C arrives at 7 ms instead of 3 ms
revisedArrival = arrivalTime;
revisedArrival(packet == "C") = 7;

fprintf('\n=== REVISED PACKET QUEUE SIMULATION (Packet C arrives at 7 ms) ===\n\n');
[startTime, finishTime] = simulateQueue(packet, revisedArrival, transmissionTime);

fprintf('\nIdle periods of the outgoing connection:\n');
for i = 2:numel(packet)
    if startTime(i) > finishTime(i-1)
        fprintf('  %d ms to %d ms (before Packet %s)\n', finishTime(i-1), startTime(i), packet(i));
    end
end
fprintf('  after %d ms (no packets left)\n', finishTime(end));

%% FCFS simulation, used by both runs
function [startTime, finishTime] = simulateQueue(packet, arrivalTime, transmissionTime)
    n = numel(packet);
    startTime   = zeros(n,1);
    waitingTime = zeros(n,1);
    finishTime  = zeros(n,1);

    for i = 1:n
        % The connection can only start a packet once the previous one is done
        if i == 1
            startTime(i) = arrivalTime(i);
        else
            startTime(i) = max(arrivalTime(i), finishTime(i-1));
        end
        waitingTime(i) = startTime(i) - arrivalTime(i);
        finishTime(i)  = startTime(i) + transmissionTime(i);
    end

    results = table(packet, arrivalTime, transmissionTime, startTime, waitingTime, finishTime, ...
        'VariableNames', {'Packet', 'ArrivalTime_ms', 'TransmissionTime_ms', ...
        'StartTime_ms', 'WaitingTime_ms', 'FinishTime_ms'});

    disp(results);
    fprintf('Average Waiting Time: %.2f ms\n', mean(waitingTime));
end
