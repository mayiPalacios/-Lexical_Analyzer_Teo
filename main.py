from lexer import analyze, get_symbol_table

if __name__ == "__main__":
    code = '''
    // This is a comment
    
    #include<bits/stdc++.h>
    
    typedef unsigned int uint;
    
    using namespace std;
    
    unsigned short tasks[3000000u];
    
    unsigned int dp[3000000][3][8] = {0};
    
    uint solve(uint ct, uint t, uint tools, uint count, uint lim){
        uint solved, skipped;
        if(tools == 0)
            return count;
        if(ct >= lim)
            return count;
        if(dp[ct][t][tools] != 0)
            return dp[ct][t][tools];
        if(t == tasks[ct]){
                solved = solve(ct + 1, t, tools,  count + 1, lim);
        }
        else if(tools & 1<<(tasks[ct])){
                uint auxt = tools;
                if(count > 0){
                    auxt = 0;
                    for(uint i = 0; i < 3; i++){
                        if(1<<i & tools && i != t){
                            auxt |= 1<<i;
                        }
                    }
                }
                solved = solve(ct + 1, tasks[ct], auxt, count+1, lim);
        }
        else{
            solved = count;
        }
        skipped = solve(ct + 1, t, tools, count, lim);
        dp[ct][t][tools] = max(solved, skipped);
        return dp[ct][t][tools];
    }
    
    int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        uint n;
        cin >> n;
        for(uint i = 0; i < n; i++){
            cin >> tasks[i];
        }
        unsigned int res = solve(0, tasks[0], 7u, 0, n);
        for (int i = 0; i < 3; i++) res = max(res, solve(0, tasks[0], 7u- (1 << i), 0, n));
        cout << res  << endl;
        return 0;
    }
    '''

    analyze(code)
    symbols = get_symbol_table()

    print("\nSymbol Table:")
    for symbol, properties in symbols.items():
        print(f'{symbol}: {properties}')
