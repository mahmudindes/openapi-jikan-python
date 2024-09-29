# PersonAnime

Person anime staff positions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PersonAnimeDataInner]**](PersonAnimeDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_anime import PersonAnime

# TODO update the JSON string below
json = "{}"
# create an instance of PersonAnime from a JSON string
person_anime_instance = PersonAnime.from_json(json)
# print the JSON string representation of the object
print(PersonAnime.to_json())

# convert the object into a dict
person_anime_dict = person_anime_instance.to_dict()
# create an instance of PersonAnime from a dict
person_anime_form_dict = person_anime.from_dict(person_anime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


