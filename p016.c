#include<stdio.h>

int main() {
	char parts[126];
	parts[125] = 1;
	for(int i=0; i<125; i++)
		parts[i] = 0;
	int part_index = 125;
	int result = 0;

	while(part_index > -1) {
		int remainder = 0;
		for(int i=part_index; i>=0; i--) {
			int dividend = remainder * 256 + parts[i];
			parts[i] = dividend / 10;
			remainder = dividend % 10;
		}
		result += remainder;
		if(parts[part_index] == 0)
			part_index--;
	}

	printf("%d\n", result);
}
