unrar x "Data 2018-2023.rar" 
echo "Extracted Data 2018-2023.rar"

unrar x -o+ data_only_engineer_FULL.rar Project/2024/
echo "Extracted data_only_engineer_FULL.rar to Project/2024/"

sudo mkdir -p "merge"
echo "Created merge directory"

years=("2018" "2019" "2020" "2021" "2022" "2023" "2024")
for year in "${years[@]}"; do
    mkdir -p "data/$year" 2>/dev/null || sudo mkdir -p "data/$year"
    echo "Created data/$year directory"
done

years=("2018" "2019" "2020" "2021" "2022" "2023" "2024")
for year in "${years[@]}"; do
    mkdir -p "Project/$year" 2>/dev/null || sudo mkdir -p "Project/$year"
    echo "Created Project/$year directory"
done

find ./Project -type f | while read file; do
    jq . "$file" > "${file}.json"
    echo "Converted $file to JSON"
done

find ./Project -type f | while read file; do
    if [[ $file != *.json ]]; then
        echo "Removing non-JSON file: $file"
        rm "$file"
    fi
done

cd src/
echo "Changed directory to src/"

sudo python data_extraction.py
echo "Executed data_extraction.py"

sudo python merge_data.py
echo "Executed merge_data.py"