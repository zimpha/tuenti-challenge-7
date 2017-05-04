#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>

using ll = long long;

const int N = 5000 + 10;
std::vector<std::pair<int, ll>> G[N];

int main() {
  int T;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    printf("Case #%d: ", cas);
    ll F;
    int S;
    scanf("%lld%d", &F, &S);
    std::vector<ll> xs = {1ll, F};
    std::vector<ll> A(S), B(S), Y(S);
    for (int i = 0; i < S; ++i) {
      scanf("%lld%lld%lld", &A[i], &B[i], &Y[i]);
      xs.push_back(A[i]);
      xs.push_back(B[i]);
    }
    std::sort(xs.begin(), xs.end());
    xs.erase(std::unique(xs.begin(), xs.end()), xs.end());
    int n = xs.size();
    for (int i = 0; i < n; ++i) G[i].clear();
    for (int i = 0; i + 1 < n; ++i) {
      ll a = xs[i], b = xs[i + 1] - 1;
      G[i].emplace_back(i + 1, (a + b) * (b - a + 1) / 2);
      for (int j = 0; j < i; ++j) {
        G[i].emplace_back(j, 0);
      }
    }
    for (int i = 0; i < S; ++i) {
      int a = std::lower_bound(xs.begin(), xs.end(), A[i]) - xs.begin();
      int b = std::lower_bound(xs.begin(), xs.end(), B[i]) - xs.begin();
      G[a].emplace_back(b, Y[i]);
    }
    std::vector<ll> dis(n, -1);
    std::vector<bool> vis(n, false);
    dis[0] = 0;
    vis[0] = true;
    std::queue<int> Q;
    Q.push(0);
    while (!Q.empty()) {
      int u = Q.front();
      vis[u] = false;
      Q.pop();
      for (auto &&e: G[u]) {
        int v = e.first;
        ll w = e.second;
        if (dis[v] == -1 || dis[v] > dis[u] + w) {
          dis[v] = dis[u] + w;
          if (!vis[v]) vis[v] = true, Q.push(v);
        }
      }
    }
    printf("%lld\n", dis[n - 1]);
  }
  return 0;
}
