class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        inBlock = False
        newLine = []

        for line in source:
            i = 0
            while i < len(line):
                
                if not inBlock and i+1 < len(line) and line[i:i+2] == "//":
                    break
                elif not inBlock and i+1 < len(line) and line[i:i+2] == "/*":
                    inBlock = True
                    i += 2
                elif inBlock and i+1 < len(line) and line[i:i+2] == "*/":
                    inBlock = False
                    i += 2
                else:
                    if not inBlock:
                        newLine.append(line[i])
                    i += 1

            if not inBlock and newLine:
                res.append("".join(newLine))
                newLine = []
        return res
