#!/bin/bash
java -jar $1 -role node -hub http://$2:4444/grid/register -browser "browserName=firefox, maxInstances=1"
