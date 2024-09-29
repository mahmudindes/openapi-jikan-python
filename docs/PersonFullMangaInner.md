# PersonFullMangaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | Person&#39;s position | [optional] 
**manga** | [**MangaMeta**](MangaMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.person_full_manga_inner import PersonFullMangaInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonFullMangaInner from a JSON string
person_full_manga_inner_instance = PersonFullMangaInner.from_json(json)
# print the JSON string representation of the object
print(PersonFullMangaInner.to_json())

# convert the object into a dict
person_full_manga_inner_dict = person_full_manga_inner_instance.to_dict()
# create an instance of PersonFullMangaInner from a dict
person_full_manga_inner_form_dict = person_full_manga_inner.from_dict(person_full_manga_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


