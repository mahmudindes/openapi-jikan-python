# AnimeStaffDataInnerPerson

Person details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**images** | [**PeopleImages**](PeopleImages.md) |  | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from jikan_openapi.models.anime_staff_data_inner_person import AnimeStaffDataInnerPerson

# TODO update the JSON string below
json = "{}"
# create an instance of AnimeStaffDataInnerPerson from a JSON string
anime_staff_data_inner_person_instance = AnimeStaffDataInnerPerson.from_json(json)
# print the JSON string representation of the object
print(AnimeStaffDataInnerPerson.to_json())

# convert the object into a dict
anime_staff_data_inner_person_dict = anime_staff_data_inner_person_instance.to_dict()
# create an instance of AnimeStaffDataInnerPerson from a dict
anime_staff_data_inner_person_form_dict = anime_staff_data_inner_person.from_dict(anime_staff_data_inner_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


