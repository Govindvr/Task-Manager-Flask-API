from .resources import TaskResource, TasksResource, TaskStatusResource

def initialise_routes(api):
    api.add_resource(TaskResource, '/tasks/<int:task_id>')
    api.add_resource(TasksResource, '/tasks')
    api.add_resource(TaskStatusResource, '/tasks/<int:task_id>/status')