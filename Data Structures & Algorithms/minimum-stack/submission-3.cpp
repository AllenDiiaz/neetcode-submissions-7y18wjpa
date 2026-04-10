#include <stack>
#include <algorithm>

class MinStack {
private:
    // 我們使用 long long 來預防 32-bit 溢位問題，展現架構的健壯性。
    std::stack<long long> data_stack;
    std::stack<long long> min_stack;

public:
    /** * Constructor (建構子)
     * 在 C++ 裡，成員變數會自動調用其預設建構子，
     * 所以這裡我們不需要在 __init__ 裡手動分配。
     */
    MinStack() {}

    /** * Mutator Method: push
     * 這裡我們展示了「同步存入」的邏輯。
     */
    void push(int val) {
        long long v = (long long)val; // 型別轉換，安全第一
        data_stack.push(v);
        
        // 如果 min_stack 為空，或新值比目前的最小值還小，就更新它
        if (min_stack.empty()) {
            min_stack.push(v);
        } else {
            // 維持兩邊高度同步，這對 pop 的一致性至關重要
            min_stack.push(std::min(v, min_stack.top()));
        }
    }

    /** * Mutator Method: pop
     */
    void pop() {
        // 同步彈出，確保時間線的一致性
        data_stack.pop();
        min_stack.pop();
    }

    /** * Accessor Method: top
     */
    int top() {
        return (int)data_stack.top();
    }

    /** * Accessor Method: getMin
     * 這裡就是 O(1) 的核心實現。
     */
    int getMin() {
        return (int)min_stack.top();
    }
};