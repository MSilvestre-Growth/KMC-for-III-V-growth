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

['A01', 'A01i', 'B02', 'B02i', 'A03', 'A03i', 'B04', 'B04i', 'A05', 'A05i', 'B06', 'B06i', 'A07', 'A07i', 'B08', 'B08i', 'A09', 'A09i', 'B10', 'B10i', 'A11', 'A11i', 'B12', 'B12i', 'A13', 'A13i', 'B14', 'B14i', 'A15', 'A15i', 'B16', 'B16i', 'A17', 'A17i', 'B18', 'B18i', 'A19', 'A19i', 'B20', 'B20i', 'A21', 'A21i', 'B22', 'B22i', 'A23', 'A23i', 'B24', 'B24i', 'A25', 'A25i', 'B26', 'B26i', 'A27', 'A27i', 'B28', 'B28i', 'A29', 'A29i', 'B30', 'B30i', 'A31', 'A31i', 'B32', 'B32i', 'A33', 'A33i', 'B34', 'B34i', 'A35', 'A35i', 'B36', 'B36i', 'A37', 'A37i', 'B38', 'B38i', 'A39', 'A39i', 'B40', 'B40i', 'A41', 'A41i', 'B42', 'B42i', 'A43', 'A43i', 'B44', 'B44i']
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
    repetitions=(10,10,1),
    periodic=(True, True, False))

# -----------------------------------------------------------------------------
# Configuration

types = ['A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','B24','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23','A23','A23','A23','A23','A23','A23','A23','A23',
         'A23']

possible_types = ['B34i','B10i','B28','B02i','B20i','B28i','A13i','A33i',
                  'B44i','A23i','A03i','B36i','A43i','B06i','B26','B24',
                  'B22','B20','B04i','A19i','B38','B22i','B34','A05i',
                  'B36','B30','B32','B18','B42i','A35i','A21i','A29i',
                  'A43','A41','A11i','B08','B02','B18i','B32i','B04',
                  'B06','B16','A41i','B14','B12','B10','B14i','A33','A31',
                  'A37','A35','A07i','A39','A27i','A23','A17i','B24i',
                  'A37i','B40i','A21','B08i','A25','A27','B12i','A29',
                  'B16i','A15','A17','A11','A13','A19','B30i','A15i',
                  'A09i','A31i','B26i','A01i','A39i','B38i','A25i','B44',
                  'A09','B40','B42','A03','A01','A07','A05']

configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=possible_types)

