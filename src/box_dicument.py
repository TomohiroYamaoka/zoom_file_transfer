from boxsdk.object.collaboration import CollaborationRole

user = client.user(user_id='11111')
collaboration = client.folder(folder_id='22222').collaborate(
    user, CollaborationRole.VIEWER)

collaborator = collaboration.accessible_by
item = collaboration.item
has_accepted = 'has' if collaboration.status == 'accepted' else 'has not'
print('{0} {1} accepted the collaboration to folder "{2}"'.format(
    collaborator.name, has_accepted, item.name))
