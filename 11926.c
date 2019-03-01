/*
    Would appear that Python can not be used for this one.

    This C solution is a port of Sai Cheemalapati's C++ solution from
    https://saicheems.wordpress.com/2013/08/22/uva-11926-multitasking/.

    NOTE: TO GET THIS WORKING ON UVa YOU HAVE TO USE AN OLD, UGLY,
    VERSION OF C. Apparently you can't do `for (int i = ...)`. Yecch!
*/
#define bool int
#define false 0
#define true 1
#include <stdio.h>
#include <string.h>

#define MAX 1000000
bool schedule[MAX + 1];

bool overlaps(int start, int end) {
    int i;
    for (i = start; i < end; i++) {
        if (schedule[i]) return false;
        schedule[i] = true;
    }
    return true;
}

int main() {
    int m, n, start, end, interval, i;
    while (true) {
        scanf("%d %d", &m, &n);
        if (m + n == 0) break;
        bool conflict = false;

        /* Maybe if Python had something like this.... :) */
        memset(schedule, false, sizeof schedule);

        for (i = 0; i < m; i++) {
            scanf("%d %d", &start, &end);
            if (!conflict && !overlaps(start, end)) conflict = true;
        }
        for (i = 0; i < n; i++) {
            scanf("%d %d %d", &start, &end, &interval);
            while (!conflict && start < MAX) {
                if (!overlaps(start, end)) conflict = true;
                start += interval;
                end += interval;
                if (end > MAX) end = MAX;
            }
        }
        if (!conflict) printf("NO ");
        printf("CONFLICT\n");
    }
    return 0;
}
