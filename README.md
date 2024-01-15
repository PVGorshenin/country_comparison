# country-comparison

### Цель.

Какую метрику придумаем такое место и займём

Данный репозиторий - попытка создать рейтинг стран на основании отдельных
показателей. Много циферок хорошо, но одна цифра понятней. При этом рейтинг не про то, где лучше номаду, а
скорее про то, где лучше гражданам в целом.

Конечный скор не претендует на объективность. Как говорил мой декан: `жизнь шире всех систем`.

<details>

<summary> Таблица источников</summary>

| Показытель         | Год актуальности | Источник                                                                                                                       |
|--------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| gdp ppp            | 2024 start-year  | https://www.imf.org/external/datamapper/PPPPC@WEO/OEMDC/ADVEC/WEOWORLD                                                         |
| homicide rate      | 2018             | https://dataunodc.un.org/content/homicide-rate-option-2                                                                        |
| numbeo             | 2023 mid-year    | https://www.numbeo.com/quality-of-life/rankings_by_country.jsp                                                                 |
| suicide rate       | 2019             | https://apps.who.int/gho/data/node.main.MHSUICIDEASDR?lang=en                                                                  |
| life expectancy    | 2020 end-year    | https://apps.who.int/gho/data/node.main.688                                                                                    |
| happiness index    | 2021             | https://worldhappiness.report/ed/2021/#appendices-and-data                                                                     |
| unesco objects     | 2023             | https://en.wikipedia.org/wiki/World_Heritage_Sites_by_country                                                                  |
| median age         | 2022             | https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_Population/WPP2019_POP_F05_MEDIAN_AGE.xlsx |
| gini               | 2022             | https://data.worldbank.org/indicator/SI.POV.GINI/                                                                              |
| incarceration rate | 2023 mid-year    | https://www.prisonstudies.org/highest-to-lowest/prison_population_rate?field_region_taxonomy_tid=All                           |


</details>


<details>  

<summary> Сумбурная критика показателей  </summary> 

Numbeo отличный бейзлайн, но у него есть следующие недостатки

`Numbeo purchasing power index` - не учитывает количество бесплатных или условно бесплатных благ. Например,
оплата садика в РФ и Нидерландах отличается раз в 20. Высшее образование тоже мегатрата в некоторых странах. 
Также показатель не учитывает безработицу, размер пенсии или налог на пользование автомобилем.  

`Numbeo property to income index` - отражает ситуацию в моменте. Но не учитывает долю населения, имеющую 
недвижимость во владении. Или качество жилья, как таковое.

`Идеальный медианный возраст(distance_to_30_years)` - я взял равным 30 исключительно из субъективных соображений.
Более молодые нации имеют иждивенцев внизу половозрастной пирамиды, более старые вверху. Можно было бы взять 35 лет, но всё же у 
более молодых стран больше надежды. 

**Отклонённые показатели**

`Median Wealth per adult от Credit Suisse` - 3K$ для РФ не покрывает даже недвижимость. 
Сложно не поверить в теории заговора, глядя на эти цифры 

`уровеь безработицы` - умеют считать нормально только развитые бюрократии, к. не так чтобы много.

</details>


### Визуальный интерфейс
![img.png](data/aux/interface.png)


### Ссылка для ознакомления

[Visit](https://share.streamlit.io/pvgorshenin/country_comparison/main/main.py)


### Сбор данных

В качестве базового набора стран использован набор из numbeo. Набор стран разнится между источниками, 
но мэтчинг редких стран и разных написаний одной страны слишком трудоёмкий.

Сбор данных происходит в полурочном режиме внутри ветки
[making_data](https://github.com/PVGorshenin/country_comparison/tree/making_data)
Многие показатели выкладываются в виде excel-файлов. Поэтому труд на автоматизацию не факт, что окупится.
Внутри `making_data` [парсится](https://github.com/PVGorshenin/country_comparison/tree/making_data/get_data/parse), что доступно парсингу.
Excel файлы пинаются костылём в `data/input/<year>`.

Далее файлы обрабатываются ноутбуками 
[здесь](https://github.com/PVGorshenin/country_comparison/tree/making_data/notebook).
Финальный результат, сметчинных показателей хранится 
[здесь](https://github.com/PVGorshenin/country_comparison/blob/making_data/data/result/mega_table.csv). 
В main этот файл попадает без мёрджа через checkout из making_data.

### Запуск

Проект написан на **python** с использование  **streamlit** в качестве веб-интерфейса. 
Команда для установки
`pip install -e .`

и запуска

`streamlit run main.py`

web-интерфейс станет доступен по адресу `localhost:8501`

### Конфигурирование

Настройки передаются через [конфиг-файл](config.yaml). Здесь можно задать базовые веса для коэффециентов.
Данные веса будут использованы в качестве дефолтных и далее могут быть измененины в web-интерфейсе. 

Перед запуском нужно указать в конфиге `res_filepath`. В эту папку выгрузится картинка с финальным
положением стран.

### Методология

Каждый параметр маппится в интервал `[0, 100]` с помощью `MinMax scaling`. Далее показатели 
суммируются с весами из [конфиг-файла](config.yaml) (для локального запуска) или с весами с формы.
В web-интерфесе границы бегунка находятся в интервале `[0, 10]` для удобства. 
Но под капотом веса приводятся к интервалу `[0, 1]`.
Полученный результат повтор маппится в `[0, 100]`

Некоторые показатели, например `gdp_ppp` содержат выбросы(мин-макс сильно удалённые от основной массы точек).
Лечится обрезанием по квантилям. Уникальная возможность обрезать Норвегию или Люксембург в поле `feature_clips` 
конфига.

### Текущие показатели

`
gdp_ppp, homicide_rate, suicide_rate, purchasing_power_numbeo, property_price_to_income_numbeo,
safety_numbeo, health_care_numbeo, traffic_commute_time_numbeo, pollution_numbeo, climate_numbeo, 
life_expectancy, happiness, unesco_objects, distance_to_30_years, gini, incarceration_rate`

### Search a buddie

Алгоритм ищет ближайшую страну в признаковом пространстве по евклидовой метрике.
Исходная страна указывается в (`config[country_to_highlight]`). 
Данный алгоритм - это попытка найти самую приближённую страну к рассматриваемой. 
Ручка для включения - поле `is_buddie_highlight` в конфиге.
