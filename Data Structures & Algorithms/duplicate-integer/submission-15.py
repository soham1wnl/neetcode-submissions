class Solution:
    def hasDuplicate(self, dick: List[int]) -> bool:
        sex = set()
        for semen in dick:
            if semen in sex:
                return True
            sex.add(semen)
        return False