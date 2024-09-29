# GetTopReviews200ResponseDataAllOfDataInnerAnyOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList review URL | [optional] 
**type** | **str** | Entry type | [optional] 
**reactions** | [**MangaReviewReactions**](MangaReviewReactions.md) |  | [optional] 
**var_date** | **str** | Review created date ISO8601 | [optional] 
**review** | **str** | Review content | [optional] 
**score** | **int** | Number of user votes on the Review | [optional] 
**tags** | **List[str]** | Review tags | [optional] 
**is_spoiler** | **bool** | The review contains spoiler | [optional] 
**is_preliminary** | **bool** | The review was made before the entry was completed | [optional] 
**user** | [**UserMeta**](UserMeta.md) |  | [optional] 
**manga** | [**MangaMeta**](MangaMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.get_top_reviews200_response_data_all_of_data_inner_any_of1 import GetTopReviews200ResponseDataAllOfDataInnerAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetTopReviews200ResponseDataAllOfDataInnerAnyOf1 from a JSON string
get_top_reviews200_response_data_all_of_data_inner_any_of1_instance = GetTopReviews200ResponseDataAllOfDataInnerAnyOf1.from_json(json)
# print the JSON string representation of the object
print(GetTopReviews200ResponseDataAllOfDataInnerAnyOf1.to_json())

# convert the object into a dict
get_top_reviews200_response_data_all_of_data_inner_any_of1_dict = get_top_reviews200_response_data_all_of_data_inner_any_of1_instance.to_dict()
# create an instance of GetTopReviews200ResponseDataAllOfDataInnerAnyOf1 from a dict
get_top_reviews200_response_data_all_of_data_inner_any_of1_form_dict = get_top_reviews200_response_data_all_of_data_inner_any_of1.from_dict(get_top_reviews200_response_data_all_of_data_inner_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


