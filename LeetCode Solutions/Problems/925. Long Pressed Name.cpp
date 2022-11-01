class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        int size1 = name.length();
        int size2 = typed.length();
        char prev;
        if (name[0] != typed[0]){
            return false;
        }
        else if (size1 > size2){
            return false;
        }
        prev = name[0];
        int left = 1,right = 1;
        while (left < size1 && right < size2){
            if (name[left] == typed[right]){
                prev = name[left];
                left++;
                right++;
            } else if (prev == typed[right]){
                right++;
            } else{
                return false;
            }
        }
        if (left != size1){
            return false;
        }
        while (right < size2){
            if (prev != typed[right]){
                return false;
            }
            right++;
        }
        return true;
    }
};