class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        List, left, right = [], 0, len(products)-1
        for i in range(len(searchWord)):
            count, result = searchWord[i], []
            while(left <= right and (len(products[left]) == i or products[left][i] < count)):
                  left += 1
            while(left <= right and (len(products[right]) == i or products[right][i] > count)):
                right -= 1
            for j in range(3):
                if(left + j > right):
                    break
                else:
                    result.append(products[left+j])
            List.append(result)
        return List