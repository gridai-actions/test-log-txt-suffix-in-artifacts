# Issue

Artifacts with .log extension were missing from some of the runs.

# Observations

When .log file is written and it is the last artifact, this file is not present in saved artifacts

# Test Case

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

## run2.py


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