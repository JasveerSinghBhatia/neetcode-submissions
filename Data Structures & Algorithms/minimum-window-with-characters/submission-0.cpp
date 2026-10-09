class Solution {
public:
    string minWindow(string s, string t) {
        int n=s.length();
        if (t.length() > n){
            return "";
        }
        unordered_map<char,int> mp;
        for(char &ch: t){
            mp[ch] ++;
        }
        int req_cnt = t.length();

        int i=0, j=0;
        int minwindow_size = INT_MAX;
        int start_i = 0;
        while(j<n){
            char ch = s[j];
            if(mp[ch] > 0){
                req_cnt--;
            }
            mp[ch]--;
            while(req_cnt == 0){
                //shrink window
                int currWindowSize = j-i+1;
                if(minwindow_size > currWindowSize){
                    minwindow_size = currWindowSize;
                    start_i = i;
                }
                mp[s[i]]++;
                if(mp[s[i]]> 0){
                    req_cnt++;
                }
                i++;
            }
            j++;
        }
        return minwindow_size ==  INT_MAX ? "" : s.substr(start_i, minwindow_size); 

    }
};
