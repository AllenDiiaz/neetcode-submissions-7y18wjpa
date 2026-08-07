class TimeMap {
// Allen: [[Happy, 1],[Joyful,3]...]
private:
unordered_map<string, vector<pair<string, int>>> store;
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        store[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if (store.find(key) == store.end())
        {return "";}

        vector<pair<string, int>> &arr = store[key];
        int left = 0;
        int right = arr.size() - 1;
        string ans = "";

        // 1 2 3 4 5 6 7 8 9

        while (left<=right)
        {
            int mid = left + (right-left) / 2;

            if (arr[mid].second <= timestamp)
            {
                ans = arr[mid].first;
                left = mid + 1;
            } else {
                right = mid -1;
            }
        }
        return ans;
        
    }
};
