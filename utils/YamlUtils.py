import yaml

#函数功能：读取整个yaml文件中指定的Key部分，并拼接成列表，并返回列表！
def yaml_data_with_file(file_name, key):
    with open(file_name, "r") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)[key]
        ret = list()
        for case_data in data.values():
            #print(case_data)
            ret.append(case_data)
        return ret


#带测试用例编号key一起读取！
def yaml_data_with_file1(file_name, key):
    with open(file_name, "r") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)[key]
        ret = list()
        for k in data.keys():
            v=data[k];
            v["key"]=k;
            ret.append(v);
        return ret
