# Issue

Artifacts with .log extension were missing from some of the runs.

## Expectations
5 x 3 x 2 = 30 experiments
script-args: --extension "['txt', 'log', 'hello', 'log2', 'xyz']" --sleep "[0, 60, 120]" --close_file "[0,1]"

https://github.com/gridai-actions/test-log-txt-suffix-in-artifacts/runs/4049681176?check_suite_focus=true

## Run

```
cat > run2.py.log <<EOF
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Experiment               ┃  Command ┃    Status ┃ Queued Duration ┃ Run Duration ┃ extension, ┃ sleep, ┃ close_file, ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━┩
│ antique-elion-9796-exp5  │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:02:42 │       log, │     0, │          0] │
│ antique-elion-9796-exp2  │ run2.py, │ succeeded │     0d-00:03:47 │  0d-00:02:40 │      log2, │     0, │          0] │
│ antique-elion-9796-exp9  │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:02:39 │     hello, │     0, │          0] │
│ antique-elion-9796-exp13 │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:03:50 │       txt, │   120, │          0] │
│ antique-elion-9796-exp8  │ run2.py, │ succeeded │     0d-00:05:25 │  0d-00:02:42 │       txt, │    60, │          0] │
│ antique-elion-9796-exp12 │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:03:47 │       xyz, │   120, │          1] │
│ antique-elion-9796-exp1  │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:03:53 │     hello, │   120, │          0] │
│ antique-elion-9796-exp14 │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:03:56 │      log2, │   120, │          0] │
│ antique-elion-9796-exp3  │ run2.py, │ succeeded │     0d-00:03:58 │  0d-00:02:57 │     hello, │    60, │          1] │
│ antique-elion-9796-exp16 │ run2.py, │ succeeded │     0d-00:03:48 │  0d-00:02:39 │      log2, │     0, │          1] │
│ antique-elion-9796-exp11 │ run2.py, │ succeeded │     0d-00:04:53 │  0d-00:02:43 │      log2, │    60, │          1] │
│ antique-elion-9796-exp6  │ run2.py, │ succeeded │     0d-00:04:11 │  0d-00:02:46 │       xyz, │     0, │          0] │
│ antique-elion-9796-exp10 │ run2.py, │ succeeded │     0d-00:03:59 │  0d-00:03:57 │     hello, │   120, │          1] │
│ antique-elion-9796-exp0  │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:02:54 │     hello, │    60, │          0] │
│ antique-elion-9796-exp15 │ run2.py, │ succeeded │     0d-00:03:56 │  0d-00:02:44 │       xyz, │     0, │          1] │
│ antique-elion-9796-exp4  │ run2.py, │ succeeded │     0d-00:04:44 │  0d-00:02:44 │       txt, │     0, │          0] │
│ antique-elion-9796-exp7  │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:02:53 │       log, │    60, │          1] │
│ antique-elion-9796-exp25 │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:03:48 │       xyz, │   120, │          0] │
│ antique-elion-9796-exp28 │ run2.py, │ succeeded │     0d-00:04:11 │  0d-00:03:51 │      log2, │   120, │          1] │
│ antique-elion-9796-exp21 │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:02:45 │       log, │     0, │          1] │
│ antique-elion-9796-exp27 │ run2.py, │ succeeded │     0d-00:04:11 │  0d-00:02:50 │       txt, │    60, │          1] │
│ antique-elion-9796-exp26 │ run2.py, │ succeeded │     0d-00:04:43 │  0d-00:02:58 │       xyz, │    60, │          0] │
│ antique-elion-9796-exp24 │ run2.py, │ succeeded │     0d-00:04:42 │  0d-00:03:54 │       log, │   120, │          0] │
│ antique-elion-9796-exp18 │ run2.py, │ succeeded │     0d-00:04:11 │  0d-00:03:57 │       log, │   120, │          1] │
│ antique-elion-9796-exp19 │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:02:35 │     hello, │     0, │          1] │
│ antique-elion-9796-exp29 │ run2.py, │ succeeded │     0d-00:05:24 │  0d-00:03:40 │       txt, │   120, │          1] │
│ antique-elion-9796-exp22 │ run2.py, │ succeeded │     0d-00:04:43 │  0d-00:02:59 │       log, │    60, │          0] │
│ antique-elion-9796-exp17 │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:02:35 │       txt, │     0, │          1] │
│ antique-elion-9796-exp23 │ run2.py, │ succeeded │     0d-00:03:59 │  0d-00:02:55 │       xyz, │    60, │          1] │
│ antique-elion-9796-exp20 │ run2.py, │ succeeded │     0d-00:04:42 │  0d-00:02:52 │      log2, │    60, │          0] │
└──────────────────────────┴──────────┴───────────┴─────────────────┴──────────────┴────────────┴────────┴─────────────┘
EOF
grep "log," run2.py.log | grep '1]'

│ antique-elion-9796-exp7  │ run2.py, │ succeeded │     0d-00:04:21 │  0d-00:02:53 │       log, │    60, │          1] │
│ antique-elion-9796-exp21 │ run2.py, │ succeeded │     0d-00:04:10 │  0d-00:02:45 │       log, │     0, │          1] │
│ antique-elion-9796-exp18 │ run2.py, │ succeeded │     0d-00:04:11 │  0d-00:03:57 │       log, │   120, │          1] 
```

## Run

6 runs did not produce an artifacts 
```
grid artifacts antique-elion-9796
cd grid_artifacts
ls | wc -l

      24
```

