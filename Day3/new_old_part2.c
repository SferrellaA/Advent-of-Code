#include <stdio.h>

int minX = 0;
int curX = 0;
int maxX = 1;

int minY = 0;
int curY = 0;
int maxY = 0;

int path = 0;

int main(){
	while(path < 25){
		path++;
		printf("%d -- (%d, %d)\n", path, curX, curY);

		// Bottom
		if(curX < maxX && curY == minY){
			curX++;

			// Bottom Right
			if(curX == maxX){
				maxY++;
			}
			continue;
		}

		// Right
		if(curX == maxX && curY < maxY){
			curY++;

			// Top Right
			if(curY == maxY){
				minX--;
			}
			continue;
		}

		// Top
		if(curX > minX && curY == maxY){
			curX--;

			// Top Left
			if(curX == minX){
				minY--;
			}
			continue;
		}

		// Left
		if(curX == minX && curY > minY){
			curY--;

			// Bottom Left
			if(curY == minY){
				maxX++;
			}
			continue;
		}
	}

	return 0;
}