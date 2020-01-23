"""
    Title: Data Getter for Discord Bot and Reddit Functions
    Author: John Mock
    Description: Gathers data from text files to be passed into other functions
"""


def get_r_info():
    """ Method Description: Get Reddit Info from the rinfo file """

    r_info = {}
    r_info_list = []
    file = open("../data/rinfo.txt")
    line = file.readline()

    while line != '':
        r_info_list.append(line.strip('').split(','))
        line = file.readline()

    file.close()

    for item in r_info_list:
        r_info[item[0]] = item[1]

    return r_info


def get_d_info():
    """ Method Description: Get Discord Info from the dinfo file """

    d_info = {}
    d_info_list = []
    file = open("../data/dinfo.txt")
    line = file.readline()

    while line != '':
        d_info_list.append(line.strip('').split(','))
        line = file.readline()

    file.close()

    for item in d_info_list:
        d_info[item[0]] = item[1]

    return d_info


def get_c_info():
    """ Method Description: Get Database Connection Info from the cinfo file """

    c_info = {}
    c_info_list = []
    file = open("../data/cinfo.txt")
    line = file.readline()

    while line != '':
        c_info_list.append(line.strip('').split(','))
        line = file.readline()

    file.close()

    for item in c_info_list:
        c_info[item[0]] = item[1]

    return c_info
