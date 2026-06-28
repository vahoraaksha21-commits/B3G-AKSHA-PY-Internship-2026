admin_permission={"read","write","delete"}
editor_permission={"read","write"}
required_permission="delete"

if required_permission in editor_permission:
    print("Editor Can Perform the Action.")
else:
    print("Editor cannot perform the Action.")