#!/bin/sh
SERVICE_NAME=ConsecroMUD
SERVER_LOG=server/logs/startup.log
RUNNING_LOCK=server/server.pid
CODEBASE_UPGRADE=../cMUD/server/logs/upgrade.log


case $1 in
    start)
        if [ ! -f ${RUNNING_LOCK} ]; then
            source /Users/Daniel/ConsecroMUD/pyenv/bin/activate
            cd ~/ConsecroMUD/cMUD
            echo "-- STARTED --" >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            date >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            evennia start >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            echo "$SERVICE_NAME started ..."
        else
            echo "$SERVICE_NAME is already running ..."
        fi
    ;;
    stop)
        if [ -f ${RUNNING_LOCK} ]; then
            source /Users/Daniel/ConsecroMUD/pyenv/bin/activate
            cd ~/ConsecroMUD/cMUD
            echo "-- STOPPED --" >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            date >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            evennia stop >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            deactivate
            echo "$SERVICE_NAME stopped ..."
        else
            echo "$SERVICE_NAME is not running ..."
        fi
    ;;
    restart)
        if [ -f ${RUNNING_LOCK} ]; then
            source /Users/Daniel/ConsecroMUD/pyenv/bin/activate
            cd ~/ConsecroMUD/cMUD
            echo "-- RESTARTED --" >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            date >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            evennia reload >> ${SERVER_LOG} 2>> ${SERVER_LOG}
            echo "$SERVICE_NAME restarted ..."
        else
            echo "$SERVICE_NAME is not running ..."
        fi
    ;;
    upgrade)
        cd ~/ConsecroMUD/evennia
        date >> ${CODEBASE_UPGRADE} 2>> ${CODEBASE_UPGRADE}
        git pull >> ${CODEBASE_UPGRADE} 2>> ${CODEBASE_UPGRADE}
        echo "$SERVICE_NAME upgraded ..."
        open ${CODEBASE_UPGRADE}
    ;;
esac