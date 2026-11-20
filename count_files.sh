#!/bin/bash
echo "Кількість файлів у /etc:"
find /etc -maxdepth 1 -type f | wc -l
# Оновлено під час виконання самостійної роботи
