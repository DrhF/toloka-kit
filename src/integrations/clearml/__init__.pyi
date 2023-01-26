__all__ = [
    'register_to_clearml',
    'get_clearml_dataset'
]

from typing import List, Optional

import pandas as pd

from clearml import Dataset


def get_clearml_dataset(
    dataset_id: Optional[str] = None,
    dataset_project: Optional[str] = None,
    dataset_name: Optional[str] = None,
    alias: Optional[str] = None
) -> str:
    """Gets a local copy of ClearML Dataset
    Args:
        dataset_id: Requested dataset ID
        dataset_project: Requested dataset project name
        dataset_name: Requested dataset name
        alias: Alias of the dataset. If set, the 'alias : dataset ID' key-value pair
            will be set under the hyperparameters section 'Datasets'
    Example:
        The example shows how to get a local copy of ClearML Dataset by dataset_id
        >>> get_clearml_dataset(dataset_id=dataset_id)
        ...
    """
    ...


def register_to_clearml(
    toloka_df: pd.DataFrame,
    toloka_dataset_path: Optional[str] = None,
    external_url_columns: Optional[List[str]] = None,
    dataset_project: Optional[str] = None,
    dataset_name: Optional[str] = None,
    parent_dataset_ids: Optional[List[str]] = None,
    verbose: bool = False
) -> None:
    """Registers a new Dataset to ClearML containing files annotated by Toloka
    Args:
        toloka_df: pandas Dataframe containing data from Toloka. Can be obtained using `TolokaClient.get_assignments_df` or using web UI.
        toloka_dataset_path: path to store `toloka_df` locally. This is a temp file used to register to clearml
        dataset_project: Project containing the dataset in ClearML.
        dataset_name: Naming the new dataset in ClearML
        parent_dataset_id: Parent dataset ID
        external_url_columns: columns containing external urls. If specified, the URLs in the columns will be added to the clearml Dataset
                              as links and can be retrieved when calling get_clearml_dataset
        verbose: If True print to console files added/modified
    Examples:
        The example shows how register  a new Dataset in ClearML.
        >>> answers_df = toloka_client.get_assignments_df(pool_id='1')
        >>> register_to_clearml(toloka_df=answers_df,
        >>>             dataset_project='ClearMLProject', dataset_name='TolokaDataset')
        ...
        The example shows how to register a new Dataset in ClearML as a child Dataset.
        >>> answers_df = toloka_client.get_assignments_df(pool_id='1')
        >>> parent_dataset_id = # id of Dataset from ClearML
        >>> register_to_clearml(parent_dataset_ids=parent_dataset_id, toloka_df=answers_df,
        >>>                     dataset_project='ClearMLProject', dataset_name='TolokaDataset')
        ...
    """
    ...
