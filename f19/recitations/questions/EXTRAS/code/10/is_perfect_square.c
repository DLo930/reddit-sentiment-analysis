int is_perfect_square(int x) {
    REQUIRES(1 <= x && x <= 10);
    switch (x) {
        case 1:
        case 4:
        case 9:
            return 1;
            break;
        default:
            return 0;
            break;
    }
}

