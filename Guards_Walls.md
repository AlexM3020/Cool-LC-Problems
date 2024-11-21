LC problem: 2257. Count Unguarded Cells in the Grid

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.



![image](https://github.com/user-attachments/assets/008f2ffd-a33f-450e-8660-d9a727222ef1)

![image](https://github.com/user-attachments/assets/f99a22c5-91c9-4093-b9d0-0c0de14d1e2f)

![image](https://github.com/user-attachments/assets/cc96103a-d975-4996-8ece-3838bf127455)
