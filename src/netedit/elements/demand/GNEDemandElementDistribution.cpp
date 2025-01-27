/****************************************************************************/
// Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.dev/sumo
// Copyright (C) 2001-2023 German Aerospace Center (DLR) and others.
// This program and the accompanying materials are made available under the
// terms of the Eclipse Public License 2.0 which is available at
// https://www.eclipse.org/legal/epl-2.0/
// This Source Code may also be made available under the following Secondary
// Licenses when the conditions for such availability set forth in the Eclipse
// Public License 2.0 are satisfied: GNU General Public License, version 2
// or later which is available at
// https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
// SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
/****************************************************************************/
/// @file    GNEDemandElementDistribution.cpp
/// @author  Pablo Alvarez Lopez
/// @date    Aug 2023
///
// A abstract class for demand elements distributions
/****************************************************************************/
#include <config.h>

#include <netedit/GNEUndoList.h>

#include "GNEDemandElementDistribution.h"

// ===========================================================================
// member method definitions
// ===========================================================================

// ---------------------------------------------------------------------------
// GNEDemandElementDistribution - methods
// ---------------------------------------------------------------------------

GNEDemandElementDistribution::GNEDemandElementDistribution() {

}


std::string
GNEDemandElementDistribution::getAttributeDistribution() const {

    return "";
}


void
GNEDemandElementDistribution::addDistribution(const std::string& key, const std::string& value, GNEUndoList* undoList) {

}


void
GNEDemandElementDistribution::removeDistribution(const std::string& key, GNEUndoList* undoList) {

}


bool
GNEDemandElementDistribution::isValidDistribution(const std::string& key, const std::string& value) {

    return false;
}


void
GNEDemandElementDistribution::addDistribution(const std::string& key, const std::string& value) {

}


void
GNEDemandElementDistribution::removeDistribution(const std::string& key) {

}

/****************************************************************************/
