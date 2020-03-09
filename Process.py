import pandas as pd

class Process:

    def __init__(self,prefix):
        self.cnt = prefix[0]

    """
    mismatch : count mismatching number from main_str to str_list
    :param
        main_str : a string to match 
        str_list : string from list to match
    :return
        count : the result of mismatch counting
    """
    def mismatch(self, main_str, str_list):
        count = 0
        for i in range(0, len(main_str)):
            if main_str[i] != str_list[i]:
                count += 1
            # exit the loop if count is highert than self.cnt
            if count > self.cnt: break
        return count

    """
    print_result : 
    :param
        main_str_list :
        str_list :
    """
    def print_result(self, main_str_list, str_list):
        for main_str in main_str_list:
            if pd.notnull(main_str):
                for tmp_str in str_list:
                    if pd.notnull(tmp_str):
                        if self.mismatch(main_str, tmp_str) <= self.cnt:
                            print(main_str + "\n" + tmp_str + " >>>", self.mismatch(main_str, tmp_str))

    """
    get_result1 :
    :param
        main_str_list :
        str_list :
    :return
        dict object : 
            {
                main_str : { 0 : cnt , 1 : cnt , 2 : cnt }
            }
    """
    def get_result1(self,main_str_list, str_list):
        for main_str in main_str_list.keys():
            if pd.notnull(main_str):
                for tmp_str in str_list:
                    if pd.notnull(tmp_str):
                        if self.mismatch(main_str, tmp_str) <= self.cnt:
                            temp = main_str_list[main_str]
                            temp[str(self.mismatch(main_str, tmp_str))] += 1
        return main_str_list

    """
    get_result2 : 
    :param
        main_str_list :
        str_list :
    :return
        dict object : 
            {
                main_str : [ str , cnt_result ]
            }
    """
    def get_result2(self,main_str_list, str_list):
        tmp_dict = {}
        for main_str in main_str_list:
            if pd.notnull(main_str):
                for tmp_str in str_list:
                    if pd.notnull(tmp_str):
                        cnt_result = self.mismatch(main_str, tmp_str)
                        if cnt_result <= self.cnt:
                            tmp_dict[main_str] = [tmp_str, cnt_result]
        return tmp_dict


