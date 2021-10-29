from argparse import ArgumentParser
from time import sleep

def main(extension, sleep_time, close_file=false):
    with open(f"results.{extension}", "w") as outf:
        outf.write(f"Extension: {extension}\n")
        outf.write(f"Sleep: {sleep_time}\n")
    sleep(sleep_time)
    if close_file:
       close(outf)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--extension", type=str, default="txt")
    parser.add_argument("--sleep", type=int, default=0)
    parser.add_argument("--close", type=boolean, default=false)
    args = parser.parse_args()
    main(args.extension, args.sleep)
