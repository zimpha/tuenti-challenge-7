#include <cstdio>
#include <cassert>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

const int N = 500 + 10, M = 1024;

std::vector<std::pair<int, int>> G[N];
std::vector<std::string> cl[M];
std::string name[M];
int dis[N][M], gather[N][M];
bool vis[N][M];
int n, m;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(0);
  int T; std::cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    printf("Case #%d:", cas);
    std::map<std::string, int> color;
    int K; std::cin >> K;
    m = 0;
    for (int i = 0; i < K; ++i) {
      std::cin >> name[i];
      int s; std::cin >> s;
      cl[i].resize(s);
      for (int j = 0; j < s; ++j) {
        std::cin >> cl[i][j];
        assert(color.count(cl[i][j]));
      }
      color[name[i]] = -1;
      if (s == 0) color[name[i]] = 1 << (m++);
    }
    for (int i = 0; i < K; ++i) {
      if (!cl[i].size()) continue;
      color[name[i]] = 0;
      for (auto &&s: cl[i]) color[name[i]] |= color[s];
    }
    m = 1 << m;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
      int E; std::cin >> E;
      G[i].clear();
      std::vector<std::pair<int, int>> valid;
      for (int j = 0; j < E; ++j) {
        std::string X;
        int time;
        std::cin >> X >> time;
        valid.emplace_back(time, color[X]);
      }
      for (int j = 0; j < m; ++j) gather[i][j] = -1;
      gather[i][0] = 0;
      for (int mask = 0; mask < m; ++mask) {
        if (gather[i][mask] == -1) continue;
        for (auto &&e: valid) if ((mask & e.second) != e.second) {
          int new_mask = mask | e.second;
          if (gather[i][new_mask] == -1 || gather[i][new_mask] > gather[i][mask] + e.first) {
            gather[i][new_mask] = gather[i][mask] + e.first;
          }
        }
      }
    }
    int W; std::cin >> W;
    for (int i = 0; i < W; ++i) {
      std::string H;
      int A, B;
      std::cin >> H >> A >> B;
      G[A].emplace_back(B, color[H]);
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        dis[i][j] = -1;
        vis[i][j] = false;
      }
    }
    dis[0][0] = 0;
    std::queue<std::pair<int, int>> Q;
    Q.emplace(0, 0);
    vis[0][0] = true;
    while (!Q.empty()) {
      int u = Q.front().first;
      int c = Q.front().second;
      Q.pop();
      vis[u][c] = false;
      // gather color
      for (int i = 0; i < m; ++i) {
        if (gather[u][i] == -1) continue;
        int mask = i | c;
        if (dis[u][mask] == -1 || dis[u][mask] > dis[u][c] + gather[u][i]) {
          dis[u][mask] = dis[u][c] + gather[u][i];
          if (!vis[u][mask]) vis[u][mask] = true, Q.emplace(u, mask);
        }
      }
      for (auto &&e: G[u]) {
        if ((c & e.second) != e.second) continue;
        int mask = c ^ e.second;
        if (dis[e.first][mask] == -1 || dis[e.first][mask] > dis[u][c]) {
          dis[e.first][mask] = dis[u][c];
          if (!vis[e.first][mask]) vis[e.first][mask] = true, Q.emplace(e.first, mask);
        }
      }
    }
    for (int i = 0; i < n; ++i) {
      int ret = -1;
      for (int mask = 0; mask < m; ++mask) {
        if (dis[i][mask] == -1) continue;
        if (ret == -1 || ret > dis[i][mask]) ret = dis[i][mask];
      }
      printf(" %d", ret);
    }
    puts("");
  }
  return 0;
}
