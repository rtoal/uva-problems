#include <stdio.h>

int main() {
    int quote_count = 0;
    char c;
    while (scanf("%c", &c) == 1) {
        if (c == '"') {
            printf(++quote_count % 2 == 0 ? "''" : "``");
        } else {
            printf("%c", c);
        }
    }
    return 0;
}
