"""Zowe Python Client SDK.

This program and the accompanying materials are made available under the terms of the
Eclipse Public License v2.0 which accompanies this distribution, and is available at

https://www.eclipse.org/legal/epl-v20.html

SPDX-License-Identifier: EPL-2.0

Copyright Contributors to the Zowe Project.
"""
from ..utilities import ZosmfApi


class Console(ZosmfApi):
    """
    Class used to represent the base z/OSMF Console API.

    ...

    Attributes
    ----------
    connection
        z/osmf connection object

    Methods
    -------
    issue_command(command, console=None)
        Execute a z/OS console command and return a JSON with the response.
    """

    def __init__(self, connection):
        """
        Construct a Console object.

        Parameters
        ----------
        connection
            The z/OSMF connection object (generated by the ZoweSDK object)
        """
        super().__init__(connection, "/zosmf/restconsoles/consoles/defcn")

    def issue_command(self, command, console=None):
        """Issues a command on z/OS Console.

        Parameters
        ----------
        command
            The z/OS command to be executed
        console
            The console that should be used to execute the command (default is None)

        Returns
        -------
        response_json
            A JSON containing the response from the console command
        """
        custom_args = self.create_custom_request_arguments()
        request_body = '{"cmd": "%s"}' % (command)
        custom_args["data"] = request_body
        response_json = self.request_handler.perform_request("PUT", custom_args)
        return response_json
