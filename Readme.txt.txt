---SHUBHAM KAKADE---
	
	I have used python for this project which provided some inbuild libraries to store complex numbers and also calculate the math computation easily. For task 2 and 3 I have 
	used common FFT function as it remains same for both which removed the code redundancy. Basically all the tasks are performed in single python script and using command line
	we can perform all of them easily ex " python project1 DFT-Horner inputfile.txt outputfile.txt".
		





Task 1): DFT-Horner

	DFT-Horner is basically an O(n^2) algorithm to evaluate the polynomial on n points. So in this task we are provided with polynomial with it's coefficients as an input and we need 	to evaluate it at nth roots of unity. So for given length n as an input we see n length output which are points. DFT-Horner is an efficient way to evaluate polynomials as the trick 	is if we have polynomial ex: P(x)=a0​+a1​x+a2​x2+⋯+an−1​xn−1 it can be written in the form of P(x)=(((an−1​⋅x+an−2​)⋅x+an−3​)⋅x+⋯+a1​)⋅x+a0​ which helps us to get time complexity O(n^2).
	My approach was to use two for loops the outer to iterate through all nth roots of unity and inner to loop through coefficients and get the point for each root. In my code 
	to represent the complex number I made use of "complex" data type which is capable of storing it and also some basic functions of files to read and write. I have expanded the
	omega representation wiht e^i*theta = cos(theta) + i*sin(Theta) so I used math library to compute the thetas which makes it look simple to understand ans also I have made sure 
	that if we get -0.000 as an imaginary part which usually comes due to omega multiplication wind it up to 0.000 so it makes more sense.



Task 2a): FFT

	FFT is basically an divide and conquer algorithm which effeciently performs DFT with O(nlogn) running time which is much less that DFT-Horner. The key insight is to know the math 
	which makes this algorithm much faster. Let's go through the example and find it out how actually it works. Lets say we have polynomial of degree 3 so n=4 and we need to compute 
	points on 4th roots of unity which is {1,i,-1,-i} now using partition if p(x) = 1+x+2x^2+5x^3  it can be written as p(x) = (1+2x^2) + x(1+5x^2) , p(-x)=(1+2x^2) - x(1+5x^2) and we 	can evaluate at four points(1,i,-1,-i) using just 2 points which are(1,i). But now when we make recursive call to get evluation at (1,i) but we dont have such pair of +- so that we 	can make further recursive calls. Here comes the math in which some fundamental properties of nth roots of unity which helps us compute or make the recursive calls further. Like 	evaluating the polynomila at such points by changing the degrees of polynomial itself such that using single value we can compute it at 2 values thus reducing the time. 

	
	In the code I have used the recurisve divide and conquer approach and made sure of things like the "n" should be in the order of power of 2 as FFT works only with power 2 n which  	requires padding and I have also used numpy to compute the (w) omega.


Task2b): IFFT
	
	
	IFFT is same as FFT with some minute changes like the points here we take are inverse so is why we take omega with negative power to make sure we are taking inverse of matrix 	multiplication and finally divide coefficients by n. This task also uses same function as FFT so the running time remains same as FFT.


Task3): Multiplication

	In this task we make combine task 2a and 2b and perform FFT first for both polynomials get the points the  multiply them to get points for result polunomial and then perform
	IFFT to get the coefficients of product polynomial.