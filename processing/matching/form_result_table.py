import json
import os
import pandas as pd
import yaml

from collections import Counter


indicators_path = '../../data/intermediate/2023'
numbeo_filepath = '../../data/intermediate/2023/numbeo_renamed.csv'
res_filepath = '../../data/result/2023/all_indicators.csv'

with open('roots_n_match.yaml') as f:
    roots_n_match = yaml.safe_load(f)


country_name_roots = roots_n_match['country_name_roots']
countries_w_complicated_naming = roots_n_match['countries_w_comlicated_naming']


def get_country_aliases(indicators_path, indicatores_filenames, country_name_root):
    alias_lst = []
    for filename in indicatores_filenames:
        df = pd.read_csv(os.path.join(indicators_path, filename))

        curr_alias = [name for name in df['country'].to_list() if country_name_root in name]

        alias_lst.extend(curr_alias)

    return alias_lst


def get_country_alias_match(country_name_roots, indicators_path, indicatores_filenames):

    for country_name_root in country_name_roots:

        alias_lst = get_country_aliases(indicators_path, indicatores_filenames, country_name_root)
        n_country_occurences = 0
        curr_alliases = []

        for i_item, item in enumerate(Counter(alias_lst).most_common()):
            n_country_occurences += item[1]

            if i_item == 0:
                curr_country = item[0]
            else:
                curr_alliases.append(item[0])


        if n_country_occurences == len(indicatores_filenames):
            country_alias_match[curr_country] = curr_alliases
        else:
            print(Counter(alias_lst), n_country_occurences)

    return country_alias_match


def rename_aliases_in_df(df, country_alias_match):

    for country_name, country_aliases in country_alias_match.items():
        for alias in country_aliases:
            is_alias_found_mask = df['country'] == alias

            assert is_alias_found_mask.sum() <= 1

            if is_alias_found_mask.sum():

                df.loc[is_alias_found_mask, 'country'] = country_name

    return df


indicatores_filenames = os.listdir(indicators_path)

country_alias_match = {}

print(get_country_aliases(indicators_path, indicatores_filenames, 'Venez'))


country_alias_match = get_country_alias_match(
    country_name_roots,
    indicators_path,
    indicatores_filenames
)

country_alias_match |= countries_w_complicated_naming

numbeo_df = pd.read_csv(numbeo_filepath)

numbeo_df = rename_aliases_in_df(numbeo_df, country_alias_match)
print(numbeo_df.shape)

for filename in indicatores_filenames:
    if filename == 'numbeo_renamed.csv':
        continue

    curr_df = pd.read_csv(os.path.join(indicators_path, filename))
    curr_df = rename_aliases_in_df(curr_df, country_alias_match)

    numbeo_df = numbeo_df.merge(
        curr_df, how='left', on='country'
    )

not_enough_indicators = ['Hong Kong (China)', 'Taiwan']
not_enough_indicators_mask = numbeo_df['country'].map(lambda z: z in not_enough_indicators)
numbeo_df = numbeo_df[~not_enough_indicators_mask]


numbeo_df.to_csv(res_filepath, index=None)





