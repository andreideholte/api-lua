# API Lua 🌘

Webservice to generate Astrological charts using kerykeion, a Python library for astrology that computes planetary and house positions, detects aspects, and generates SVG charts—including birth, synastry, transit, and composite charts. You can also customize which planets to include in your calculations. Also use the full version of Pyswisseph which is a python implementation of swiss ephemeris (https://github.com/astrorigin/pyswisseph).

This is published under the GNU Affero General Public License version 3. See the LICENSE.txt file.

Note that the original swisseph library is distributed under a dual licensing system: GNU Affero General Public License, or Swiss Ephemeris Professional License. For more information, see file libswe/LICENSE (https://github.com/astrorigin/swisseph/blob/696bda432298d482d27e67a0cf1238920301a7dd/LICENSE).

Instructions to setup (assuming use of VS Code)

- uses ZSH scripts to build (will require changing the permission of these scripts to enable execution)
- Requires Python 3.9 or higher and a docker environment
- Setup a virtual Python environment (https://code.visualstudio.com/docs/python/environments) in the project's root directory
