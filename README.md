# sudoku.solver
This simple Sudoku.Solver will solve any difficult Sudoku puzzel. It will look for alternative solutions as well.

<img src="Screen_Shot0.png" width="480" />

Once the solver is build, next step was to build a GUI so that the user can input any puzzel and solve it. QtDesigner was used to build the GUI and pyuic was used to translate to python code.

$ pyuic5 -x gui_solver.ui -o gui_solver.py

After incorpoprting the solver code and executing will promt the following GUI.

<img src="Screen_Shot1.png" width="480" />

Fill in the array as needed.

<img src="Screen_Shot2.png" width="480" />

Once you press the "Solve" Button, the soultion will be populated on the same GUI

<img src="Screen_Shot3.png" width="480" />

If the puzzel have multiple solutions and when you press the "Solve" button once agon, it will populate with the next solution.
<img src="Screen_Shot4.png" width="480" />
