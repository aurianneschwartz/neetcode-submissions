class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dico = {}

        for index, string in enumerate(strs):
            sorted_string = "".join(sorted(string))
 
            if sorted_string in dico:
                dico[sorted_string].append(index)
            else:
                dico[sorted_string] = [index]

        result = []
        idx = 0
        for key, value in dico.items():
            result.append([])
            for i in range(len(value)):
                result[idx].append(strs[value[i]])
            idx += 1
        return result
