

set -ex



clustalw2 H 2>&1 | grep "CLUSTAL 2.1"
clustalw H 2>&1 | grep "CLUSTAL 2.1"
exit 0
