function [ m,dm,b,db ] = WeightedLinearLeastSquaresFit( x,y,dy )
%This calculates the weighted linear least squares fit  
%   Input an x,y and uncertainty in y as dy to the program to return the
%   m,b,dm,db values
w = 1./(dy.^2)

m = (sum(w)*sum(w.*x.*y)-sum(w.*x)*sum(w.*y))/(sum(w)*sum(w.*x.^2)-(sum(w.*x)).^2);
b = (sum(w.*x.^2)*sum(w.*y)-sum(w.*x)*sum(w.*x.*y))/(sum(w)*sum(w.*x.^2)-(sum(w.*x)).^2);
dm = sqrt((sum(w))/(sum(w)*sum(w.*x.^2)-(sum(w.*x)).^2));
db = sqrt((sum(w.*x.^2))/(sum(w)*sum(w.*x.^2)-(sum(w.*x)).^2));



end




