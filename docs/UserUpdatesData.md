# UserUpdatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime** | [**List[UserUpdatesDataAnimeInner]**](UserUpdatesDataAnimeInner.md) | Last updated Anime | [optional] 
**manga** | [**List[UserUpdatesDataMangaInner]**](UserUpdatesDataMangaInner.md) | Last updated Manga | [optional] 

## Example

```python
from jikan_openapi.models.user_updates_data import UserUpdatesData

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdatesData from a JSON string
user_updates_data_instance = UserUpdatesData.from_json(json)
# print the JSON string representation of the object
print(UserUpdatesData.to_json())

# convert the object into a dict
user_updates_data_dict = user_updates_data_instance.to_dict()
# create an instance of UserUpdatesData from a dict
user_updates_data_form_dict = user_updates_data.from_dict(user_updates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


