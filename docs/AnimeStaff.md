# AnimeStaff

Anime Staff Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AnimeStaffDataInner]**](AnimeStaffDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.anime_staff import AnimeStaff

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeStaff from a JSON string
anime_staff_instance = AnimeStaff.from_json(json)
# print the JSON string representation of the object
print(AnimeStaff.to_json())

# convert the object into a dict
anime_staff_dict = anime_staff_instance.to_dict()
# create an instance of AnimeStaff from a dict
anime_staff_form_dict = anime_staff.from_dict(anime_staff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


