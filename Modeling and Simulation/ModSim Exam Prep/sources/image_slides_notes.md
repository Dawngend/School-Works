# ModSim (CS0019) M1-M3 picture-slide content (read by Claude 2026-10-06; M3 pages 39-68 NOT yet viewed)

M1: p7 physical system (factory line); p8 notional system (target->observer chain); p11 model examples
(h = 1/2 a t^2 + v t + s, v0=100 ft/s, s=1000 ft, a=-32 ft/s^2); p12 physical (wind tunnel) vs notional model;
p13 software / tabular / graphic simulation of falling object. p16 Ways to Study a System tree: experiment with actual
system vs with a model -> physical model / mathematical model -> analytical solution / simulation.
p17 examples table (System, Entities, Attributes, Activities): Supermarket-Customers-Shopping list-Checking out;
Banking-Customers-Account number, balance, credit status-Deposits, withdrawals; Communication-Messages-Length,
priority-Transmitting; Rapid Rail-Passengers-Origin, destination-Traveling; Traffic-Cars-Speed, distance-Driving.
p19 endogenous vs exogenous: Supermarket (purchasing, check-out | arrival of customers); Car parking in supermarket
(arrival of customers in supermarket | arrival of cars). p23 model tree: Physical (static, dynamic); Mathematical
(static -> numerical or analytical; dynamic -> analytical or numerical -> system simulation).
p29 process of simulation: define problem, introduce important variables, construct simulation model, specify values
of variables to be tested, conduct the simulation, examine results, select best course of action (loops back).
p36 10 steps in simulation and model building (define goal, mix of skills, involve end-user, choose tools, level of
detail, collect input data early, documentation, verification plan = "right answers", validation plan = "right
questions", statistical output analysis). p37 cycle: Model -> (implement) Simulation -> (execute) Results ->
(analyze) Insight -> (model); technologies: modeling, development, computation, data/information.
p47 Tables 1.1-1.3 fidelity/resolution/scale examples (chess, flight simulator, WoW, Halo, Doom, WarSim).
p54 Table 1.4: Live = real participants, real systems; Virtual = real, simulated; Constructive = simulated, simulated.
MATLAB p82-p118: variables (mynum = 6 is 1x1), who/whos/clear, types double default, int8 range -128..127
(intmin/intmax), format short/long/loose/compact, 2e4 = 20000, operators table and precedence (parentheses, power,
unary negation, * / \, + -, relational, &&, ||, assignment), pi i j inf NaN, double('a') = 97, char(97) = 'a',
char('abcd'+1) = 'bcde', relational ~= inequality, logical || && ~, xor; vectors 1x1 / 3x1 / 1x4 / 2x3; v=[1 2 3 4],
1:5, 1:2:9 -> 1 3 5 7 9; column via ; or transpose '; newvec(5), newvec(4:6), b(2)=11; reshape(mat,2,6), fliplr,
flipud, rot90 (counterclockwise), repmat(intmat,3,2); evec=[] length 0, evec=[evec 4]; min/sum/max/prod,
cumsum(1:5)=1 3 6 10 15, cumprod(1:5)=1 2 6 24 120; max(mat') rowwise; v*3, v/2; v1+v2; .^ and .* need the dot;
A(2x3)*B(3x4)=C(2x4) = [35 46 17 19; 9 22 20 5]; det([1 2 3;2 3 4;1 2 5]) = -2.
M2: p9 sets example (answers: A u B = {2,4,6,8,10}; A n B = {4,10}; A-B = {2}; B-A = {6,8}; A^c = {6,8,12});
p18 die probability table {}0, B 1/6, C 1/3, D 1/2, BC 1/2, BD 2/3, CD 5/6, S 1; p21 CDF step function;
p29 LCG Z(k+1) = (a Zk + c) mod m, Uk = Zk/m; p31 full-cycle conditions (c relatively prime to m; every prime factor
of m divides a-1; if 4 divides m then 4 divides a-1), example a=1 c=3 m=20 seed 2; p38 input data categories
(simple: sample/empirical/theoretical; complex: no data, multimodal, correlated, nonstationary); p59 DES flowchart
(main program, initialization, timing, event, library, stop?, report generator); p68 coffee shop cost table (best
total cost $320 at 2 baristas); p72-p75 four queue types with diagrams; p78-79 worked single-server table.
SLIDE ERRORS TO CORRECT: waiting time = service begin - arrival (slide reversed); "FIFO - Last in First Out" is LIFO;
M3 p61 odd/even code prints "Even number" twice and uses % (a comment in MATLAB; use mod(x,2)).
M3 seen so far: p5 x(t) -> continuous system -> y(t); p6 reservoir dq/dt = x, y = q; p8 classes table (1st-order
ODE predator-prey; 2nd-order F=ma orbits, oscillators, ballistics, RLC; 2nd-order PDE not covered); p11 orbit
r, v, E formulas; p17 Lotka-Volterra orbits r=b=d=p=1; p18 Euler x(t+dt) ~ x(t) + f(x,t)dt; p19 Runge-Kutta
midpoint t1/2 = t0 + dt/2, x1/2 = x0 + f(t0,x0) dt/2, x1 = x0 + f(t1/2,x1/2) dt; p31 mkdir/chdir/edit;
p32 script1.m radius 5 area 78.5398; p37 I/O command table (disp, fscanf, format, fprintf, input, ;);
p38 format codes %s %d %f %e %g \n \t.
