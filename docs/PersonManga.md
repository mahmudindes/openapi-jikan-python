# PersonManga

Person's mangaography

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PersonFullMangaInner]**](PersonFullMangaInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_manga import PersonManga

# TODO update the JSON string below
json = "{}"
# create an instance of PersonManga from a JSON string
person_manga_instance = PersonManga.from_json(json)
# print the JSON string representation of the object
print(PersonManga.to_json())

# convert the object into a dict
person_manga_dict = person_manga_instance.to_dict()
# create an instance of PersonManga from a dict
person_manga_form_dict = person_manga.from_dict(person_manga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


