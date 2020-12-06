import requests
import json
import datetime
import time

# 设置用户的cookie，可以从浏览器中获取
def get_cookies():
    # str需要替换成自己账号的cookies，获取步骤详看图片指引
    str = r''
    return str

# 设置用户的权限token，可以从浏览器中获取
def get_authenticity_token():
    # str需要替换成自己账号的authenticity_token，获取步骤详看图片指引
    str = r''
    return str

# 模拟登陆INaturalist，用于获取token与cookie
# 待定

# 设置创建的时间段、需要包含的字段信息，1代表选择，0代表不选择
# 输入参数：d1(起始日期),d2(终止日期)
def get_form_data(d1, d2):
    data = {
        'utf8': '✓',
        'observations_export_flow_task[inputs_attributes][0][extra][query]': 'quality_grade=any&identifications=any&d1='+ d1 + '&d2=' + d2,
        'observations_export_flow_task[options][columns][id]': '1',
        'observations_export_flow_task[options][columns][observed_on_string]': '1',
        'observations_export_flow_task[options][columns][observed_on]': '1',
        'observations_export_flow_task[options][columns][time_observed_at]': '1',
        'observations_export_flow_task[options][columns][time_zone]': '1',
        'observations_export_flow_task[options][columns][user_id]': '1',
        'observations_export_flow_task[options][columns][user_login]': '1',
        'observations_export_flow_task[options][columns][created_at]': '1',
        'observations_export_flow_task[options][columns][updated_at]': '1',
        'observations_export_flow_task[options][columns][quality_grade]': '1',
        'observations_export_flow_task[options][columns][license]': '1',
        'observations_export_flow_task[options][columns][url]': '1',
        'observations_export_flow_task[options][columns][image_url]': '1',
        'observations_export_flow_task[options][columns][sound_url]': '1',
        'observations_export_flow_task[options][columns][tag_list]': '1',
        'observations_export_flow_task[options][columns][description]': '1',
        'observations_export_flow_task[options][columns][num_identification_agreements]': '1',
        'observations_export_flow_task[options][columns][num_identification_disagreements]': '1',
        'observations_export_flow_task[options][columns][captive_cultivated]': '1',
        'observations_export_flow_task[options][columns][oauth_application_id]': '1',
        'observations_export_flow_task[options][columns][place_guess]': '1',
        'observations_export_flow_task[options][columns][latitude]': '1',
        'observations_export_flow_task[options][columns][longitude]': '1',
        'observations_export_flow_task[options][columns][positional_accuracy]': '1',
        'observations_export_flow_task[options][columns][private_place_guess]': '1',
        'observations_export_flow_task[options][columns][private_latitude]': '1',
        'observations_export_flow_task[options][columns][private_longitude]': '1',
        'observations_export_flow_task[options][columns][private_positional_accuracy]': '1',
        'observations_export_flow_task[options][columns][geoprivacy]': '1',
        'observations_export_flow_task[options][columns][taxon_geoprivacy]': '1',
        'observations_export_flow_task[options][columns][coordinates_obscured]': '1',
        'observations_export_flow_task[options][columns][positioning_method]': '1',
        'observations_export_flow_task[options][columns][positioning_device]': '1',
        'observations_export_flow_task[options][columns][place_town_name]': '1',
        'observations_export_flow_task[options][columns][place_county_name]': '1',
        'observations_export_flow_task[options][columns][place_state_name]': '1',
        'observations_export_flow_task[options][columns][place_country_name]': '1',
        'observations_export_flow_task[options][columns][place_admin1_name]': '1',
        'observations_export_flow_task[options][columns][place_admin2_name]': '1',
        'observations_export_flow_task[options][columns][species_guess]': '1',
        'observations_export_flow_task[options][columns][scientific_name]': '1',
        'observations_export_flow_task[options][columns][common_name]': '1',
        'observations_export_flow_task[options][columns][iconic_taxon_name]': '1',
        'observations_export_flow_task[options][columns][taxon_id]': '1',
        'observations_export_flow_task[options][columns][taxon_kingdom_name]': '0',
        'observations_export_flow_task[options][columns][taxon_phylum_name]': '0',
        'observations_export_flow_task[options][columns][taxon_subphylum_name]': '0',
        'observations_export_flow_task[options][columns][taxon_superclass_name]': '0',
        'observations_export_flow_task[options][columns][taxon_class_name]': '0',
        'observations_export_flow_task[options][columns][taxon_subclass_name]': '0',
        'observations_export_flow_task[options][columns][taxon_superorder_name]': '0',
        'observations_export_flow_task[options][columns][taxon_order_name]': '0',
        'observations_export_flow_task[options][columns][taxon_suborder_name]': '0',
        'observations_export_flow_task[options][columns][taxon_superfamily_name]': '0',
        'observations_export_flow_task[options][columns][taxon_family_name]': '0',
        'observations_export_flow_task[options][columns][taxon_subfamily_name]': '0',
        'observations_export_flow_task[options][columns][taxon_supertribe_name]': '0',
        'observations_export_flow_task[options][columns][taxon_tribe_name]': '0',
        'observations_export_flow_task[options][columns][taxon_subtribe_name]': '0',
        'observations_export_flow_task[options][columns][taxon_genus_name]': '0',
        'observations_export_flow_task[options][columns][taxon_genushybrid_name]': '0',
        'observations_export_flow_task[options][columns][taxon_species_name]': '0',
        'observations_export_flow_task[options][columns][taxon_hybrid_name]': '0',
        'observations_export_flow_task[options][columns][taxon_subspecies_name]': '0',
        'observations_export_flow_task[options][columns][taxon_variety_name]': '0',
        'observations_export_flow_task[options][columns][taxon_form_name]': '0',
        'commit': '创建导出'
    }
    return data

