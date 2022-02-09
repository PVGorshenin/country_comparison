from sklearn.metrics.pairwise import euclidean_distances


def search_a_buddie(standings_df, config):
    #TODO: kill hardcode
    start_of_values_col = 'gdp_ppp'
    country_buddie = None
    min_dist = 100500

    inp_country = standings_df.loc[standings_df['country'] == config['country_to_highlight'],
                                  start_of_values_col:].values
    other_countries = standings_df.loc[standings_df['country'] != config['country_to_highlight'],
                                      start_of_values_col:].values
    other_countries_n =standings_df.loc[standings_df['country'] != config['country_to_highlight'],
                                        'country'].values
    for country_name, country_vect in zip(other_countries_n, other_countries):
        curr_dist = euclidean_distances(inp_country.reshape(1, -1), country_vect.reshape(1, -1))
        if curr_dist < min_dist:
            country_buddie = country_name
            min_dist = curr_dist

    return country_buddie
