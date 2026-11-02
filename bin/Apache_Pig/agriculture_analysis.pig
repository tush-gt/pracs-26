-- Run in Pig Grunt. Sample schema must match crop_production.csv column order.
-- Expected fields: State_Name,District_Name,Crop_Year,Season,Crop,Area,Production

agriculture = LOAD 'crop_production.csv'
USING PigStorage(',')
AS (state_name:chararray, district_name:chararray, crop_year:int,
    season:chararray, crop:chararray, area:double, production:double);

-- If CSV has a header row, filter it out:
agriculture_clean = FILTER agriculture BY state_name IS NOT NULL
    AND state_name != 'State_Name';

DESCRIBE agriculture_clean;
DUMP agriculture_clean;

-- Group all records state-wise.
state_groups = GROUP agriculture_clean BY state_name;
DESCRIBE state_groups;
DUMP state_groups;

-- Sum production for each state.
state_production = FOREACH state_groups GENERATE
    group AS state,
    SUM(agriculture_clean.production) AS total_production;
DUMP state_production;

-- Highest production record/crop in each state.
-- This is the highest individual crop/district/year record per state.
ordered_per_state = FOREACH state_groups {
    sorted_rows = ORDER agriculture_clean BY production DESC;
    top_row = LIMIT sorted_rows 1;
    GENERATE group AS state, FLATTEN(top_row);
};
DUMP ordered_per_state;

STORE ordered_per_state INTO 'data_top_output' USING PigStorage(',');
