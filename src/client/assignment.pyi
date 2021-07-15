from datetime import datetime
from decimal import Decimal
from enum import Enum
from toloka.client.primitives.base import BaseTolokaObject
from toloka.client.primitives.parameter import Parameters
from toloka.client.solution import Solution
from toloka.client.task import Task
from typing import (
    Any,
    Dict,
    List,
    Optional
)

class Assignment(BaseTolokaObject):
    """Contains information about an assigned task suite and the results

    Attributes:
        id: ID of the task suite assignment to a performer.
        task_suite_id: ID of a task suite.
        pool_id: ID of the pool that the task suite belongs to.
        user_id: ID of the performer who was assigned the task suite.
        status: Status of an assigned task suite.
            * ACTIVE - In the process of execution by the performer.
            * SUBMITTED - Completed but not checked.
            * ACCEPTED - Accepted by the requester.
            * REJECTED - Rejected by the requester.
            * SKIPPED - Skipped by the performer.
            * EXPIRED - The time for completing the tasks expired.
        reward: Payment received by the performer.
        tasks: Data for the tasks.
        automerged: Flag of the response received as a result of merging identical tasks. Value:
            * True - The response was recorded when identical tasks were merged.
            * False - Normal performer response.
        created: The date and time when the task suite was assigned to a performer.
        submitted: The date and time when the task suite was completed by a performer.
        accepted: The date and time when the responses for the task suite were accepted by the requester.
        rejected: The date and time when the responses for the task suite were rejected by the requester.
        skipped: The date and time when the task suite was skipped by the performer.
        expired: The date and time when the time for completing the task suite expired.
        first_declined_solution_attempt: For training tasks. The performer's first responses in the training task
            (only if these were the wrong answers). If the performer answered correctly on the first try, the
            first_declined_solution_attempt array is omitted.
            Arrays with the responses (output_values) are arranged in the same order as the task data in the tasks array.
        solutions: performer responses. Arranged in the same order as the data for tasks in the tasks array.
        mixed: Type of operation for creating a task suite:
            * True - Automatic ("smart mixing").
            * False - Manually.
        public_comment: Public comment about an assignment. Why it was accepted or rejected.
    """

    class Status(Enum):
        """An enumeration.
        """

        ACTIVE = 'ACTIVE'
        SUBMITTED = 'SUBMITTED'
        ACCEPTED = 'ACCEPTED'
        REJECTED = 'REJECTED'
        SKIPPED = 'SKIPPED'
        EXPIRED = 'EXPIRED'

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        task_suite_id: Optional[str] = None,
        pool_id: Optional[str] = None,
        user_id: Optional[str] = None,
        status: Optional[Status] = None,
        reward: Optional[Decimal] = None,
        tasks: Optional[List[Task]] = None,
        automerged: Optional[bool] = None,
        created: Optional[datetime] = None,
        submitted: Optional[datetime] = None,
        accepted: Optional[datetime] = None,
        rejected: Optional[datetime] = None,
        skipped: Optional[datetime] = None,
        expired: Optional[datetime] = None,
        first_declined_solution_attempt: Optional[List[Solution]] = None,
        solutions: Optional[List[Solution]] = None,
        mixed: Optional[bool] = None,
        public_comment: Optional[str] = None
    ) -> None:
        """Method generated by attrs for class Assignment.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    id: Optional[str]
    task_suite_id: Optional[str]
    pool_id: Optional[str]
    user_id: Optional[str]
    status: Optional[Status]
    reward: Optional[Decimal]
    tasks: Optional[List[Task]]
    automerged: Optional[bool]
    created: Optional[datetime]
    submitted: Optional[datetime]
    accepted: Optional[datetime]
    rejected: Optional[datetime]
    skipped: Optional[datetime]
    expired: Optional[datetime]
    first_declined_solution_attempt: Optional[List[Solution]]
    solutions: Optional[List[Solution]]
    mixed: Optional[bool]
    public_comment: Optional[str]


class AssignmentPatch(BaseTolokaObject):
    """Allows you to accept or reject tasks, and leave a comment

    Used in "TolokaClient.patch_assignment" method.

    Attributes:
        public_comment: Public comment about an assignment. Why it was accepted or rejected.
        status: Status of an assigned task suite.
            * ACCEPTED - Accepted by the requester.
            * REJECTED - Rejected by the requester.
    """

    def __init__(
        self,
        *,
        public_comment: Optional[str] = None,
        status: Optional[Assignment.Status] = None
    ) -> None:
        """Method generated by attrs for class AssignmentPatch.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    public_comment: Optional[str]
    status: Optional[Assignment.Status]


class GetAssignmentsTsvParameters(Parameters):
    """Allows you to downloads assignments as pandas.DataFrame

    Used in "TolokaClient.get_assignments_df" method.
    Implements the same behavior as if you download results in web-interface and then read it by pandas.

    Attributes:
        status: Assignments in which statuses will be downloaded.
        start_time_from: Upload assignments submitted after the specified date and time.
        start_time_to: Upload assignments submitted before the specified date and time.
        exclude_banned: Exclude answers from banned performers, even if assignments in suitable status "ACCEPTED".
        field: The names of the fields to be unloaded. Only the field names from the Assignment class, all other fields
            are added by default.
    """

    class Field(Enum):
        """An enumeration.
        """

        LINK = 'ASSIGNMENT:link'
        ASSIGNMENT_ID = 'ASSIGNMENT:assignment_id'
        TASK_SUITE_ID = 'ASSIGNMENT:task_suite_id'
        WORKER_ID = 'ASSIGNMENT:worker_id'
        STATUS = 'ASSIGNMENT:status'
        STARTED = 'ASSIGNMENT:started'
        SUBMITTED = 'ASSIGNMENT:submitted'
        ACCEPTED = 'ASSIGNMENT:accepted'
        REJECTED = 'ASSIGNMENT:rejected'
        SKIPPED = 'ASSIGNMENT:skipped'
        EXPIRED = 'ASSIGNMENT:expired'
        REWARD = 'ASSIGNMENT:reward'

    class Status(Enum):
        """An enumeration.
        """

        ACTIVE = 'ACTIVE'
        SUBMITTED = 'SUBMITTED'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
        SKIPPED = 'SKIPPED'
        EXPIRED = 'EXPIRED'

    def __init__(
        self,
        *,
        status: Optional[List[Status]] = ...,
        start_time_from: Optional[datetime] = None,
        start_time_to: Optional[datetime] = None,
        exclude_banned: Optional[bool] = None,
        field: Optional[List[Field]] = ...
    ) -> None:
        """Method generated by attrs for class GetAssignmentsTsvParameters.
        """
        ...

    @classmethod
    def structure(cls, data): ...

    def unstructure(self) -> dict: ...

    _unexpected: Optional[Dict[str, Any]]
    status: Optional[List[Status]]
    start_time_from: Optional[datetime]
    start_time_to: Optional[datetime]
    exclude_banned: Optional[bool]
    field: Optional[List[Field]]
