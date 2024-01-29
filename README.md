# country-comparison

### Таблица источников

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



### Текущие показатели

`
gdp_ppp, homicide_rate, suicide_rate, purchasing_power_numbeo, property_price_to_income_numbeo,
safety_numbeo, health_care_numbeo, traffic_commute_time_numbeo, pollution_numbeo, climate_numbeo, 
life_expectancy, happiness, unesco_objects, distance_to_30_years, gini, incarceration_rate`

