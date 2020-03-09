
from time import clock
"""
length가 같은 training과 test의 seq를 idx순서로 1:1 비교하여
test 기준으로 training에 mismatch 되는 갯수를 세어준다
result 는 test seq 목록에 각각mismatch 갯수
"""

import Process
import Utils
############### start to set env ################
# mismatch 갯수
# CNT = 2 # 0, 1, 2개 각각 확인
CNT = 3 # 0, 1, 2, 3 개 각각 확인

# 엑셀 파일 경로
FILE_PATH = "D:/000_WORK/KimNahye/20200304/Genomic 10ng_다시 - 복사본.xlsx"
# FILE_PATH = "D:/000_WORK/KimNahye/20200304/Lib 10fg - 복사본 (2) - 복사본.xlsx"
# FILE_PATH = "D:/000_WORK/KimNahye/20200304/비교 from 20200106/kwon 쌤 - 복사본.xlsx"
# FILE_PATH = "D:/000_WORK/KimNahye/20200304/비교 from 20200106/kwon 쌤.xlsx"
RESULT_PATH = "D:/000_WORK/KimNahye/20200304/비교 from 20200106/kwon 쌤_result"
# RESULT_PATH = "D:/000_WORK/KimNahye/20200304/Genomic 10ng_result"

SHEET_NAME01 = "training"
SHEET_NAME02 = "test" # 기준
# Target 컬럼을 가져 오는 경우
# COL_NAME01 = "Target"
# COL_NAME02 = "Target"
# Target context sequence 컬럼을 가져 오는 경우
# COL_NAME01 = "Target context sequence"
# COL_NAME02 = "Target context sequence"

COL_NAME01 = "Guide (X19)"
COL_NAME02 = "guide"

PREFIX_TRAINING = [
    FILE_PATH
    , ""
    , SHEET_NAME01
    , COL_NAME01
]
PREFIX_TESTING = [
    FILE_PATH
    , ""
    , SHEET_NAME02
    , COL_NAME02
]
PREFIX_RESULT =[
    RESULT_PATH
    , ""
    , ""
    , ""
]
############### end setting env #################

def main():
    u_training = Utils.Utils(PREFIX_TRAINING)
    tr_dict = u_training.get_excel()
    training_targets = u_training.get_data_by_col(tr_dict)
    # print(training_targets)
    # training_targets = p_training.get_data()

    u_testing = Utils.Utils(PREFIX_TESTING)
    te_dict = u_testing.get_excel()
    test_targets = u_testing.get_data_by_col(te_dict)
    target_dict = u_testing.make_dic(test_targets, CNT)
    # print(len(test_targets))
    # print(target_dict)
    # print(len(target_dict))

    process = Process.Process([CNT])
    result_dict = process.get_result2(target_dict, training_targets)
    PREFIX_RESULT[1] = result_dict

    u_result = Utils.Utils(PREFIX_RESULT)
    u_result.make_excel_by_openpyxl([COL_NAME02,COL_NAME01,'mismatch(es)'])




start_time = clock()
main()
print("::::::::::: %.2f seconds ::::::::::::::" % (clock() - start_time))