# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class MavenPackageVersionDeletionState(Model):
    """MavenPackageVersionDeletionState.

    :param artifact_id:
    :type artifact_id: str
    :param deleted_date:
    :type deleted_date: datetime
    :param group_id:
    :type group_id: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, deleted_date=None, group_id=None, version=None):
        super(MavenPackageVersionDeletionState, self).__init__()
        self.artifact_id = artifact_id
        self.deleted_date = deleted_date
        self.group_id = group_id
        self.version = version
