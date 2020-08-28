#!/bin/bash
NET='192.168'
for I in {0..255}; do
  for J in {0..255}; do
    if ping -w 0.1 $NET.$I.$J &>/dev/null; then
      echo -e "\033[32m $NET.$I.$J\033[0m is up"
      touch ~/Desktop/port/$NET-$I-$J
    else
      echo -e "\033[31m $NET.$I.$J\033[0m is down"
    fi
  done
done
