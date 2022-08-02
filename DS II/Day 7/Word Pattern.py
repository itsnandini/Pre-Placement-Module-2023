class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        unique_pattern = len(set([char for char in pattern]))
        unique_s = len(set([char for char in str.split(' ')]))
        if unique_pattern != unique_s:
            return False
        matching_elements = dict(zip([char for char in pattern],str.split(' ')))
        pattern_list = [char for char in pattern]
        result_list = list(map(matching_elements.get, pattern_list))
        if None in result_list:
            return False
        result_string = ' '.join(result_list)
        if result_string == str:
            return True
        return False