# 通过get方法进行查询，并返回response
# 输入参数：访问的url
def get_method(session, url):
    # 添加请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': get_cookies()
    }
    resp = None
    # 如果查询引发异常，则跳过，睡眠5秒后再次查询
    session.headers = headers
    while(resp == None):
        try:
            resp = session.get(url)
        except:
            resp = None
            time.sleep(5)
    resp.close()
    return resp

# 通过post方法进行提交，并返回response
# 输入参数：访问的url、表单数据(目前为固定内容)
def post_method(session, url, headers, data):
    resp = None
    session.headers = headers
    while (resp == None):
        try:
            resp = session.post(url, data=data)
        except:
            resp = None
            time.sleep(5)
    resp.close()
    return resp

# 用于查询指定日期内有多少条记录
# 输入参数：d1(起始日期),d2(终止日期)
# 返回内容：时间段中的记录条数
def check_data_count_during_date(session, d1, d2):
    url_str = r'https://www.inaturalist.org/observations?quality_grade=any&identifications=any&d1=' + d1 + '&d2=' + d2 + '&partial=cached_component'
    resp = get_method(session, url_str)
    # 从response的头文件中查找记录条数总数，每次下载最大量不超过20w
    return int(resp.headers.get('X-Total-Entries'))

# 发送打包数据的任务
# 输入参数：d1(起始日期),d2(终止日期)
# 返回内容：任务的id号
def send_pack_data_proceess(session, d1, d2):
    # 添加请求头
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Length': '8917',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': get_cookies(),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.inaturalist.org',
        'Origin': 'https://www.inaturalist.org',
        'Referer': 'https://www.inaturalist.org/observations/export',
        'X-CSRF-Token': get_authenticity_token(),
        'X-Requested-With': 'XMLHttpRequest'
    }
    url_str = r'https://www.inaturalist.org/flow_tasks'
    resp = post_method(session, url_str, headers, get_form_data(d1, d2))
    # 解析并返回任务的id号
    user_dict = json.loads(resp.text)
    return str(user_dict['id'])

# 获取创建进度查询的url
# 输入参数：任务的的id号
# 返回内容：output中的id和file_file_name
def check_proceess(session, projectId):
    url_str = r'https://www.inaturalist.org/flow_tasks/' + projectId + r'/run.json'
    print('开始检查任务进度...')
    resp = get_method(session, url_str)
    print('结束检查任务进度...')
    # 如果打包完成，则output中存在相应的数据
    user_dict = json.loads(resp.text)
    if len(user_dict['outputs']) > 0:
        return {'id': str(user_dict['outputs'][0]['id']), 'file_file_name': user_dict['outputs'][0]['file_file_name']}
    else:
        return {'id': 'null', 'file_file_name': 'null'}

# 下载数据，需要提供下载id号和文件名称
def download_zip(session, id, file_file_name, save_path, chunk_size=128) -> bool:
    str_url = r'https://www.inaturalist.org/attachments/flow_task_outputs/' + id + '/' + file_file_name
    resp = None
    while(resp == None):
        try:
            resp = session.get(str_url, stream=True)
        except:
            resp = None
            time.sleep(5)
    with open(save_path, 'wb') as fd:
        for chunk in resp.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    resp.close()

# 删除任务
def delete_proceess(session, id) -> bool:
    # 设置请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Length': '128',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Connection': 'keep-alive',
        'Cookie': get_cookies(),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.inaturalist.org',
        'Origin': 'https://www.inaturalist.org',
        'Referer': 'https://www.inaturalist.org/observations/export'
    }
    # 设置请求url
    url_str = r'https://www.inaturalist.org/flow_tasks/' + id
    # 构建请求表单数据
    data = {
        '_method': 'delete',
        'authenticity_token': get_authenticity_token()
    }
    resp = post_method(session, url_str, headers, data)
    if (resp != None):
        print('删除任务成功...')
        return True
    else:
        return False

