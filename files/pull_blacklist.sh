#!/usr/bin/env bash
# {{ ansible_managed }}
# Chain name
CHAIN=blacklist
# REJECT/DROP
ACTION=DROP

if [ $# -ne 1 ]; then
  echo "Usage $0 blacklist_url"
  exit 1
fi

# Fail on error
set -e

TMPFILE=$(mktemp)
curl --silent --location "${1}" --output "${TMPFILE}"

# Create chain if not present
iptables -nL ${CHAIN} &>/dev/null || iptables -N ${CHAIN}
# Flush chain
iptables -F ${CHAIN}

while IFS= read -r IP; do
  # iptables -A "${CHAIN}" -s "${IP}" -j LOG --log-prefix "blacklist:${ACTION}:" --log-level 6
  echo "Adding ${IP} to blocked"
  iptables -A "${CHAIN}" -s "${IP}" -j "${ACTION}"
done < "${TMPFILE}"

rm -f "${TMPFILE}"
echo
echo "NOTE:"
echo "To start blocking, you have to manually redirect your traffic to ${CHAIN} chain with"
echo
echo "iptables -I INPUT -j ${CHAIN}"
echo
