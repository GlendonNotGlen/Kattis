#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    int *intArr = (int *)malloc(n * sizeof(int));
    for (int i = n - 1; i >= 0; i--)
    {
        scanf("%d", &(intArr[i]));
    }
    for (int i = 0; i < n - 1; i++)
    {
        printf("%d\n", intArr[i]);
    }
    printf("%d", intArr[n - 1]);

    free(intArr);
}