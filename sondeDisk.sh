#!/bin/bash
df -h / | awk '{print $3}' | sed 1d
