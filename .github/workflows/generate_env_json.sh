#!/bin/bash

config_file="$1"

# Generate the output JSON file name by replacing .properties with .json
json_output_file="${config_file%.properties}.json"

# Declare an associative array to hold environment variables
declare -A new_env_vars

# Read key-value pairs from the config file
while IFS='=' read -r key value; do
  # Skip empty lines or lines starting with #
  [[ -z "$key" || "$key" =~ ^# ]] && continue
  new_env_vars["$key"]="$value"
done < "$config_file"

# Add additional environment variables from script arguments
shift # Skip the first argument (config_file)
while (( "$#" )); do
  # Split each argument into key=value, preserving '=' in the value
  key="${1%%=*}"
  value="${1#*=}"
  new_env_vars["$key"]="$value"
  shift
done

# Construct JSON string for Environment Variables
variables_json="{"
for key in "${!new_env_vars[@]}"; do
  variables_json+="\"$key\":\"${new_env_vars[$key]}\","
done
variables_json="${variables_json%,}}"

# Encapsulate in Environment object
json_string="{\"Environment\": {\"Variables\": $variables_json}}"

# Output the JSON string to a file
echo "$json_string" | jq -c . > "$json_output_file"

# Print the JSON file content
echo "Generated JSON content:"
cat "$json_output_file"