# MangaUserupdatesAllOfData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserMeta**](UserMeta.md) |  | [optional] 
**score** | **int** | User Score | [optional] 
**status** | **str** | User list status | [optional] 
**volumes_read** | **int** | Number of volumes read | [optional] 
**volumes_total** | **int** | Total number of volumes | [optional] 
**chapters_read** | **int** | Number of chapters read | [optional] 
**chapters_total** | **int** | Total number of chapters | [optional] 
**var_date** | **str** | Last updated date ISO8601 | [optional] 

## Example

```python
from jikan_openapi.models.manga_userupdates_all_of_data import MangaUserupdatesAllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of MangaUserupdatesAllOfData from a JSON string
manga_userupdates_all_of_data_instance = MangaUserupdatesAllOfData.from_json(json)
# print the JSON string representation of the object
print(MangaUserupdatesAllOfData.to_json())

# convert the object into a dict
manga_userupdates_all_of_data_dict = manga_userupdates_all_of_data_instance.to_dict()
# create an instance of MangaUserupdatesAllOfData from a dict
manga_userupdates_all_of_data_form_dict = manga_userupdates_all_of_data.from_dict(manga_userupdates_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


