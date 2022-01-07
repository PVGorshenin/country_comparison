import Levenshtein


def match_country_spelling(df, diff_btw_sources, is_first_word, country_col='country'):
    closest_dict = {}

    for country_n in diff_btw_sources:
        min_levi = 100

        for country_g in set(df[country_col]):
            if is_first_word:
                curr_levi = Levenshtein.distance(country_n.split(' ')[0], country_g.split(' ')[0])
            else:
                curr_levi = Levenshtein.distance(country_n, country_g)

            if curr_levi < min_levi:
                min_levi = curr_levi
                closest_dict[country_n] = country_g

    return closest_dict
