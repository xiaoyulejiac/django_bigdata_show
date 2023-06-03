from django.shortcuts import render
import json
from random import randrange
 
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
 
import ssl
# pyechart模块导入
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie, Radar
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from pyecharts.charts import Map
from pyecharts.globals import ThemeType
from pyecharts.datasets import register_url
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from data.function.const_data_provider import age_data_provider, edu_data_provider, edu_list_data_provider, age_sorted_data_provider, changchun_edu_list_data_provider, marriage_data_provider
 
# ---------------------------数据段---------------------------
# 本地调试数据初始化
changchun_age_data = {0: 6408, 1: 10540, 2: 10614, 3: 10903, 4: 10785, 5: 10624, 6: 10562, 7: 10654, 8: 10518, 9: 10645, 10: 10673, 11: 10725, 12: 10599, 13: 10619, 14: 10809, 15: 7570, 16: 5176, 17: 5116, 18: 5344, 19: 5279, 20: 5267, 21: 5337, 22: 5324, 23: 5321, 24: 5349, 25: 5229, 26: 5138, 27: 5231, 28: 5349, 29: 5358, 30: 5321, 31: 5388, 32: 5306, 33: 5250, 34: 5439, 35: 5140, 36: 5300, 37: 5271, 38: 5195, 39: 5188, 40: 5300, 41: 5300, 42: 5346, 43: 5360, 44: 5337, 45: 5257, 46: 5438, 47: 5250, 48: 5447, 49: 5180, 50: 5240, 51: 5301, 52: 5169, 53: 5318, 54: 5191, 55: 5272, 56: 5128, 57: 5322, 58: 5351, 59: 5265, 60: 2192, 61: 66, 62: 57, 63: 66, 64: 76, 65: 62, 66: 59, 67: 80, 68: 63, 69: 73, 70: 60, 71: 54, 72: 66, 73: 64, 74: 68, 75: 61, 76: 77, 77: 60, 78: 52, 79: 60, 80: 56, 81: 58, 82: 75, 83: 68, 84: 58, 85: 54, 86: 64, 87: 61, 88: 66, 89: 69, 90: 52, 91: 69, 92: 64, 93: 58, 94: 60, 95: 74, 96: 22}
changchun_age_sorted_data = [400080, 155648, 242444, 1988]
changchun_edu_data = {'专科': 31272, '其他': 93378, '本科': 9515, '硕士学历及以上': 2474, '高中学历及以下': 263441}
edu_list_data = [['专科', 31272, '7.82%'], ['其他', 93378, '23.34%'], ['本科', 9515, '2.38%'], ['硕士学历及以上', 2474, '0.62%'], ['高中学历及以下', 263441, '65.85%']]
changchun_edu_list_data = [[31272, 93378, 9515, 2474, 263441]]
changchun_marry_data = [156956, 243124, 408000]

# (数据库)数据初始化
# changchun_age_data = age_data_provider()
# changchun_age_sorted_data = age_sorted_data_provider()
# changchun_edu_data = edu_data_provider()
# edu_list_data = edu_list_data_provider()
# changchun_edu_list_data = changchun_edu_list_data_provider()
# changchun_marry_data = marriage_data_provider()

# 其他常量数据
## 长春
changchun_gdp_data = [5986.42, 6495.02, 7175.71, 5904.14, 6638.03, 7103.10, 6744.60]
## 大连
dalian_age_sorted_data = [380785, 87942, 325650, 2306]
dalian_edu_list_data = [[7129, 21457, 9372, 1181, 253641]]
dalian_gdp_data = [6810.20, 7363.90, 7668.50, 7001.70, 7030.40, 7825.90, 8430.90]
dalian_marry_data = [511206, 105380, 616586]
# ---------------------------数据段---------------------------


# # Create your views here.
# def index_unlog(request):
#     return render(request,'index_unlog.html')

# 超链接
def get_profile(request):
    return render(request, 'pages/users-profile.html')






