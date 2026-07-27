class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> remaining;

        for(int a : asteroids){
            bool destroyed = false;

            while(!remaining.empty() && remaining.back() > 0 && a < 0 && !destroyed){
                if(remaining.back() == -a){
                    remaining.pop_back();
                    destroyed = true;
                } else if(remaining.back() < -a){
                    remaining.pop_back();
                } else{
                    destroyed = true;
                }
            }

            if(!destroyed) remaining.push_back(a);
        }

        return remaining;
    }
};