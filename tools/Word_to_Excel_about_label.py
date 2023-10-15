#读取word中的表格数据，写入excel中

import docx
from openpyxl import Workbook
import os
from collections import OrderedDict


# 读取Word文档中的表格数据
def read_table_from_word(docx_file_path):
    doc = docx.Document(docx_file_path)
    table_data = []
    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)
    return table_data

def find_element_after_value(nested_list, target_value):   #这是找之后的一个元素
    for sublist in nested_list:
        for i, item in enumerate(sublist):
            if item == target_value and i < len(sublist) - 1 and sublist[i + 1] != target_value:
                return sublist[i + 1]
    return None  # 如果未找到目标元素或目标元素位于子列表的末尾，返回None

def find_element_after_all_value(nested_list, target_value):  #这是找之后的所有非空元素
    all_value = []
    for sublist in nested_list:
        for i, item in enumerate(sublist):
            if item == target_value and i < len(sublist) - 1 and sublist[i + 1] != target_value:
                all_value.append(sublist[i + 1])
                #获取sublist[i + 1]之后的所有非空元素
                for j in range(i+2, len(sublist)):
                    if sublist[j] != "":
                        all_value.append(sublist[j])
                    else:
                        break
                return all_value
    return None  # 如果未找到目标元素或目标元素位于子列表的末尾，返回None


# 对table_data进行筛选，选择需要的数据到final_table_data中
def final_table_data_select(table_data):
    table_data = table_data
    soil_info = []
    
    #1、找土壤代码
    Soil_code = "土壤代码"
    Soil_code_value = find_element_after_value(table_data, Soil_code)
    soil_info.append(Soil_code_value)
    
    #2、找土类
    great_soil_group = "土类"
    great_soil_group_value = find_element_after_value(table_data, great_soil_group)
    soil_info.append(great_soil_group_value)

    #3、找亚类
    Subclass = "亚类"
    Subclass_value = find_element_after_value(table_data, Subclass)
    soil_info.append(Subclass_value)
    
    #4、找土属
    Soil_genus = "土属"
    Soil_genus_value = find_element_after_value(table_data, Soil_genus)
    soil_info.append(Soil_genus_value)
    
    #5、找土种
    Soil_species = "土种"
    Soil_species_value = find_element_after_value(table_data, Soil_species)
    soil_info.append(Soil_species_value)
    
    #6、层次代号
    Hierarchy_code = "层次代号"
    Hierarchy_code_value = find_element_after_all_value(table_data, Hierarchy_code)
    #逐个取出层次代号的值
    for i in range(len(Hierarchy_code_value)):
        #将土壤代码Soil_code_value的变量分别和对应的层次代号Hierarchy_code_value变量分别结合，再传入到Soil_code_value_and_Hierarchy_code_value中
        Soil_code_and_Hierarchy_code = Soil_code_value + "_" + Hierarchy_code_value[i]
        
        Soil_code_value_and_Hierarchy_code_value.append(Soil_code_and_Hierarchy_code)
        
        soil_info.append(Hierarchy_code_value[i])
    
    #7、层次名称
    Hierarchy_Name = "层次名称"
    Hierarchy_Name_value = find_element_after_all_value(table_data, Hierarchy_Name)
    for i in range(len(Hierarchy_Name_value)):
        soil_info.append(Hierarchy_Name_value[i])
    
    #8、层次深度
    Hierarchy_depth = "层次深度"
    Hierarchy_depth_value = find_element_after_all_value(table_data, Hierarchy_depth)
    for i in range(len(Hierarchy_depth_value)):
        soil_info.append(Hierarchy_depth_value[i])

    return soil_info

# 将数据写入Excel文件
def write_data_to_excel(data, excel_file_path):
    wb = Workbook()
    ws = wb.active

    for row in data:
        ws.append(row)

    wb.save(excel_file_path)

def remove_duplicates(seq):
    #将’改为'，否则会报错
    seq = [item.replace('’', "'") for item in seq]
    # 使用OrderedDict来保持元素顺序且去重
    return list(OrderedDict.fromkeys(seq))

