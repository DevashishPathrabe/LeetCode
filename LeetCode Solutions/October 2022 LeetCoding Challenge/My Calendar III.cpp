class MyCalendarThree {
public:
    map<int,int> calendar;
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        ++calendar[start];
        --calendar[end];
        int counter = 0;
        int maxNo = 0;
        for (auto iter = calendar.begin(); iter != calendar.end(); ++iter){
            counter += iter->second;
            maxNo = max(maxNo,counter);
        }
        return maxNo;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */