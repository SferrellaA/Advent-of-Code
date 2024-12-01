#include <stdio.h>
#include <stdlib.h>


void thing(int input){

	// Set up variables
	int x = 0;
	int y = 0;
	int path = 0;
	int even = 0;

	// Find the nearest perfect square
	int nps = 1;
	while(1){
		if(input == nps*nps){
			break;
		}		
		if(input < nps*nps){
			nps--;
			break;
		}
		nps++;
	}
	path = nps * nps;

	printf("nps: %d\n", nps);
	if(nps % 2 == 0) {	// NPS is even
		printf("nps is even\n");
		even = 1;
	} else {			// NPS is odd
		printf("nps is odd\n");
		even = 0;
	}

	// Check if inout is perfect square
	if(input == path){
		if(even){
			printf("I am an even perfect square\n");
			y = nps / 2;
			x = 1 - y;
			if(input == 1){ // bleh...
				x = 0;
			}
		} else {
			printf("I am an odd perfect square\n");
			x = nps / 2;
			y = -x;
		}
		printf("Perfect square %d is at (%d, %d).\n", input, x, y);
		return;
	} 

	// Is the input closer to nearest or next perfect square?
	int half = ((nps + 1) * (nps + 1) - path - 1) / 2;
	if(input > path + half){
		path += half + 1;
		if(even){
			x = 0 - nps / 2;
		} else {
			x = (nps - 1) / 2 + 1;
		}
		y = x;
	} else {
		path++;
		if(even){
			y = nps / 2 ;
			x = -y;
		} else {
			y = (1 - nps) / 2; 
			x = (nps + 1) / 2;
		}
	}
}

// This needs to be four functions that are called once the closet corner is determined
// I'm moving this to version 2
void thing2X(int x, int y, int x2, int path){
	for(; x < x2; )


	// Test
	printf("Reached %d at (%d, %d).\n", path, x, y);
}


int main(int argc, char *argv[]){
	thing(atoi(argv[1]));
	return argc*0;
}
