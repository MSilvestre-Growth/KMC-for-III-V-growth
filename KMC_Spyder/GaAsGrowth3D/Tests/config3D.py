# # -----------------------------------------------------------------------------
# # KMCLib version 2.0-a1
# # Distributed under the GPLv3 license
# # Copyright (C)  2012-2016  Mikael Leetmaa
# # Developed by Mikael Leetmaa <leetmaa@kth.se>
# #
# # This program is distributed in the hope that it will be useful
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# # LICENSE and README files, and the source code, for details.
# #
# # You should have received a copy of the GNU General Public License version 3
# # (GPLv3) along with this program. If not, see <http://www.gnu.org/licenses/>.
# # -----------------------------------------------------------------------------

# from KMCLib import *

# # -----------------------------------------------------------------------------
# # Unit cell

# cell_vectors = [[   1.000000e+00,   0.000000e+00,   0.000000e+00],
#                 [   0.000000e+00,   1.000000e+00,   0.000000e+00],
#                 [   0.000000e+00,   0.000000e+00,   1.000000e+00]]

# basis_points = [[   0.000000e+00,   0.000000e+00,   0.000000e+00]]

# unit_cell = KMCUnitCell(
#     cell_vectors=cell_vectors,
#     basis_points=basis_points)

# # -----------------------------------------------------------------------------
# # Lattice

# lattice = KMCLattice(
#     unit_cell=unit_cell,
#     repetitions=(42,10,10),
#     periodic=(True, True, False))

# # -----------------------------------------------------------------------------
# # Configuration

types = ['A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','B_Si','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','A_Si','V','V','V','V','V','V','V','A_Si','B_Si',
         'A_Si','V','V','V','V','V','V','V','A_Si','B_Si','A_Si',
         'V','V','V','V','V','V','V','A_Si','B_Si','A_Si','V',
         'V','V','V','V','V','V','A_Si','B_Si','A_Si','V','V',
         'V','V','V','V','V','A_Si','B_Si','A_Si','V','V','V',
         'V','V','V','V','A_Si','B_Si','A_Si','V','V','V','V',
         'V','V','V','A_Si','B_Si','A_Si','V','V','V','V','V',
         'V','V','A_Si','B_Si','A_Si','V','V','V','V','V','V',
         'V','A_Si','B_Si','A_Si','V','V','V','V','V','V','V',
         'A_Si','B_Si','A_Si','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','B_Si','V','V',
         'V','V','V','V','V','V','A_Si','B_Si','V','V','V','V',
         'V','V','V','V','A_Si','B_Si','V','V','V','V','V','V',
         'V','V','A_Si','B_Si','V','V','V','V','V','V','V','V',
         'A_Si','B_Si','V','V','V','V','V','V','V','V','A_Si',
         'B_Si','V','V','V','V','V','V','V','V','A_Si','B_Si',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'A_Si','V','V','V','V','V','V','V','V','V','A_Si','V',
         'V','V','V','V','V','V','V','V','A_Si','V','V','V',
         'V','V','V','V','V','V','A_Si','V','V','V','V','V',
         'V','V','V','V','A_Si','V','V','V','V','V','V','V',
         'V','V','A_Si','V','V','V','V','V','V','V','V','V',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00','V00','V00','V00','V00','V00','V00','V00',
         'V00','V00']

# possible_types = ['VBB','VBA','VAA','B_Si','V0B','VAB','V00','A_GaAs',
#                   'VB0','V0A','V','A_Si','VA0','B_GaAs']

# configuration = KMCConfiguration(
#     lattice=lattice,
#     types=types,
#     possible_types=possible_types)

# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

path = "C:/Users/msilvestre/Documents/GitHub/Images/GaAsGrowth/Arrival_test/"

####################
#    Image size    #
####################

X = 42
Y = 10
Z = 10

####################

max_dimension = max([X, Y, Z])

for i in range(1):
    
    file_name = "Imtest%d.png" % i
    KMC_Result_current = types
    
    Voids = np.full((X, Y, Z), False)
    A_Si = np.full((max_dimension, max_dimension, max_dimension), False)
    B_Si = np.full((max_dimension, max_dimension, max_dimension), False)
    A_GaAs = np.full((max_dimension, max_dimension, max_dimension), False)
    B_GaAs = np.full((max_dimension, max_dimension, max_dimension), False)
    
    # Interface states
    V00 = np.full((max_dimension, max_dimension, max_dimension), False)
    V0A = np.full((max_dimension, max_dimension, max_dimension), False)
    V0B = np.full((max_dimension, max_dimension, max_dimension), False)
    VA0 = np.full((max_dimension, max_dimension, max_dimension), False)
    VAA = np.full((max_dimension, max_dimension, max_dimension), False)
    VAB = np.full((max_dimension, max_dimension, max_dimension), False)
    VB0 = np.full((max_dimension, max_dimension, max_dimension), False)
    VBA = np.full((max_dimension, max_dimension, max_dimension), False)
    VBB = np.full((max_dimension, max_dimension, max_dimension), False)
    
    for x in range(X):
        for y in range(Y):
            for z in range(Z):
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "A_Si":
                    A_Si[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "B_Si":
                    B_Si[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "A_GaAs":
                    A_GaAs[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "B_GaAs":
                    B_GaAs[x][y][z] = True
                
                # Interface states
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "V00":
                    V00[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "V0A":
                    V0A[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "V0B":
                    V0B[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "VA0":
                    VA0[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "VAA":
                    VAA[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "VAB":
                    VAB[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "VB0":
                    VB0[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "VBA":
                    VBA[x][y][z] = True
                if KMC_Result_current[(Y*Z) * x + (Z) * y + (1) * z] == "VBB":
                    VBB[x][y][z] = True

                    
    
    #combine the objects into a single boolean array
    voxelarray = A_Si | B_Si | A_GaAs | B_GaAs | V00 | V0A | V0B | VA0 | VAA | VAB | VB0 | VBA | VBB
    
    colors = np.empty(voxelarray.shape, dtype=object)
    #colors[void] = '#FF000000' # == transparent
    colors[A_Si] = 'grey'
    colors[B_Si] = 'grey'
    colors[A_GaAs] = 'blue'
    colors[B_GaAs] = 'yellow'
    
    # Interface states
    colors[V00] = 'green'
    colors[V0A] = 'green'
    colors[V0B] = 'green'
    colors[VA0] = 'green'
    colors[VAA] = 'green'
    colors[VAB] = 'green'
    colors[VB0] = 'green'
    colors[VBA] = 'green'
    colors[VBB] = 'green'
    
    ax = plt.axes(projection='3d')
    
    # turn off/on axis
    plt.axis('off')
    #settings
    # X-axis : left 7.8908618514956235
    # X-axis : right 33.60440199006097
    # Y-axis : bottom -6.302167259329746
    # Y-axis : top 19.411372879235586
    plt.xlim((10.268365867838938,35.98190600640428))
    plt.ylim((-12.04950983931609,13.66403029924924))
    
    ax.voxels(voxelarray, facecolors=colors, edgecolor='#FF000000')
    # plt.savefig(path+file_name) 
    # plt.close()