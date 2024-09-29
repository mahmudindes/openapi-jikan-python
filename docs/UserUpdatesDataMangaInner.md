# UserUpdatesDataMangaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**MangaMeta**](MangaMeta.md) |  | [optional] 
**score** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**chapters_read** | **int** |  | [optional] 
**chapters_total** | **int** |  | [optional] 
**volumes_read** | **int** |  | [optional] 
**volumes_total** | **int** |  | [optional] 
**var_date** | **str** | ISO8601 format | [optional] 

## Example

```python
from jikan_openapi.models.user_updates_data_manga_inner import UserUpdatesDataMangaInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdatesDataMangaInner from a JSON string
user_updates_data_manga_inner_instance = UserUpdatesDataMangaInner.from_json(json)
# print the JSON string representation of the object
print(UserUpdatesDataMangaInner.to_json())

# convert the object into a dict
user_updates_data_manga_inner_dict = user_updates_data_manga_inner_instance.to_dict()
# create an instance of UserUpdatesDataMangaInner from a dict
user_updates_data_manga_inner_form_dict = user_updates_data_manga_inner.from_dict(user_updates_data_manga_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


