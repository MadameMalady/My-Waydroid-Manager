prompt_sudo_password() {
  sudo -v
  local max_attempts=3
  local attempt=1

  while true; do
    sudo -n true
    if [ $? -eq 0 ]; then
      break
    fi

    if [ $attempt -ge $max_attempts ]; then
      echo "Incorrect password. Exiting."
      exit 1
    fi

    attempt=$((attempt + 1))
    echo "Incorrect password. Please try again."
    sleep 1
  done
}

echo "This operation will require your password:"
prompt_sudo_password
echo "Successfully obtained root privilages"
sudo chmod +x My_Waydroid_Manager.py
cd scripts
sudo chmod +x build.sh dependencies.sh install_application.sh purge.sh purge_images.sh
cd ..
./My_Waydroid_Manager.py