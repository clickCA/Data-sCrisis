unrar x "Data 2018-2023.rar" 
years=("2018" "2019" "2020" "2021" "2022" "2023" "2024")
for year in "${years[@]}"; do
    mkdir -p "data/$year" 2>/dev/null || sudo mkdir -p "data/$year"
done

years=("2018" "2019" "2020" "2021" "2022" "2023" "2024")
for year in "${years[@]}"; do
    mkdir -p "Project/$year" 2>/dev/null || sudo mkdir -p "Project/$year"
done


find ./Project -type f | while read file; do
    jq . "$file" > "${file}.json"
done

find ./Project -type f | while read file; do
    if [[ $file != *.json ]]; then
        echo "Removing non-JSON file: $file"
        rm "$file"
    fi
done


unrar x -o+ data_only_engineer_FULL.rar Project/2024
cd src/
python data_extraction.py
python merge_data.py