from kjson import kjson

kjson.print({'key':1})

description = 'description'
user_defined_package_name = 'user_defined_package_name'
print('description="' + (description or user_defined_package_name) + '",')
print('description="' + description or user_defined_package_name + '",')