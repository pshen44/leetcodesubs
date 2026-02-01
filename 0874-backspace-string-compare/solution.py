class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack, tstack = [], []
        for sch in s:
            if sch == '#':
                if sstack:
                    sstack.pop()
                continue
            sstack.append(sch)

        for tch in t:
            if tch == '#':
                if tstack:
                    tstack.pop()
                continue
            tstack.append(tch)
            
        return sstack == tstack
