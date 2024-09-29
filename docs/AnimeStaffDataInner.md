# AnimeStaffDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**AnimeStaffDataInnerPerson**](AnimeStaffDataInnerPerson.md) |  | [optional] 
**positions** | **List[str]** | Staff Positions | [optional] 

## Example

```python
from jikan_openapi.models.anime_staff_data_inner import AnimeStaffDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeStaffDataInner from a JSON string
anime_staff_data_inner_instance = AnimeStaffDataInner.from_json(json)
# print the JSON string representation of the object
print(AnimeStaffDataInner.to_json())

# convert the object into a dict
anime_staff_data_inner_dict = anime_staff_data_inner_instance.to_dict()
# create an instance of AnimeStaffDataInner from a dict
anime_staff_data_inner_form_dict = anime_staff_data_inner.from_dict(anime_staff_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


