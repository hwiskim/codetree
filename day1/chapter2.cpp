#include <iostream>

using namespace std;

int n;
int r, c;
int a[100][100];
int max_x, max_y;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0 ,1};

bool inRange(int x, int y) {
    return (1 <= x && x <= n) && (1 <= y && y <= n);
}

int main() {
    cin >> n >> r >> c;
    int curr_x = r;
    int curr_y = c;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
        }
    }
    cout << a[curr_x][curr_y];
    while (true){
        bool moved = false;
        for (int i = 0; i < 4; i++){
            int next_x = curr_x + dx[i];
            int next_y = curr_y + dy[i];
            if (inRange(next_x, next_y) && a[next_x][next_y] > a[curr_x][curr_y]) {
                curr_x = next_x;
                curr_y = next_y;
                cout << " " << a[curr_x][curr_y];
                moved = true;
                break;
            }
        }
        if (!moved){
            break;
        }
    }
    
    return 0;
}