SELECT episode_date, tc.neighbourhood_name, age_group, gender, outcome, ever_hospitalized, ever_in_icu, ever_intubated, population_density, average_income, commute_public_transit, avg_temperature, avg_relative_humidity
FROM "Toronto_Cases" tc
INNER JOIN "Toronto_Stats" ts ON tc.neighbourhood_name = ts.neighbourhood_name
LEFT JOIN (SELECT neighbourhood_name, (commute_car_driver::NUMERIC + commute_car_passenger::NUMERIC) / commute_total::NUMERIC AS "commute_car",
commute_public_transit::NUMERIC / commute_total::NUMERIC AS "commute_public_transit", commute_walk::NUMERIC / commute_total::NUMERIC AS "commute_walk",
commute_bicycle::NUMERIC / commute_total::NUMERIC AS "commute_bicycle", commute_other::NUMERIC / commute_total::NUMERIC AS "commute_other"
FROM "Toronto_Commute"
) commute ON tc.neighbourhood_name = commute.neighbourhood_name
LEFT JOIN "Toronto_Weather" tw ON tc.episode_date = tw.date