#!/usr/bin/env bash

# Python Project Bootstrapped Installer by Alex Goretoy <alex@goretoy.com>
# only change packages in the install_project_packages function and the install_test_packages function
# run the script as part of development process to keep project deps and requirement files all in sync

function install_project_packages() {
    # dependencies
    pip install names;
    pip install termcolor;

    # documentation
    pip install sphinx;
    pip install sphinx_rtd_theme;
}
function install_test_packages() {
    # unittests
    pip install tox;
    pip install nose;
    pip install pytest;
    pip install coverage;
}

#####################################################
# DO NOT EDIT BELOW THIS LINE UNLESS THERE IS A BUG #
#####################################################

realpath() {
  OURPWD=$PWD
  cd "$(dirname "$1")"
  LINK=$(readlink "$(basename "$1")")
  while [ "$LINK" ]; do
    cd "$(dirname "$LINK")"
    LINK=$(readlink "$(basename "$1")")
  done
  REALPATH="$PWD/$(basename "$1")"
  cd "$OURPWD"
  echo "$REALPATH"
}
# realpath "$@"

if [ "$0" == "-bash" ]; then
    BASEDIR=$(realpath $(dirname ${BASH_SOURCE[0]})"/..");
else
    BASEDIR=$(realpath $(dirname "$0")"/..");
fi

function create_virtualenv() {
    local INTERPRETER="${1:-"python3"}";
    local MAJOR_MINOR="`${INTERPRETER} -c 'import sys; print(str(sys.version_info[0:2]).strip("()").replace(", ", ""))'`";
    local ve_dir="py${MAJOR_MINOR}";
    local VE_DIR="${2:-"${ve_dir}"}";

    if [ -d "${BASEDIR}/${VE_DIR}" ]; then
        echo -e "\033[33m+ Removing virtualenv in ${BASEDIR}/${VE_DIR}\033[0m";
        rm -rf "${BASEDIR}/${VE_DIR}";
    fi

    echo -e "\033[32m+ Creating virtualenv in ${BASEDIR}/${VE_DIR}\033[0m";
    virtualenv -p "${INTERPRETER}" "${BASEDIR}/${VE_DIR}";
}

function install_dependencies() {
    local INTERPRETER="${1:-"python3"}";
    if [[ "${INTERPRETER}" != *"python"* ]]; then
        echo -e "\033[31m+ Invalid python interpreter: ${INTERPRETER}!\033[0m";
        exit 1;
    fi
    local MAJOR_MINOR="`${INTERPRETER} -c 'import sys; print(str(sys.version_info[0:2]).strip("()").replace(", ", ""))'`";
    local ve_dir="py${MAJOR_MINOR}";
    local VE_DIR="${2:-"${ve_dir}"}";
    local REQUIREMENTS_FILE="${3:-"requirements-${VE_DIR}.txt"}";

    if [ -f "${BASEDIR}/${VE_DIR}/bin/activate" ]; then
        source "${BASEDIR}/${VE_DIR}/bin/activate";
        local VE_NAME="`env | grep VIRTUAL_ENV | tr "=" " " | awk '{print $2}'`";
        if [ "${VE_NAME}" != "" ];then
            echo -e "\033[32m+ Using virtualenv in ${VE_NAME}\033[0m";
        else
            echo -e "\033[33m+ No virtualenv activated!\033[0m";
        fi

        if [ -f "${BASEDIR}/${VE_DIR}/bin/activate" ]; then
            pip install --upgrade pip;
            if [ -f "${BASEDIR}/${REQUIREMENTS_FILE}" ]; then
                pip install -r "${BASEDIR}/${REQUIREMENTS_FILE}";
                pip install -r "${BASEDIR}/test-${REQUIREMENTS_FILE}";
            else
                install_project_packages

                pip freeze > "${BASEDIR}/${REQUIREMENTS_FILE}";

                install_test_packages

                pip freeze > "${BASEDIR}/test-${REQUIREMENTS_FILE}";
            fi
        else
            echo -e "\033[31m+ Python virtualenv not found in ${BASEDIR}/${VE_DIR}\033[0m";
        fi
    else
        echo -e "\033[31m+ Unable to find virtualenv ${BASEDIR}/${VE_DIR}\033[0m";
    fi
}

function install() {
    local INTERPRETER="${1:-"python3"}";
    local MAJOR_MINOR="`${INTERPRETER} -c 'import sys; print(str(sys.version_info[0:2]).strip("()").replace(", ", ""))'`";
    local ve_dir="`echo ${INTERPRETER}|tr "thon" " "|awk '{print $1}'`${MAJOR_MINOR}";
    local VE_DIR="${2:-"${ve_dir}"}";

    if [ "${INTERPRETER}" == "python3" ]; then
        echo -e "\033[32m+ Installing for ${INTERPRETER}\033[0m";
        create_virtualenv "${INTERPRETER}" "${VE_DIR}";
        install_dependencies "${INTERPRETER}" "${VE_DIR}";
    else
        echo -e "\033[31m+ Interpreter ${INTERPRETER} not supported!\033[0m";
    fi
}

if [ "$1" == "" ];then
    install python3;
else
    if [ "$1" == "python3" ]; then
        if [ "$2" == "" ];then
            install "$1";
        else
            install "$1" "$2";
        fi
    else
        echo -e "\033[31m+ Unable to install for unsupported python version!\033[0m";
    fi
fi
