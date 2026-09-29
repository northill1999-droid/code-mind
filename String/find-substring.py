from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        n = len(s)
        m = len(words)
        w = len(words[0])
        total_len = m * w
        
        if n < total_len:
            return []
        
        target_counts = Counter(words)
        res = []
        
        for i in range(w):
            left = i
            right = i
            window_counts = {}
            count = 0
            
            while right + w <= n:
                w_right = s[right : right + w]
                right += w
                
                if w_right in target_counts:
                    window_counts[w_right] = window_counts.get(w_right, 0) + 1
                    if window_counts[w_right] <= target_counts[w_right]:
                        count += 1
                    
                    while right - left > total_len:
                        w_left = s[left : left + w]
                        left += w
                        
                        if w_left in target_counts:
                            if window_counts[w_left] <= target_counts[w_left]:
                                count -= 1
                            window_counts[w_left] -= 1
                            
                    if count == m:
                        res.append(left)
                else:
                    window_counts.clear()
                    count = 0
                    left = right
                    
        return res
    