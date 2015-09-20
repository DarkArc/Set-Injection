# Set Inject - Easy text injection script
# Copyright (C) 2015 Wyatt Childers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

if (len(sys.argv) != 2):
    print("You must specify the target file.")
    sys.exit(1)

sourceFile = sys.argv[1]

targetFile = sourceFile + ".txt"

seperateFiles = False

gen = [
    ['a', 'dog'],
    ['my', 'cow'],
    ['a', 'dragon']
]

input = open(sourceFile, 'r')
inputText = input.read()
input.close()

for i in range(0, len(gen)):

    if seperateFiles:
        targetFile = sourceFile + "." + str(i) + ".txt"

    output = open(targetFile, 'w' if seperateFiles else 'a')

    outText = inputText

    for k in range(0, len(gen[i])):
        outText = outText.replace("{{" + str(k) + "}}", gen[i][k])

    output.write(outText)
    output.close()
