#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2010-2021 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    computeStoppingPlaceUsage.py
# @author  Jakob Erdmann
# @date    2021-03-23


from __future__ import print_function
from __future__ import absolute_import
import os
import sys
import optparse
from collections import defaultdict

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
import sumolib  # noqa
from sumolib.miscutils import parseTime

import os,sys

def get_options(args=None):
    parser = sumolib.options.ArgumentParser(description="Compute Stopping Place usage")
    parser.add_argument("-s", "--stop-output-file", dest="stopOutput",
        help="simulation stop-output file")
    parser.add_argument("-t", "--stopping-place", dest="stoppingPlace",
        help="stoppingPlace type (busStop, parkingArea...)", default="parkingArea")
    parser.add_argument("--csv", action="store_true", default=False,
        help="write in CSV format")
    parser.add_argument("--only-changes", action="store_true", default=False,
        help="write output only for steps where the occupancy changes")
    options = parser.parse_args(args=args)
    if not options.stopOutput:
        optParser.print_help()
        sys.exit()
    return options


def main(options):
    # declare veh counts
    vehCounts = defaultdict(list)

    time = None
    for stop in sumolib.xml.parse(options.stopOutput, "stopinfo"):
        splace = stop.getAttributeSecure(options.stoppingPlace, "")
        if splace != "":
            vehCounts[splace].append((parseTime(stop.started), 1))
            vehCounts[splace].append((parseTime(stop.ended), -1))
    #iterate over vehCounts
    for splace, times in vehCounts.items():
        times.sort()
        steps = []
        tPrev = None
        count = 0
        for t,change in times:
            if t != tPrev and tPrev is not None:
                steps.append((tPrev, count))
            count += change
            tPrev = t
        steps.append((tPrev, count))

        suffix = ".csv" if options.csv else ".xml"
        with open(splace + suffix, "w") as outf:
            # write header
            if options.csv:
                # write CSV header
                outf.write("step,number\n")
                for time, number in steps:
                    outf.write("%s,%s\n" % (time, number))
            else:
                # write XML header
                outf.write("<?xml version= \"1.0\" encoding=\"UTF-8\"?>\n\n")
                # open route rag
                outf.write("<stoppingPlace>\n")
                for time, number in steps:
                    outf.write('    <step time="%s" number="%s"/>\n' % (time, number))
                outf.write("</stoppingPlace>\n")


if __name__ == "__main__":
    main(get_options())
