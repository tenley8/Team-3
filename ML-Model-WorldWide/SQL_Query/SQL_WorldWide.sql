SELECT location, date, date_first_case, DATE_PART('day', date - date_first_case) AS "day_from_first_case",
total_cases, total_deaths, new_cases, new_deaths, stringency_index, population, population_density, median_age, aged_65_older, aged_70_older, 
gdp_per_capita, extreme_poverty, diabetes_prevalence, female_smokers, male_smokers, handwashing_facilities, hospital_beds_per_thousand, life_expectancy
FROM "WorldWide_Cases" ww
LEFT JOIN "Country_FirstCase" fc ON ww.iso_code = fc.iso_code
LEFT JOIN "Country_Stats" cs ON ww.iso_code = cs.iso_code