def index(request):
    #表格实现



    # -----------------------长春市年龄分布详细表-----------------------
    changchun_people_age_data_show = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    changchun_people_age_data_show.add_xaxis(list(map(str, changchun_age_data.keys())))
    changchun_people_age_data_show.add_yaxis("详细年龄数据", list(map(str, changchun_age_data.values())))
    changchun_people_age_data_show.set_global_opts(
                                        title_opts=opts.TitleOpts(title="详细年龄数据"),
                                        datazoom_opts=[opts.DataZoomOpts()],
                                    )
    changchun_people_age_data_show_html = changchun_people_age_data_show.render_embed()
    # -----------------------长春市年龄分布详细表-----------------------



    # -----------------------两市GDP对比图--------------------------
    gdp_contrast_data_show = Line()
    gdp_contrast_data_show.add_xaxis(["2016","2017","2018","2019","2020","2021","2022"])
    gdp_contrast_data_show.add_yaxis(
        "大连市数据",
        dalian_gdp_data,
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
    )
    gdp_contrast_data_show.add_yaxis(
        "长春市数据",
        changchun_gdp_data,
        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
    )
    gdp_contrast_data_show.set_global_opts(title_opts=opts.TitleOpts(title="两市年GDP对比",subtitle="单位: 亿元"))
    # 渲染图表为HTML代码片段
    gdp_contrast_data_show_html = gdp_contrast_data_show.render_embed()
    # -----------------------两市GDP对比图--------------------------



    # -----------------------学历分布图------------------------------
    changchun_poeple_edu_data_show = Pie()
    x_data = list(map(str, changchun_edu_data.keys()))
    y_data = list(map(str, changchun_edu_data.values()))
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])
    changchun_poeple_edu_data_show.add(
                            "",
                            [list(z) for z in zip(x_data, y_data)],
                            radius=["40%", "55%"],
                            label_opts=opts.LabelOpts(
                                position="outside",
                                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                                background_color="#eee",
                                border_color="#aaa",
                                border_width=1,
                                border_radius=4,
                                rich={
                                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                                    "abg": {
                                        "backgroundColor": "#e3e3e3",
                                        "width": "100%",
                                        "align": "right",
                                        "height": 22,
                                        "borderRadius": [4, 4, 0, 0],
                                    },
                                    "hr": {
                                        "borderColor": "#aaa",
                                        "width": "100%",
                                        "borderWidth": 0.5,
                                        "height": 0,
                                    },
                                    "b": {"fontSize": 16, "lineHeight": 33},
                                    "per": {
                                        "color": "#eee",
                                        "backgroundColor": "#334455",
                                        "padding": [2, 4],
                                        "borderRadius": 2,
                                    },
                                },
                            ),
                        )
    changchun_poeple_edu_data_show.set_global_opts(title_opts=opts.TitleOpts(title="长春市学历分布图"))
    changchun_poeple_edu_data_show_html = changchun_poeple_edu_data_show.render_embed()
    # -----------------------学历分布图------------------------------  





    # ------------------------省市学历对比雷达图-------------------
    edu_contrast_data_show = Radar(init_opts=opts.InitOpts(bg_color="#ddd",width="820px"))
    edu_contrast_data_show.add_schema(
                            schema=[
                                opts.RadarIndicatorItem(name="专科", max_=35000),
                                opts.RadarIndicatorItem(name="其他", max_=120000),
                                opts.RadarIndicatorItem(name="本科", max_=25000),
                                opts.RadarIndicatorItem(name="硕士学历及以上", max_=6000),
                                opts.RadarIndicatorItem(name="高中学历及以下", max_=300000),
                            ],
                            splitarea_opt=opts.SplitAreaOpts(
                                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                            ),
                            textstyle_opts=opts.TextStyleOpts(color="#fff"),
                        )
    edu_contrast_data_show.add(
                            series_name="大连市学历分布情况",
                            data=dalian_edu_list_data,
                            linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
                        )
    edu_contrast_data_show.add(
                            series_name="长春市学历分布详情",
                            data=changchun_edu_list_data,
                            linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),
                        )
    edu_contrast_data_show.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    edu_contrast_data_show.set_global_opts(
                            title_opts=opts.TitleOpts(title="学历分布雷达图",subtitle="比赛用数据库数据存在较大偏差,效果仅供参考"), legend_opts=opts.LegendOpts()
                            )
    edu_contrast_data_show_html = edu_contrast_data_show.render_embed()
    # ------------------------省市学历对比雷达图-------------------





    # --------------------------长春市学历表格-----------------------
    changchun_poeple_edu_table_data_show = Table()
    headers = ["学历", "人数", "百分比"]
    rows = edu_list_data
    changchun_poeple_edu_table_data_show.add(headers, rows).set_global_opts(
                                            title_opts=opts.ComponentTitleOpts(title="长春市学历分布具体数据")
                                        )
    changchun_poeple_edu_table_data_show_html = changchun_poeple_edu_table_data_show.render_embed()    
    # --------------------------长春市学历表格-----------------------



    # ----------------------两市人口对比图---------------------------
    people_distribution_data_show = Bar({"theme": ThemeType.MACARONS})
    people_distribution_data_show.add_xaxis(["总人口","0-14岁","15-65岁","大于65岁",])
    people_distribution_data_show.add_yaxis("长春市", changchun_age_sorted_data)
    people_distribution_data_show.add_yaxis("大连市", dalian_age_sorted_data)
    people_distribution_data_show.set_global_opts(
                        title_opts={"text": "两市人口结构对比", "subtext": "备注:因为数据库数据并非全部数据,对大连市人口数据进行了缩放"}
                        )
    people_distribution_data_show_html = people_distribution_data_show.render_embed()
    # ----------------------两市人口对比图---------------------------



    # -----------------长春市人口分布示意图----------------
    ssl._create_default_https_context = ssl._create_unverified_context

    WIKI_LINK = ("http://tjj.changchun.gov.cn/tjgb/202106/t20210602_2830528.html")
    MAP_DATA = [
        ["南关区", 657682],
        ["宽城区", 669148],
        ["朝阳区", 614021],
        ["二道区", 522453],
        ["绿园区", 714919],
        ["双阳区", 335723],
        ["九台区", 569976],
        ["农安县", 867274],
        ["经济技术开发区", 429387],
        ["净月高新技术产业开发区", 408740],
        ["长春新区", 502165],
        ["汽车经济技术开发区", 317978],
        ["莲花山生态旅游度假区", 37513],
        ["中韩（长春）国际合作示范区", 29966],
        ["榆树市", 836098],
        ["德惠市", 691550],
        ["公主岭市", 862313],
    ]


    NAME_MAP_DATA = {
        # "key": "value"
        # "name on the hong kong map": "name in the MAP DATA",
        "南关区": "南关区",
        "宽城区": "宽城区",
        "朝阳区": "朝阳区",
        "二道区": "二道区",
        "绿园区": "绿园区",
        "双阳区": "双阳区",
        "九台区": "九台区",
        "农安县": "农安县",
        "经济技术开发区": "经济技术开发区",
        "净月高新技术产业开发区": "净月高新技术产业开发区",
        "长春新区": "长春新区",
        "汽车经济技术开发区": "汽车经济技术开发区",
        "莲花山生态旅游度假区": "莲花山生态旅游度假区",
        "中韩（长春）国际合作示范区": "中韩（长春）国际合作示范区",
        "榆树市": "榆树市",
        "德惠市": "德惠市",
        "公主岭市": "公主岭市",
    }

    changchun_people_distribution_map_data_show = Map()
    changchun_people_distribution_map_data_show.add(
                                                series_name="长春市17区人口密度",
                                                maptype="长春",
                                                data_pair=MAP_DATA,
                                                name_map=NAME_MAP_DATA,
                                                is_map_symbol_show=False,
                                            )
    changchun_people_distribution_map_data_show.set_global_opts(
                                            title_opts=opts.TitleOpts(
                                                title="长春市17区人口密度 (2020)",
                                                subtitle="人口密度数据来自 数据库&人口普查报告",
                                                subtitle_link=WIKI_LINK,
                                            ),
                                            tooltip_opts=opts.TooltipOpts(
                                                trigger="item", formatter="{b}<br/>{c} (p / km2)"
                                            ),
                                            visualmap_opts=opts.VisualMapOpts(
                                                min_=35000,
                                                max_=900000,
                                                range_text=["High", "Low"],
                                                is_calculable=True,
                                                range_color=["lightskyblue", "yellow", "orangered"],
                                                ),
                                            )
    changchun_people_distribution_map_data_show_html = changchun_people_distribution_map_data_show.render_embed()
    # -----------------长春市人口分布示意图----------------




    # -----------------------人口结构对比--------------------------
    list2 = [
        {"value": changchun_marry_data[0], "percent": changchun_marry_data[0] / changchun_marry_data[2]},
        {"value": dalian_marry_data[0], "percent": dalian_marry_data[0] / dalian_marry_data[2]},
        {"value": 179560, "percent": 179560 / (179560 + 261234)},
        {"value": 520611, "percent": 520611 / (520611 + 118053)},
        {"value": 485976, "percent": 485976 / (485976 + 128996)},
    ]

    list3 = [
        {"value": changchun_marry_data[1], "percent": changchun_marry_data[1] / changchun_marry_data[2]},
        {"value": dalian_marry_data[1], "percent": dalian_marry_data[1] / dalian_marry_data[2]},
        {"value": 261234, "percent": 261234 / (179560 + 261234)},
        {"value": 118053, "percent": 118053 / (520611 + 118053)},
        {"value": 128996, "percent": 128996 / (485976 + 128996)},
    ]
    test = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    test.add_xaxis(["长春市(数据库)", "大连市(拟合)", "虚拟数据1", "虚拟数据2", "虚拟数据3"])
    test.add_yaxis("已婚", list2, stack="stack1", category_gap="50%")
    test.add_yaxis("未婚", list3, stack="stack1", category_gap="50%")
    test.set_series_opts(
            label_opts=opts.LabelOpts(
                position="right",
                formatter=JsCode(
                    "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
                ),
            )
        )
    test.set_global_opts(title_opts=opts.TitleOpts(
                                                title="长春市&大连市婚姻情况(2022)",
                                                subtitle="人口密度数据来自 数据库&人口普查报告",
                                            ),)
    test_html = test.render_embed()
    # -----------------------人口结构对比--------------------------

    # -----------------长春市房价分布示意图----------------
    MAP_DATA = [
        ["南关区", 10436],
        ["宽城区", 8125],
        ["朝阳区", 10486],
        ["二道区", 8881],
        ["绿园区", 8313],
    ]

    changchun_fangjia_distribution_map_data_show = Map()
    changchun_fangjia_distribution_map_data_show.add(
                                                series_name="长春市5区房价",
                                                maptype="长春",
                                                data_pair=MAP_DATA,
                                                name_map=NAME_MAP_DATA,
                                                is_map_symbol_show=False,
                                            )
    changchun_fangjia_distribution_map_data_show.set_global_opts(
                                            title_opts=opts.TitleOpts(
                                                title="长春市5区房价 (2023)",
                                                subtitle="人口密度数据来自 网络",
                                                subtitle_link=WIKI_LINK,
                                            ),
                                            tooltip_opts=opts.TooltipOpts(
                                                trigger="item", formatter="{b}<br/>{c} (元 / m2)"
                                            ),
                                            visualmap_opts=opts.VisualMapOpts(
                                                min_=8000,
                                                max_=11000,
                                                range_text=["High", "Low"],
                                                is_calculable=True,
                                                range_color=["lightskyblue", "yellow", "orangered"],
                                                ),
                                            )
    changchun_fangjia_distribution_map_data_show_html = changchun_fangjia_distribution_map_data_show.render_embed()
    # -----------------长春市房价分布示意图----------------

    # -----------------长春市GDP分布示意图----------------
    MAP_DATA = [
        ["南关区", 427.9],
        ["宽城区", 328.0],
        ["朝阳区", 699.3],
        ["二道区", 207.4],
        ["绿园区", 276.6],
    ]

    changchun_GDP_distribution_map_data_show = Map()
    changchun_GDP_distribution_map_data_show.add(
                                                series_name="长春市5区GDP / 亿元",
                                                maptype="长春",
                                                data_pair=MAP_DATA,
                                                name_map=NAME_MAP_DATA,
                                                is_map_symbol_show=False,
                                            )
    changchun_GDP_distribution_map_data_show.set_global_opts(
                                            title_opts=opts.TitleOpts(
                                                title="长春市5区GDP / 亿元",
                                                subtitle="人口密度数据来自 网络",
                                                subtitle_link=WIKI_LINK,
                                            ),
                                            tooltip_opts=opts.TooltipOpts(
                                                trigger="item", formatter="{b}<br/>{c} (元 / m2)"
                                            ),
                                            visualmap_opts=opts.VisualMapOpts(
                                                min_=205,
                                                max_=700,
                                                range_text=["High", "Low"],
                                                is_calculable=True,
                                                range_color=["lightskyblue", "yellow", "orangered"],
                                                ),
                                            )
    changchun_GDP_distribution_map_data_show_html = changchun_GDP_distribution_map_data_show.render_embed()
    # -----------------长春市GDP分布示意图----------------

    # 将图表传递给模板
    context = {'changchun_people_age_data_show_html': changchun_people_age_data_show_html,
                'gdp_contrast_data_show_html': gdp_contrast_data_show_html,
                'changchun_poeple_edu_data_show_html':changchun_poeple_edu_data_show_html,
                'edu_contrast_data_show_html' :edu_contrast_data_show_html,
                'changchun_poeple_edu_table_data_show_html' :changchun_poeple_edu_table_data_show_html,
                'people_distribution_data_show_html' :people_distribution_data_show_html,
                'changchun_people_distribution_map_data_show_html' :changchun_people_distribution_map_data_show_html,
                'test_html' :test_html,
                'changchun_fangjia_distribution_map_data_show_html' : changchun_fangjia_distribution_map_data_show_html,
                'changchun_GDP_distribution_map_data_show_html' : changchun_GDP_distribution_map_data_show_html,
                }

    
    return render(request, 'index_unlog.html', context)
