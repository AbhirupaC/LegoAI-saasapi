

# class RulesABC:
#     # store all rules map to from great expectations
#     rules_map = {
#         "nullcheck":"expect_column_values_to_not_be_null",
#         "uniquecheck":"expect_column_values_to_be_unique",
#         "inlist":"expect_column_values_to_be_in_set"
#     }
#     def __init__(self, validator, rule,  params={}):
#         # get _rule from the rules_map
#         _rule = self.rules_map[rule.lower()]
#         # from validator get the rule method 
#         _validator= getattr(validator, _rule)
#         # call the validator method from validator and get summary. 
#         # assign the summary to object
#         column = params["column"]
#         self.summary = _validator(column, **params)

#     def getSummary(self):
#         # return summary
#         return self.summary

#     def addRuleColumn(self):
#         ...
class RulesABC:
    # store all rules map to from great expectations
    ge_rules_map = {
    'expect_table_row_count_to_equal': 'expect_table_row_count_to_equal',
	'expect_table_columns_to_match_ordered_list': 'expect_table_columns_to_match_ordered_list',
	'expect_column_to_exist': 'expect_column_to_exist',
	'expect_column_to_not_exist': 'expect_column_to_not_exist',
	'expect_column_values_to_be_unique': 'expect_column_values_to_be_unique',
	'expect_column_values_to_not_be_null': 'expect_column_values_to_not_be_null',
	'expect_column_values_to_be_null': 'expect_column_values_to_be_null',
	'expect_column_values_to_be_of_type': 'expect_column_values_to_be_of_type',
	'expect_column_values_to_be_in_set': 'expect_column_values_to_be_in_set',
	'expect_column_values_to_not_be_in_set': 'expect_column_values_to_not_be_in_set',
	'expect_column_values_to_be_in_type_list': 'expect_column_values_to_be_in_type_list',
	'expect_column_values_to_be_between': 'expect_column_values_to_be_between',
	'expect_column_value_lengths_to_be_between': 'expect_column_value_lengths_to_be_between',
	'expect_column_values_to_match_regex': 'expect_column_values_to_match_regex',
	'expect_column_values_to_not_match_regex': 'expect_column_values_to_not_match_regex',
	'expect_column_mean_to_be_between': 'expect_column_mean_to_be_between',
	'expect_column_median_to_be_between': 'expect_column_median_to_be_between',
	'expect_column_quantile_values_to_be_between': 'expect_column_quantile_values_to_be_between',
	'expect_column_stdev_to_be_between': 'expect_column_stdev_to_be_between',
	'expect_table_row_count_to_be_between': 'expect_table_row_count_to_be_between',
	'expect_column_distinct_values_to_be_in_set': 'expect_column_distinct_values_to_be_in_set',
	'expect_column_distinct_values_to_contain_set': 'expect_column_distinct_values_to_contain_set',
	'expect_column_distinct_values_to_equal_set': 'expect_column_distinct_values_to_equal_set',
	'expect_column_mean_to_be_greater_than': 'expect_column_mean_to_be_greater_than',
	'expect_column_mean_to_be_less_than': 'expect_column_mean_to_be_less_than',
	'expect_column_median_to_be_greater_than': 'expect_column_median_to_be_greater_than',
	'expect_column_median_to_be_less_than': 'expect_column_median_to_be_less_than',
	'expect_column_sum_to_be_between': 'expect_column_sum_to_be_between',
	'expect_column_min_to_be_between': 'expect_column_min_to_be_between',
	'expect_column_max_to_be_between': 'expect_column_max_to_be_between',
	'expect_column_values_to_be_unique_within_record': 'expect_column_values_to_be_unique_within_record',
	'expect_column_values_to_match_strftime_format': 'expect_column_values_to_match_strftime_format',
	'expect_column_values_to_be_dateutil_parseable': 'expect_column_values_to_be_dateutil_parseable',
	'expect_column_values_to_be_json_parseable': 'expect_column_values_to_be_json_parseable',
	'expect_column_values_to_match_json_schema': 'expect_column_values_to_match_json_schema',
	'expect_column_values_to_match_regex_list': 'expect_column_values_to_match_regex_list',
	'expect_column_values_to_not_match_regex_list': 'expect_column_values_to_not_match_regex_list',
	'expect_column_values_to_be_increasing': 'expect_column_values_to_be_increasing',
	'expect_column_values_to_be_decreasing': 'expect_column_values_to_be_decreasing',
	'expect_column_values_to_be_monotonically_increasing': 'expect_column_values_to_be_monotonically_increasing',
	'expect_column_values_to_be_monotonically_decreasing': 'expect_column_values_to_be_monotonically_decreasing',
	'expect_column_values_to_be_in_set_proportion_of_time': 'expect_column_values_to_be_in_set_proportion_of_time',
	'expect_column_kl_divergence_to_be_less_than': 'expect_column_kl_divergence_to_be_less_than',
	'expect_column_bootstrapped_ks_test_p_value_to_be_greater_than': 'expect_column_bootstrapped_ks_test_p_value_to_be_greater_than',
	'expect_compound_columns_to_be_unique': 'expect_compound_columns_to_be_unique',
	'expect_select_column_values_to_be_unique_within_record': 'expect_select_column_values_to_be_unique_within_record',
	'expect_column_pair_values_A_to_be_greater_than_B': 'expect_column_pair_values_A_to_be_greater_than_B',
	'expect_column_pair_values_to_be_equal': 'expect_column_pair_values_to_be_equal',
	'expect_multicolumn_values_to_be_unique': 'expect_multicolumn_values_to_be_unique',
	'expect_multicolumn_unique_composite_constraint': 'expect_multicolumn_unique_composite_constraint',
	'expect_column_values_to_be_within_n_std_devs': 'expect_column_values_to_be_within_n_std_devs',
	'expect_column_values_to_be_unique_within_tolerance': 'expect_column_values_to_be_unique_within_tolerance',
	'expect_multicolumn_values_to_be_unique_within_record': 'expect_multicolumn_values_to_be_unique_within_record',
	'expect_compound_columns_to_be_unique_within_record': 'expect_compound_columns_to_be_unique_within_record',
	'expect_column_values_to_be_increasing_strictly': 'expect_column_values_to_be_increasing_strictly',
	'expect_column_values_to_be_decreasing_strictly': 'expect_column_values_to_be_decreasing_strictly',
	'expect_column_values_to_be_non_increasing': 'expect_column_values_to_be_non_increasing',
	'expect_column_values_to_be_non_decreasing': 'expect_column_values_to_be_non_decreasing',
	'expect_column_values_to_be_mixture_of_datatypes': 'expect_column_values_to_be_mixture_of_datatypes',
	'expect_column_values_to_be_increasing_logical_units': 'expect_column_values_to_be_increasing_logical_units',
	'expect_column_values_to_be_decreasing_logical_units': 'expect_column_values_to_be_decreasing_logical_units',
	'expect_column_values_to_match_like_pattern': 'expect_column_values_to_match_like_pattern',
	'expect_column_values_to_match_regex_pattern': 'expect_column_values_to_match_regex_pattern',
	'expect_column_values_to_not_match_like_pattern': 'expect_column_values_to_not_match_like_pattern',
	'expect_column_values_to_not_match_regex_pattern': 'expect_column_values_to_not_match_regex_pattern',
	'expect_column_values_to_be_valid_email': 'expect_column_values_to_be_valid_email',
	'expect_column_values_to_be_valid_url': 'expect_column_values_to_be_valid_url',
	'expect_column_values_to_be_unique_within_groups': 'expect_column_values_to_be_unique_within_groups',
	'expect_column_values_to_match_yaml_schema': 'expect_column_values_to_match_yaml_schema',
	'expect_column_values_to_match_regex_with_options': 'expect_column_values_to_match_regex_with_options',
	'expect_column_values_to_be_increasing_batch_over_batch': 'expect_column_values_to_be_increasing_batch_over_batch',
	'expect_column_values_to_be_decreasing_batch_over_batch': 'expect_column_values_to_be_decreasing_batch_over_batch',
	'expect_table_column_count_to_equal': 'expect_table_column_count_to_equal',
	'expect_table_columns_to_match_set': 'expect_table_columns_to_match_set',
	'expect_table_columns_to_match_regex': 'expect_table_columns_to_match_regex',
	'expect_table_columns_to_match_ordered_set': 'expect_table_columns_to_match_ordered_set',
	'expect_table_columns_to_not_contain_duplicates': 'expect_table_columns_to_not_contain_duplicates',
	'expect_table_columns_to_be_of_type': 'expect_table_columns_to_be_of_type',
	'expect_table_columns_to_match_ordered_schema': 'expect_table_columns_to_match_ordered_schema',
	'expect_table_row_count_to_be_zero': 'expect_table_row_count_to_be_zero',
	'expect_table_row_count_to_equal_other_table': 'expect_table_row_count_to_equal_other_table',
	'expect_table_row_count_to_be_between_other_table': 'expect_table_row_count_to_be_between_other_table',
	'expect_table_row_count_to_match_regex': 'expect_table_row_count_to_match_regex',
	'expect_table_columns_to_match_ordered_list_ignore_missing': 'expect_table_columns_to_match_ordered_list_ignore_missing',
	'expect_table_columns_to_match_set_ignore_missing': 'expect_table_columns_to_match_set_ignore_missing',
	'expect_table_columns_to_match_ordered_set_ignore_missing': 'expect_table_columns_to_match_ordered_set_ignore_missing',
	'expect_table_columns_to_match_regex_ignore_missing': 'expect_table_columns_to_match_regex_ignore_missing',
	'expect_table_columns_to_match_ordered_schema_ignore_missing': 'expect_table_columns_to_match_ordered_schema_ignore_missing',
	'expect_table_columns_to_match_ordered_list_ignore_extra': 'expect_table_columns_to_match_ordered_list_ignore_extra',
	'expect_table_columns_to_match_set_ignore_extra': 'expect_table_columns_to_match_set_ignore_extra',
	'expect_table_columns_to_match_ordered_set_ignore_extra': 'expect_table_columns_to_match_ordered_set_ignore_extra',
	'expect_table_columns_to_match_regex_ignore_extra': 'expect_table_columns_to_match_regex_ignore_extra',
	'expect_table_columns_to_match_ordered_schema_ignore_extra': 'expect_table_columns_to_match_ordered_schema_ignore_extra',
	'expect_table_row_count_to_be_even': 'expect_table_row_count_to_be_even',
	'expect_table_row_count_to_be_odd': 'expect_table_row_count_to_be_odd',
	'expect_table_row_count_to_be_in_set': 'expect_table_row_count_to_be_in_set',
	'expect_column_proportion_of_unique_values_to_be_between': 'expect_column_proportion_of_unique_values_to_be_between',
	'expect_column_proportion_of_missing_values_to_be_between': 'expect_column_proportion_of_missing_values_to_be_between',
	'expect_column_proportion_of_unique_values_to_be_greater_than': 'expect_column_proportion_of_unique_values_to_be_greater_than',
	'expect_column_proportion_of_missing_values_to_be_greater_than': 'expect_column_proportion_of_missing_values_to_be_greater_than',
	'expect_table_columns_to_match_regex_list': 'expect_table_columns_to_match_regex_list',
	'expect_table_columns_to_not_match_regex_list': 'expect_table_columns_to_not_match_regex_list',
	'expect_multicolumn_sum_to_equal': 'expect_multicolumn_sum_to_equal',
	'expect_multicolumn_sum_to_be_between': 'expect_multicolumn_sum_to_be_between',
	'expect_multicolumn_mean_to_equal': 'expect_multicolumn_mean_to_equal',
	'expect_multicolumn_mean_to_be_between': 'expect_multicolumn_mean_to_be_between',
	'expect_multicolumn_median_to_equal': 'expect_multicolumn_median_to_equal',
	'expect_multicolumn_median_to_be_between': 'expect_multicolumn_median_to_be_between',
	'expect_column_values_to_be_in_list': 'expect_column_values_to_be_in_list',
	'expect_column_values_to_not_be_in_list': 'expect_column_values_to_not_be_in_list',
	'expect_table_row_count_to_equal_other_table_subset': 'expect_table_row_count_to_equal_other_table_subset',
	'expect_table_row_count_to_be_increasing_batch_over_batch': 'expect_table_row_count_to_be_increasing_batch_over_batch',
	'expect_table_column_count_to_be_between': 'expect_table_column_count_to_be_between',
	'expect_table_row_count_to_equal_other_table_filtered': 'expect_table_row_count_to_equal_other_table_filtered',
	'expect_table_row_count_to_match_other_table_filtered_regex': 'expect_table_row_count_to_match_other_table_filtered_regex',
	'expect_table_row_count_to_be_null': 'expect_table_row_count_to_be_null',
	'expect_table_row_count_to_not_be_null': 'expect_table_row_count_to_not_be_null',
	'expect_column_distinct_values_to_be_unique': 'expect_column_distinct_values_to_be_unique',
	'expect_column_distinct_values_to_not_be_null': 'expect_column_distinct_values_to_not_be_null',
	'expect_column_distinct_values_to_not_be_in_set': 'expect_column_distinct_values_to_not_be_in_set',
	'expect_column_pair_values_to_be_equal_within_tolerance': 'expect_column_pair_values_to_be_equal_within_tolerance',
	'expect_multicolumn_values_to_not_be_null': 'expect_multicolumn_values_to_not_be_null',
	'expect_multicolumn_values_to_be_of_type': 'expect_multicolumn_values_to_be_of_type',
	'expect_compound_columns_to_not_be_null': 'expect_compound_columns_to_not_be_null',
	'expect_compound_columns_to_be_of_type': 'expect_compound_columns_to_be_of_type',
	'expect_column_values_to_be_of_type_with_regex': 'expect_column_values_to_be_of_type_with_regex',
	'expect_column_values_to_be_between_time': 'expect_column_values_to_be_between_time',
	'expect_column_values_to_be_dateutil_parseable_to_format': 'expect_column_values_to_be_dateutil_parseable_to_format'
}


    summary = {}
    def __init__(self, df, rule,  params={}):
        if self.ge_rules_map.get(rule) !=None:
            rulehandler = RulesGEHandler(df,self.ge_rules_map.get(rule), params)
            self.summary = rulehandler.getSummary()
        else:
            print("use next rule")
            
    def getSummary(self):
        return self.summary

    def ___del___(self):
        self.summary = {}

from src.core.dataset import GeDataset
class RulesGEHandler:
    def __init__(self, df, rule,  params={}):
        # get _rule from the rules_map
        dataset = GeDataset()
        validator = dataset.getValidator(df, "testDf", "testSuite" ,datatype="spark") 
        # from validator get the rule method 
        _validator= getattr(validator, rule)
        # call the validator method from validator and get summary. 
        # assign the summary to object
        column = params["column"]
        self.summary = _validator(column, **params)

    def getSummary(self):
        # return summary
        return self.summary