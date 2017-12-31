#!/usr/bin/env bash

# Bootstrap a dev environment


VENV_NAME=trend-analysis
REQUIREMENTS=('python3' 'virtualenvwrapper.sh')


do_the_thing() {
    [ -n "$VIRTUAL_ENV" ] && { echo "Deactivate virtualenvs first"; exit 1; }

    echo "Running setup for $os"
    for requirement in "${REQUIREMENTS[@]}"; do
        which "$requirement" >/dev/null 2>&1 \
           && echo "Found $requirement" \
           || { echo "Missing $requirement"; exit 1; }
    done

    source virtualenvwrapper.sh
    mkvirtualenv --python $(which python3) "$VENV_NAME"

    cat debug/postactivate > "$VIRTUAL_ENV/bin/postactivate"

    pip install -Ur requirements.txt

    echo
    echo "Now type \`workon $VENV_NAME\`"
}


case "$(uname -s)" in
     Linux*) os=Linux ;;
    Darwin*) os=MacOS ;;
esac

do_the_thing
