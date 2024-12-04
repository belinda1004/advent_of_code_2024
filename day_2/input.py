input = """
10 11 13 16 15
3 6 9 10 11 12 12
43 46 49 52 54 58
59 60 61 63 65 68 75
60 62 63 65 63 66 69 71
80 83 85 88 85 87 84
30 31 32 31 33 33
9 11 14 12 16
38 39 40 43 42 45 50
58 61 63 63 66
15 17 18 20 20 21 23 21
17 19 22 24 25 25 28 28
60 63 66 67 67 69 73
42 44 44 45 52
22 23 27 30 32 34
22 23 25 26 28 31 35 33
11 14 16 19 22 26 26
38 41 44 48 52
15 17 21 24 26 33
50 51 54 61 62 65 68
37 40 42 44 49 50 47
6 7 8 14 14
17 20 25 27 31
68 69 70 73 76 81 87
83 81 82 83 85 87 90 92
52 51 54 56 58 57
93 90 91 92 92
12 9 10 12 14 15 16 20
26 24 26 27 33
17 15 14 17 19
99 96 97 96 97 99 98
9 7 5 8 8
59 58 61 63 62 64 68
24 23 25 28 26 28 35
93 90 92 94 94 95
72 69 72 73 76 77 77 75
46 45 47 47 49 49
61 60 63 64 64 66 70
35 32 35 36 37 37 40 47
6 3 6 9 13 15 16
29 28 31 33 35 36 40 38
22 21 25 26 26
51 50 51 54 58 60 64
83 82 86 88 95
79 76 83 86 89
19 17 23 25 26 25
19 18 21 28 30 31 31
72 70 72 73 74 77 82 86
40 39 40 47 53
7 7 9 12 15 18 19
57 57 59 62 63 65 63
57 57 59 62 65 66 66
26 26 29 31 33 34 38
44 44 47 50 52 59
19 19 21 20 22 25 27
76 76 79 77 74
61 61 64 63 65 65
80 80 81 83 85 83 87
63 63 66 67 65 71
48 48 48 50 51 53 56 58
17 17 17 18 17
66 66 68 68 68
78 78 79 79 83
1 1 3 4 7 8 8 13
14 14 18 20 21
22 22 25 27 31 28
32 32 34 38 38
49 49 51 52 54 56 60 64
85 85 89 91 93 94 99
28 28 29 30 35 38 39
10 10 11 18 20 22 25 24
87 87 90 96 96
47 47 48 51 58 62
7 7 8 9 11 12 18 25
70 74 75 77 79 82
27 31 32 33 34 35 37 34
45 49 52 55 57 60 62 62
39 43 44 47 50 51 55
42 46 49 50 53 54 59
5 9 12 10 12
69 73 74 73 74 75 72
76 80 82 84 81 84 84
29 33 31 33 35 39
49 53 54 55 56 57 54 59
42 46 46 47 50 52
65 69 69 72 70
72 76 76 78 80 82 83 83
45 49 52 53 53 57
37 41 42 45 45 50
56 60 62 63 67 68
35 39 40 43 46 49 53 51
7 11 15 17 20 21 24 24
2 6 7 9 13 17
43 47 50 52 56 59 64
12 16 19 22 28 30 33
43 47 48 53 54 57 55
83 87 88 95 95
57 61 63 64 66 73 75 79
57 61 64 69 71 76
86 93 95 96 97 99
30 35 37 39 38
11 17 19 20 20
20 26 29 32 36
68 73 74 77 80 87
37 42 44 43 46 49 50 51
48 55 58 56 57 58 57
36 42 39 42 43 44 44
20 25 28 25 27 29 31 35
14 20 23 21 22 23 25 32
77 82 83 83 84 86 88 91
30 36 37 40 40 42 43 42
15 21 22 25 27 27 28 28
46 52 55 55 56 58 62
15 22 23 23 24 27 34
22 29 30 34 37
5 11 14 18 20 18
7 12 16 18 21 22 22
39 45 47 51 54 56 58 62
57 63 67 70 71 76
72 79 84 86 87 90
80 85 92 93 96 93
72 78 83 84 84
46 52 55 57 58 64 68
69 75 78 80 87 93
89 88 85 82 80 77 74 75
14 13 11 9 8 5 2 2
93 91 88 86 83 79
39 37 35 34 32 30 28 21
52 51 52 49 47 45
96 95 94 93 90 88 91 93
35 34 36 35 34 33 33
39 37 38 37 34 32 31 27
24 23 24 22 16
60 57 57 54 53 52 50 48
36 35 34 33 33 32 31 34
76 74 71 71 71
32 29 28 26 23 23 19
91 88 86 86 83 77
42 41 39 35 33
27 24 22 18 19
19 16 15 13 10 6 6
50 49 45 43 41 38 34
48 46 45 41 34
83 80 78 77 71 68
46 44 38 37 39
39 38 37 31 29 27 27
21 19 18 16 15 9 5
81 79 78 71 69 66 63 56
69 71 68 67 66 65
11 12 11 10 7 10
83 84 83 81 78 77 75 75
19 20 18 15 14 12 11 7
80 81 80 77 75 69
17 19 20 17 16 15
45 48 47 44 41 44 41 42
40 43 41 44 44
56 57 59 57 53
93 96 99 96 93 91 88 83
79 80 78 75 73 73 72
4 7 4 4 3 4
65 66 65 65 62 60 58 58
43 45 44 44 40
81 83 82 82 81 76
92 95 91 89 88 87
30 31 27 24 26
20 22 21 18 15 11 11
31 32 31 27 26 24 21 17
43 46 45 44 42 40 36 31
47 50 48 47 46 40 37 36
23 26 24 22 16 15 12 13
86 88 86 84 81 80 75 75
88 90 88 87 82 80 76
83 85 80 77 75 70
13 13 12 10 8 5 3 1
48 48 46 44 41 43
86 86 83 81 78 78
82 82 81 80 77 73
23 23 20 19 18 16 14 7
76 76 75 73 71 73 71
41 41 39 38 35 37 39
98 98 96 94 92 93 93
49 49 48 51 47
79 79 81 80 77 75 72 67
37 37 36 35 35 32
18 18 17 15 15 13 15
6 6 6 4 4
35 35 34 33 33 29
71 71 70 70 69 67 62
91 91 89 85 82 79 77
62 62 60 56 58
16 16 14 11 7 7
88 88 86 82 78
88 88 86 85 81 78 73
21 21 19 18 11 8
12 12 6 4 6
79 79 74 71 71
65 65 60 59 55
45 45 43 40 38 33 28
44 40 37 36 34 33 32 31
15 11 8 7 9
83 79 77 74 74
68 64 62 60 59 55
77 73 71 68 67 64 61 55
56 52 50 49 47 49 48
74 70 67 70 68 66 68
56 52 54 52 49 47 47
31 27 25 26 23 21 20 16
89 85 83 86 81
38 34 34 31 28 26 24
48 44 43 40 38 38 40
23 19 19 17 16 15 15
93 89 88 87 86 86 82
91 87 85 85 82 77
58 54 50 48 46 44 41
90 86 82 80 77 76 77
83 79 77 73 73
52 48 47 43 39
38 34 30 27 21
98 94 93 92 85 82
63 59 53 51 52
69 65 63 61 56 55 55
84 80 75 74 70
68 64 58 55 54 49
28 23 22 19 17 16
27 20 19 16 14 17
78 73 72 69 66 66
23 18 16 13 11 8 7 3
29 22 19 18 15 12 10 3
26 21 23 21 18 15 13 12
48 43 44 41 38 35 36
20 15 12 10 7 9 9
37 30 28 25 23 25 21
24 18 19 16 14 7
38 31 30 30 29 26
11 5 5 2 4
74 67 64 63 62 62 60 60
95 90 88 87 87 84 80
36 29 26 25 25 22 19 13
70 64 60 59 57 56
93 87 83 80 78 77 78
77 72 68 65 65
65 58 54 53 50 48 44
91 84 80 77 75 74 69
84 77 76 71 69 68
74 67 65 59 61
58 52 50 45 45
49 43 41 40 34 33 31 27
78 71 70 63 58
32 33 36 39 37
29 30 32 35 36 37 38 38
5 7 9 10 13 17
36 37 39 41 42 44 50
62 64 65 66 69 68 71
27 29 26 29 31 34 32
34 37 39 40 43 41 41
36 39 42 43 45 44 45 49
78 80 81 80 82 83 89
7 9 12 12 13 16 18
32 35 36 36 38 35
10 11 11 13 13
43 44 44 46 48 52
49 51 53 55 56 56 63
14 16 18 20 24 27 28 29
64 65 69 70 72 73 76 73
63 66 69 70 72 76 76
33 35 39 40 41 42 46
13 15 18 21 25 32
31 33 35 36 39 44 47
56 57 62 65 66 69 66
18 21 22 23 28 28
67 68 69 72 78 82
81 83 84 89 92 99
54 51 54 55 57 58
56 54 57 59 61 62 61
62 61 63 66 67 68 68
40 37 38 40 43 46 48 52
37 34 37 38 39 42 45 52
6 4 6 9 7 8 10
31 30 32 31 28
94 92 93 96 98 97 99 99
70 69 72 71 75
18 15 17 16 23
75 72 72 75 78 81
33 30 32 32 35 36 35
51 50 52 53 53 53
53 51 54 54 58
37 34 34 35 38 45
17 14 17 21 23 24 26
71 69 72 74 78 80 82 80
15 13 17 19 19
80 78 80 84 86 90
25 22 26 29 34
83 82 88 89 92 95 96
53 51 52 53 54 60 59
35 34 39 40 41 41
65 62 67 70 73 76 79 83
82 80 82 83 88 91 97
65 65 67 69 70 73 74 75
22 22 23 25 27 26
69 69 72 75 78 81 82 82
40 40 43 44 46 49 50 54
81 81 84 87 89 96
4 4 7 4 7 10
73 73 70 73 70
86 86 87 86 86
72 72 74 73 77
7 7 9 10 7 9 11 16
54 54 57 57 58
53 53 56 57 59 62 62 59
74 74 76 76 76
80 80 82 83 83 86 90
2 2 2 4 9
88 88 90 93 97 98 99
32 32 36 37 34
72 72 74 78 78
32 32 36 37 40 41 42 46
12 12 15 19 21 26
3 3 9 10 11 13
23 23 30 32 30
58 58 65 67 69 69
39 39 42 43 49 50 51 55
9 9 10 17 19 22 27
82 86 89 92 93 96
34 38 40 42 44 46 45
22 26 28 29 29
52 56 59 62 65 66 70
61 65 68 71 74 75 77 83
38 42 39 41 44 47 50
63 67 68 70 68 71 68
33 37 38 36 38 38
3 7 10 12 11 14 18
21 25 27 25 27 32
45 49 49 50 52 55
27 31 33 33 34 31
8 12 13 13 15 17 17
6 10 10 11 14 16 20
65 69 72 72 75 76 82
86 90 94 96 99
47 51 55 57 60 62 59
63 67 69 72 74 78 79 79
13 17 18 22 23 27
58 62 65 66 67 71 78
66 70 72 74 76 78 83 84
27 31 32 37 40 38
57 61 63 68 68
27 31 34 36 42 43 47
38 42 43 44 46 49 55 60
4 9 11 12 14 16
20 26 27 29 32 30
75 81 84 86 87 90 90
16 22 23 26 30
9 15 16 19 22 25 28 34
26 33 32 35 38
1 8 10 12 9 6
6 12 15 13 14 16 19 19
80 85 88 89 91 93 90 94
59 65 68 69 67 73
8 14 16 18 19 21 21 24
85 90 91 92 92 93 92
32 38 38 41 43 46 47 47
53 60 61 62 62 64 67 71
67 73 75 78 78 81 88
61 67 70 74 77 78 79 80
67 74 78 79 81 80
24 29 31 35 38 38
7 12 16 19 23
13 19 20 24 27 28 29 35
53 60 63 70 72
69 75 78 79 86 88 86
3 10 12 13 20 20
31 36 39 41 46 50
64 71 77 79 82 84 90
83 80 77 74 75
99 97 94 92 89 86 83 83
59 57 55 53 49
77 75 74 73 67
10 8 5 4 2 4 3 1
37 34 33 36 35 34 36
55 52 51 53 53
30 27 24 23 24 23 21 17
84 83 86 85 78
36 34 33 33 31
19 16 16 14 13 14
80 78 76 76 76
70 68 66 64 64 61 60 56
84 81 80 79 79 73
93 91 88 84 83
63 61 57 56 53 52 50 51
85 84 80 77 77
85 84 82 81 77 74 70
21 20 16 15 12 9 2
41 39 38 32 31 28
82 81 80 74 76
64 61 55 54 53 50 50
39 36 31 28 26 22
78 75 68 65 60
96 97 95 92 89 88 86 84
97 98 96 94 97
86 89 87 84 84
58 61 58 56 52
72 73 72 70 69 68 67 60
33 34 35 32 29 28
62 65 63 61 60 59 61 63
33 36 39 36 34 31 31
48 50 49 52 50 46
17 20 22 20 19 12
65 66 65 64 64 62 59
84 85 84 84 85
31 32 31 28 26 26 26
63 66 64 61 61 58 57 53
66 69 68 66 66 60
20 23 19 16 15
85 86 83 81 77 74 75
49 50 48 44 44
54 57 53 51 47
45 46 42 39 38 36 29
29 32 30 29 24 21 18 17
19 22 21 16 15 13 14
76 77 72 71 68 65 64 64
86 87 85 83 77 76 72
62 63 61 60 57 54 47 41
36 36 35 33 32 30 28 25
98 98 96 93 96
72 72 71 68 67 65 62 62
29 29 26 23 21 19 17 13
41 41 39 37 36 29
36 36 33 30 27 29 28
77 77 78 75 72 71 73
56 56 53 52 49 48 50 50
75 75 77 74 70
78 78 79 77 74 73 71 66
30 30 29 26 25 22 22 19
43 43 43 41 38 36 37
18 18 18 17 16 15 13 13
55 55 52 51 48 48 44
65 65 63 63 62 60 54
58 58 54 51 50
51 51 50 46 49
63 63 62 59 57 53 53
68 68 64 61 58 55 54 50
32 32 30 27 26 22 21 15
66 66 60 57 54 51 49 47
84 84 81 78 72 75
81 81 75 74 74
49 49 46 44 42 41 35 31
41 41 39 38 32 30 23
98 94 91 88 86 85 83
66 62 60 58 59
66 62 59 58 58
63 59 58 55 54 53 50 46
69 65 62 59 58 55 48
37 33 36 34 31
53 49 48 46 44 47 49
97 93 92 94 91 89 86 86
76 72 71 70 73 72 68
39 35 33 31 34 27
70 66 65 65 64
89 85 84 83 82 80 80 81
77 73 70 68 68 68
66 62 59 58 58 57 53
43 39 36 36 33 32 25
79 75 72 70 66 65
71 67 65 62 58 56 53 55
82 78 75 71 71
40 36 32 31 29 28 27 23
91 87 86 83 82 78 72
76 72 70 69 64 63 60 57
69 65 60 57 59
24 20 18 17 14 8 8
43 39 37 34 32 31 24 20
74 70 63 62 60 54
21 16 13 12 11 10 8
79 73 72 69 66 63 60 61
30 25 23 21 19 19
63 57 55 52 49 47 46 42
26 19 18 17 16 14 7
60 54 56 53 52 49
42 37 36 39 38 37 35 36
81 76 79 77 74 74
27 20 19 18 15 12 15 11
58 53 52 53 50 44
17 12 10 9 8 7 7 5
26 21 20 20 21
99 93 90 87 87 84 82 82
31 24 21 18 15 12 12 8
36 31 29 27 26 26 19
32 27 26 22 20 18
75 68 64 61 59 62
22 15 13 9 9
64 58 57 53 49
47 42 40 36 33 30 28 23
19 12 10 4 3
20 14 11 10 9 7 1 4
16 10 5 4 2 2
88 83 78 75 71
98 92 87 86 83 81 75
70 72 74 77 75
36 38 40 43 46 46
40 42 44 45 47 48 49 53
73 75 77 80 82 89
67 69 67 68 71
80 83 85 87 89 87 84
71 73 74 71 74 74
31 34 36 33 34 35 39
77 80 79 82 83 84 90
19 22 25 25 27 28
74 76 77 77 78 79 82 79
91 94 94 95 95
66 69 70 71 71 72 76
44 47 49 52 52 58
4 6 7 11 14 16 18
80 81 85 87 89 88
81 84 86 90 93 93
5 8 10 12 14 18 22
15 16 20 21 26
16 19 24 26 27
81 83 86 88 93 94 91
61 62 63 66 71 74 74
13 14 16 23 27
46 47 53 54 57 63
34 33 36 38 41 43 46 48
50 47 49 52 55 56 58 57
10 9 10 12 12
36 33 34 35 37 39 40 44
68 66 67 69 71 74 80
83 80 81 79 80 81
78 76 78 79 78 80 83 80
56 53 56 54 57 57
31 28 29 31 30 34
62 59 56 58 63
6 5 7 7 9
22 19 21 23 23 24 21
31 28 30 33 34 36 36 36
65 64 65 68 68 70 71 75
7 6 8 11 11 12 13 18
60 58 59 61 63 65 69 72
48 46 47 49 53 51
78 77 81 84 86 88 88
15 13 15 16 19 23 27
48 46 50 52 54 55 58 63
18 16 18 19 25 27 29
71 68 69 72 73 80 82 80
68 66 68 70 77 77
75 74 76 79 85 86 90
69 67 70 72 74 81 83 89
66 66 67 70 72 73
6 6 9 11 10
15 15 16 19 19
53 53 54 57 58 62
79 79 82 85 91
25 25 23 25 28 29
1 1 3 1 4 1
80 80 81 82 80 82 85 85
36 36 38 41 40 41 45
8 8 10 13 16 13 16 21
7 7 7 10 12 13 15 18
39 39 41 43 43 46 48 45
10 10 13 13 14 17 17
71 71 72 74 76 76 80
53 53 56 59 59 65
19 19 23 26 28 29 32
67 67 68 69 71 75 74
62 62 65 69 71 73 74 74
42 42 46 48 49 51 55
47 47 51 53 56 58 63
54 54 61 64 65
77 77 84 85 87 84
15 15 20 23 24 25 25
87 87 94 95 99
17 17 22 24 29
42 46 47 49 51 54 55 57
54 58 59 62 59
60 64 66 67 69 71 73 73
6 10 11 14 15 18 22
46 50 52 55 58 61 68
13 17 20 23 22 25 28
35 39 40 43 46 45 44
24 28 31 29 32 32
24 28 30 31 30 33 36 40
75 79 80 81 78 79 85
23 27 27 29 30
47 51 52 52 53 51
34 38 38 41 43 44 46 46
61 65 66 66 70
86 90 91 91 97
5 9 11 13 15 18 22 24
70 74 77 81 83 81
5 9 12 16 19 19
61 65 66 70 72 75 79
59 63 67 70 73 78
12 16 18 24 27
19 23 25 26 28 33 36 33
78 82 87 89 91 91
76 80 83 88 92
8 12 14 21 28
24 29 30 32 33 34 36
51 58 60 61 62 63 61
38 45 47 50 50
57 63 64 66 67 68 72
6 12 14 15 18 20 26
5 10 9 12 14
50 55 52 53 51
16 21 18 20 23 25 25
9 14 11 14 18
72 79 80 82 80 81 82 87
85 91 92 92 93 94
85 91 91 93 92
3 8 10 10 11 11
12 19 19 21 25
40 47 48 51 52 54 54 61
78 83 84 88 90 92 93 95
48 54 57 61 58
76 81 82 85 89 89
56 63 64 65 68 72 76
64 71 72 75 76 80 85
38 45 50 53 54 56
56 61 62 67 69 70 67
45 51 54 59 60 62 64 64
2 8 11 18 19 23
60 67 70 71 73 80 82 89
65 63 61 59 60
85 82 79 76 73 71 69 69
18 17 14 11 8 6 5 1
20 18 16 15 13 12 7
61 60 58 56 53 54 51
54 51 54 52 51 52
14 12 11 8 11 8 7 7
81 78 77 76 78 75 72 68
17 15 13 12 15 10
44 43 41 39 39 38 37
63 61 58 57 57 55 56
82 80 79 77 75 73 73 73
98 95 92 92 88
54 52 52 51 49 46 41
16 15 14 12 8 6 5
44 41 37 36 37
39 36 34 32 28 27 24 24
94 92 89 85 84 80
61 60 56 54 51 49 48 42
50 48 42 41 39
92 90 89 87 80 82
57 54 48 45 44 41 39 39
67 66 64 59 57 53
49 47 45 38 36 35 30
97 98 95 93 90 89 87 86
24 26 24 21 24
37 39 37 36 33 30 30
61 63 60 59 58 54
63 66 64 62 56
68 71 70 72 71 70
88 89 92 91 89 91
28 29 28 27 30 28 28
21 22 24 22 20 19 15
91 92 95 92 85
68 71 70 69 68 68 66 63
73 76 73 72 70 67 67 70
38 41 38 38 37 37
71 73 72 72 71 68 65 61
17 19 16 15 15 14 7
38 40 37 35 34 30 28 27
11 12 10 8 4 6
89 92 91 88 84 81 81
80 81 79 76 72 68
51 52 50 48 44 39
35 37 34 27 25
60 63 61 56 55 58
47 48 43 42 39 39
24 26 19 17 13
68 69 67 62 60 53
95 95 94 92 89
80 80 77 76 74 72 70 72
81 81 78 75 75
99 99 98 97 96 95 93 89
16 16 14 13 12 7
98 98 95 92 90 93 92
92 92 95 92 89 92
41 41 38 41 40 40
50 50 48 50 46
21 21 22 19 16 14 9
49 49 49 47 44 41 38
74 74 72 71 71 72
10 10 8 6 3 3 2 2
71 71 69 66 65 65 63 59
81 81 81 80 75
20 20 16 14 13
46 46 42 40 39 38 39
9 9 8 7 3 3
76 76 72 71 69 68 67 63
47 47 46 44 40 39 34
25 25 22 21 16 14
78 78 72 71 68 67 70
26 26 20 17 17
21 21 14 11 10 6
63 63 56 55 53 51 50 43
95 91 90 88 86 84 83 81
54 50 48 46 43 45
84 80 78 76 76
44 40 37 36 34 30
32 28 26 25 23 18
29 25 24 23 24 22 21 20
77 73 70 67 70 68 69
60 56 58 56 54 53 51 51
92 88 85 84 86 82
62 58 55 53 52 54 53 46
45 41 41 38 37 35
38 34 31 31 33
71 67 65 65 65
27 23 20 18 15 15 11
82 78 78 75 74 71 70 64
80 76 74 72 70 66 65
56 52 51 47 46 43 41 44
71 67 65 61 61
81 77 74 73 69 65
98 94 92 91 88 84 79
41 37 35 30 27
88 84 81 80 75 77
34 30 27 25 24 19 19
54 50 48 45 43 38 36 32
64 60 59 54 52 45
93 88 86 85 82
54 47 46 43 46
26 21 19 18 18
24 18 15 13 12 9 6 2
73 68 66 63 60 57 54 49
62 56 55 56 54 51 50
65 58 56 59 57 54 52 55
92 87 86 85 82 85 85
15 9 7 10 6
73 66 63 62 61 64 59
77 71 70 67 67 66 63
65 60 57 55 55 53 56
76 70 70 68 66 65 62 62
37 30 28 28 27 25 22 18
43 38 35 35 32 25
93 87 83 81 79 76
72 66 62 61 60 57 60
78 73 69 67 67
96 90 87 83 79
53 46 45 41 35
74 68 66 61 58
96 90 84 81 79 76 79
90 83 82 77 76 76
98 92 86 83 82 78
63 58 55 54 52 45 44 38
66 71 71 72 74 75 77
6 4 6 10 13 14 14
42 40 39 36 31 25
45 44 46 45 44 43 42 38
37 39 40 43 45 46 46
15 11 8 7 3 1 3
53 53 52 51 47
24 19 18 13 7
39 35 34 33 30 27 20
32 32 30 26 29
75 75 80 83 85 88 88
26 26 30 32 33 34 37
46 46 48 47 42
46 41 39 36 32 31 27
91 88 86 83 80 73
71 67 66 63 59
41 45 47 46 47 50 51
43 37 35 36 32
8 9 10 10 12 13 15 20
28 28 29 30 30 31 34 38
66 69 66 63 65 66
98 94 91 87 86 86
35 34 33 33 32
9 6 6 7 8 13
7 10 12 15 17 19 24 24
52 48 51 49 43
97 98 91 88 85 83 82 78
79 79 78 75 70 70
47 43 40 39 36 32 28
11 8 7 4 1 1
37 36 39 39 41 42 45 47
58 58 58 57 54 53 50 48
25 25 24 23 18
49 47 44 38 37 36 34 36
33 32 37 38 40 42 43
12 19 24 25 26
38 40 41 42 45 46 49 55
64 60 57 56 56 54 51 49
47 47 49 52 53 60 62 67
28 31 27 24 21 19 22
38 45 48 51 51 56
73 70 70 68 64
82 82 81 79 77 72 73
43 45 48 50 53 56 58 59
60 63 64 67 68 69 72
72 74 77 79 81 84
60 57 55 54 52 50 47
57 54 52 50 47 44
8 9 11 14 15
82 79 77 74 71 68 66
34 31 30 29 26 23 21
10 13 14 17 18 21 22 23
79 77 76 73 71 70
87 89 92 93 96 97
82 81 80 78 77 76 73 72
22 19 16 14 13
79 80 82 83 84 86 88
76 78 80 82 83
15 18 19 20 23 24 27
65 67 68 71 73 75 77 79
42 41 40 39 38
33 34 37 38 41 44 46
69 72 75 76 78 81
90 87 86 85 83
57 56 54 53 50 49 47 45
67 65 62 61 59 56 55
23 25 27 29 32 33
70 67 66 63 60 57 55
90 88 85 83 82 79 76 73
91 88 86 83 80 79 76 73
37 35 32 31 28 26 25 22
22 23 25 27 28 29 32
96 93 90 89 88
59 57 56 55 54
38 37 35 32 31
11 10 7 6 5 3
51 50 48 45 42 40 38 35
69 68 65 64 63 61 59 58
45 42 39 37 36 34 32
3 4 7 8 9
43 46 48 49 50 53 54 55
35 37 40 43 46
46 44 41 38 36 33
15 13 10 7 5 2
13 11 10 9 8 7 6
40 43 46 47 48 51
70 71 74 76 79
59 58 56 55 52 49
86 89 91 92 95 97 98
85 88 90 92 93
63 62 59 57 55 52 50
77 74 72 70 68 67
50 47 45 44 41 38 36
82 84 85 88 90 91 94 97
13 15 16 18 20 23 26 28
61 63 65 68 70 72 75 76
80 81 82 83 85
73 71 68 67 66 65 62
45 48 50 53 56 58 59 62
9 10 13 16 19 22 23 26
40 39 36 34 31 30 27 25
90 88 86 83 82 81
29 31 33 35 38 41 44
57 54 53 51 49 46 43
89 87 85 84 83 82
43 41 38 35 34 33 31 30
26 23 22 21 18 16 14
80 81 82 84 87
42 43 45 48 50 51 53 55
15 12 10 8 5 4
36 34 31 29 28 27
15 13 12 9 6 3
54 51 50 49 47
40 43 46 47 48 51 53
38 36 33 32 31 28 26 23
65 64 61 59 57 55
84 83 81 79 78 77
12 15 16 18 20
37 38 40 43 46 48 50
20 21 22 23 24 25 27
82 83 84 87 89
30 32 34 37 39 42 45 48
87 85 83 80 77 74
65 66 69 70 71
76 79 80 83 86 87
5 8 11 14 15
6 8 10 13 16 19
18 15 14 12 10
71 72 75 77 79 81 82 83
33 30 28 26 24 22
67 68 69 71 72 73
89 90 93 94 97
25 22 21 19 16 13
70 68 66 64 63 60
26 27 29 31 32 35 38
22 24 26 27 29 32 33 34
25 27 29 30 33 36 39
56 53 51 50 48 47 46
20 22 23 24 26 27 28
24 27 29 31 34
86 83 81 78 76 75 72 71
33 35 36 39 40 41 43
13 14 16 19 21 23
64 61 58 56 54 53 51 49
25 28 31 33 34 36
79 77 75 72 69 66 65
85 87 90 92 93 95 96
40 42 44 47 49 52 54
39 38 35 34 33 32 29
29 30 33 35 38 40 42
96 93 92 90 88 87 85
50 52 53 54 57 60
29 28 25 22 19 17
55 54 53 52 50 48
27 26 23 20 17 16
60 63 65 67 70 72 73 75
31 28 26 24 23 22
50 47 46 44 43
30 31 33 36 37 40 43
79 78 76 74 73 70 67
51 52 53 56 58 60 61
83 82 79 76 74 72 71 68
33 34 35 37 40 42 45
81 82 85 86 87 90
94 93 92 91 89 87 85 83
12 14 16 19 21 23
3 5 8 11 13 15 17
82 80 77 75 74
28 30 31 34 36 38
83 80 78 77 76 75 74 71
47 49 52 54 56 59 60
45 43 40 39 38 35 33 30
9 7 6 5 4 3
15 18 21 22 24 27
19 21 24 27 30 32 33
30 27 25 22 19
38 37 34 31 29 27 24 22
74 77 79 81 82 83 85 86
81 79 78 77 75 73
52 51 50 49 47 44 43
15 12 9 7 4 2 1
32 29 26 23 21 18 15
6 7 10 12 13 16
22 24 25 27 28 31 33
9 12 15 16 19 21 23
23 21 20 19 18 15 12 10
50 52 55 58 59
2 3 6 8 10 12 15 18
94 91 88 87 84
54 52 51 49 48 46 45
82 85 86 89 90
21 19 17 15 14 11
53 56 59 62 64
3 6 8 11 13 14
83 85 88 90 92
60 57 55 54 52 49 48
77 74 73 70 68 66 63
22 25 27 30 31 33 34
31 33 34 35 36 39
84 83 81 80 79 78
20 23 26 27 28 31 32 34
15 16 18 19 22 25 26
99 97 96 94 92 90
73 72 70 68 67 66 63 61
65 63 62 61 58 56 55 52
78 79 81 84 85 88 91 92
74 71 68 67 65
46 49 51 53 56 57
21 22 23 24 25 26
33 35 38 40 41 44 47
88 91 92 93 96
25 28 30 33 35
89 92 95 96 97
92 90 88 85 82 79 78 77
77 80 81 84 86 89 90 92
74 76 78 80 81 83 84
75 74 71 69 68 65
17 16 13 10 9
10 12 15 18 19
47 49 52 54 55
91 88 87 85 84
52 51 49 48 46 43 40 37
86 84 83 81 78 75
11 13 15 18 20 21 23 25
94 93 91 88 86 84 81
71 70 67 65 64
41 44 45 47 48
77 80 82 84 87
98 95 93 92 90 88
76 79 81 82 84 85 87 90
52 50 49 47 44 41 39
84 85 88 89 91 94 97 98
76 79 80 81 83 84 86 88
21 23 26 27 29
94 93 90 87 85 84 81
76 77 80 83 85 88 90 93
56 53 50 47 44 43 41 40
78 81 82 85 87
86 87 89 90 93
92 90 89 88 86 85
45 44 43 42 39
75 72 71 69 66 64 62
75 73 71 69 67 65 63 60
14 16 18 19 20 21
77 74 72 70 69 67
46 45 42 41 39 37 36 35
20 18 16 13 10 7 6 3
64 66 69 71 72 75
16 18 21 23 24 25 26 28
61 59 57 56 54 52 50
44 45 48 51 54 57 58 60
25 28 31 32 35
79 78 76 73 71 70
64 65 68 71 73 74
58 60 63 64 67
33 35 36 37 39 41
"""