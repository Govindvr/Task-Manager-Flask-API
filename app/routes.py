from .resources import TaskResource, TasksResource, TaskStatusResource

def initialise_routes(api):
    api.add_resource(TaskResource, '/api/tasks/<int:task_id>')
    api.add_resource(TasksResource, '/api/tasks')
    api.add_resource(TaskStatusResource, '/api/tasks/<int:task_id>/status')