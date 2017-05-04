#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>

const uint64_t mask = 6148914691236517205ll;

uint64_t f(int64_t n) {
  if (n >= (1ll << 32)) return 0;
  return (((n + 1) & mask) >> 1) | ((n * (n + 1) / 2) & mask);
}

bool solve(uint64_t n) {
  uint64_t odd = n & ~mask;
  if (odd > (1ll << 32)) return false;
  std::vector<int> p = {0};
  for (int i = 1; i < 32; i += 2) {
    p.push_back(i);
  }
  int m = p.size();
  for (int mask = 0; mask < (1 << m); ++mask) {
    uint64_t now = odd << 1;
    for (int i = 0; i < m; ++i) {
      if (mask >> i & 1) now |= 1ll << p[i];
    }
    if (f(now - 1) == n) {
      std::cout << now - 1 << std::endl;
      return true;
    }
  }
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    printf("Case #%d: ", cas);
    uint64_t n;
    std::cin >> n;
    if (!solve(n)) puts("IMPOSSIBLE");
  }
  return 0;
}
