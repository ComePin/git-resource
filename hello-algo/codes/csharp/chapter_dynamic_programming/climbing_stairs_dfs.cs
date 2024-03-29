﻿/**
* File: climbing_stairs_dfs.cs
* Created Time: 2023-06-30
* Author: hpstory (hpstory1024@163.com)
*/

namespace hello_algo.chapter_dynamic_programming;

public class climbing_stairs_dfs {
    /* 搜索 */
    public int dfs(int i) {
        // 已知 dp[1] 和 dp[2] ，返回之
        if (i == 1 || i == 2)
            return i;
        // dp[i] = dp[i-1] + dp[i-2]
        int count = dfs(i - 1) + dfs(i - 2);
        return count;
    }

    /* 爬楼梯：搜索 */
    public int climbingStairsDFS(int n) {
        return dfs(n);
    }

    [Test]
    public void Test() {
        int n = 9;
        int res = climbingStairsDFS(n);
        Console.WriteLine($"爬 {n} 阶楼梯共有 {res} 种方案");
    }
}
