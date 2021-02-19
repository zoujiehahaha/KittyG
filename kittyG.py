import pyecharts.options as opts
from pyecharts.charts import Calendar
import pandas as pd 
from pyecharts.charts import Page, Tab
from pyecharts.globals import ThemeType
df=pd.read_excel('kittycommit.xlsx')
l = []
for x in range(len(df)):
    l.append([str(df["date"][x]), df["commit"][x]])
print(l)
Calendar_1 = Calendar(
    init_opts=opts.InitOpts(
        width="100%", height="400px", theme=ThemeType.WONDERLAND
    )
)

Calendar_1.add(
    series_name="JustDoit",
    yaxis_data=l,
    calendar_opts=opts.CalendarOpts(
        pos_top="120",
        pos_left="30",
        pos_right="30",
        range_= 2021,
        daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
        monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
        yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
    ),
)
Calendar_1.set_global_opts(
    title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2021年日历"),
    visualmap_opts=opts.VisualMapOpts(
        max_=10,
        min_=0,
        orient="horizontal",
        is_piecewise=False,
        pos_right=20,
        pos_bottom=20,
    ),
)
pages2 = Page(layout=Page.SimplePageLayout, interval=20)
pages2.add(Calendar_1)
pages2.render("./kittyG2021.html")
