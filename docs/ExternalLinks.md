# ExternalLinks

External links

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AnimeFullExternalInner]**](AnimeFullExternalInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.external_links import ExternalLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLinks from a JSON string
external_links_instance = ExternalLinks.from_json(json)
# print the JSON string representation of the object
print(ExternalLinks.to_json())

# convert the object into a dict
external_links_dict = external_links_instance.to_dict()
# create an instance of ExternalLinks from a dict
external_links_form_dict = external_links.from_dict(external_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


