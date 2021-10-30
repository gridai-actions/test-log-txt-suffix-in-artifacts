## 🐛 Bug

Artifacts with .log extension are missing if there are no subsequent artifacts generated. 

### Expected behavior

All artifacts are present from  `grid artifacts` 

### Current behavior

A run with .log generated on the last step will not have that artifact available via `grid artifacts` command.

### To Reproduce

Steps to reproduce the issue as follows:

| Test | Expected Results | Actual Results | Script | Runner | Run |
| -- | -- | -- | -- | -- | -- |
| at end, write weights.log then results.log | both .log files are present | the last .log is missing | [run.py](./run.py) | [unittest-run.yml](./.github/workflows/unittest-run.yml) | [![run.py](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/actions/workflows/unittest-run.yml/badge.svg)](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/actions/workflows/unittest-run.yml) |
| at end, HPO run `--extension "['txt', 'log', 'hello', 'log2', 'xyz']" --sleep "[0, 60, 120]" --close_file "[0,1]"` | all 6 .log files are present | no .log files are present but all other extensions are ok | [run2.py](./run2.py) | [unittest-run2.yml](./.github/workflows/unittest-run2.yml) | [![run2.py](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/actions/workflows/unittest-run2.yml/badge.svg)](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/actions/workflows/unittest-run2.yml) |
| write weights.log then results.log then some more artifacts| both .log files are present | all artifacts are found including the two .log files are present| [run.py](./run.py) | [unittest-run.yml](./.github/workflows/unittest-run.yml) | [![run3.py](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/actions/workflows/unittest-run3.yml/badge.svg)](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/actions/workflows/unittest-run3.yml) |

# Evidence

## run.py

[log](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/runs/4052318275?check_suite_focus=true) show only   
 `1 log` (1 file with .log extension)

```
list of artifacts
grid_artifacts/proficient-hertz-137/proficient-hertz-137-exp0/lightning_logs/hello/events.out.tfevents.1635551954.exp-01fk77rx6pv7z9pdx8yxahm7e5.14.0
grid_artifacts/proficient-hertz-137/proficient-hertz-137-exp0/results.pt
grid_artifacts/proficient-hertz-137/proficient-hertz-137-exp0/weights.log
grid_artifacts/proficient-hertz-137/proficient-hertz-137-exp0/weights.pt
file count group by extensions
      1 0
      1 log
      2 pt
assert by expected file count
```

[log](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/runs/4052467716?check_suite_focus=true) show no .log files

## run2.py


```
list of artifacts
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp0/results.txt
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp1/results.txt
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp10/results.hello
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp11/results.hello
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp12/results.txt
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp13/results.txt
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp14/results.log2
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp15/results.txt
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp16/results.log2
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp17/results.log2
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp19/results.xyz
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp2/results.hello
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp20/results.hello
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp21/results.hello
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp22/results.log2
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp24/results.log2
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp25/results.xyz
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp26/results.hello
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp28/results.log2
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp29/results.xyz
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp3/results.xyz
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp6/results.xyz
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp8/results.txt
grid_artifacts/rebel-bardeen-2144/rebel-bardeen-2144-exp9/results.xyz
file count group by extensions
      6 hello
      6 log2
      6 txt
      6 xyz
assert by expected file count
```

## run3.py

[log](https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/runs/4052318205?check_suite_focus=true) show only   
 `1 log` (1 file with .log extension)

```
list of artifacts
grid_artifacts/defiant-gauss-7889/defiant-gauss-7889-exp0/lightning_logs/hello/events.out.tfevents.1635552049.exp-01fk77rxmcfky4wbdsr04p5g44.15.0
grid_artifacts/defiant-gauss-7889/defiant-gauss-7889-exp0/results.pt
grid_artifacts/defiant-gauss-7889/defiant-gauss-7889-exp0/weights.log
grid_artifacts/defiant-gauss-7889/defiant-gauss-7889-exp0/weights.pt
file count group by extensions
      1 0
      1 log
      2 pt
```

### Environment

 - OS (e.g., Windows): Ubuntu
 - Browser (e.g., Chrome, Safari): N/A
 - CLI version: 
 - Python version: 3.8 

### Additional context

N/A