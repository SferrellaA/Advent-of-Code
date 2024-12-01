#include <stdio.h>
#include <stdlib.h>

// Coordinates
int x = 0;
int y = 0;

// Say the findings you have so far
void say_findings(int final){

	printf("%d is at (%d, %d)\n", final, x, y);

	// Get the manhattan distance
	if(x < 0){
		x *= -1;
	}
	if(y < 0){
		y *= -1;
	}	
	printf("Manhattan distance is %d\n", x + y);
}

// Find the nearest, smaller, perfect square
int nearest_perfect_square(int input){
	int nps = 1;
	while(1){
		if(nps * nps >= input){
			if(nps * nps > input)
				nps--;
			break;
		}
		nps++;
	}
	return nps;
}

// Check if the nps is even or odd
int nps_is_even(int nps){
	if(nps % 2 == 0){
		return 1;
	} 
	return 0;
}

// Check if the input is a perfect square
int check_perfect_square(int input, int nps, int even){

	// Check if input is perfect square
	if(input == nps * nps){

		// Find the coordinates of input
		if(even){
			y = nps / 2;
			x = 1 - y;
			if(input == 1){ // bleh...
				x = 0;
			}
		} else {
			x = nps / 2;
			y = 0 - x;
		}

		// Perfect square
		return 1;
	}

	// Not a perfect square
	return 0;
}


// Find the coordinates of the input
void find_coordinates(int input, int nps, int even){

	// Distance of nearest perfect square
	int path = nps * nps;

	// Distance to halfway to next perfect square	
	int half = ((nps + 1) * (nps + 1) - path - 1) / 2;

	// Do the thing
	if(input > path + half){
		path += half + 1;
		if(even){ // bottom left
			x = 0 - nps / 2;
			y = x + (input - path);
		} else { // top right
			y = (nps - 1) / 2 + 1 ;
			x = y - (input - path);;
		}
	} else {
		path++;
		if(even){ // top left
			y = 0 - nps / 2; //(nps / 2) - (input - path);
			x = -y;
		} else { // bottom right
			y = (1 - nps) / 2 + (input - path);
			x = (nps + 1) / 2;
		}
	}
}

// The main function
int main(int argc, char *argv[]){
	// Get the number to check
	int input = atoi(argv[1]);

	// Find the nearest perfect square
	int nps = nearest_perfect_square(input);

	// Check if the nps is even (1) or odd (0)
	int even = nps_is_even(nps);

	// Check if the input is not a perfect square
	if(!check_perfect_square(input, nps, even)){
		// Find what the coordinates are
		find_coordinates(input, nps, even);
	} 

	// Report findings
	say_findings(input);
	return argc * 0;
}


