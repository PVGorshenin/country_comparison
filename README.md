# country-comparison

### The goal.

What the metric we will choose such a place we will take).

I like to compare countries. But I haven't succeeded in finding a fair and
comprehensive rating. 
So I have made my own. Just for fun. 

This repo is an attempt to unite different statistics(features)
in one score. To achieve user-specific results one could regulate the weight of the 
parameter by changing it in the config. 

I chose features for my taste. I didn't use those which look suspicious to me. 
Or just gave them lower coefficients. 

Next will be the section with examples of inaccuracies in methodology. If you are not interested
just jump to the next section

**Numbeo is good**. But only to compare private services.

**Purchasing power index** does not evaluate the cost of school, university, and kinder
garden with respect to the ratio of free public institutions available.

**Property to income index** does not account for home ownership rate. 
Ex-social block countries look much better that way. 


**Coefficients in quality of life index** doesn't reflect my view of an image too.

**Median Wealth per adult by Credit Suisse**  3K $ for Russia looks really awkward. 
Because 86% of adults leave in their own homes. A lot of households have two and more.
Some people have land in possession. Those should give roughly around 10K without consideration of cars,
stocks, banking accounts, cash, etc.

And a lot more.

### To run

The whole project has been made in python. To run it simply install it with

`pip install -e .`

and run

`python run main.py`

The config file is placed in config.yaml. There you can specify which features to use and corresponding 
coefficients. 

You should specify the output folder with `res_filepath` in the config. 

I placed the script's input data in `match_table_filepath` in the config. Right now it 
`data/result/mega_table.csv` 

### Data

Data sources are placed in `source_lst.csv`. As the basic set of countries, I chose the one from the
numbeo. It covers my needs, and it makes matching different sources easier.

I chose not to make automatic scrapping and matching. Sources are pretty diverse in naming, and it is
just faster to make a manual matching. 
Data cleaning and matching could be found in the `making_data` branch.

### Methodology

Each feature is mapped to a `[0, 100]` interval by MinMax scaling. Next, they summed up after multiplying
with **weights** from the config. Obtained results are passed to the MinMax scaling once again to get
the final score.

If the feature contains **outliers** you can specify left and right quantile for clipping an input. 

### Currently available features

`gdp_ppp, homicide_rate, suicide_rate, purchasing_power_numbeo, property_price_to_income_numbeo,
safety_numbeo, health_care_numbeo, traffic_commute_time_numbeo, pollution_numbeo, climate_numbeo, 
life_expectancy`