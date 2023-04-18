import functools
# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}

# You code starts here:
# Define a check_permission() decorator:
def check_permission(func):
    @functools.wraps(func)
    def wraper():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError('You are not an admin.')
    return wraper

# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
@check_permission
def delete_database():
    # perform deletion
    print('Database deleted!')

print(delete_database())
print(delete_database.__name__)