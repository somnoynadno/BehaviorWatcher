"""
This is the 'metrics' module and supports all the REST actions for the
metric data
"""

from flask import make_response, abort
# from config import db
# from models import


def read_all(userId=None, taskId=None):
    """
    Respond to a GET request for /api/metrics

    :return json array of metrics
    """
    if userId is None:
        userId = 0
    if taskId is None:
        taskId = 0

    return [
        {
            "id": 0,
            "userId": 0,
            "taskId": 0,
            "taskCopied": True,
            "taskViewed": True,
            "readingTime": 0
        }
    ]


def create(metric: 'dict'):
    """
    Respond to a POST request for /api/metrics
    Creates new metric with metric data, assigns metric.id

    :param metric   metric to create
    :return 201 on success, 409 if metric already exists
    """

    metric['id'] = 0
    return metric, 201

    abort(
        409,
        f"Metric with userId: {metric['userId']} and taskId: {metric['taskId']} already exists."
    )



def read_one(metricId):
    """
    Respond to a GET request for /api/metrics/{metricId}
    Returns specified metric

    :param metricId Id of the metric to read
    :return metric on success or 404
    """
    return  {
        "id": metricId,
        "userId": 0,
        "taskId": 0,
        "taskCopied": True,
        "taskViewed": True,
        "readingTime": 0
    }

    abort(404, f"Metric with metricId: {metricId} does not exists.")



def patch(metricId, metricData):
    """
    Respond to a PATCH request for /api/metrics/{metricId}
    Patches the metric with the properties of metricData or leaves unchanged

    :param metricId    Id of the metric to update
    :param metricData Data to update the metric with
    :return 200 on success
    """
    pass


def delete(metricId):
    """
    Respond to a DELETE request for /api/metrics/{metricId}
    Deletes the metric

    :param metricId    Id of the metric to update
    :return 200|204 on success
    """
    pass
