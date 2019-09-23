#include <iostream>
#include <cstdio>

int main() {
	int a[10001];
	int b, c, i, j;

	scanf("%d", &b);

	for (i=0; i<b; i++) {
		scanf("%d", &c);
		a[c] += 1;
	}

	for (i=0; i<10001; i++) {
		for (j = 0; j < a[i]; j++) {
			printf("%d\n", a[i]);
		}
	)

	return 0;
}