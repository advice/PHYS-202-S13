experiment = importdata('radioactivedecay.dat');
t = experiment.data(:,1);
N = experiment.data(:,2);
figure(42)
plot(t,N,'b:')
%%
hold on
% function to fit 
fun = @(x) 40*exp(-x);
%%
% Start at t
guess = fun(t); % fun(t)
plot(t,guess,'r:')
%%
hold on
% fit the data
fittedmodel = fit(t', N',fun);
% plot the result
plot(fittedmodel,'r-');