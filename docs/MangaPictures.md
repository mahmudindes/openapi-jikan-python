# MangaPictures

Manga Pictures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MangaImages]**](MangaImages.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.manga_pictures import MangaPictures

# TODO update the JSON string below
json = "{}"
# create an instance of MangaPictures from a JSON string
manga_pictures_instance = MangaPictures.from_json(json)
# print the JSON string representation of the object
print(MangaPictures.to_json())

# convert the object into a dict
manga_pictures_dict = manga_pictures_instance.to_dict()
# create an instance of MangaPictures from a dict
manga_pictures_form_dict = manga_pictures.from_dict(manga_pictures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


