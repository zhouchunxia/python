import xlrd

########################################
# Author:zhouchunxia                   #
# OFFN:003956                          #
# MAIL:zhouchunxia@inner.czy.com       #
# function:read_excel()读excel中的数据 #
#         splitVersion()分隔版本号     #
########################################

# 将版本号分割开
def splitVersion(versions):
    #print(versions.split(','))
    return versions.split(',')

def read_excel(tagVersion):
    taglist = []
    celllist=[]
    # 打开一个workbook
    workbook = xlrd.open_workbook('C:\\ZCX\\20171010计划更新集成构建计划.xlsx')
    # 抓取所有sheet页的名称
    worksheets = workbook.sheet_names()
    #print('worksheets is %s' % worksheets)
    # 定位到sheet1
    worksheet1 = workbook.sheet_by_index(0)
    #获取版本号
    col = worksheet1.col_values(7)
    #print(col)
    for i in col:
        if i != '':
            taglist.append(i.strip())
    del taglist[0]
    # print(taglist)
    # 获取合并的单元格行数和列数
    tag_cell = worksheet1.merged_cells
    # print(tag_cell)
    for cell in tag_cell:
        if cell[2] == 7:
            celllist.append(cell)
            beg = cell[0]
            end = cell[1]
            for version in tagVersion:
                # 项目名称
                prodict = {'ch': ['---ch---'],
                           'ShareService': ['---ShareService---'],
                           'Scheduler': ['---Scheduler---'],
                           'MobileWeb': ['---MobileWeb---'],
                           'Spring.SSO': ['---Spring.SSO---'],
                           'admin': ['---admin---'],
                           'jp.ch.com': ['---jp.ch.com---'],
                           'CdnSite': ['---CdnSite---']}
                if worksheet1.cell(beg, 7).value.strip() == version:
                    # 创建properties
                    file = open('C:\\ZCX\\' + version + '.properties', 'w')
                    #print(worksheet1.cell(beg, 7).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'ch':
                            prodict['ch'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'ShareService':
                            prodict['ShareService'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'Scheduler':
                            prodict['Scheduler'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'MobileWeb':
                            prodict['MobileWeb'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'Spring.SSO':
                            prodict['Spring.SSO'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'admin':
                            prodict['admin'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'jp.ch.com':
                            prodict['jp.ch.com'].append(worksheet1.cell(i, 3).value.strip())
                    for i in range(beg, end):
                        if worksheet1.cell(i, 0).value == 'CdnSite':
                            prodict['CdnSite'].append(worksheet1.cell(i, 3).value.strip())
                    if len(prodict['ch']) > 1:
                        for i in prodict['ch']:
                            # print(i.strip())
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['ShareService']) > 1:
                        for i in prodict['ShareService']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['Scheduler']) > 1:
                        for i in prodict['Scheduler']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['MobileWeb']) > 1:
                        for i in prodict['MobileWeb']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['Spring.SSO']) > 1:
                        for i in prodict['Spring.SSO']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['admin']) > 1:
                        for i in prodict['admin']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['CdnSite']) > 1:
                        for i in prodict['CdnSite']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    if len(prodict['jp.ch.com']) > 1:
                        for i in prodict['jp.ch.com']:
                            file.write(i.strip()+'\n')
                        file.write('\n')
                    file.close()

if __name__ == '__main__':
    data = splitVersion('V5_0_0_20171010,V5_1_0_20171010,V5_1_1_20171010')
    read_excel(data)