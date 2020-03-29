# sudoku.solver
This simple Sudoku.Solver will solve any difficult Sudoku puzzel. It will look for alternative solutions as well.

![alternativetext](Screen_Shot0.png)

Once the solver is build, next step was to build a GUI so that the user can input any puzzel and solve it. QtDesigner was used to build the GUI and pyuic was used to translate to python code.

$pyuic5 -x gui_solver.ui -o gui_solver.py

After incorpoprting the solver code and executing will promt the following GUI.

![alternativetext](Screen_Shot1.png)

Fill in the array as needed.

![alternativetext](Screen_Shot2.png)

Once you press the "Solve" Button, the soultion will be populated on the same GUI

![alternativetext](Screen_Shot3.png)

If the puzzel have multiple solutions and when you press the "Solve" button once agon, it will populate with the next solution.

![alternativetext](Screen_Shot4.png)