# 计算第n天后的日期，一般为6天后，总共是7天
# 输入参数：起始日期
# 返回内容：第n天后的日期
def get_date(date_str, n = 6):
    the_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    result_date = the_date + datetime.timedelta(days = n) # 第n天后是几号
    d = result_date.strftime('%Y-%m-%d')
    return d

# 比较两个真实日期之间的大小，如果截止日期小于终止日期，则返回True
def date_compare(date, end_date) -> bool:
    satrt_day = datetime.datetime.strptime(date, '%Y-%m-%d')
    end_day = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    return satrt_day <= end_day

#  执行函数
if __name__ == '__main__':
    # 流程步骤
    # 0、在浏览器登录INaturalist网站，按F12，点击Network，在Name列表中找到export请求，点击Headers->Request Headers->Cookies，复制粘贴到get_cookies函数中；
    # 0、点击查找数据范围，在Network的Name列表中找到observations?quality_grade=any&identifications=any请求，点击Headers->Request Headers->X-CSRF-Token，复制粘贴到get_csrf函数中；
    # 0、点击Elements左侧的第二个图标，变为蓝色后选择任务列表的删除按钮，右侧菜单栏自动索引到按钮的DOM位置，找到authenticity_token对应的value，复制粘贴到get_authenticity_token函数中；
    # 1、设置存储路径和总的起始日期、终止日期
    # 2、设置一定的时间段，比如6天或7天，得到截止日期，查询后如果返回的记录超过20w，则减少一天，直至记录在20w之内
    # 3、提交打包任务
    # 4、设置一定时间后检查任务完成进度，如果完成，则获取任务的输出结果id和file名称
    # 5、下载输出结果
    # 6、下载完建议删除任务结果，防止占用内存
    # 7、再次开始执行步骤2，直到终止日期
    store_path = r'' # 存储的路径，如果不设置，则默认与py文件同路径
    start_day = '2020-03-16' # 起始日期
    end_day = '2020-10-27' # 终止日期
    init_data_interval = 6 # 天数间隔
    day_interval = init_data_interval
    stop_day = get_date(start_day, day_interval) # 截止日期
    m_session = requests.session() # 创建网络会话连接
    # 如果截止日期小于终止日期，则允许执行
    while(date_compare(stop_day, end_day)):
        # 如果返回的数目超过20w，则将日期减少一天，直至满足条件
        while(check_data_count_during_date(m_session, start_day, stop_day) > 200000):
            day_interval = day_interval - 1
            if (day_interval < 0):
                with open("download_record.txt", "a") as f:
                    f.write(start_day + '  can not download automatically!' + '\n')
                break
            stop_day = get_date(start_day, day_interval)
            time.sleep(5) # 5秒之后再访问
        # 如果单天的数据量超过20w，则跳过当天数据的下载
        if (day_interval < 0):
            # 更新时间段
            day_interval = 6
            start_day = get_date(stop_day, 1)  # 起始日期为上次结束日期的下一天
            stop_day = get_date(start_day, day_interval)
            continue
        # 某个时间段中的总记录数
        record_count = check_data_count_during_date(m_session, start_day, stop_day)
        # 满足打包条件后，发送打包任务
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' 发送任务...')
        project_id = send_pack_data_proceess(m_session, start_day, stop_day)
        # 发送打包任务后，先发两次查询，相隔一段时间后再查询一次
        file_result = check_proceess(m_session, project_id)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + file_result['id'] + ' ' + file_result['file_file_name'])
        minute_45 = 2700  #45分钟，下载近20w数据量的轮询时间
        minute_20 = 1200 #20分钟，下载单天数据量的轮询时间
        while(file_result['id'] == 'null'):
            time.sleep(minute_45)
            file_result = check_proceess(m_session, project_id)  # 更新检查
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' ' + file_result['id'] + ' ' + file_result['file_file_name'])
        # 下载文件
        file_name = 'observations-' + start_day + '-' + stop_day + '.csv.zip'
        download_zip(m_session, file_result['id'], file_result['file_file_name'], store_path + file_name)
        # 将文件基本信息进行记录
        with open("download_record.txt", "a") as f:
            f.write(file_name + '    ' + start_day + '    ' + stop_day + '    ' + str(record_count) + '\n')
        time.sleep(5) # 停止操作5秒后执行删除任务
        delete_proceess(m_session, project_id) # 下载完成后，删除任务数据，防止占用后台空间
        time.sleep(30)  # 删除操作后，停顿30秒后继续下一个任务
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' 下载结束，开始新任务... ')
        # 更新时间段
        day_interval = 6
        start_day = get_date(stop_day, 1) #起始日期为上次结束日期的下一天
        stop_day = get_date(start_day, day_interval)
    m_session.close() # 结束网络会话连接