#/bin/bash

# frontmatter and endmatter take up approximately 500 and 400 lines,
# respectively
tail -n +500 "$1" | head -n -400 | tr -cs '[:alnum:]' '[\n*]' |
    shuf -n $2
