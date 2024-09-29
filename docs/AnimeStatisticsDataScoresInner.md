# AnimeStatisticsDataScoresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | Scoring value | [optional] 
**votes** | **int** | Number of votes for this score | [optional] 
**percentage** | **float** | Percentage of votes for this score | [optional] 

## Example

```python
from jikan_openapi.models.anime_statistics_data_scores_inner import AnimeStatisticsDataScoresInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeStatisticsDataScoresInner from a JSON string
anime_statistics_data_scores_inner_instance = AnimeStatisticsDataScoresInner.from_json(json)
# print the JSON string representation of the object
print(AnimeStatisticsDataScoresInner.to_json())

# convert the object into a dict
anime_statistics_data_scores_inner_dict = anime_statistics_data_scores_inner_instance.to_dict()
# create an instance of AnimeStatisticsDataScoresInner from a dict
anime_statistics_data_scores_inner_form_dict = anime_statistics_data_scores_inner.from_dict(anime_statistics_data_scores_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


