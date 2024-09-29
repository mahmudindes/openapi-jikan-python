# Pictures

Pictures Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PicturesDataInner]**](PicturesDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.pictures import Pictures

# TODO update the JSON string below
json = "{}"
# create an instance of Pictures from a JSON string
pictures_instance = Pictures.from_json(json)
# print the JSON string representation of the object
print(Pictures.to_json())

# convert the object into a dict
pictures_dict = pictures_instance.to_dict()
# create an instance of Pictures from a dict
pictures_form_dict = pictures.from_dict(pictures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


