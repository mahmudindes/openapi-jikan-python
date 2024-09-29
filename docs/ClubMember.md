# ClubMember

Club Member

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClubMemberDataInner]**](ClubMemberDataInner.md) |  | [optional] 

## Example

```python
from jikan_openapi.models.club_member import ClubMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClubMember from a JSON string
club_member_instance = ClubMember.from_json(json)
# print the JSON string representation of the object
print(ClubMember.to_json())

# convert the object into a dict
club_member_dict = club_member_instance.to_dict()
# create an instance of ClubMember from a dict
club_member_form_dict = club_member.from_dict(club_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


