######
Windows10 installed Python3.6.3
In order to run the python script, install packages first in cmd.
> py -m pip install networks numpy pandas scipy pyteomics
Then change to the working directory and run a test.
> D:
> cd \Github\diffacto\src
> py run_diffacto.py -h
Run the examples.
> py run_diffacto.py -i iPRG.novo.pep.csv -samples iPRG.samples.lst -out iPRG.denovo.protein.txt -mc_out iPRG.denovo.protein.FDR -min_samples 4 -impute_threshold 0.9 -use_unique True -log2 False
> py run_diffacto.py -i HBY20Mix.peptides.csv -samples HBY20Mix.samples.lst -db UP000002311_559292.fasta -out HBY20Mix.protein.txt -min_samples 30 -impute_threshold 0.7 -log2 False -reference REF

######
Try to figure out the logic of the python script by creating a 'DiffactoProject' with Visual Studio.
The script runs slow in Visual Studio python project compared with running in cmd.
- Creat new python project. 
- Copy the run_diffacto.py to the DiffactoProject\DiffactoProject folder. 
- Add the exist run_diffacto.py script and set as StartUp file.
- Open the project property and change the Search Paths to E:\GitHub\diffacto\example (*Maybe useless) 
- Change the Script Arguments:
    -h
    -i iPRG.novo.pep.csv -samples iPRG.samples.lst -out iPRG.denovo.protein.txt -mc_out iPRG.denovo.protein.FDR -min_samples 4 -impute_threshold 0.9 -use_unique True -log2 False
    -i HBY20Mix.peptides.csv -samples HBY20Mix.samples.lst -db UP000002311_559292.fasta -out HBY20Mix.protein.txt -min_samples 30 -impute_threshold 0.7 -log2 False -reference REF
- Debug the project.