if __name__ == "__main__":
    
    #读取rough_surface文件夹中的txt文件
    rough_txt_dir = "D:/Graduate_documents/soil_image_segmentation/python_code/5_normalize_image_add_ruler/rough_surface/"
    rough_txt_filenames = os.listdir(rough_txt_dir)
    #读取rough_txt_filenames中的txt文件
    rough_txt_filename = [filename for filename in rough_txt_filenames if filename.endswith('.txt')]
    
    #读取smooth_surface文件夹中的txt文件
    smooth_txt_dir = "D:/Graduate_documents/soil_image_segmentation/python_code/5_normalize_image_add_ruler/smooth_surface/"
    smooth_txt_filenames = os.listdir(smooth_txt_dir)
    #读取smooth_txt_filenames中的txt文件
    smooth_txt_filename = [filename for filename in smooth_txt_filenames if filename.endswith('.txt')]
    
    rough_json_filename = "D:/Graduate_documents/soil_image_segmentation/python_code/5_normalize_image_add_ruler/rough_surface/rough_json/labels.txt"
    
    
    smooth_json_filename = "D:/Graduate_documents/soil_image_segmentation/python_code/5_normalize_image_add_ruler/smooth_surface/smooth_json/labels.txt"
    
    #读取word_filenames中的word文件
    word_dir = 'D:/Graduate_documents/soil_image_segmentation/python_code/2_survey_table/'
    word_filenames = os.listdir(word_dir)#获取文件夹下所有文件名
    
    #读取excel文件，且路径中含有中文时，需要将路径转换为unicode编码
    excel_dir = 'D:/Graduate_documents/soil_image_segmentation/'
    excel_filenames = os.listdir(excel_dir)
    
    #定义一个汇总的空列表
    final_table_data = []
    
    #定义一个将土壤代码分别和对应的层次代号分别结合的列表，并且是全局变量，列表初始值有__ignore__和_background_
    Soil_code_value_and_Hierarchy_code_value = ['__ignore__', '_background_']
    
    for word_filename in word_filenames:
        word_file_path = word_dir + word_filename
        table_data = read_table_from_word(word_file_path)
        #对table_data进行筛选，选择需要的数据到final_table_data中
        final_table_data_select_list = final_table_data_select(table_data)
        
        #插入文件名在final_table_data_select_list的第一个位置，并且去掉后缀名
        final_table_data_select_list.insert(0, word_filename.split('.')[0])
        
        final_table_data.append(final_table_data_select_list)
    
   #读取excel_filenames中的excel文件
    excel_filename = [filename for filename in excel_filenames if filename.endswith('.xlsx')]
    if len(excel_filename) > 1:
        excel_file_path = os.path.join(excel_dir, excel_filename[1]) #在打开文件夹的状态下，同一目录会生成临时文件需要读取第二个
    else:
        excel_file_path = excel_dir + excel_filename[0]
    
    #将数据写入Excel文件
    write_data_to_excel(final_table_data, excel_file_path)
    
    #对Soil_code_value_and_Hierarchy_code_value列表进行去重，但是列表元素顺序不能变
    Soil_code_value_and_Hierarchy_code_value_unique = remove_duplicates(Soil_code_value_and_Hierarchy_code_value)
    
    #将Soil_code_value_and_Hierarchy_code_value列表输入到label.txt中，每次输入完要换行
    rough_label_txt_dir = rough_txt_dir + rough_txt_filename[0]
    smooth_label_txt_dir = rough_txt_dir + rough_txt_filename[0]
    
    rough_label_txt_file = open(rough_label_txt_dir, 'w', encoding = "gb18030")
    for i in range(len(Soil_code_value_and_Hierarchy_code_value_unique)):
        rough_label_txt_file.write(Soil_code_value_and_Hierarchy_code_value_unique[i] + '\n')
        
    smooth_label_txt_file = open(smooth_label_txt_dir, 'w', encoding = "gb18030")
    for i in range(len(Soil_code_value_and_Hierarchy_code_value_unique)):
        smooth_label_txt_file.write(Soil_code_value_and_Hierarchy_code_value_unique[i] + '\n')
        
    rough_json_filename_file = open(rough_json_filename, 'w', encoding = "gb18030")
    for i in range(len(Soil_code_value_and_Hierarchy_code_value_unique)):
        rough_json_filename_file.write(Soil_code_value_and_Hierarchy_code_value_unique[i] + '\n')

    smooth_json_filename_file = open(smooth_json_filename, 'w', encoding = "gb18030")
    for i in range(len(Soil_code_value_and_Hierarchy_code_value_unique)):
        smooth_json_filename_file.write(Soil_code_value_and_Hierarchy_code_value_unique[i] + '\n')
    
    #关闭文件
    rough_label_txt_file.close()
    smooth_label_txt_file.close()
    rough_json_filename_file.close()
    smooth_json_filename_file.close()