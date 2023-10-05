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

0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
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
    repetitions=(6,6,1),
    periodic=(True, True, False))

# -----------------------------------------------------------------------------
# Configuration

types = ['0','1','2','3','4','5','6','7','8','9','10','11',
         '12','13','14','15','16','17','18','19','20','21','22',
         '23','24','25','26','27','28','29','30','31','32','33',
         '34','35']

possible_types = ['24','25','26','27','20','21','22','23','28','29',
                  '1','0','3','2','5','4','7','6','9','8','11','10','13',
                  '12','15','14','17','16','19','18','31','30','35','34',
                  '33','32']

configuration = KMCConfiguration(
    lattice=lattice,
    types=types,
    possible_types=possible_types)

