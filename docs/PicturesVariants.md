# PicturesVariants

Pictures Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PicturesVariantsDataInner]**](PicturesVariantsDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.pictures_variants import PicturesVariants

# TODO update the JSON string below
json = "{}"
# create an instance of PicturesVariants from a JSON string
pictures_variants_instance = PicturesVariants.from_json(json)
# print the JSON string representation of the object
print(PicturesVariants.to_json())

# convert the object into a dict
pictures_variants_dict = pictures_variants_instance.to_dict()
# create an instance of PicturesVariants from a dict
pictures_variants_form_dict = pictures_variants.from_dict(pictures_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


