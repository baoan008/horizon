# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2011 Fourth Paradigm Development, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Template tags for parsing date strings.
"""

import datetime
from django import template

register = template.Library()

def _parse_datetime(dtstr):
    try:
        return datetime.datetime.strptime(dtstr, "%Y-%m-%dT%H:%M:%S.%f")
    except:
        return datetime.datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S.%f")


class ParseDateNode(template.Node):
    def render(self, context):
        """Turn an iso formatted time back into a datetime."""
        if context == None:
            return "None"
        date_obj = _parse_datetime(context)
        return date_obj.strftime("%d/%m/%y at %H:%M:%S")


@register.filter(name='parse_date')
def parse_date(value):
    return ParseDateNode().render(value)


@register.filter(name='parse_datetime')
def parse_datetime(value):
    return _parse_datetime(value)


@register.filter(name='pretty_date')
def pretty_date(value):
    return value.strftime("%d/%m/%y at %H:%M:%S")
