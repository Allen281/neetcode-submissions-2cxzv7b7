class MedianFinder {
public:
    priority_queue<int> bottomHalf;
    priority_queue<int, vector<int>, greater<int>> topHalf;
    MedianFinder() {
    }
    
    void addNum(int num) {
        if(bottomHalf.empty()){
            bottomHalf.push(num);
            return;
        }
        
        if(num <= bottomHalf.top()){
            bottomHalf.push(num);

            while(bottomHalf.size()-1 > topHalf.size()){
                topHalf.push(bottomHalf.top());
                bottomHalf.pop();
            }
        } else{
            topHalf.push(num);

            while(bottomHalf.size() < topHalf.size()){
                bottomHalf.push(topHalf.top());
                topHalf.pop();
            }
        }
    }
    
    double findMedian() {
        int size = topHalf.size() + bottomHalf.size();

        if(size%2 == 0){
            return (bottomHalf.top()+topHalf.top())/2.0;
        } else{
            return bottomHalf.top();
        }
    }
};
