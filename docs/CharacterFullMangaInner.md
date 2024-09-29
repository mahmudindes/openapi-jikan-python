# CharacterFullMangaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Character&#39;s Role | [optional] 
**manga** | [**MangaMeta**](MangaMeta.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.character_full_manga_inner import CharacterFullMangaInner

# TODO update the JSON string below
json = "{}"
# create an instance of CharacterFullMangaInner from a JSON string
character_full_manga_inner_instance = CharacterFullMangaInner.from_json(json)
# print the JSON string representation of the object
print(CharacterFullMangaInner.to_json())

# convert the object into a dict
character_full_manga_inner_dict = character_full_manga_inner_instance.to_dict()
# create an instance of CharacterFullMangaInner from a dict
character_full_manga_inner_form_dict = character_full_manga_inner.from_dict(character_full_manga_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


