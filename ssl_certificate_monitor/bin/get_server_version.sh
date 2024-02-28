#!/bin/bash

# Monitor server version

SERVER_VERSION=$(lsb_release -a 2>/dev/null | grep "Release" | awk '{print $2}')
echo "server_version::$SERVER_VERSION"

