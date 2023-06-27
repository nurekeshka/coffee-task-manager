# ''' This file contains datastore repositories '''
# from apps.common.exceptions import EntityDoesNotExist
# from apps.tasks.models import Task as TaskORM
# from apps.tasks.entities import Task


# class TaskDBRepository:
#     ''' This class represents a task database repository '''

#     def get_find_by_id(self, identity: int) -> Task:
#         ''' This method return a task object for a given identity '''
#         try:
#             orm_task = TaskORM.objects.get(id=identity)
#         except TaskORM.DoesNotExist as exception:
#             raise EntityDoesNotExist from exception

#         return self.decode_orm_task(orm_task)

#     def decode_orm_task(self, orm_task_queryset: Task) -> Task:
#         task = Task()

#         task_entity = task.set_params(
#             identity=orm_task_queryset.id,
#             name=orm_task_queryset.name,
#             description=orm_task_queryset.description,
#             status=orm_task_queryset.status,
#             assignee=orm_task_queryset.assignee,

#         )

#         return [task]
