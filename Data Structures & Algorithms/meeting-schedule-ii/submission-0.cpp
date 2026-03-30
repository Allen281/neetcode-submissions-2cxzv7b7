/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    static bool cmp(Interval& a, Interval& b){
        return a.start == b.start ? a.end < b.end : a.start < b.start;
    }

    int minMeetingRooms(vector<Interval>& intervals) {
        if(intervals.size() <= 1) return (int)intervals.size();

        sort(intervals.begin(), intervals.end(), cmp);

        int start = intervals[0].start, end = intervals[0].end;

        vector<Interval> nextDay;
        for(int i = 1; i < intervals.size(); i++){
            if(intervals[i].start < end) nextDay.push_back(intervals[i]);
            else{
                start = intervals[i].start;
                end = intervals[i].end;
            }
        }

        return 1 + minMeetingRooms(nextDay);
    }
};
