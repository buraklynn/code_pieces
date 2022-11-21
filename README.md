# feasible_route
Find the feasible route for Electric Vehicle with given combinations.
Combinations are charge stations.
First function checks route is feasible for a combination and return True or False.
Second function return a dictionary. The keys are id of routes and values are id of feasible combinations for the routes.
If first district of a route is first charge station of a combination at the same time, charge is full(40) at the beginning. 
If they are not equal, charge is half(20) at the begining.
