function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

h1 = sigmoid([ones(m, 1) X] * Theta1');
h2 = sigmoid([ones(m, 1) h1] * Theta2');
[dummy, p] = max(h2, [], 2);

X = [ones(m, 1) X];

for c = 1:m
	one_example = X(c, :);
	
	z2 = Theta1 * one_example';
	a2 = sigmoid(z2);

	a2 = [1; a2];

	z3 = Theta2 * a2;
	a3 = sigmoid(z3);

	[max_value, max_index] = max(a3);
	p(c, 1) = max_index;
% =========================================================================


end
