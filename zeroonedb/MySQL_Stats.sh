#!/usr/bin/env sh

print ":: MYSQL STATISTICS FOR SYSTEM ADMINSTRATORS ::"
mysql -e "show variables; show status" | awk '
    {
        VAR[$1]=$2;;
    }

    END {
        for (i = 0; i < 99999; i++)
            print VAR[$i]
    }
'