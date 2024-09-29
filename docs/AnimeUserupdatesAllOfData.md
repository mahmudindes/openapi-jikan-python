# AnimeUserupdatesAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserMeta**](UserMeta.md) |  | [optional] 
**score** | **int** | User Score | [optional] 
**status** | **str** | User list status | [optional] 
**episodes_seen** | **int** | Number of episodes seen | [optional] 
**episodes_total** | **int** | Total number of episodes | [optional] 
**var_date** | **str** | Last updated date ISO8601 | [optional] 

## Example

```python
from jikan_openapi.models.anime_userupdates_all_of_data import AnimeUserupdatesAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeUserupdatesAllOfData from a JSON string
anime_userupdates_all_of_data_instance = AnimeUserupdatesAllOfData.from_json(json)
# print the JSON string representation of the object
print(AnimeUserupdatesAllOfData.to_json())

# convert the object into a dict
anime_userupdates_all_of_data_dict = anime_userupdates_all_of_data_instance.to_dict()
# create an instance of AnimeUserupdatesAllOfData from a dict
anime_userupdates_all_of_data_form_dict = anime_userupdates_all_of_data.from_dict(anime_userupdates_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


