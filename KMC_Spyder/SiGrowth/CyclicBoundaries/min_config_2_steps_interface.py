# -----------------------------------------------------------------------------
# KMCLib version 2.0-a1
# Distributed under the GPLv3 license
# Copyright (C)  2012-2016  Mikael Leetmaa
# Developed by Mikael Leetmaa <leetmaa@kth.se>
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE and README files, and the source code, for details.
#
# You should have received a copy of the GNU General Public License version 3
# (GPLv3) along with this program. If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

['A1', 'A1i', 'B2', 'B2i', 'A3', 'A3i', 'B4', 'B4i', 'A5', 'A5i', 'B6', 'B6i', 'A7', 'A7i', 'B8', 'B8i']
from KMCLib import *

# -----------------------------------------------------------------------------
# Unit cell

cell_vectors = [[   1.000000e+00,   0.000000e+00,   0.000000e+00],
                [   0.000000e+00,   1.000000e+00,   0.000000e+00],
                [   0.000000e+00,   0.000000e+00,   1.000000e+00]]

basis_points = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]

unit_cell = KMCUnitCell(
    cell_vectors=cell_vectors,
    basis_points=basis_points)

# -----------------------------------------------------------------------------
# Lattice

lattice = KMCLattice(
    unit_cell=unit_cell,
    repetitions=(3,1,1),
    periodic=(True, True, False))

# -----------------------------------------------------------------------------
# Configuration

types = ['A1i','B2','A1']

possible_types = ['B4','B2','A5i','B4i','B6','A1','A7i','A3','A5','B8',
                  'B2i','A7','B8i','A3i','A1i','B6i']

configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=possible_types)

