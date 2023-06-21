#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
# Copyright (C) 2009-2023 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2019-07-16

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to demand mode
netedit.supermodeDemand()

# go to vehicle mode
netedit.vehicleMode()

# select trip over TAZs
netedit.changeElement("trip (from-to TAZs)")

# set color using dialog color
netedit.changeColorUsingDialog(netedit.attrs.tripFromToTAZ.create.colorButton, 5)

# try to create trip
netedit.leftClick(referencePosition, 50, 250)
netedit.leftClick(referencePosition, 430, 250)

# press enter to create trip
netedit.typeEnter()

# set invalid color
netedit.changeDefaultValue(netedit.attrs.tripFromToTAZ.create.color, "dummyColor")

# try to create trip
netedit.leftClick(referencePosition, 50, 250)
netedit.leftClick(referencePosition, 430, 250)

# press enter to create trip
netedit.typeEnter()

# set valid color
netedit.changeDefaultValue(netedit.attrs.tripFromToTAZ.create.color, "cyan")

# create trip
netedit.leftClick(referencePosition, 50, 250)
netedit.leftClick(referencePosition, 430, 250)

# press enter to create trip
netedit.typeEnter()

# set valid color
netedit.changeDefaultValue(netedit.attrs.tripFromToTAZ.create.color, "12,13,14")

# create trip
netedit.leftClick(referencePosition, 50, 250)
netedit.leftClick(referencePosition, 430, 250)

# press enter to create trip
netedit.typeEnter()

# Check undo redo
netedit.undo(referencePosition, 2)
netedit.redo(referencePosition, 2)

# save Netedit config
netedit.saveNeteditConfig(referencePosition)

# quit netedit
netedit.quit(neteditProcess)