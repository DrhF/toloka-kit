__all__ = [
    'Pipeline',
]
import asyncio
import datetime
import enum
import toloka.streaming.observer
import toloka.streaming.storage
import typing


class _Worker:
    """_Worker object that run observer's __call__() and should_resume() methods.
    Keep track of the observer's should_resume state.

    Attributes:
        name: Unique key to be identified by.
        observer: BaseObserver object to run.
        should_resume: Current observer's should_resume state.
    """

    async def __call__(self) -> None: ...

    def __hash__(self) -> int: ...

    def __eq__(self, other) -> bool: ...

    def __init__(
        self,
        name: str,
        observer: toloka.streaming.observer.BaseObserver,
        should_resume: bool = False
    ) -> None:
        """Method generated by attrs for class _Worker.
        """
        ...

    name: str
    observer: toloka.streaming.observer.BaseObserver
    should_resume: bool


class IterationMode(enum.Enum):
    """Possible values:
        * `ALL_COMPLETED` – start next iteration only when all current tasks are done.
        * `FIRST_COMPLETED` – start next iteration as soon as any single task is done.
    """

    ALL_COMPLETED = 'ALL_COMPLETED'
    FIRST_COMPLETED = 'FIRST_COMPLETED'


class Pipeline:
    """An entry point for toloka streaming pipelines.
    Allow you to register multiple observers and call them periodically
    while at least one of them may resume.

    Attributes:
        period: Period of observers calls. By default, 60 seconds.
        storage: Optional storage object to save pipeline's state.
            Allow to recover from previous state in case of failure.
        iteration_mode: When to start new iteration. Default is `FIRST_COMPLETED`

    Examples:
        Get assignments from segmentation pool and send them for verification to another pool.

        >>> def handle_submitted(events: List[AssignmentEvent]) -> None:
        >>>     verification_tasks = [create_verification_task(item.assignment) for item in events]
        >>>     toloka_client.create_tasks(verification_tasks, open_pool=True)
        >>>
        >>> def handle_accepted(events: List[AssignmentEvent]) -> None:
        >>>     do_some_aggregation([item.assignment for item in events])
        >>>
        >>> async_toloka_client = AsyncTolokaClient.from_sync_client(toloka_client)
        >>>
        >>> observer_123 = AssignmentsObserver(async_toloka_client, pool_id='123')
        >>> observer_123.on_submitted(handle_submitted)
        >>>
        >>> observer_456 = AssignmentsObserver(async_toloka_client, pool_id='456')
        >>> observer_456.on_accepted(handle_accepted)
        >>>
        >>> pipeline = Pipeline()
        >>> pipeline.register(observer_123)
        >>> pipeline.register(observer_456)
        >>> await pipeline.run()
        ...

        One-liners version.

        >>> pipeline = Pipeline()
        >>> pipeline.register(AssignmentsObserver(toloka_client, pool_id='123')).on_submitted(handle_submitted)
        >>> pipeline.register(AssignmentsObserver(toloka_client, pool_id='456')).on_accepted(handle_accepted)
        >>> await pipeline.run()
        ...

        With external storage.

        >>> from toloka.streaming import S3Storage, ZooKeeperLocker
        >>> locker = ZooKeeperLocker(...)
        >>> storage = S3Storage(locker=locker, ...)
        >>> pipeline = Pipeline(storage=storage)
        >>> await pipeline.run()  # Save state after each iteration. Try to load saved at start.
        ...
    """

    def register(self, observer: toloka.streaming.observer.BaseObserver) -> toloka.streaming.observer.BaseObserver:
        """Register given observer.

        Args:
            observer: Observer object.

        Returns:
            The same observer object. It's usable to write one-liners.

        Examples:
            Register observer.

            >>> observer = SomeObserver(pool_id='123')
            >>> observer.do_some_preparations(...)
            >>> toloka_loop.register(observer)
            ...

            One-line version.

            >>> toloka_loop.register(SomeObserver(pool_id='123')).do_some_preparations(...)
            ...
        """
        ...

    def observers_iter(self) -> typing.Iterator[toloka.streaming.observer.BaseObserver]:
        """Iterate over registered observers.

        Returns:
            An iterator over all registered observers except deleted ones.
            Might contain observers scheduled for deletion and not deleted yet.
        """
        ...

    class RunState:
        """State of a single Pipeline run.

        Attributes:
            workers: all known workers
            waiting: currently running workers
            pending: currently not running workers
        """

        def add_new_observers(self, new_observers: typing.Iterable[toloka.streaming.observer.BaseObserver]) -> None: ...

        def __init__(
            self,
            pipeline_key: str,
            workers: typing.Dict[_Worker, None] = ...,
            waiting: typing.Dict[_Worker, asyncio.Task] = ...,
            pending: typing.Dict[_Worker, datetime.datetime] = ...
        ) -> None:
            """Method generated by attrs for class Pipeline.RunState.
            """
            ...

        pipeline_key: str
        workers: typing.Dict[_Worker, None]
        waiting: typing.Dict[_Worker, asyncio.Task]
        pending: typing.Dict[_Worker, datetime.datetime]

    def run_manually(self) -> typing.AsyncGenerator['Pipeline.RunState', None]: ...

    async def run(self) -> None: ...

    def __init__(
        self,
        period: datetime.timedelta = ...,
        storage: typing.Optional[toloka.streaming.storage.BaseStorage] = None,
        iteration_mode: IterationMode = IterationMode.FIRST_COMPLETED,
        *,
        name: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class Pipeline.
        """
        ...

    period: datetime.timedelta
    storage: typing.Optional[toloka.streaming.storage.BaseStorage]
    iteration_mode: IterationMode
    name: typing.Optional[str]
    _observers: typing.Dict[int, toloka.streaming.observer.BaseObserver]
    _got_sigint: bool
