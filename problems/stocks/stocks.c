#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))

int maxProfit(int k, int* prices, int n) {

  if (n < 2) return 0;

  if (k > n/2) {
    int result = 0;
    for (int i = 1; i < n; i++) {
      result += max(prices[i] - prices[i-1], 0);
    }
    return result;
  }

  int d[k+1][n+1];
  memset(d, 0, (k+1)*(n+1)*sizeof(int));
  for(int i = 1; i <= k; i++) {
    int t = d[i-1][0] - prices[0];
    for (int j = 1; j <= n; j++) {
      d[i][j] = max(d[i][j-1], t + prices[j-1]);
      if (j < n) {
        t = max(t, d[i-1][j] - prices[j]);
      }
    }
  }

  return d[k][n];

}

int main() {
  int k;
  int n;
  scanf("%d %d", &k, &n);
  int* prices = malloc(n * sizeof(int));
  for (int i = 0; i < n; i++) {
    scanf("%d", prices + i);
  }
  int p = maxProfit(k, prices, n);
  printf("%d\n", p);
  return 0;
}
