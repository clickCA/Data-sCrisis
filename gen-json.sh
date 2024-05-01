find ./data -type f | while read file; do
    jq . "$file" > "${file}.json"
done

find ./data -type f | while read file; do
    if [[ $file != *.json ]]; then
        echo "Removing non-JSON file: $file"
        rm "$file"
    fi
done