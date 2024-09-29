# ProducerFull

Producers Resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mal_id** | **int** | MyAnimeList ID | [optional] 
**url** | **str** | MyAnimeList URL | [optional] 
**titles** | [**List[Title]**](Title.md) | All titles | [optional] 
**images** | [**CommonImages**](CommonImages.md) |  | [optional] 
**favorites** | **int** | Producers&#39;s member favorites count | [optional] 
**count** | **int** | Producers&#39;s anime count | [optional] 
**established** | **str** | Established Date ISO8601 | [optional] 
**about** | **str** | About the Producer | [optional] 
**external** | [**List[AnimeFullExternalInner]**](AnimeFullExternalInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.producer_full import ProducerFull

# TODO update the JSON string below
json = "{}"
# create an instance of ProducerFull from a JSON string
producer_full_instance = ProducerFull.from_json(json)
# print the JSON string representation of the object
print(ProducerFull.to_json())

# convert the object into a dict
producer_full_dict = producer_full_instance.to_dict()
# create an instance of ProducerFull from a dict
producer_full_form_dict = producer_full.from_dict(producer_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


