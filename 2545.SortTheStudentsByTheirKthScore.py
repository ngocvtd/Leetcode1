class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        score_k = [(E[k], i) for i, E in enumerate(score)]

        score_k.sort(reverse = True)

        score_rs = [[0] * len(score[0]) for _ in range(len(score))]  
        
        for idx, (_, i) in enumerate(score_k):
            score_rs[idx] = score[i]
        
        return score_rs
