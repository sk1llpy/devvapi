def _type(project_name: str):
    with open('/home/skilldev/Desktop/python_my_framework/setup/default/manage.py', 'r') as manage__file:
        manage__file = manage__file.read()

        with open(f'{project_name}/manage.py', 'w') as manage_file:
            manage_file.write(manage__file)
