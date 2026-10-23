%% CS0019 - Modeling and Simulation
%  Exercise 1: Plot in MATLAB (results of Technical Assessment 2, original arrivals)
%  Name    : Dawn Andrei Pamesa
%  Section : TS31
%  Prof    : Sir Abraham Magpantay

clc; clear;

%% Given data
packet           = ["A"; "B"; "C"];
arrivalTime      = [0; 1; 3];
transmissionTime = [4; 2; 1];

%% Waiting and finish times (FCFS, one outgoing connection)
n           = numel(packet);
startTime   = zeros(n, 1);
waitingTime = zeros(n, 1);
finishTime  = zeros(n, 1);

for i = 1:n
    if i == 1
        startTime(i) = arrivalTime(i);
    else
        startTime(i) = max(arrivalTime(i), finishTime(i-1));
    end
    waitingTime(i) = startTime(i) - arrivalTime(i);
    finishTime(i)  = startTime(i) + transmissionTime(i);
end

fprintf('Student Name: Dawn Andrei Pamesa\n\n');
disp(table(packet, waitingTime, finishTime, transmissionTime));

%% Grouped bar chart, 3 bars per packet
figure('Name', 'Exercise 1: Plot in MATLAB');
bar(categorical(packet), [waitingTime finishTime transmissionTime]);
legend('Waiting Time', 'Finish Time', 'Transmission Time', 'Location', 'northwest');
xlabel('Packet');
ylabel('Time (ms)');
title({'Packet Times, Original Arrivals', 'Dawn Andrei Pamesa'});
grid on;
