#define ARRAY_LENGTH 10
struct point {
    int x;
    int y;
};
int main () {
    struct point a;
    a.x = 3;
    a.y = 4;
    struct point* arr = xmalloc(ARRAY_LENGTH * sizeof(struct point));
    // Initialize the points to be on a line with slope 1
    for (int i = 0; i < ARRAY_LENGTH; i++) {
        arr[i].x = i;
        arr[i].y = i;
    }
}
